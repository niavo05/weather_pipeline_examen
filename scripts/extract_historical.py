from meteostat import Daily, Stations
from datetime import datetime
import pandas as pd
import os

def extract_historical():
    cities = {
        "Antananarivo": (-18.8792, 47.5079),
        "Paris": (48.8566, 2.3522),
        "Tokyo": (35.6895, 139.6917)
    }

    start = datetime.now().replace(year=datetime.now().year - 5)
    end = datetime.now()

    all_data = []

    for city, (lat, lon) in cities.items():
        stations = Stations().nearby(lat, lon)
        station = stations.fetch(1)

        df = Daily(station, start, end).fetch()
        df = df.reset_index()
        df["city"] = city

        all_data.append(df)

    df_all = pd.concat(all_data)

    os.makedirs("data/raw", exist_ok=True)
    df_all.to_csv("data/raw/historical.csv", index=False)
