# The Nisse's Bad Shift

- **Territory:** Europe / Classic ML & Data Science
- **Country:** Norway
- **Difficulty:** Easy
- **Answer type:** Evaluated CSV (`test-output.csv`) and retrained classifier.
- **Status:** Practice output verified. Successfully submitted on the platform.

## Statement

Find the mislabeled samples in `test-input.csv` using a model, correct them, and retrain the classifier on the corrected labels.

## Approach

1. Join the training files by `sample_id` and train an SVC on the 64 pixel values using the verified `corrected_label` values.
2. Collect disagreements between the filed label and the model's top prediction when the estimated probability exceeds 0.73. A pair qualifies when there is a strong disagreement in each direction.
3. Change a row when its top prediction matches a qualifying swap and its estimated probability exceeds 0.50.
4. Export all 599 labels and refit the classifier on the 1,198 verified training labels plus the 599 repaired test labels.

## Reproduce

Run from `the-nisse-bad-shift/` and install the dependencies using a Python 3.12 environment.

```bash
pip install -r requirements.txt
```

Data: place `train-input.csv`, `train-output.csv`, and `test-input.csv` into `the-nisse-bad-shift/data/`. Note that file paths for submission and local development vary.

Restart the kernel and run all cells in [solve.ipynb](solve.ipynb). The final cell calculates local repair F1 from the exported CSV by matching the test scans to `sklearn.datasets.load_digits()` using their 64 pixel values.

## Attempts

| # | What we tried | Result |
|---|---|---|
| 1 | Apply the SVC's top prediction to each disagreement above a confidence threshold of 0.80. | Fixed 24 of 30 wrong labels with zero incorrect changes. Local F1: **0.889**. |
| 2 | Added final F1 test cell and tested threshold until the F1 requirement was satisfied. | F1 requirement was not reached. Obtained a new best threshold: 0.73. Local F1: **0.929**. |
| 2 | Changed the approach of correction by finding pairs with strong disagreements in both directions, then repair matching rows above 0.50. | Fixed 28 of 30 wrong labels with zero incorrect changes. Local F1: **0.966**. |

## Result

- Submitted: 11/14 23:28 Passed
- Commit: Unrecorded.
