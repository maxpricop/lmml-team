# LMML 2.0 — team solutions

Solutions of our team for **LMML 2.0** (Sigmoid, 14–15 Nov 2026). Each task represents a country within a continent. One folder per task. Each task folder has a README that explains the approach and how to reproduce the result.

## Reproduce

Run notebooks with the working directory set to the repository root unless the task README says otherwise. Standalone scripts may require the task folder as their working directory; follow that task's reproduction steps.

Each team member runs everything locally on their own machine. Install the packages in `requirements.txt` and the additional dependencies listed in the task README into your local Python environment, then select that environment as the notebook kernel.

Download each task's data from its platform page and put it in the location specified by that task's README. Data files are not tracked in this repository. For notebook tasks, open the notebook, restart its kernel, run all cells, and save the outputs.

## Tasks

| Task | Continent | Country | Folder | Status | Commit |
|---|---|---|---|---|---|
| Fry-ndship | Europe | Belgium | [fry-ndship](fry-ndship/README.md) | Accepted: `SIGMOID_SUPERVISION` | Not recorded |
| ¡Feliz Navidad! | Europe | Spain | [feliz-navidad](feliz-navidad/README.md) | Flag identified: `SIGMOID_CRUCIO`; platform result not recorded | [679752a](https://github.com/maxpricop/lmml-team/commit/679752ab6d26694076cfaa2d74964f4db0ab584a) |
| Looks like an anomaly! | Europe | Albania | [looks-like-an-anomaly](looks-like-an-anomaly/README.md) | Submitted; local training score: 96.71/100; platform result not recorded | Not recorded |
| Pipes, Leaks, and the Graph Beneath | Europe | Finland | [pipes-leaks-graph](pipes-leaks-graph/README.md) | Submitted: `SIGMOID_HOTLINE` | [a8a19ab](https://github.com/maxpricop/lmml-team/commit/a8a19ab1133025604e8f77d6ed215e4041e50e0d) |
| What The Data? | Europe | Iceland | [what-the-data](what-the-data/README.md) | Practice verified: exact match; platform result not recorded | Not recorded |
| The Weak Layer | Europe | Switzerland | [the-weak-layer](the-weak-layer/README.md) | Practice verified: exact match; platform result not recorded | [2d8e923](https://github.com/maxpricop/lmml-team/commit/2d8e923c0bc76c9f19173e2704ebf168e7533fc6) |
| The Nisse's Bad Shift | Europe | Norway | [the-nisse-bad-shift](the-nisse-bad-shift/README.md) | Local repair F1 0.966. Platform result passed. | [56285bf](https://github.com/maxpricop/lmml-team/commit/56285bffe3f87b81ec74d821863de84ffb44dabe) |
| Call My BLEUff | Europe | United Kingdom | [call-my-bleuff](call-my-bleuff/README.md) | Flag identified: `SIGMOID_FRINDLOW`; platform result not recorded | Not recorded |
| Point par point | Europe | France | [point-par-point](point-par-point/solve.ipynb) (no README yet) | Flag identified: `SIGMOID_ANOURE`; platform result not recorded | Not recorded |
| Twins Separated at Birth | Asia | India | [twins-separated-at-birth](twins-separated-at-birth/README.md) | Passed (F1 >= 0.88 on the hidden test); local training F1 0.962 | Not recorded |
| Bad BOMB | Asia | Laos | [bad-bomb](bad-bomb/README.md) | Passed: 20/28 defects matched (accuracy 0.714, 0.70 needed) | Not recorded |
| Please, You Are So Delusional! | Africa | Tanzania | [please-you-are-so-delusional](please-you-are-so-delusional/README.md) | Passed (100 pts): `SIGMOID_A69EE28C5B2214A9AD99` | Not recorded |

The Fry-ndship [notebook](fry-ndship/solve.ipynb) contains the accepted model and its saved numerical output. We tried two model specifications: long and estimated short sides alone revealed REGRESSION, which the platform rejected; adding declared ditch length revealed SUPERVISION, which the platform accepted. The [residual plot](fry-ndship/figures/residuals.png) shows SUPERVISION. Its [task README](fry-ndship/README.md) records both attempts, the accepted result, dependencies, and reproduction steps. The exact submission time and submitted commit link have not been recorded here.

The Pipes, Leaks, and the Graph Beneath [notebook](pipes-leaks-graph/solve.ipynb) documents town-name cleanup, reconstruction of the route network, and the ranking by distinct connections. Its [task README](pipes-leaks-graph/README.md) records the submitted flag and the commit linked above.

The What The Data? [script](what-the-data/main.py) cleans geothermal station exports. On 14 November 2026, its generated practice CSV was compared with the supplied reference: the files were byte-for-byte identical, at 952 bytes and 30 data rows each. This verifies the practice case only, not the held-back export or platform acceptance. Its [task README](what-the-data/README.md) records the implemented approach, runtime requirements, reproduction steps, and validation details.

The ¡Feliz Navidad! [notebook](feliz-navidad/solve.ipynb) reconstructs a 6 × 21 Christmas board by marking pilot/product pairs with at least one receipt inside the fair unit-price range. The saved [board](feliz-navidad/figures/crucio.png) spells CRUCIO. Its [task README](feliz-navidad/README.md) documents the observed flag, dependencies, and reproduction steps; platform acceptance is not recorded.

The Looks like an anomaly! [detector](looks-like-an-anomaly/detector.py) scores streaming sensor anomalies using per-zone baselines and point, collective, and drift checks. Its [task README](looks-like-an-anomaly/README.md) records the submitted file, three local attempts, robustness checks, and reproduction steps. The final local training score is 96.71/100 with F1 0.968 and one false alarm; this is not a held-back evaluation or confirmation of platform acceptance.

The Weak Layer trains a decision tree on labeled Swiss snow-pit observations and recovers a hidden word from the first letters of the split features in preorder. The practice table yields `SIGMOID_DEMO`. See the [task README](the-weak-layer/README.md) for reproduction steps.

The Nisse's Bad Shift uses an SVC to find evidence of two-way label swaps in handwritten digits. The final rule fixes 28 of 30 wrong labels with zero incorrect changes in the local check. The [task README](the-nisse-bad-shift/README.md) records previous attempts and how to regenerate the CSV and retrained classifier.

The Call My BLEUff [notebook](call-my-bleuff/solve.ipynb) shows how two bluffing panellists per round game BLEU (leaving facts out, word salad, padding) and replaces BLEU with a fact checklist. In all 24 rounds exactly one deck has no bluff cards; the honest seats spell FRINDLOW, while BLEU's own picks spell SKELDRAP. The [task README](call-my-bleuff/README.md) records the evidence figure, what did not work, and reproduction steps.

The Point par point [notebook](point-par-point/solve.ipynb) finds the letters an artist hid among 28,108 Paris rental listings: the fake listings form flat, dense sheets in the space of price, reviews, availability and location, HDBSCAN groups them into 6 letters, the letters are ordered by arrondissement and read by matching rendered capitals. The notebook prints `SIGMOID_ANOURE` (the first and second letters were a close call between L/A and Z/N, settled by hand). This task has no README yet.

The Twins Separated at Birth [script](twins-separated-at-birth/main.py) finds pairs of monument photos that come from the same source photograph. It compares only images with the same aspect ratio and a different size, and calls a pair a duplicate when at least 45 SIFT keypoints match unambiguously (Lowe's ratio test). On the training archive it reaches F1 0.962 (precision 0.959, recall 0.966), and it passed the platform's hidden test (F1 >= 0.88 needed). It needs `opencv-python` in addition to `requirements.txt`. See the [task README](twins-separated-at-birth/README.md) for the approach, the threshold choice and reproduction steps.

The Bad BOMB [notebook](bad-bomb/solve.ipynb) finds 28 defective artillery shells among 1,225 unlabelled photos with PatchCore-style anomaly detection: a frozen WideResNet-50 describes every patch, only patches on the shell are scored against the 40 most similar photos, and the top of the ranking was reviewed by eye. The platform matched 20 of the 28 (accuracy 0.714, 0.70 needed). The [task README](bad-bomb/README.md) records the attempts, the defect types and reproduction steps.

The Please, You Are So Delusional! [pipeline](please-you-are-so-delusional/retrieval_pipeline.py) repairs a broken retrieval pipeline: one embedding model for both questions and documents (the starter mixed two), paragraph chunks instead of fixed 180-character slices, and archived notices excluded. All 72 questions then retrieve their current access notice, which gives `SIGMOID_A69EE28C5B2214A9AD99`; the platform accepted it (100 pts). The [task README](please-you-are-so-delusional/README.md) records each fix and reproduction steps.

## Team rules

- Code is written, committed and pushed **by us**. AI only for explaining, discussing, finding bugs we fix, and small snippets we understand (official rules).
- After every platform submission: **commit + push immediately** (limit 1 h) and put the commit link in the submission. Never force-push or squash.
- Never commit data, model weights or secrets. Note in the task README where the data comes from.
- Everyone should be able to explain every solved task.
