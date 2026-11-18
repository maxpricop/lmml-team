"""
Link records that refer to the same reader.

Reads the input CSV (source_table, record_id, first_name, last_name, address)
and writes {"matches": [[id, id], ...]} with every pair of records of the same person.
"""
import csv
import difflib
import itertools
import json
import os
import re
import sys
import unicodedata
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
INPUT_NAMES = ["test-input.csv", "input.csv"]
OUTPUT_NAMES = ["test-output.json", "output.json"]
TRAIN_INPUT = os.path.join("task_mexico", "train-input.csv")
TRAIN_OUTPUT = os.path.join("task_mexico", "train-output.json")
NAME_THRESHOLD = 0.5  # only used to split an ambiguous address group


def find_input():
    """Return (input path, test mode). Test input wins; training data is the fallback."""
    if len(sys.argv) > 1:
        return sys.argv[1], True
    for folder in (os.getcwd(), HERE):
        for name in INPUT_NAMES:
            path = os.path.join(folder, name)
            if os.path.isfile(path):
                return path, True
    return os.path.join(HERE, TRAIN_INPUT), False


def address_key(address):
    """All numbers in the address (house, interior, building, flat, postcode), order-free.

    Duplicates reword the street (Av./Avenida, number before or after the street name)
    but never change these numbers, so they identify the address.
    """
    return tuple(sorted(re.findall(r"\d+", address)))


def name_tokens(record):
    text = unicodedata.normalize("NFKD", f"{record['first_name']} {record['last_name']}")
    text = "".join(c for c in text.lower() if c.isalpha() or c == " ")
    return text.split()


def name_similarity(r1, r2):
    """Best similarity of the two full names, allowing first/last name to be swapped."""
    a, b = name_tokens(r1), name_tokens(r2)
    target = " ".join(b)
    return max(
        difflib.SequenceMatcher(None, " ".join(order), target).ratio()
        for order in (a, a[::-1])
    )


def match_group(records):
    """All cross-table pairs of records sharing one address."""
    tables = [r["source_table"] for r in records]
    pairs = [
        (r1, r2)
        for r1, r2 in itertools.combinations(records, 2)
        if r1["source_table"] != r2["source_table"]
    ]
    # Each person appears at most once per table. Two records from the same table at
    # this address means two different people live there: keep only name-similar pairs.
    if len(set(tables)) < len(tables):
        pairs = [(r1, r2) for r1, r2 in pairs if name_similarity(r1, r2) >= NAME_THRESHOLD]
    return [sorted((r1["record_id"], r2["record_id"])) for r1, r2 in pairs]


def find_matches(records):
    groups = defaultdict(list)
    for record in records:
        groups[address_key(record["address"])].append(record)
    matches = []
    for group in groups.values():
        matches.extend(match_group(group))
    return sorted(matches)


def main():
    input_path, test_mode = find_input()
    with open(input_path, encoding="utf-8-sig", newline="") as f:
        records = list(csv.DictReader(f))
    result = {"matches": find_matches(records)}
    text = json.dumps(result)

    if test_mode:
        for name in OUTPUT_NAMES:
            with open(name, "w", encoding="utf-8") as f:
                f.write(text)
        if not sys.stdout.isatty():
            print(text)
        print(f"{len(result['matches'])} matches from {len(records)} records", file=sys.stderr)
        return

    # Practice run on the training data: compare with the supplied answers.
    with open(os.path.join(HERE, TRAIN_OUTPUT), encoding="utf-8") as f:
        expected = {tuple(sorted(p)) for p in json.load(f)["matches"]}
    found = {tuple(p) for p in result["matches"]}
    print(f"found {len(found)}, expected {len(expected)}, "
          f"missing {len(expected - found)}, extra {len(found - expected)}")
    print("PASS" if found == expected else "FAIL")


if __name__ == "__main__":
    main()
