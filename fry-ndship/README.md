# Fry-ndship

- **Continent:** Europe
- **Country:** Belgium
- **Domain:** Classic ML & Data Science
- **Difficulty:** Easy
- **Points available:** 100
- **Answer type:** Flag, supported by fitting code and a figure

## Objective

Model potato fields' edge lengths from their declared dimensions and find the word hidden in Mariette's measurements. The expected flag format is `SIGMOID_<WORD>`.

## Approach

Treat each field as approximately rectangular. Convert its area from hectares to square metres and estimate the short side as `short_m = area_ha * 10_000 / long_side_m`.

Fit ordinary least squares with an intercept:

`edge_m = intercept + b1 * long_side_m + b2 * short_m + residual`

The predictors use declared dimensions only. The on-site hedge measurement and the post-survey fencing quote are excluded because they are unavailable for prediction from declarations alone. The ditch measurement is also omitted to keep the model based on field dimensions; high correlation alone would not establish leakage.

Plot `residual = observed edge_m - fitted edge_m` against fitted edge length. The residuals form the word **REGRESSION** despite the high R².

## Reproduce

1. Download `potato_fields.csv` from the Fry-ndship task page on [the competition platform](https://sigmoid.academy/) and place it at `fry-ndship/data/potato_fields.csv`. The CSV is not tracked in Git.
2. Run locally on your own machine using a Python environment with `pandas`, `statsmodels`, `matplotlib`, and a Jupyter kernel such as `ipykernel`. The saved notebook used Python 3.14.10. Select your local environment as the notebook kernel. The root `requirements.txt` does not currently include `statsmodels` or `ipykernel`, so install those as well when preparing a fresh environment.
3. Set the notebook's working directory to your local repository root (the folder containing `fry-ndship/`), then open [solve.ipynb](solve.ipynb).
4. Restart the kernel, run all cells in order, and save the notebook with its outputs. The final plot reveals the word.

The notebook saves the PNG to `fry-ndship/figures/residuals.png`, relative to your local repository root. The `figures/` folder and saved plot are included in the task.

## Result

The saved fit reports:

- **In-sample R²:** 0.9983673004221523 (approximately 99.84%)
- **Intercept:** -0.000348
- **Long-side coefficient:** 1.900000
- **Estimated short-side coefficient:** 1.899994
- **Observed word:** REGRESSION
- **Flag:** `SIGMOID_REGRESSION`

These values are from the notebook's saved output. The plot shows why a high R² is not a substitute for inspecting residuals.

![Residuals plotted against fitted edge length spell REGRESSION](figures/residuals.png)

The platform requires the flag and a URL to the fitting code; reviewers also inspect the supporting figure. Submission time and a submitted commit link have not been recorded yet.
