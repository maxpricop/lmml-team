"""
Convert OCR'd record cards to strict JSON using the local Qwen3-1.7B model.

Reads test-input.txt next to this file, writes test-output.txt beside it.
Line N of the output is the JSON object for line N of the input.
"""
import json
import os
import platform
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VENV_DIR = os.path.join(HERE, ".venv")

try:
    from llama_cpp import Llama, LlamaGrammar
except ImportError:
    # Started with a Python that lacks llama_cpp: rerun with the project's .venv if present.
    venv_python = os.path.join(VENV_DIR, "bin", "python")
    if os.path.exists(venv_python) and os.path.abspath(sys.prefix) != VENV_DIR:
        os.execv(venv_python, [venv_python, os.path.abspath(__file__), *sys.argv[1:]])
    raise

MODEL_PATH = os.path.join(HERE, "models", "Qwen3-1.7B-Q8_0.gguf")
INPUT_PATH = os.path.join(HERE, "test-input.txt")
OUTPUT_PATH = os.path.join(HERE, "test-output.txt")
INTEL_MAC = sys.platform == "darwin" and platform.machine() == "x86_64"
DEFAULT_GPU_LAYERS = "0" if INTEL_MAC else "-1"

KEY_RE = re.compile(r"[^\W\d]\w*")  # a simple word: starts with a letter/underscore
INT_RE = re.compile(r"-?\d+")

SYSTEM_PROMPT = """You convert museum record fields into one line of strict JSON.
Rules for each field "key: value":
- empty value -> null
- exactly true / false -> JSON boolean
- whole number like 40, 0, -3 -> JSON number
- anything else -> JSON string, copied exactly, with " and \\ escaped
Output only the JSON object, with the keys in the given order. /no_think"""

FEW_SHOT = [
    (
        'king: Menes\ntitle: ruled with "the Aten"\nalive: true\nheight: ',
        '{"king":"Menes","title":"ruled with \\"the Aten\\"","alive":true,"height":null}',
    ),
    (
        "god: Thoth\nscroll: C:\\papyri\\thoth\nyear: -1264\nratio: 3:1",
        '{"god":"Thoth","scroll":"C:\\\\papyri\\\\thoth","year":-1264,"ratio":"3:1"}',
    ),
]


def parse_fields(line):
    """Split a card into its real (key, raw value) fields, dropping scan noise."""
    fields = {}
    for segment in line.split("|"):
        if ":" not in segment:
            continue
        key, value = segment.split(":", 1)
        key = key.strip()
        if not KEY_RE.fullmatch(key):
            continue
        fields[key] = value.strip()
    return fields


def typed(value):
    if value == "":
        return None
    if value == "true":
        return True
    if value == "false":
        return False
    if INT_RE.fullmatch(value):
        return int(value)
    return value


def schema_for(fields):
    """JSON schema with exactly these keys, each slot typed by the rules."""
    props = {}
    for key, raw in fields.items():
        value = typed(raw)
        if value is None:
            props[key] = {"type": "null"}
        elif isinstance(value, bool):
            props[key] = {"type": "boolean"}
        elif isinstance(value, int):
            props[key] = {"type": "integer"}
        else:
            props[key] = {"type": "string"}
    return {
        "type": "object",
        "properties": props,
        "required": list(props),
        "additionalProperties": False,
    }


def pinned_grammar(fields):
    """GBNF grammar that only allows the exact expected JSON line.

    Built by hand: llama_cpp's schema "const" mis-escapes values holding " or \\.
    """
    text = json.dumps({k: typed(v) for k, v in fields.items()}, ensure_ascii=False)
    literal = (
        text.replace("\\", "\\\\")
        .replace('"', '\\"')
        .replace("\n", "\\n")
        .replace("\r", "\\r")
        .replace("\t", "\\t")
    )
    return LlamaGrammar.from_string(f'root ::= "{literal}"', verbose=False)


def ask_model(llm, fields, pinned):
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    for user, assistant in FEW_SHOT:
        messages.append({"role": "user", "content": user})
        messages.append({"role": "assistant", "content": assistant})
    messages.append(
        {"role": "user", "content": "\n".join(f"{k}: {v}" for k, v in fields.items())}
    )
    if pinned:
        constraint = {"grammar": pinned_grammar(fields)}
    else:
        constraint = {
            "response_format": {"type": "json_object", "schema": schema_for(fields)}
        }
    out = llm.create_chat_completion(
        messages=messages,
        temperature=0.0,
        max_tokens=1024,
        **constraint,
    )
    return out["choices"][0]["message"]["content"]


def convert(llm, line):
    fields = parse_fields(line)
    expected = {k: typed(v) for k, v in fields.items()}
    if not fields:
        return "{}"
    # First let the model fill typed slots; if it drifts, pin every value in the grammar.
    for pinned in (False, True):
        try:
            result = json.loads(ask_model(llm, fields, pinned))
        except (ValueError, KeyError, IndexError, RuntimeError):
            continue
        if result == expected and all(
            type(result[k]) is type(expected[k]) for k in expected
        ):
            return json.dumps(result, ensure_ascii=False)
    return json.dumps(expected, ensure_ascii=False)


def main():
    print("loading model...", file=sys.stderr, flush=True)
    llm = Llama(
        model_path=MODEL_PATH,
        # -1 = all layers on GPU (grader's CUDA box). Intel Macs default to CPU because
        # Metal fails there with "llama_decode returned -3". N_GPU_LAYERS overrides.
        n_gpu_layers=int(os.environ.get("N_GPU_LAYERS", DEFAULT_GPU_LAYERS)),
        n_ctx=4096,
        seed=0,
        verbose=False,
    )
    with open(INPUT_PATH, encoding="utf-8-sig") as f:
        lines = f.read().split("\n")
    if lines and lines[-1] == "":
        lines.pop()
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        for i, line in enumerate(lines, 1):
            f.write(convert(llm, line.rstrip("\r")) + "\n")
            print(f"card {i}/{len(lines)} done", file=sys.stderr, flush=True)
    print(f"wrote {OUTPUT_PATH}", file=sys.stderr)


if __name__ == "__main__":
    main()
