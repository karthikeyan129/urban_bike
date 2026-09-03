# 🚲 Urban Bike Rental Demand & Operations Analysis

> Data-driven analysis of Seoul's bike-sharing demand to identify
> peak rental periods, seasonal patterns, weather effects and
> operational opportunities.

---

## 📌 Project Overview

This project analyzes hourly bike rental demand in Seoul using
historical rental, weather, seasonal and calendar information.

The goal is to identify when demand is highest and provide
data-driven recommendations for bike fleet and operational planning.

---

## 🎯 Business Objectives

The project answers the following questions:

1. Which hours have the highest bike demand?
2. Which season generates the most rentals?
3. Do holidays affect bike usage?
4. How does rainfall affect bike demand?
5. Which season and time category produce the highest demand?
6. When should the company provide the maximum number of bikes?

---

## 📊 Dataset

**Dataset:** Seoul Bike Sharing Demand Dataset

The dataset contains hourly bike rental observations along with:

- Rental count
- Hour
- Temperature
- Humidity
- Wind speed
- Visibility
- Dew point temperature
- Solar radiation
- Rainfall
- Snowfall
- Seasons
- Holiday
- Functioning Day

---

## 🛠️ Technologies

| Technology | Purpose |
|---|---|
| Python | Data analysis |
| Pandas | Data cleaning and analysis |
| NumPy | Numerical processing |
| BeautifulSoup | Web scraping |
| Requests | Web requests |
| PostgreSQL | SQL business analysis |
| Excel | Pivot analysis and charts |
| Power BI | Interactive dashboard |
| GitHub | Version control |

---

## 🔄 Project Workflow

```text
Raw Dataset
    ↓
Data Cleaning
    ↓
Feature Engineering
    ↓
Time & Weather Categorization
    ↓
Business Analysis
    ↓
BeautifulSoup Web Scraping
    ↓
PostgreSQL Analysis
    ↓
Excel Reporting
    ↓
Power BI Dashboard
    ↓
Business Recommendations
🐍 Python Analysis

The Python stage performs:

Dataset inspection
Data type validation
Missing-value checking
Duplicate checking
Date conversion
Invalid-value handling
Feature engineering
Time category creation
Weather category creation
Hourly demand analysis
Seasonal analysis
Holiday analysis
Rainfall analysis
Weather correlation analysis
Time Categories
Hours	Category
05:00–11:00	Morning
12:00–16:00	Afternoon
17:00–21:00	Evening
Remaining hours	Night
Weather Categories
Rainfall	Category
0 mm	No Rain
>0 to 5 mm	Light Rain
>5 mm	Heavy Rain
🕸️ Web Scraping

BeautifulSoup is used to collect Seoul attraction information
from the official Visit Seoul attractions page.

The output contains:

Attraction
Category
Area
URL

Output:

seoul_attractions.csv

Source:

https://english.visitseoul.net/attractions
🗄️ PostgreSQL

Five business queries are included:

Top 5 hours by average demand
Highest-demand season
Holiday vs non-holiday average demand
Rainfall category comparison
Highest-demand season + time category

SQL file:

sql/business_queries.sql
📗 Excel

The Excel workbook contains:

Rentals by hour
Rentals by season
Holiday vs non-holiday analysis
Conditional formatting
Hourly demand chart

Output:

bike_sharing_analysis.xlsx
📊 Power BI

Dashboard:
Urban Bike Demand Operations Dashboard

KPIs
Total Bike Rentals
Average Hourly Rentals
Peak Rental Hour
Highest-Demand Season
Visuals
Rentals by Hour
Rentals by Season
Temperature vs Rentals
Rainfall vs Rentals
Holiday vs Non-Holiday
Time Category vs Rentals
Slicers
Season
Holiday
Time Category
Weather Category
💡 Key Findings

The analysis identifies:

Peak rental hours
Highest-demand season
Holiday demand differences
Weather-related demand changes
Highest-demand season and time combination

See:
reports/FINAL_FINDINGS.md
🚀 Business Recommendations

The final report provides exactly three recommendations based
on the analysis results.

📁 Project Structure
urban_bike/
│
├── data/
│   ├── SeoulBikeData.csv
│   ├── data_cleaned.csv
│   └── seoul_attractions.csv
│
├── python/
│   └── python_analysis.py
│
├── web_scraping/
│   └── scrape_attractions.py
│
├── sql/
│   └── business_queries.sql
│
├── excel/
│   └── bike_sharing_analysis.xlsx
│
├── powerbi/
│   └── Urban_Bike_Demand_Operations_Dashboard.pbix
│
├── reports/
│   └── FINAL_FINDINGS.md
│
├── requirements.txt
├── .gitignore
└── README.md
⚙️ Installation

Clone the repository:

git clone https://github.com/karthikeyan129/urban_bike.git
cd urban_bike

Install Python dependencies:

pip install -r requirements.txt
▶️ Run Python Analysis
python python_analysis.py

This generates:

data_cleaned.csv
▶️ Run Web Scraper
python scrape_attractions.py

This generates:

seoul_attractions.csv
👥 Project Information

Team: Targaryens

Project: Urban Bike Rental Demand and Operations Analysis

Contributor: T. Karthikeyan

GitHub: karthikeyan129

⭐ Project Outcome

This project demonstrates an end-to-end data analytics workflow
using Python, BeautifulSoup, PostgreSQL, Excel and Power BI.

The analysis converts historical bike-sharing data into
actionable operational insights for fleet planning and
resource allocation.
