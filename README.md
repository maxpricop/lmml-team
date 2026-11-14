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
| ¡Feliz Navidad! | Europe | Spain | [feliz-navidad](feliz-navidad/README.md) | Flag identified: `SIGMOID_CRUCIO`; platform result not recorded | Not recorded |
| Looks like an anomaly! | Europe | Albania | [looks-like-an-anomaly](looks-like-an-anomaly/README.md) | Submitted; local training score: 96.71/100; platform result not recorded | Not recorded |
| Pipes, Leaks, and the Graph Beneath | Europe | Finland | [pipes-leaks-graph](pipes-leaks-graph/README.md) | Submitted: `SIGMOID_HOTLINE` | [a8a19ab](https://github.com/maxpricop/lmml-team/commit/a8a19ab1133025604e8f77d6ed215e4041e50e0d) |
| What The Data? | Europe | Iceland | [what-the-data](what-the-data/README.md) | Practice verified: exact match; platform result not recorded | Not recorded |
| The Weak Layer | Europe | Switzerland | [the-weak-layer](the-weak-layer/README.md) | Practice verified: exact match; platform result not recorded | Not recorded |
| The Nisse's Bad Shift | Europe | Norway | [the-nisse-bad-shift](the-nisse-bad-shift/README.md) | Local repair F1 0.966. Platform result passed. | Not recorded |

The Fry-ndship [notebook](fry-ndship/solve.ipynb) contains the accepted model and its saved numerical output. We tried two model specifications: long and estimated short sides alone revealed REGRESSION, which the platform rejected; adding declared ditch length revealed SUPERVISION, which the platform accepted. The [residual plot](fry-ndship/figures/residuals.png) shows SUPERVISION. Its [task README](fry-ndship/README.md) records both attempts, the accepted result, dependencies, and reproduction steps. The exact submission time and submitted commit link have not been recorded here.

The Pipes, Leaks, and the Graph Beneath [notebook](pipes-leaks-graph/solve.ipynb) documents town-name cleanup, reconstruction of the route network, and the ranking by distinct connections. Its [task README](pipes-leaks-graph/README.md) records the submitted flag and the commit linked above.

The What The Data? [script](what-the-data/main.py) cleans geothermal station exports. On 14 November 2026, its generated practice CSV was compared with the supplied reference: the files were byte-for-byte identical, at 952 bytes and 30 data rows each. This verifies the practice case only, not the held-back export or platform acceptance. Its [task README](what-the-data/README.md) records the implemented approach, runtime requirements, reproduction steps, and validation details.

The ¡Feliz Navidad! [notebook](feliz-navidad/solve.ipynb) reconstructs a 6 × 21 Christmas board by marking pilot/product pairs with at least one receipt inside the fair unit-price range. The saved [board](feliz-navidad/figures/crucio.png) spells CRUCIO. Its [task README](feliz-navidad/README.md) documents the observed flag, dependencies, and reproduction steps; platform acceptance is not recorded.

The Looks like an anomaly! [detector](looks-like-an-anomaly/detector.py) scores streaming sensor anomalies using per-zone baselines and point, collective, and drift checks. Its [task README](looks-like-an-anomaly/README.md) records the submitted file, three local attempts, robustness checks, and reproduction steps. The final local training score is 96.71/100 with F1 0.968 and one false alarm; this is not a held-back evaluation or confirmation of platform acceptance.

The Weak Layer trains a decision tree on labeled Swiss snow-pit observations and recovers a hidden word from the first letters of the split features in preorder. The practice table yields `SIGMOID_DEMO`. See the [task README](the-weak-layer/README.md) for reproduction steps.

The Nisse's Bad Shift uses an SVC to find evidence of two-way label swaps in handwritten digits. The final rule fixes 28 of 30 wrong labels with zero incorrect changes in the local check. The [task README](the-nisse-bad-shift/README.md) records previous attempts and how to regenerate the CSV and retrained classifier.

## Team rules

- Code is written, committed and pushed **by us**. AI only for explaining, discussing, finding bugs we fix, and small snippets we understand (official rules).
- After every platform submission: **commit + push immediately** (limit 1 h) and put the commit link in the submission. Never force-push or squash.
- Never commit data, model weights or secrets. Note in the task README where the data comes from.
- Everyone should be able to explain every solved task.
