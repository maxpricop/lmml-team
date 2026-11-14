from __future__ import annotations

import argparse
import sys
from pathlib import Path

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import FeatureUnion, make_pipeline
from sklearn.preprocessing import Normalizer

import model_utils as mu

DATASET = Path("dataset")


class ShippedVectorizer(BaseEstimator, TransformerMixin):

    def __init__(self, vectorizer=None):
        self.vectorizer = vectorizer

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return self.vectorizer.transform(list(X))


def labelled_rows():
    rows = [(r["text"], r["label"]) for r in mu.load_records(DATASET / "old_task_sample.json")]
    texts = {r["id"]: r["text"] for r in mu.load_records(DATASET / "train-input.json")}
    for r in mu.load_records(DATASET / "train-output.json"):
        rows.append((texts[r["id"]], r["label"]))
    return [t for t, _ in rows], [l for _, l in rows]


def build_recovered_model():
    texts, labels = labelled_rows()
    blocks = [
        ("word", TfidfVectorizer(ngram_range=(1, 2), sublinear_tf=True)),
        ("char", TfidfVectorizer(analyzer="char_wb", ngram_range=(2, 5), sublinear_tf=True)),
    ]
    try:
        shipped = mu.load_vectorizer()
        shipped.transform(texts[:2])                     
        blocks.insert(0, ("shipped", make_pipeline(ShippedVectorizer(shipped), Normalizer())))
    except Exception as error:                        
        print(f"shipped vectorizer not used ({type(error).__name__})", file=sys.stderr)
    model = make_pipeline(FeatureUnion(blocks), LogisticRegression(C=10, max_iter=5000))
    model.fit(texts, labels)
    print(f"recovered model trained on {len(texts)} labelled requests ({len(blocks)} feature blocks)")
    return model


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="test-input.json", help="filename only, no path")
    parser.add_argument("--output", default="predictions.json", help="filename only, no path")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"input file not found: {input_path}", file=sys.stderr)
        return 2

    model = build_recovered_model()
    try:
        mu.save_model(model, mu.RECOVERED_MODEL_PATH)    
    except Exception:
        pass

    records = mu.load_records(input_path)
    ids = [r["id"] for r in records]
    texts = [r["text"] for r in records]
    labels = [str(label) for label in model.predict(texts)]
    predictions = [{"id": rid, "label": label} for rid, label in zip(ids, labels)]
    mu.save_records(predictions, Path(args.output))
    print(f"wrote {len(predictions)} predictions to {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())