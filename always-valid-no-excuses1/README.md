# Always Valid, No Excuses

- **Territory:** Egypt
- **Points:** 100
- **Answer type:** evaluated file (`test-output.txt`)

## Statement

📖 **Storyline**

Historians in Cairo have run OCR over thousands of old Egyptology books and pulled out record cards, one per figure or monument, as plain key: value text. The digital catalogue accepts only strictly valid JSON: one malformed card and it is rejected. You are handed the museum's small talking oracle, a local model (Qwen3-1.7B), and told: use the oracle, not your own hand. Left to itself the oracle drifts: it quotes a number, forgets a missing field, mangles a backslash, keeps a torn page number. Hold it to the format until all 100 cards are flawless. 99 is a failure.

📌 **Task Title**

Always Valid, No Excuses

🔥 **Difficulty**

Easy

🎯 **Objective**

Write a main.py that uses the provided local model to convert each OCR'd record into one line of strictly valid JSON carrying exactly the same data. main.py reads test-input.txt from its own directory (one record per line, UTF-8) and writes test-output.txt beside it, where line N is the JSON for input line N. Non-interactive and offline.

🚩 **FLAG**

SIGMOID_<WORD>, released by the evaluator only when all 100 hidden records are correct.

📂 **Task Input**

Sample data: LMML_Egypt_TRAIN_DATA.zip

Example sample (not training data, there is nothing to train): train-input.txt (OCR records, one per line) and train-output.txt (one valid JSON line per record). The hidden test set uses different values: match the format, not the sample data.

Each record is key: value fields separated by |. It is not JSON, and it is messy in two ways:

- Messy spacing around : and |, and at the ends. Trim each key and value.
- Scan noise that is not a field and must be dropped: page numbers (page 22), headers (Chapter IX), footers (- 45 -), bracketed marks ([torn], [illegible], (margin)), figure labels, garble (###). Only a segment shaped like key: value with a simple word key is a real field.

```
Input : page 22| king :Menes| title: ruled with "the Aten" |[torn]| alive :true | Chapter IX
Output: {"king":"Menes","title":"ruled with \"the Aten\"","alive":true}
```

Conversion rules for each real field (after trimming):

- empty value → null
- exactly true / false → JSON booleans
- whole number (40, 0, -3) → JSON number
- anything else → JSON string, with " and \ escaped. Only the first : separates key from value (ratio: 3:1 → "ratio":"3:1").

Model: Qwen/Qwen3-1.7B-GGUF (~1.8 GB, not bundled). Download it once into models/ next to main.py, then run offline:

```
huggingface-cli download Qwen/Qwen3-1.7B-GGUF Qwen3-1.7B-Q8_0.gguf --local-dir models
```

Environment: Python 3.10–3.12 with huggingface-hub==0.26.2 and llama-cpp-python==0.3.35 built with CUDA (load with n_gpu_layers=-1). See requirements.txt for the build command. Evaluation runs on GPU with a 60-second time limit.

✅ **Expected Output**

Submit test-output.txt: one strict JSON object per input record, holding every real field typed by the rules above, with scan noise dropped and nothing added. Key order and whitespace do not matter (the grader compares parsed data, not bytes).

🏆 **Scoring Criteria**

Each of the 100 hidden records passes iff its output line parses as strict JSON and decodes to exactly the expected data.

- ✅ 100/100 records pass: 100 points (PASS, flag released)
- ❌ 99 or fewer: 0 points (FAIL)

## Approach

Python splits each card on `|`, trims each piece, splits it on the first `:` only, and keeps it only if the key is a simple word. That drops all the scan noise before the model sees anything. Qwen3-1.7B (llama.cpp, temperature 0, `/no_think`, two few-shot examples) then writes the JSON under a grammar built from a per-card JSON schema: exactly these keys, each typed as integer, boolean, null or string. Invalid JSON, extra or missing keys, and quoted numbers can't be generated at all. Each answer is parsed and compared with the rules. On a mismatch, the model is asked again under a grammar that allows only the exact correct line, and Python writes that line itself as a last resort, because 99/100 scores zero.

## Reproduce

```bash
python3.12 -m venv .venv
.venv/bin/python -m pip install huggingface-hub==0.26.2 llama-cpp-python==0.3.35
# on an NVIDIA GPU machine, build with CUDA instead:
# CMAKE_ARGS="-DGGML_CUDA=on" .venv/bin/python -m pip install llama-cpp-python==0.3.35
.venv/bin/huggingface-cli download Qwen/Qwen3-1.7B-GGUF Qwen3-1.7B-Q8_0.gguf --local-dir models
python main.py                    # -> test-output.txt
```

`main.py` restarts itself with `.venv/bin/python` if it's started with a Python that lacks `llama_cpp`. It uses the GPU (`n_gpu_layers=-1`) everywhere except Intel Macs, where it falls back to the CPU; set `N_GPU_LAYERS` to override.

Data: `test-input.txt` (100 cards) sits next to `main.py`. The sample cards are in `LMML_Egypt_TRAIN_DATA/` (from `LMML_Egypt_TRAIN_DATA.zip`). The model goes in `models/` (~1.8 GB, download it with the command above; don't commit it).

## Attempts

| # | What we tried | Result |
|---|---|---|
| 1 | Per-card typed JSON-schema grammar + few-shot prompt, `n_gpu_layers=-1` on an Intel Mac | Crashed: `llama_decode returned -3` (Metal fails on Intel Macs). Fixed by defaulting to CPU there. |
| 2 | Retry with each value pinned via schema `const` | `llama_cpp` built an invalid grammar for values containing `"` or `\`. Fixed by building the exact-line GBNF grammar by hand. |
| 3 | 13 sample cards vs `train-output.txt` | Model alone, first try: 12/13 (dropped the quotes in `"lord of the moon"`). Final output: 13/13. |
| 4 | Full run on the 100 cards in `test-input.txt` (CPU) | 100/100 lines are valid JSON and match the rules on a local check. |

## Result

- Submitted: `test-output.txt`, <time>
- Commit: <link>
