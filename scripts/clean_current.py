import pandas as pd
from datetime import datetime

def clean_current():
    current_file = f"data/raw/current_{datetime.now().date()}.csv"
    df_curr = pd.read_csv(current_file)
    df_curr.to_csv("data/processed/current_cleaned.csv", index=False)
