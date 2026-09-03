import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data_cleaned.csv")
print(df.info())
print(df.describe(include="all"))
print("Missing values:\n", df.isna().sum())
print("Duplicates:", df.duplicated().sum())

print("\nPeak hours:")
print(df.groupby("Hour")["Rented_Bike_Count"].mean().sort_values(ascending=False).head(10))

print("\nSeasonal demand:")
print(df.groupby("Seasons")["Rented_Bike_Count"].agg(["sum","mean"]).sort_values("sum", ascending=False))

print("\nMonthly demand:")
print(df.groupby("Month")["Rented_Bike_Count"].agg(["sum","mean"]).sort_values("mean", ascending=False))

weather = ["Temperature","Humidity","Wind_speed","Visibility",
           "Dew_point_temperature","Solar_Radiation","Rainfall","Snowfall"]
print("\nWeather correlations:")
print(df[weather + ["Rented_Bike_Count"]].corr()["Rented_Bike_Count"].sort_values(ascending=False))
