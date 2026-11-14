# Please, You Are So Delusional!

- **Continent:** Africa
- **Country:** Tanzania
- **Domain:** NLP / Retrieval
- **Difficulty:** Easy
- **Points available:** 100
- **Answer type:** Flag + link to repaired code and `retrieved_ids.json`
- **Platform status:** Passed (100 pts)
- **Flag:** `SIGMOID_A69EE28C5B2214A9AD99`

## Objective

Repair the supplied retrieval pipeline so every one of the 72 questions retrieves the correct source document (the current access notice for the asked exhibit and city). The flag is derived by `flag_utils.py` from the verification codes of the retrieved documents, in question order.

## Data

- `corpus.jsonl`: 744 documents: 600 generic operations bulletins (no collection information), and 144 exhibit documents = 24 exhibits × 3 cities (Dar es Salaam, Arusha, Mwanza) × 2 versions: a **CURRENT ACCESS NOTICE** (with the collection desk and time) and an **ARCHIVED BACKGROUND** notice (same exhibit, city and venue, but outdated).
- `questions.json`: 72 questions, one per exhibit and city, e.g. *where and when can I collect the Solar Spectroscope in Dar es Salaam?*

## What was broken and how we fixed it

| # | Bug in the starter | Fix | Correct answers |
|---|---|---|---|
| 0 | (starting point) | | 6/72 |
| 1 | Documents encoded with `all-MiniLM-L6-v2`, questions with `e5-small-v2`: two different vector spaces, so the similarities were meaningless | One model (`e5-small-v2`) for both, with e5's `query:` / `passage:` prefixes | 53/72 |
| 2 | Documents cut into fixed 180-character slices, cutting sentences, exhibit names and city names in half | Split into paragraphs, each prefixed with the document title | **72/72** |
| 3 | Archived notices (near-duplicates of the current ones) could be returned | Documents titled `ARCHIVED BACKGROUND` are not searchable (extra safeguard; fix 2 alone already reaches 72/72) | 72/72 |

The remaining errors after fix 1 were all the archived twin of the right document. Paragraphs solve this because only the current notice has an "Access details: … collect the kit from … Collection begins at …" paragraph, which is exactly what the questions ask.

## Verification

Every question names its exhibit and city, and there is exactly one current access notice per exhibit and city. Matching those by document title independently gives the same 72 documents and the same flag. Question `q001` retrieves `TZ-01-1A`, which is also the example given in the task description.

## Reproduce

1. Download `corpus.jsonl` and `questions.json` from the task's [Google Drive folder](https://drive.google.com/drive/folders/1E94rYgT1d4vum8zPRHr-TMATz4NxJssb) into `please-you-are-so-delusional/data/`.
2. `pip install -r requirements.txt`
3. From this folder run:
   ```bash
   python retrieval_pipeline.py --corpus data/corpus.jsonl --questions data/questions.json
   ```
   It writes `retrieved_ids.json` and prints `SIGMOID_A69EE28C5B2214A9AD99`.

## Files

| File | |
|---|---|
| `retrieval_pipeline.py` | the repaired pipeline |
| `flag_utils.py` | the organisers' flag helper (unchanged) |
| `retrieved_ids.json` | the 72 results, in question order |
| `requirements.txt` | the organisers' pinned packages |