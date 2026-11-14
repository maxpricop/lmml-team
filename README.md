# LMML 2.0 — team solutions

Solutions of our team for **LMML 2.0** (Sigmoid, 14–15 Nov 2026). Each task represents a country within a continent. One folder per task. Each task folder has a README that explains the approach and how to reproduce the result.

## Reproduce

Run notebooks with the working directory set to the repository root.

Each team member runs everything locally on their own machine. Install the packages in `requirements.txt` and the additional dependencies listed in the task README into your local Python environment, then select that environment as the notebook kernel.

Download each task's data from its platform page and put it in the location specified by that task's README. Data files are not tracked in this repository. Open the notebook, restart its kernel, run all cells, and save the outputs.

## Tasks

| Task | Continent | Country | Folder | Status | Commit |
|---|---|---|---|---|---|
| Fry-ndship | Europe | Belgium | [fry-ndship](fry-ndship/README.md) | Solved locally: `SIGMOID_REGRESSION` | Not recorded |
| Pipes, Leaks, and the Graph Beneath | Europe | Finland | [pipes-leaks-graph](pipes-leaks-graph/README.md) | Submitted: `SIGMOID_HOTLINE` | [a8a19ab](https://github.com/maxpricop/lmml-team/commit/a8a19ab1133025604e8f77d6ed215e4041e50e0d) |

The Fry-ndship [notebook](fry-ndship/solve.ipynb) contains the fitted model and its outputs. The [residual plot](fry-ndship/figures/residuals.png) shows the word. Its task README records the approach, dependencies, and reproduction steps. Submission time and a submitted commit link have not been recorded yet.

The Pipes, Leaks, and the Graph Beneath [notebook](pipes-leaks-graph/solve.ipynb) documents town-name cleanup, reconstruction of the route network, and the ranking by distinct connections. Its [task README](pipes-leaks-graph/README.md) records the submitted flag and the commit linked above.

## Team rules

- Code is written, committed and pushed **by us**. AI only for explaining, discussing, finding bugs we fix, and small snippets we understand (official rules).
- After every platform submission: **commit + push immediately** (limit 1 h) and put the commit link in the submission. Never force-push or squash.
- Never commit data, model weights or secrets. Note in the task README where the data comes from.
- Everyone should be able to explain every solved task.
