# Looks like an anomaly!

- **Continent:** Europe
- **Country:** Albania
- **Domain:** Classic ML & Data Science
- **Difficulty:** Medium
- **Points available:** 200
- **Answer type:** Evaluated file (`detector.py`), flag released at a score of 70/100 or more
- **Platform status:** Submitted

## Objective

Build a streaming anomaly detector for sensors in an Albanian bunker. The organizer's harness calls `Detector.update(reading)` once per minute and the detector must return an anomaly score between 0 and 1 using only past readings. Scores of 0.5 or more count as alarms. The final score is `100 × (0.80 × F1 + 0.05 × point recall + 0.075 × drift recall + 0.075 × collective recall)`. The evaluator runs Python 3.11 with numpy, pandas and scikit-learn only, on CPU, with a 60-second limit.

## Files

| File | Purpose |
|---|---|
| `detector.py` | The solution: the `Detector` class submitted to the platform. Standard library only. |
| `evaluate.py` | Local check: feeds the training readings to `Detector` one at a time and prints the task's score formula. |
| `data/` | `train-input.csv` and `train-output.csv` (not tracked in Git). |

## Data

`train-input.csv` has 3600 readings (one per minute, about 2.5 days) from two zones, `north_gallery` and `south_gallery`, in blocks of 900 minutes. Each reading has temperature, humidity, vibration, sound level, air pressure and CO2. `train-output.csv` marks 287 readings (8%) as anomalies:

| Type | Readings | What happens |
|---|---|---|
| point | 7 | one sensor (vibration, sound or CO2) spikes to about 15–25 times its normal spread for one minute |
| drift | 3 × 60 | one sensor (humidity, CO2 or pressure) moves steadily away from normal, up to about 11 times its spread |
| collective | 3 × 30–35 | vibration, sound and CO2 all rise together by about 4–5 times their spread |

Normal readings are noise around a stable level. Temperature and pressure also follow a slow daily cycle.

## Attempts

All scores are local, computed with `evaluate.py` on the training data using the task's formula.

| Attempt | Change | Score | F1 | False alarms |
|---|---|---|---|---|
| 1 | z-score baseline that stops learning completely when a reading looks suspicious | 72.6 | 0.665 | 261 |
| 2 | Baseline keeps learning slowly during suspicious readings; drift alarm needs the current reading on the same side | 96.7 | 0.968 | 1 |
| 3 | Warm-up: each zone learns its normal level from its first 50 readings | 96.7 | 0.968 | 1 |

### First attempt: frozen baseline

The first detector stopped updating its idea of "normal" whenever a reading looked suspicious. After the first drift it never updated again, so the daily temperature and pressure cycle slowly looked abnormal and caused 261 false alarms. The drift alarm also stayed on for about 10 minutes after each drift ended.

### Second attempt: slow learning instead of freezing

The baseline now learns 20 times slower from suspicious readings but never stops completely, and it never learns from spikes. The drift alarm only fires while the current reading is on the same side as the recent average, so it switches off as soon as the sensor returns to normal. This removed almost all false alarms.

### Third attempt: warm-up

Starting from the training data's normal levels would fail if the test data has different levels (the score dropped to 60.9 when we shifted all sensors by 3 spreads). With a warm-up, each zone learns its own levels from its first 50 readings, and shifted data now scores 96.7 as well.

## How the detector works

For each zone and sensor, the detector keeps a running mean and variance (exponential moving average). Each reading is turned into a z-score: how many normal spreads it is away from the baseline. Then it runs three checks:

- **Point:** the largest absolute z-score of any sensor, with the alarm line at 6.
- **Collective:** z(vibration) + z(sound) + z(CO2), with the alarm line at 7. Three moderate rises add up to a clear signal.
- **Drift:** a running average of each sensor's z-score (about the last 10 readings), with the alarm line at 2.5.

Each check is divided by its alarm line, so 1.0 means exactly at the line. The detector takes the largest value `r` and returns `r / (1 + r)`, which is 0.5 exactly at the alarm line and always between 0 and 1.

| Parameter | Value | Meaning |
|---|---|---|
| `POINT_Z` | 6 | single-sensor alarm line |
| `COLL_Z` | 7 | collective alarm line |
| `DRIFT_Z` | 2.5 | drift alarm line |
| `DRIFT_ALPHA` | 0.1 | drift average covers about the last 10 readings |
| `BASE_ALPHA` | 0.01 | baseline covers about the last 100 readings |
| `WARMUP` | 50 | readings per zone used to learn the starting levels |

The detector uses only the Python standard library, so it runs on the evaluator without installing anything. One pass over the training data takes about 0.05 seconds.

### Robustness checks

| Check | Score |
|---|---|
| First half of the data only | 96.0 |
| Second half of the data only | 97.3 |
| Noise × 0.8 / × 1.3 | 95.7 / 96.6 |
| All sensor levels shifted −3 to +5 spreads | 96.7 |
| Each parameter changed by ±15% | 92.7–97.7 |

The 17 missed readings are the first minutes of each drift, where the sensor has barely moved yet.

## Reproduce

1. Download `train-input.csv` and `train-output.csv` from the task's [Google Drive folder](https://drive.google.com/drive/folders/14AMHetQATgeB-wSm0-Da10NffyxOGQVo) and place them in `looks-like-an-anomaly/data/`. The CSVs are not tracked in Git.
2. Use a Python environment with `pandas` (needed only by `evaluate.py`; `detector.py` itself uses only the standard library).
3. From the `looks-like-an-anomaly/` folder, run `python evaluate.py`. It should print `FINAL 96.71  F1 0.968  (tp 270, fp 1, fn 17)` and recall of 1.00 for point, 0.91 for drift and 1.00 for collective anomalies.
4. Submit `detector.py` on the platform.

## Result

- **Local score (training data):** 96.71
- **F1:** 0.968
- **Recall:** point 1.00, drift 0.91, collective 1.00
- **Submitted file:** `detector.py`