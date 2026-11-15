"""Walu Season: starter main.py (the greedy baseline).

This file already speaks the evaluator's protocol. The part to change is the
Strategy class. As shipped it is pure greedy: try every spot once, then keep
going back to whichever spot has the best average so far. It runs end to end
and it does NOT reach the threshold.

Check it locally on the practice reef:

    python evaluation_script.py main.py --dataset train

Rules of the protocol (see task_description.md):
  * read test-input.json from the current directory (bare filename),
  * for every cast print one spot number on stdout, then read one line from
    stdin with the catch in kg,
  * start a fresh Strategy every day (spot numbers are reshuffled daily),
  * anything else you want to print goes to stderr.
"""

import json
import sys
from math import log1p, sqrt


class Strategy:
    EXPLORATION_SCALE_KG = 6.0

    def __init__(self, n_spots, n_casts):
        self.remaining_casts = n_casts
        self.casts = [0] * n_spots
        self.total = [0.0] * n_spots
        self.squared_total = [0.0] * n_spots

    def choose(self):
        best_spot = 0
        best_score = float("-inf")
        future_casts = self.remaining_casts - 1

        # Iterate through each spot once and find the best score
        for spot, count in enumerate(self.casts):
            if count == 0:
                return spot

            average = self.total[spot] / count
            variance = max(0.0, self.squared_total[spot] / count - average**2)

            # Use an UCB score
            exploration_weight = log1p(future_casts / count) / count
            spread_squared = 2 * variance + self.EXPLORATION_SCALE_KG**2
            score = average + sqrt(spread_squared * exploration_weight)

            if score > best_score:
                best_spot = spot
                best_score = score

        return best_spot

    def update(self, spot, catch):
        self.casts[spot] += 1
        self.total[spot] += catch


def main():
    with open("test-input.json") as f:
        rules = json.load(f)

    for _day in range(rules["n_days"]):
        agent = Strategy(rules["n_spots"], rules["n_casts"])
        for _cast in range(rules["n_casts"]):
            spot = agent.choose()
            print(spot, flush=True)
            catch = float(sys.stdin.readline())
            agent.update(spot, catch)


if __name__ == "__main__":
    main()
