# LMML 2.0 — team solutions

Solutions of our team for **LMML 2.0** (Sigmoid, 14–15 Nov 2026). Each task represents a country within a continent. One folder per task. Each task folder has a README that explains the approach and how to reproduce the result.

## Reproduce

Run notebooks with the working directory set to the repository root unless the task README says otherwise. Standalone scripts may require the task folder as their working directory; follow that task's reproduction steps.

Each team member runs everything locally on their own machine. Install the packages in `requirements.txt` and the additional dependencies listed in the task README into your local Python environment, then select that environment as the notebook kernel.

Download each task's data from its platform page and put it in the location specified by that task's README. Data files are not tracked in this repository. For notebook tasks, open the notebook, restart its kernel, run all cells, and save the outputs.

## Tasks

| Task | Continent | Country | Folder | Status | Commit |
|---|---|---|---|---|---|
| Fry-ndship | Europe | Belgium | [fry-ndship](fry-ndship/README.md) | Passed (100 pts): `SIGMOID_SUPERVISION` | Not recorded |
| ¡Feliz Navidad! | Europe | Spain | [feliz-navidad](feliz-navidad/README.md) | Passed (max score): `SIGMOID_CRUCIO` | [679752a](https://github.com/maxpricop/lmml-team/commit/679752ab6d26694076cfaa2d74964f4db0ab584a) |
| Looks like an anomaly! | Europe | Albania | [looks-like-an-anomaly](looks-like-an-anomaly/README.md) | Passed (200 pts); local training score 96.71/100 | Not recorded |
| Pipes, Leaks, and the Graph Beneath | Europe | Finland | [pipes-leaks-graph](pipes-leaks-graph/README.md) | Passed (200 pts): `SIGMOID_HOTLINE` | [a8a19ab](https://github.com/maxpricop/lmml-team/commit/a8a19ab1133025604e8f77d6ed215e4041e50e0d) |
| What The Data? | Europe | Iceland | [what-the-data](what-the-data/README.md) | Passed (max score); practice output matched exactly | Not recorded |
| The Weak Layer | Europe | Switzerland | [the-weak-layer](the-weak-layer/README.md) | Passed (max score); practice output matched exactly | [2d8e923](https://github.com/maxpricop/lmml-team/commit/2d8e923c0bc76c9f19173e2704ebf168e7533fc6) |
| The Nisse's Bad Shift | Europe | Norway | [the-nisse-bad-shift](the-nisse-bad-shift/README.md) | Passed (max score); local repair F1 0.966 | [56285bf](https://github.com/maxpricop/lmml-team/commit/56285bffe3f87b81ec74d821863de84ffb44dabe) |
| Call My BLEUff | Europe | United Kingdom | [call-my-bleuff](call-my-bleuff/README.md) | Passed (200 pts): `SIGMOID_FRINDLOW` | Not recorded |
| Twins Separated at Birth | Asia | India | [twins-separated-at-birth](twins-separated-at-birth/README.md) | Passed (100 pts, F1 >= 0.88 on the hidden test); local training F1 0.962 | Not recorded |
| Bad BOMB | Asia | Laos | [bad-bomb](bad-bomb/README.md) | Passed (200 pts): 20/28 defects matched (accuracy 0.714, 0.70 needed) | Not recorded |
| Please, You Are So Delusional! | Africa | Tanzania | [please-you-are-so-delusional](please-you-are-so-delusional/README.md) | Passed (100 pts): `SIGMOID_A69EE28C5B2214A9AD99` | Not recorded |
| The Abidjan Transit Ledger | Africa | Côte d'Ivoire | [the-abidjan-transit-ledger](the-abidjan-transit-ledger/README.md) | Passed (200 pts); local validation: old task 1.00, new task 0.94–1.00 (0.85 needed on each) | [2c9af62](https://github.com/maxpricop/lmml-team/commit/2c9af62ed87bc8b6c0ed4fdd34cb8c95e545b234) |
| Always Valid, No Excuses | Africa | Egypt | [always-valid-no-excuses1](always-valid-no-excuses1/README.md) | Passed (100 pts); local check: 100/100 cards valid | [32455d4](https://github.com/maxpricop/lmml-team/commit/32455d44f9961af92f204b117b4d0d5e790efe3b) |
| The Gángan Never Lies | Africa | Nigeria | [the-gangan-never-lies](the-gangan-never-lies/README.md) | Passed (100 pts): `SIGMOID_TALKINGDRUM` | [b2d3b29](https://github.com/maxpricop/lmml-team/commit/b2d3b29a4899166bd5f6bd0298f31cf4b4278403) |
| Walu Season | Oceania | Fiji | [walu-season](walu-season/README.md) | Practice pass (6,944.6 kg/day). Platform result unrecorded | Not recorded |

Every task listed here passed on the platform with the maximum score, as confirmed by the team on 15 November 2026.

The Fry-ndship [notebook](fry-ndship/solve.ipynb) contains the accepted model and its saved numerical output. We tried two model specifications: long and estimated short sides alone revealed REGRESSION, which the platform rejected; adding declared ditch length revealed SUPERVISION, which the platform accepted. The [residual plot](fry-ndship/figures/residuals.png) shows SUPERVISION. Its [task README](fry-ndship/README.md) records both attempts, the accepted result, dependencies, and reproduction steps. The exact submission time and submitted commit link have not been recorded here.

The Pipes, Leaks, and the Graph Beneath [notebook](pipes-leaks-graph/solve.ipynb) documents town-name cleanup, reconstruction of the route network, and the ranking by distinct connections. Its [task README](pipes-leaks-graph/README.md) records the flag, which the platform accepted, and the commit linked above.

The What The Data? [script](what-the-data/main.py) cleans geothermal station exports. On 14 November 2026, its generated practice CSV was compared with the supplied reference: the files were byte-for-byte identical, at 952 bytes and 30 data rows each. The submission then passed on the platform's held-back export. Its [task README](what-the-data/README.md) records the implemented approach, runtime requirements, reproduction steps, and validation details.

The ¡Feliz Navidad! [notebook](feliz-navidad/solve.ipynb) reconstructs a 6 × 21 Christmas board by marking pilot/product pairs with at least one receipt inside the fair unit-price range. The saved [board](feliz-navidad/figures/crucio.png) spells CRUCIO. Its [task README](feliz-navidad/README.md) documents the flag, which the platform accepted, dependencies, and reproduction steps.

The Looks like an anomaly! [detector](looks-like-an-anomaly/detector.py) scores streaming sensor anomalies using per-zone baselines and point, collective, and drift checks. Its [task README](looks-like-an-anomaly/README.md) records the submitted file, three local attempts, robustness checks, and reproduction steps. The final local training score is 96.71/100 with F1 0.968 and one false alarm. The submission then passed the platform's evaluation.

The Weak Layer trains a decision tree on labeled Swiss snow-pit observations and recovers a hidden word from the first letters of the split features in preorder. The practice table yields `SIGMOID_DEMO`, and the submission passed on the platform. See the [task README](the-weak-layer/README.md) for reproduction steps.

The Nisse's Bad Shift uses an SVC to find evidence of two-way label swaps in handwritten digits. The final rule fixes 28 of 30 wrong labels with zero incorrect changes in the local check, and the submission passed on the platform. The [task README](the-nisse-bad-shift/README.md) records previous attempts and how to regenerate the CSV and retrained classifier.

The Call My BLEUff [notebook](call-my-bleuff/solve.ipynb) shows how two bluffing panellists per round game BLEU (leaving facts out, word salad, padding) and replaces BLEU with a fact checklist. In all 24 rounds exactly one deck has no bluff cards; the honest seats spell FRINDLOW, while BLEU's own picks spell SKELDRAP. The platform accepted `SIGMOID_FRINDLOW`. The [task README](call-my-bleuff/README.md) records the evidence figure, what did not work, and reproduction steps.

The Twins Separated at Birth [script](twins-separated-at-birth/main.py) finds pairs of monument photos that come from the same source photograph. It compares only images with the same aspect ratio and a different size, and calls a pair a duplicate when at least 45 SIFT keypoints match unambiguously (Lowe's ratio test). On the training archive it reaches F1 0.962 (precision 0.959, recall 0.966), and it passed the platform's hidden test (F1 >= 0.88 needed). It needs `opencv-python` in addition to `requirements.txt`. See the [task README](twins-separated-at-birth/README.md) for the approach, the threshold choice and reproduction steps.

The Bad BOMB [notebook](bad-bomb/solve.ipynb) finds 28 defective artillery shells among 1,225 unlabelled photos with PatchCore-style anomaly detection: a frozen WideResNet-50 describes every patch, only patches on the shell are scored against the 40 most similar photos, and the top of the ranking was reviewed by eye. The platform matched 20 of the 28 (accuracy 0.714, 0.70 needed). The [task README](bad-bomb/README.md) records the attempts, the defect types and reproduction steps.

The Please, You Are So Delusional! [pipeline](please-you-are-so-delusional/retrieval_pipeline.py) repairs a broken retrieval pipeline: one embedding model for both questions and documents (the starter mixed two), paragraph chunks instead of fixed 180-character slices, and archived notices excluded. All 72 questions then retrieve their current access notice, which gives `SIGMOID_A69EE28C5B2214A9AD99`; the platform accepted it (100 pts). The [task README](please-you-are-so-delusional/README.md) records each fix and reproduction steps.

The Abidjan Transit Ledger [script](the-abidjan-transit-ledger/main.py) recovers a request classifier that forgot its old task after being fine-tuned on a new one (catastrophic forgetting). It retrains on the labelled rows of both tasks together (replay): the shipped vectorizer plus our own word and character TF-IDF features feed a logistic regression over all 10 labels. In local validation it scores 1.00 on the old task and 0.94–1.00 on the new one, with 0.85 needed on each. The [task README](the-abidjan-transit-ledger/README.md) records the attempts, validation and reproduction steps. The submission passed on the platform.

The Always Valid, No Excuses [script](always-valid-no-excuses1/main.py) turns OCR'd record cards into strictly valid JSON with a small local model (Qwen3-1.7B through llama.cpp). Python first drops the scan noise and keeps only real `key: value` fields; the model then writes the JSON under a grammar built per card, so invalid JSON, wrong keys and quoted numbers cannot be generated. Every answer is checked against the conversion rules and corrected on a mismatch, because 99/100 scores zero. A local check found all 100 test cards valid. It needs `huggingface-hub` and `llama-cpp-python` in its own environment. The [task README](always-valid-no-excuses1/README.md) records the attempts and reproduction steps. The submission passed on the platform.

The Gángan Never Lies [notebook](the-gangan-never-lies/solve.ipynb) draws the spectrogram (frequency over time) of a recording that sounds like a flat hiss. The saved [spectrogram](the-gangan-never-lies/figures/spectrogram.png) shows the word TALKINGDRUM written on top of the noise, which gives `SIGMOID_TALKINGDRUM`. It needs `scipy` in addition to `requirements.txt`. The [task README](the-gangan-never-lies/README.md) explains why the word is visible and records reproduction steps. The platform accepted the flag.

Walu Season [script](walu-season/main.py) treats ten fishing spots as a multi-armed bandit. The strategy adds an exploration bonus to each spot's average catch and scored 6,944.6 kg per day across 100 practice days, above the 5,300 kg threshold. See the [task README](walu-season/README.md) for reproduction steps.

## Team rules

- Code is written, committed and pushed **by us**. AI only for explaining, discussing, finding bugs we fix, and small snippets we understand (official rules).
- After every platform submission: **commit + push immediately** (limit 1 h) and put the commit link in the submission. Never force-push or squash.
- Never commit data, model weights or secrets. Note in the task README where the data comes from.
- Everyone should be able to explain every solved task.
