# ¡Feliz Navidad!

- **Continent:** Europe
- **Country:** Spain
- **Difficulty:** Easy
- **Answer type:** Flag

## Objective

Rebuild the charter company's Christmas board from 577 receipts. For each of the six souvenirs, mark which of the 21 pilots bought it at least once within the office's fair price range. Read the word formed by the filled cells and submit it in the format `SIGMOID_<WORD>`.

## Approach

1. **Look up the fair prices.** We read the six products from `office_price_guide.csv` and store each product's minimum and maximum price per unit.
2. **Check each receipt.** We divide `Total_paid_eur` by `Quantity` and set `fair_price` to `True` when the unit price falls within the product's range. Both endpoints count.
3. **Build the board.** We pivot the receipt table with `Product` as the rows, `Pilot_no` as the columns, and `fair_price` as the values. The `any` aggregation marks a cell if at least one receipt for that pair qualifies. We put the rows in `List_no` order and include pilot columns 1 through 21. Missing pairs are `False`.
4. **Read the word.** We plot the 6 × 21 board with Matplotlib. Nearest-neighbor interpolation keeps the cell edges sharp, and hiding the axes leaves the letter shapes visible.

## Reproduce

1. Download `office_price_guide.csv` and `purchases.csv` from the [task's Drive folder](https://drive.google.com/drive/folders/1w4N7Y662Ak5SYM2uF-K5vzJ28y41BlIQ?usp=sharing) and put both files in `feliz-navidad/data/`.
2. Select a Python environment with `pandas`, `matplotlib`, and `ipykernel` as the notebook kernel. The saved notebook used Python 3.12.3. The repository's `requirements.txt` includes `pandas` and `matplotlib`.
3. Set the notebook's working directory to `feliz-navidad/` so the `data/` and `figures/` paths resolve. Open [solve.ipynb](solve.ipynb), restart the kernel, and run all cells in order. The last code cell saves the board to `figures/crucio.png`.

## Result

- **Observed word:** CRUCIO
- **Flag:** `SIGMOID_CRUCIO`

![Christmas board with filled cells spelling CRUCIO](figures/crucio.png)
