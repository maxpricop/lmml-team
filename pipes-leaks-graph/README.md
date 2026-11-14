# Pipes, Leaks, and the Graph Beneath

- **Territory:** Finland (Europe: Classic ML & Data Science)
- **Points:** 200
- **Answer type:** flag

## Statement

📖 Storyline
For two years, ten regional offices of the Finnish Maritime Ferry Authority have logged every inter-town route by hand, each with its own habits. The Authority now wants to know which town is the network's busiest hub, so it can prioritize it for investment. A junior analyst runs a quick group-by on the raw log and confidently reports Orivesi. Nobody checks whether the log really says what the group-by says it does.

📌 Task Title
Pipes, Leaks, and the Graph Beneath

🔥 Difficulty
Medium

🎯 Objective
Clean the route log so that every town is counted as exactly one town and every connection once, rebuild the real route network, and rank its towns by number of distinct connections.

🚩 FLAG
SIGMOID_<WORD>: <WORD> is made of the first letters of the 7 busiest towns in your cleaned network, from most to fewest connections, in uppercase.

📂 Task Input
routes.csv: the raw route log, one row per log entry.

| Column | Description |
|---|---|
| log_id | Log entry ID |
| logged_on | Date the entry was logged |
| office | Office that logged the entry |
| from_town, to_town | The two ends of the route, as logged |
| route_type | ferry, train, or bus |

✅ Expected Output
The flag, entered on the platform.

Self-check: a correctly cleaned network has 116 towns and 448 connections, and no two of the 8 busiest towns have the same number of connections.

🏆 Scoring Criteria
✅ Correct flag: 200 points (PASS)
❌ Incorrect flag: 0 points (FAIL)

## Approach

The raw log writes the same town in many ways (650 different strings for 116 real towns), so a plain group-by counts rows, not real connections.
1. **Spelling:** strip spaces and dots, lowercase, and remove accents (ä→a) with Unicode NFKD. An unsupervised ML check (TF-IDF on 2–3 letter chunks + agglomerative clustering, cosine distance < 0.2) finds the same 177 names.
2. **Swedish names:** Finland is bilingual, and offices 03/07/09 often logged the Swedish name (Helsingfors = Helsinki). We map 61 official Swedish → Finnish names, which gives 116 towns.
3. **Graph:** we rebuild the network as an undirected graph with `networkx`. Towns are nodes, and each town pair is one edge, counted once (A→B = B→A; dates and route types don't matter). That gives 116 nodes and 448 edges.
4. **Ranking:** sort towns by their degree (number of distinct neighbours). The first letters of the top 7 make the flag.

## Reproduce

```bash
pip install -r requirements.txt
pip install networkx
# download routes.csv from the Drive link below into pipes-leaks-graph/data/
# open solve.ipynb and run all cells top to bottom
```

Data: `routes.csv` from the task's Google Drive folder: https://drive.google.com/drive/folders/1vmtpg82kdxeFPGqs9IqUp80enMTYUTOR. Put it in `pipes-leaks-graph/data/`.

## Attempts

| # | What we tried | Result |
|---|---|---|
| 1 | Naive row count on raw names | Orivesi first (44 rows), which is the trap: rows ≠ connections |
| 2 | Spelling cleanup (strip, lowercase, remove accents) | 177 names, fails the 116-town self-check |
| 3 | TF-IDF + agglomerative clustering on spellings | 177 clusters, same as rule-based (confirms step 2) |
| 4 | ML matching of Swedish names (spelling / shared neighbours) | best 49/61 correct, not reliable enough |
| 5 | Official Swedish → Finnish name list (61 names) | 116 towns, 448 connections|
| 6 | Undirected graph with networkx, rank by degree | Helsinki 39, Orivesi 38, Tornio 33, Lieksa 29, Imatra 27, Nokia 23, Eura 22 (next: Närpiö 21) all top 8 distinct |

## Result

- Submitted: `SIGMOID_HOTLINE`
- Commit: https://github.com/maxpricop/lmml-team/commit/a8a19ab1133025604e8f77d6ed215e4041e50e0d
