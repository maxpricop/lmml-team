from pathlib import Path
import pandas as pd
import csv

def repair_name(name):
    try:
        return name.encode("latin-1").decode("utf-8")
    except (UnicodeEncodeError, UnicodeDecodeError):
        return name

test_mode = Path("test-input.csv").is_file()
input_file = "test-input.csv" if test_mode else "train-input.csv"
output_file = "test-output.csv" if test_mode else "train-output.csv"

readings = pd.read_csv(input_file, sep=";", comment="#", encoding="utf-8")

temperature_text = readings["temperature_raw"].astype(str).str.replace(",", ".", regex=False)
readings["temperature_c"] = pd.to_numeric(temperature_text)
fahrenheit_rows = readings["unit"].eq("F")
fahrenheit_values = readings.loc[fahrenheit_rows, "temperature_c"]
readings.loc[fahrenheit_rows, "temperature_c"] = (fahrenheit_values - 32) * 5 / 9

readings["station_name"] = readings["station_name"].map(repair_name)

readings = readings.drop_duplicates(subset="reading_id")
readings = readings.sort_values("reading_id")

readings.to_csv(
    output_file,
    columns=["reading_id", "station_name", "temperature_c", "reading_date"],
    index=False,
    float_format="%.1f",
    encoding="utf-8",
    quoting=csv.QUOTE_NONE,
)
