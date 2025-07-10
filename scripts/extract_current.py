import requests
import pandas as pd
from datetime import datetime
import os

API_KEY = "a5ff598afec568f3e6713ae24ce378fb"

cities = {
    "Antananarivo": "Antananarivo",
    "Paris": "Paris",
    "Tokyo": "Tokyo",
    "India": "New Delhi",
    "USA": "Washington",
    "UK": "London",
    "Finland": "Helsinki",
    "Brazil": "Brasilia",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Germany": "Berlin",
    "Antarctica": "Antarctica",
    "Egypt": "Cairo",
    "South Africa": "Pretoria"
}



def extract_current():
    data = []
    for city in cities.values():
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        r = requests.get(url).json()
        data.append({
            "date": datetime.now().date(),
            "city": city,
            "tavg": r["main"]["temp"],
            "tmin": r["main"]["temp_min"],
            "tmax": r["main"]["temp_max"],
            "prcp": r.get("rain", {}).get("1h", 0.0)
        })

    df = pd.DataFrame(data)

    os.makedirs("data/raw", exist_ok=True)
    df.to_csv(f"data/raw/current_{datetime.now().date()}.csv", index=False)
