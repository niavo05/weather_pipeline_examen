import pandas as pd
from datetime import datetime
import os

def clean_and_merge():
    df_hist = pd.read_csv("data/raw/historical.csv")
    df_curr = pd.read_csv(f"data/raw/current_{datetime.now().date()}.csv")

    df_hist = df_hist[["time", "city", "tavg", "tmin", "tmax", "prcp"]]
    df_hist.rename(columns={"time": "date"}, inplace=True)

    df_final = pd.concat([df_hist, df_curr], ignore_index=True)

    # Crée le dossier data/processed s'il n'existe pas
    os.makedirs("data/processed", exist_ok=True)

    df_final.to_csv("data/processed/merged_weather.csv", index=False)
