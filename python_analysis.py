import pandas as pd
from pathlib import Path

# ============================================================
# Urban Bike Rental Demand & Operations Analysis
# Team: Targaryens
# Author: T. Karthikeyan
# ============================================================

INPUT_FILE = "SeoulBikeData.csv"
OUTPUT_FILE = "data_cleaned.csv"

# ------------------------------------------------------------
# 1. Load dataset
# ------------------------------------------------------------

df = pd.read_csv(INPUT_FILE, encoding="latin1")

print("=" * 70)
print("DATASET OVERVIEW")
print("=" * 70)

print(f"Rows    : {df.shape[0]}")
print(f"Columns : {df.shape[1]}")
print("\nColumns:")
print(df.columns.tolist())

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nDescriptive statistics:")
print(df.describe(include="all"))


# ------------------------------------------------------------
# 2. Standardize column names
# ------------------------------------------------------------

df.columns = (
    df.columns
    .str.strip()
    .str.replace(" ", "_")
    .str.replace("(", "", regex=False)
    .str.replace(")", "", regex=False)
)

print("\nStandardized columns:")
print(df.columns.tolist())


# ------------------------------------------------------------
# 3. Date conversion
# ------------------------------------------------------------

df["Date"] = pd.to_datetime(
    df["Date"],
    format="%d/%m/%Y",
    errors="coerce"
)

invalid_dates = df["Date"].isna().sum()

print(f"\nInvalid dates after conversion: {invalid_dates}")


# ------------------------------------------------------------
# 4. Numeric type conversion
# ------------------------------------------------------------

numeric_columns = [
    "Rented_Bike_Count",
    "Hour",
    "Temperature",
    "Humidity",
    "Wind_speed",
    "Visibility",
    "Dew_point_temperature",
    "Solar_Radiation",
    "Rainfall",
    "Snowfall"
]

for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")


# ------------------------------------------------------------
# 5. Remove invalid records
# ------------------------------------------------------------

before = len(df)

df = df.dropna(
    subset=[
        "Date",
        "Rented_Bike_Count",
        "Hour",
        "Seasons",
        "Holiday",
        "Functioning_Day"
    ]
)

# Rental count cannot be negative
df = df[df["Rented_Bike_Count"] >= 0]

# Hour must be between 0 and 23
df = df[df["Hour"].between(0, 23)]

after = len(df)

print(f"\nRows before cleaning: {before}")
print(f"Rows after cleaning : {after}")
print(f"Rows removed        : {before - after}")


# ------------------------------------------------------------
# 6. Remove duplicates
# ------------------------------------------------------------

duplicates = df.duplicated().sum()

print(f"Duplicate rows found: {duplicates}")

df = df.drop_duplicates()


# ------------------------------------------------------------
# 7. Feature engineering
# ------------------------------------------------------------

df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Day"] = df["Date"].dt.day
df["Day_of_Week"] = df["Date"].dt.day_name()

df["Is_Weekend"] = df["Date"].dt.dayofweek >= 5


# ------------------------------------------------------------
# 8. Create Time_Category
#
# 05:00-11:00 = Morning
# 12:00-16:00 = Afternoon
# 17:00-21:00 = Evening
# Remaining     = Night
# ------------------------------------------------------------

def get_time_category(hour):

    if 5 <= hour <= 11:
        return "Morning"

    elif 12 <= hour <= 16:
        return "Afternoon"

    elif 17 <= hour <= 21:
        return "Evening"

    else:
        return "Night"


df["Time_Category"] = df["Hour"].apply(get_time_category)


# ------------------------------------------------------------
# 9. Create Weather_Category
#
# No Rain     = 0 mm
# Light Rain  = >0 and <=5 mm
# Heavy Rain  = >5 mm
#
# These thresholds are simple operational categories based
# on the rainfall distribution in the dataset.
# ------------------------------------------------------------

def get_weather_category(rainfall):

    if rainfall == 0:
        return "No Rain"

    elif rainfall <= 5:
        return "Light Rain"

    else:
        return "Heavy Rain"


df["Weather_Category"] = df["Rainfall"].apply(
    get_weather_category
)


# ------------------------------------------------------------
# 10. Save cleaned dataset
# ------------------------------------------------------------

df.to_csv(
    OUTPUT_FILE,
    index=False,
    encoding="utf-8"
)

print(f"\nCleaned dataset saved as: {OUTPUT_FILE}")


# ------------------------------------------------------------
# 11. Required Business Analysis
# ------------------------------------------------------------

total_rentals = df["Rented_Bike_Count"].sum()

average_hourly = df["Rented_Bike_Count"].mean()

hourly_demand = (
    df.groupby("Hour")["Rented_Bike_Count"]
    .mean()
    .sort_values(ascending=False)
)

busiest_hour = hourly_demand.index[0]

season_demand = (
    df.groupby("Seasons")["Rented_Bike_Count"]
    .sum()
    .sort_values(ascending=False)
)

highest_season = season_demand.index[0]

holiday_demand = (
    df.groupby("Holiday")["Rented_Bike_Count"]
    .mean()
)

weather_demand = (
    df.groupby("Weather_Category")["Rented_Bike_Count"]
    .agg(["count", "sum", "mean"])
    .sort_values("mean", ascending=False)
)

season_time_demand = (
    df.groupby(["Seasons", "Time_Category"])
    ["Rented_Bike_Count"]
    .mean()
    .sort_values(ascending=False)
)


# ------------------------------------------------------------
# 12. Print Results
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("BUSINESS ANALYSIS RESULTS")
print("=" * 70)

print(f"\nTotal Bike Rentals: {total_rentals:,}")

print(f"\nAverage Hourly Rentals: {average_hourly:.2f}")

print(f"\nBusiest Rental Hour: {busiest_hour:02d}:00")

print(f"\nHighest-Demand Season: {highest_season}")


print("\nTop 5 Hours by Average Demand:")
print(hourly_demand.head(5))


print("\nSeasonal Demand:")
print(season_demand)


print("\nHoliday vs Non-Holiday Average:")
print(holiday_demand)


print("\nRainfall Category Comparison:")
print(weather_demand)


print("\nHighest-Demand Season + Time Category:")
print(season_time_demand.head(10))


# ------------------------------------------------------------
# 13. Weather correlation
# ------------------------------------------------------------

weather_columns = [
    "Temperature",
    "Humidity",
    "Wind_speed",
    "Visibility",
    "Dew_point_temperature",
    "Solar_Radiation",
    "Rainfall",
    "Snowfall",
    "Rented_Bike_Count"
]

print("\nWeather Correlations:")
print(
    df[weather_columns]
    .corr()["Rented_Bike_Count"]
    .sort_values(ascending=False)
)


# ------------------------------------------------------------
# 14. Final validation
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("FINAL VALIDATION")
print("=" * 70)

print("Rows:", len(df))
print("Columns:", len(df.columns))
print("Missing values:", df.isnull().sum().sum())
print("Duplicates:", df.duplicated().sum())

print("\nTime categories:")
print(df["Time_Category"].value_counts())

print("\nWeather categories:")
print(df["Weather_Category"].value_counts())

print("\nAnalysis completed successfully.")
