import pandas as pd

def clean_historical():
    df_hist = pd.read_csv("data/raw/historical.csv")
    df_hist = df_hist[["time", "city", "tavg", "tmin", "tmax", "prcp"]]
    df_hist.rename(columns={"time": "date"}, inplace=True)
    df_hist.to_csv("data/processed/historical_cleaned.csv", index=False)
