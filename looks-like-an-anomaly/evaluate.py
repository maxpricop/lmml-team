import pandas as pd
from detector import Detector

X = pd.read_csv("data/train-input.csv")
y = pd.read_csv("data/train-output.csv")

det = Detector()
pred = pd.Series([det.update(row) >= 0.5 for row in X.to_dict("records")])

truth = y.is_anomaly == 1
tp = (pred & truth).sum()
fp = (pred & ~truth).sum()
fn = (~pred & truth).sum()
f1 = 2 * tp / (2 * tp + fp + fn)
rec = {t: pred[y.anomaly_type == t].mean() for t in ["point", "drift", "collective"]}
final = 100 * (0.80 * f1 + 0.05 * rec["point"] + 0.075 * rec["drift"] + 0.075 * rec["collective"])

print(f"FINAL {final:.2f}  F1 {f1:.3f}  (tp {tp}, fp {fp}, fn {fn})")
print(f"recall: point {rec['point']:.2f}, drift {rec['drift']:.2f}, collective {rec['collective']:.2f}")