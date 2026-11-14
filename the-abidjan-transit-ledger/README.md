# The Abidjan Transit Ledger

- **Continent:** Africa
- **Country:** Côte d'Ivoire
- **Domain:** Classic ML / NLP
- **Difficulty:** Medium
- **Points available:** 200
- **Answer type:** Evaluated file (`main.py`), flag released when both accuracy gates pass

## Objective

A small text classifier routes a clerk's request to one of 10 query templates (5 old e-commerce tasks, 5 new spatial/fleet tasks). The original checkpoint knows only the old task (old 1.00 / new 0.00); the fine-tuned checkpoint was trained on the new task only and forgot the old one (old 0.00 / new 1.00). Recover a single model that scores ≥ 0.85 on both tasks, run through the template's I/O contract.

## What went wrong: catastrophic forgetting

The fine-tuned model saw only new-task examples, so training overwrote what it had learned for the old task. This is a well-known problem when a neural network is trained on tasks one after another.

## Our fix: replay

The standard cure is to train on both tasks together ("replay"). `main.py` does this at run time:

1. **Data:** all labelled requests we are given: `dataset/old_task_sample.json` (40 old-task rows, provided for recovery) and `dataset/train-input.json` + `train-output.json` (250 rows covering both tasks), 290 rows in total.
2. **Features:** three blocks side by side:
   - the shipped `checkpoints/vectorizer.joblib` (already fitted, used as-is), scaled to unit length;
   - our own word TF-IDF (single words and word pairs);
   - our own character TF-IDF (2–5-letter chunks, robust to small spelling differences).
   Our own blocks make sure new-task words are covered even if the shipped vectorizer only learned the old vocabulary. If the shipped vectorizer can't be loaded, the script continues with its own features.
3. **Classifier:** logistic regression (C = 10) over all 10 labels; trains in about 2 seconds (limit 120 s).
4. **I/O exactly like `main_template.py`:** reads `test-input.json`, writes `predictions.json` with one `{"id", "label"}` per row, and saves `checkpoints/recovered_model.joblib`.

## Validation

| Check | Old task | New task |
|---|---|---|
| Cross-validation on the labelled rows (5-fold × 3) | 0.99 | 1.00 |
| Harness simulation: 30% of the public set hidden as `test-input.json`, a worst-case shipped vectorizer that only knows old-task words, `python main.py` with no arguments (6 random splits) | 1.00 | 0.94–1.00 |
| Same simulation without any shipped vectorizer | 1.00 | 0.94–1.00 |

Gates: 0.85 on each task.

## Attempts

| # | What we tried | Result |
|---|---|---|
| 1 | Shipped checkpoints as-is (reference numbers) | original: old 1.00 / new 0.00; fine-tuned: old 0.00 / new 1.00 |
| 2 | Replay retraining, unscaled shipped features + TF-IDF | old 1.00, new 0.91–1.00 |
| 3 | Same, shipped features scaled to unit length | old 1.00, new 0.94–1.00 (kept) |

## Reproduce

1. Put the organisers' files next to `main.py`: `checkpoints/` (original, fine-tuned and vectorizer `.joblib`), `dataset/` (`old_task_sample.json`, `train-input.json`, `train-output.json`) and `model_utils.py`.
2. Python with `scikit-learn`, `numpy`, `joblib`.
3. Graded run: `python main.py` (reads `test-input.json`, writes `predictions.json`).
4. Self-check: `python main.py --input dataset/train-input.json --output train_predictions.json`, then compare with `dataset/train-output.json` using `model_utils.accuracy_by_task`.