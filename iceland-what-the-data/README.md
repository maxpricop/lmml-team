# What The Data?

- **Territory:** Europe / Classic ML & Data Science
- **Country:** Iceland
- **Difficulty:** Easy
- **Answer type:** evaluated Python file, `main.py`; the platform releases a flag after a successful evaluation
- **Status:** practice output verified; platform result and submitted commit not recorded

## Statement summary

Clean a damaged geothermal monitoring export. The UTF-8 input uses semicolons and has a variable-length preamble of comments and blank lines, duplicate reading IDs, decimal commas, incorrectly decoded station names, and mixed Celsius/Fahrenheit readings. The held-back export includes additional stations and more corruption, so the cleaner must not hardcode practice values.

At evaluation time, `main.py` must read `test-input.csv` and write `test-output.csv` in its current working directory. The required output header is:

```csv
reading_id,station_name,temperature_c,reading_date
```

There must be one row per integer reading ID, sorted ascending. Station names must retain their correct Icelandic characters, temperatures must be Celsius with exactly one decimal place, and dates must remain unchanged. The output is comma-delimited UTF-8 with no index, extra columns, or quoting.

## Implemented approach

1. Prefer `test-input.csv` when present; otherwise use the local `train-input.csv` and write the corresponding output filename.
2. Read semicolon-delimited data while ignoring comment lines and blank lines.
3. Normalize decimal commas, parse numeric temperatures, and convert only Fahrenheit readings to Celsius.
4. Attempt to reverse Latin-1/UTF-8 misdecoding in station names; preserve the original text if strict conversion fails.
5. Keep the first row for each `reading_id` after cleaning, then sort IDs ascending.
6. Export only the four required columns, with one-decimal temperatures and no index or quoting.

The practice duplicates agree at the required output precision. For example, reading 25 has a converted Fahrenheit value of approximately 70.611111 and a Celsius value of 70.6; either formats as 70.6. This does not establish a conflict-resolution rule for genuinely inconsistent unseen readings. The name repair covers the observed corruption; other encoding mismatches have not been verified.

## Runtime and dependencies

The grader specifies Python 3.10–3.12, with pandas 2.2.2 and NumPy 1.26.4 available, no internet access, CPU only, and a 60-second limit. The script imports pandas plus the standard-library `pathlib` and `csv` modules.

The existing Windows workspace venv was observed to use Python 3.14.10. Its availability does not establish compatibility with the grader: repeat final checks using a Python 3.10–3.12 venv with the specified package versions. Do not replace the shared workspace's CUDA/PyTorch installation for this task.

## Reproduce

Download `train-input.csv` and `train-output.csv` from the task's platform page. Keep these untouched reference files in this folder's gitignored `data/` directory. Do not commit the data or generated CSVs.

The following PowerShell commands exercise the required test filenames with the practice input. Run them yourself, and do not overwrite a real test export with the practice copy. The interpreter path below is the existing workspace venv; substitute a compatible Python 3.10–3.12 venv for the final compatibility check.

```powershell
$venvPython = 'D:\Hackathon\.venv\Scripts\python.exe'
& $venvPython --version
Set-Location 'D:\lmml-team\iceland-what-the-data'
Copy-Item -LiteralPath '.\data\train-input.csv' -Destination '.\test-input.csv'
& $venvPython '.\main.py'
fc.exe /b '.\test-output.csv' '.\data\train-output.csv'
```

The working directory matters because the script uses bare filenames. If both input files exist, test input takes priority. With no test input, the training fallback reads `train-input.csv` and writes `train-output.csv` in the task folder; keep the supplied reference safely in `data/`.

`fc.exe /b` checks exact bytes. The platform permits normalizing line endings and trailing whitespace at the end of the file, but every other character must match. The reproduction commands above are instructions, not a record that this test-filename run has already been verified.

## Validation

On 14 November 2026, the existing generated `train-output.csv` was compared read-only against `data/train-output.csv`; the script was not rerun during that comparison.

| Check | Observed result |
|---|---|
| Byte-for-byte comparison | Identical |
| Comparison after permitted normalization | Identical |
| File size | 952 bytes each |
| Data rows | 30 each |
| Header | `reading_id,station_name,temperature_c,reading_date` |
| Strict UTF-8 decoding | Succeeds |
| Quote characters | None |

Earlier manual diagnostics also reported 30 rows, unique reading IDs, and ascending numeric ID order. This validation establishes an exact match on the supplied practice export only; it is not a held-back evaluation or platform acceptance.

## Attempts

| # | What we tried | Result |
|---|---|---|
| 1 | Clean the practice export and compare the generated CSV with the supplied reference | Exact byte-for-byte match: 30 data rows, 952 bytes |

## Result

- **Local practice:** verified exact match on 14 November 2026.
- **Held-back evaluation / platform acceptance:** not recorded.
- **Submitted flag and submission time:** not recorded.
- **Submitted commit link:** not recorded.
