from meteostat import Daily, Stations
from datetime import datetime
import pandas as pd
import os

def extract_historical():
    cities = {
    "Antananarivo": (-18.8792, 47.5079),
    "Paris": (48.8566, 2.3522),
    "Tokyo": (35.6895, 139.6917),
    "India": (28.6139, 77.2090),
    "USA": (38.9072, -77.0369),
    "UK": (51.5074, -0.1278),
    "Finland": (60.1695, 24.9354),
    "Brazil": (-15.7939, -47.8828),
    "Italy": (41.9028, 12.4964),
    "Spain": (40.4168, -3.7038),
    "Germany": (52.5200, 13.4050),
    "Antarctica": (-75.250973, -0.071389),
    "Egypt": (30.0444, 31.2357),
    "South Africa": (-25.7479, 28.2293)
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
