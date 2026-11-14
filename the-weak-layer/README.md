# The Weak Layer

- **Territory:** Europe / Classic ML & Data Science
- **Country:** Switzerland
- **Difficulty:** Easy
- **Answer type:** Evaluated Python file (`main.py`)
- **Status:** Practice output verified. Platform result and submitted commit unrecorded.

## Statement

Fit a decision tree classifier to labeled snow-pit observations (X), using `slab_released` as the target (y). The goal isto recover an uppercase word from the fitted tree's split structure and format it as `SIGMOID_<WORD>`.

## Approach

1. Fit a default `DecisionTreeClassifier` with `random_state=0`, using every column except `slab_released` as a feature.
2. Walk `tree_` in preorder depth-first order. Visit each split before its children and push the right child before the left child so the left subtree is visited first.
3. Skip leaves and take the first letter of each split feature. The practice tree gives spelling `DEMO`.

## Reproduce

Run from `the-weak-layer/` using a Python 3.12 environment.

```bash
python3 main.py
cat "test-output.txt"
```

Data: place the practice files `train-input.csv` and `train-output.txt` in the current directory. Note that file paths for submission and local development vary.

## Attempts

| # | What we tried | Result |
|---|---|---|
| 1 | Fit on the practice training split and traverse the tree using DFS. | `SIGMOID_DEMO` matched the supplied reference |

## Result

- Submitted: 11/14 18:54 Passed
- Commit: [2d8e923](https://github.com/maxpricop/lmml-team/commit/2d8e923c0bc76c9f19173e2704ebf168e7533fc6).
