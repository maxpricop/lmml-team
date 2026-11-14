"""Shared contract between generate_dataset.py, main_template.py and
evaluation_script.py: the label space, the featurizer and the
save/load/predict helpers around the shared text classifier.

The "model" in this task is a compact stand-in for a text-to-SQL system: a
small neural classifier that maps a natural-language request to one of ten
query-template labels, five per task. Template-id accuracy is what the
evaluator scores instead of literal SQL text, which keeps everything
deterministic, CPU-only and dependency-light.
"""
from __future__ import annotations

import json
from pathlib import Path

import joblib
import numpy as np

OLD_LABELS = [
    "OLD_JOIN_CUSTOMER_ORDERS",
    "OLD_GROUPBY_REVENUE_BY_CATEGORY",
    "OLD_CRUD_INSERT_ORDER",
    "OLD_CRUD_UPDATE_INVENTORY",
    "OLD_CRUD_DELETE_ACCOUNT",
]
NEW_LABELS = [
    "NEW_SPATIAL_NEAREST_WAREHOUSE",
    "NEW_SPATIAL_WITHIN_RADIUS",
    "NEW_WINDOW_LAG_DELIVERY_DELAY",
    "NEW_WINDOW_LEAD_NEXT_SHIPMENT",
    "NEW_WINDOW_PARTITION_RANK_FLEET",
]
ALL_LABELS = OLD_LABELS + NEW_LABELS

HERE = Path(__file__).parent
CHECKPOINTS_DIR = HERE / "checkpoints"
VECTORIZER_PATH = CHECKPOINTS_DIR / "vectorizer.joblib"
ORIGINAL_MODEL_PATH = CHECKPOINTS_DIR / "original_model.joblib"
FINETUNED_MODEL_PATH = CHECKPOINTS_DIR / "finetuned_model.joblib"
RECOVERED_MODEL_PATH = CHECKPOINTS_DIR / "recovered_model.joblib"


def load_vectorizer(path: Path = VECTORIZER_PATH):
    return joblib.load(path)


def load_model(path: Path):
    return joblib.load(path)


def save_model(model, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, path)


def featurize(vectorizer, texts: list[str]) -> np.ndarray:
    return vectorizer.transform(texts).toarray()


def predict_labels(model, vectorizer, texts: list[str]) -> list[str]:
    X = featurize(vectorizer, texts)
    return list(model.predict(X))


def load_records(path: Path) -> list[dict]:
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def save_records(records: list[dict], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(records, fh, indent=2, ensure_ascii=False)
        fh.write("\n")


def task_of(label: str) -> str:
    return "old" if label in OLD_LABELS else "new"


def accuracy_by_task(gold: dict[str, str], pred: dict[str, str]) -> dict[str, float]:
    """gold/pred: request id -> label. Missing predictions count as wrong."""
    totals = {"old": 0, "new": 0}
    correct = {"old": 0, "new": 0}
    for rid, gold_label in gold.items():
        task = task_of(gold_label)
        totals[task] += 1
        if pred.get(rid) == gold_label:
            correct[task] += 1
    return {
        "old": correct["old"] / totals["old"] if totals["old"] else 0.0,
        "new": correct["new"] / totals["new"] if totals["new"] else 0.0,
    }
