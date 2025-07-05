import pandas as pd
import os

def merge_data():
    df_hist = pd.read_csv("data/processed/historical_cleaned.csv")
    df_curr = pd.read_csv("data/processed/current_cleaned.csv")

    df_final = pd.concat([df_hist, df_curr], ignore_index=True)

    os.makedirs("data/processed", exist_ok=True)
    df_final.to_csv("data/processed/merged_weather.csv", index=False)
