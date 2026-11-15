# Walu Season

- **Territory:** Oceania / Reinforcement Learning
- **Country:** Fiji
- **Difficulty:** Easy
- **Answer type:** Evaluated Python file (`main.py`)
- **Status:** Practice output verified. Successfully submitted on the platform.

## Statement

Find an algorithm for choosing the optimal fishing spot in order to reach at least 5300 kg per day. You are given a number of fishing spots and a number of total casts that can be distributed however in those 10 spots.

## Approach

1. Start each day with fresh statistics and cast once at each spot.
2. Track the cast count and total catch for each spot to calculate its average catch in kg per cast.
3. Cast at the spot with the highest average plus an exploration bonus. With the 1,000-cast budget, the implemented bonus is `6 * sqrt(log1p(999 / count) / count)`, where `count` is the spot's cast count. The bonus gives sparsely sampled spots more chances to reveal a school.

## Reproduce

Run from `walu-season/` and install the dependencies using a Python 3.12 environment.

```bash
python3 evaluation_script.py main.py --dataset train
```

Data: place `train-input.json`, `train-output.json`, `reef.py`, and `evaluation_script.py` alongside `main.py`.

## Attempts

| # | What we tried | Result |
|---|---|---|
| 1 | Greedy starter. Try each spot once, then pick the highest observed average. | 3,847.4 kg/day on the practice reef |
| 2 | Sequential halving. Sample the surviving spots in rounds, then spend the remaining casts at the winner. | 6,241.7 kg/day in the practice simulator |
| 3 | UCB-style score with a fixed exploration scale. | 6,944.6 kg/day in the practice evaluator, above the 5,300 kg/day threshold |

## Result

- Submitted: 11/14 11:38 Passed
- Commit: Unrecorded
