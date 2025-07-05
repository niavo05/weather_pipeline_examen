import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Charger les données
df = pd.read_csv("/home/adriano/data/processed/merged_weather.csv", parse_dates=["date"])

# Exploration
print(df.info())
print(df.describe())
print(df['city'].value_counts())

# Valeurs manquantes
print("Valeurs manquantes :")
print(df.isna().sum())

# Température moyenne par ville
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x="date", y="tavg", hue="city")
plt.title("Température moyenne par ville (sur 5 ans)")
plt.xlabel("Date")
plt.ylabel("Température moyenne (°C)")
plt.grid(True)
plt.tight_layout()

#changement en savefig
plt.savefig("/home/adriano/airflow/output/temperature_moyenne.png")
plt.close()

# Jours de pluie
df["rainy_day"] = df["prcp"] > 0
rain_stats = df.groupby("city")["rainy_day"].sum().reset_index()
rain_stats.columns = ["Ville", "Nombre de jours pluvieux"]
print(rain_stats)

# Variabilité des températures
print(df.groupby("city")["tavg"].std().reset_index(name="variabilité_temp_moy"))

# Villes les plus extrêmes
stats = df.groupby("city")["tavg"].agg(["mean", "std", "min", "max"]).reset_index()
stats["amplitude"] = stats["max"] - stats["min"]
print(stats.sort_values("std", ascending=False))
