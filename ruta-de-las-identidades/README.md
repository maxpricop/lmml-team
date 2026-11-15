# Ruta de las Identidades

- **Territory:** Mexico
- **Points:** 100
- **Answer type:** evaluated file (`main.py`)

## Statement

📖 **Storyline**

The fictional Ruta de Lectura programme is preparing book parcels for readers across Mexico. Its regional registration desks have merged their records, but the same reader may appear more than once under different details. Link the repeated records before dispatch so every reader receives one parcel.

📌 **Task Title**

Ruta de las Identidades

🔥 **Difficulty**

Easy

🎯 **Objective**

Identify every pair of records that refers to the same person.

🚩 **FLAG**

SIGMOID_<PHRASE>, released automatically by the platform if the solution passes the test.

📂 **Task Input**

The data provided to you consists of two file.

train-input.csv contains records from three source tables. Each row contains source_table, record_id, first_name, last_name, and address. train-output.json shows the required output format.

✅ **Expected Output**

Submit main.py. It must read the provided input CSV and write a JSON object with a matches list. Each match is a two-item list of distinct record IDs.

```json
{"matches": [["a0001", "c0002"], ["b0003", "c0004"]]}
```

If three records refer to the same person, include all three unique pairs:

```json
{"matches": [["a0001", "b0003"], ["a0001", "c0002"], ["b0003", "c0002"]]}
```

The order of the IDs within a pair and the order of the pairs do not matter.

🏆 **Scoring Criteria**

- ✅ Every matching pair is submitted and no extra pair is submitted: 100 points (PASS).
- ❌ Any matching pair is missing or an extra pair is submitted: 0 points (FAIL).

## Approach

Duplicates garble the names (first and last swapped, initials like `H.`, typos like `Calra`, dropped accents) and reword the address (`Av.`/`Avenida`, `Int.`/`Interior`, the house number before or after the street), but they never change the numbers in the address. So each record is keyed by the sorted list of all numbers in its address (house, interior, building, flat, postcode), and every cross-table pair inside a group is a match. On the training data, those groups are exactly the labelled people: 2–3 records each, at most one per table. Names are too noisy to be the main signal (true pairs score as low as 0.27 name similarity, strangers up to 0.87), so they only serve as a tie-breaker if two records from the same table share an address, which never happens in training.

## Reproduce

```bash
python3 main.py                   # no test input: runs on task_mexico/train-input.csv, prints PASS/FAIL
python3 main.py some-input.csv    # any input file -> test-output.json and output.json
```

Python 3 standard library only, nothing to install. With `test-input.csv` (or `input.csv`) in the working directory, `main.py` reads it and writes the answer to both `test-output.json` and `output.json`, and prints it to stdout when the output is captured.

Data: download `train-input.csv` and `train-output.json` from the task's platform page and put them in `task_mexico/` next to `main.py` (not committed).

## Attempts

| # | What we tried | Result |
|---|---|---|
| 1 | Studied the 12,038 labelled pairs | Groups of 2–3 records, never two from the same table; names garbled, address numbers always identical |
| 2 | Name similarity (accent-stripped, swap-aware) as a match signal | Rejected: true pairs go as low as 0.27, random non-pairs up to 0.87 |
| 3 | Group by the set of numbers in the address, pair across tables | Training data: 12,038 found, 0 missing, 0 extra (PASS), in under 0.5 s |
| 4 | Same run grader-style (`test-input.csv` in an empty folder), plus a made-up case with two people at one address | Exact match on the first; the second split correctly by name |

## Result

- Submitted: `main.py`, <time>
- Commit: <link>
