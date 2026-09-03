# 🚲 Urban Bike Rental Demand & Operations Analysis

> **A data-driven analysis of Seoul's bike-sharing system to identify demand patterns, operational challenges, weather impacts, and actionable business opportunities.**

---

## 📌 Project Overview

Urban bike-sharing systems need to maintain the right number of bikes at the right locations and at the right time.

This project analyzes **hourly bike rental demand in Seoul** using historical rental, weather, seasonal, and operational data.

The objective is to transform raw bike-sharing data into meaningful business insights that can support:

* 📈 Demand forecasting
* 🚲 Fleet allocation
* 🌦️ Weather-aware operations
* 🕐 Peak-hour planning
* 📅 Seasonal resource planning
* 💼 Data-driven business decisions

---

## 🎯 Business Objective

The primary objective of this project is to answer:

> **"When, why, and under what conditions does bike rental demand increase or decrease, and how can the business use these insights to improve operations?"**

### Key Questions

1. What are the peak bike rental hours?
2. Which seasons generate the highest demand?
3. How does weather affect bike rentals?
4. How does demand change throughout the year?
5. What is the difference between holiday and non-holiday demand?
6. How can bike availability and operational resources be optimized?

---

## 🗂️ Dataset

**Dataset:** Seoul Bike Sharing Demand Dataset

The dataset contains hourly observations of bike rentals in Seoul along with environmental and operational variables.

### Major Variables

| Category       | Variables                                     |
| -------------- | --------------------------------------------- |
| Rental Demand  | Rented Bike Count                             |
| Time           | Date, Hour                                    |
| Weather        | Temperature, Humidity, Wind Speed, Visibility |
| Weather Events | Rainfall, Snowfall                            |
| Environment    | Solar Radiation, Dew Point Temperature        |
| Calendar       | Seasons, Holiday                              |
| Operations     | Functioning Day                               |

---

## 🛠️ Technology Stack

| Technology         | Purpose                           |
| ------------------ | --------------------------------- |
| 🐍 Python          | Data analysis                     |
| 🐼 Pandas          | Data cleaning & manipulation      |
| 🔢 NumPy           | Numerical operations              |
| 📊 Matplotlib      | Data visualization                |
| 🍃 BeautifulSoup   | Seoul attraction data collection  |
| 🗄️ PostgreSQL     | Business-oriented SQL analysis    |
| 📗 Microsoft Excel | Pivot analysis & reporting        |
| 📊 Power BI        | Interactive dashboard             |
| 🐙 GitHub          | Version control & project sharing |

---

## 🔄 Project Workflow

```text
Raw Dataset
     ↓
Data Cleaning
     ↓
Exploratory Data Analysis
     ↓
Feature Engineering
     ↓
Weather & Seasonal Analysis
     ↓
Web Scraping — Seoul Attractions
     ↓
PostgreSQL Business Analysis
     ↓
Excel Reporting
     ↓
Power BI Dashboard
     ↓
Business Insights
     ↓
Recommendations
```

---

## 🔍 Data Analysis

The Python/Pandas stage covers:

* Dataset inspection
* Data type validation
* Missing-value analysis
* Duplicate detection
* Descriptive statistics
* Feature engineering
* Hourly demand analysis
* Seasonal analysis
* Monthly analysis
* Weather correlation analysis
* Holiday analysis
* Operational-day analysis

---

## 🌦️ Weather Analysis

Weather variables are analyzed to understand their relationship with bike demand.

Key factors include:

* Temperature
* Humidity
* Rainfall
* Snowfall
* Wind Speed
* Visibility
* Solar Radiation
* Dew Point Temperature

This helps identify how environmental conditions influence customer demand and operational requirements.

---

## 🕐 Demand Analysis

The project analyzes demand across:

### Hourly

Identifies peak and low-demand periods to support fleet redistribution and staffing.

### Monthly

Highlights changes in demand throughout the year.

### Seasonal

Compares Spring, Summer, Autumn, and Winter demand.

### Holiday

Compares demand between holidays and regular days.

---

## 🗄️ PostgreSQL Analysis

Five business-focused SQL queries are included to answer operational questions such as:

1. Peak rental hours
2. Seasonal demand
3. Weather impact
4. Holiday vs non-holiday demand
5. Monthly rental trends

SQL scripts are available in:

```text
sql/business_queries.sql
```

---

## 🕸️ Web Scraping

BeautifulSoup is used to collect information about Seoul attractions.

The scraper generates:

```text
seoul_attractions.csv
```

This additional dataset provides contextual information about Seoul locations that can potentially support future geographic and tourism-oriented analysis.

---

## 📊 Excel Analysis

The Excel workbook contains:

* Summary analysis
* Hourly demand analysis
* Seasonal analysis
* Monthly analysis
* Weather correlation analysis
* Pivot-style reporting
* Charts

### Output

```text
bike_sharing_analysis.xlsx
```

---

## 📈 Power BI Dashboard

### Dashboard Name

**Urban Bike Demand Operations Dashboard**

### Planned KPIs

* Total Rentals
* Average Hourly Rentals
* Peak Rental Hour
* Peak Season
* Weather Impact

### Dashboard Visuals

* Hourly demand trend
* Monthly demand trend
* Seasonal comparison
* Temperature vs rental demand
* Holiday comparison
* Hour × Day-of-Week demand matrix
* Interactive filters

---

## 💡 Key Findings

Based on the analysis:

* Evening hours represent the strongest rental-demand period.
* Summer records the highest overall demand among the seasons.
* Temperature has a positive relationship with bike rental demand.
* Rain and snowfall are associated with significantly lower rental demand.
* Demand varies considerably across months.
* Non-holiday days generally show stronger demand than holidays.
* Winter requires a different operational strategy because of substantially lower demand.

---

## 🚀 Business Recommendations

### 1. Optimize Evening Fleet Redistribution

Increase bike availability and redistribution efforts before the evening demand peak, particularly during the high-demand 17:00–20:00 period.

### 2. Implement Weather-Aware Operations

Use weather forecasts to dynamically adjust fleet movement, staffing, maintenance schedules, and operational resources during adverse weather conditions.

### 3. Adopt Seasonal Capacity Planning

Increase operational capacity during high-demand seasons while reducing unnecessary fleet movement and resource utilization during low-demand winter periods.

---

## 📁 Project Structure

```text
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
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/karthikeyan129/urban_bike.git
cd urban_bike
```

Install the required Python libraries:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Analysis

Run the Python analysis:

```bash
python python_analysis.py
```

Run the attraction scraper:

```bash
python scrape_attractions.py
```

The scraper generates:

```text
seoul_attractions.csv
```

---

## 👥 Project Information

**Team:** Targaryens
**Project:** Urban Bike Rental Demand and Operations Analysis
**Contributor:** T. Karthikeyan
**GitHub:** `karthikeyan129`

---

## 📌 Future Improvements

Possible extensions include:

* Machine-learning-based demand prediction
* Geographic station-level analysis
* Real-time demand forecasting
* Interactive map visualization
* Weather-based demand prediction
* Bike redistribution optimization
* Integration with live bike availability APIs

---

## ⭐ Project Outcome

This project demonstrates an end-to-end **data analytics workflow**, transforming raw bike-sharing data into operational insights using Python, SQL, Excel, web scraping, and Power BI.

The final objective is to help bike-sharing operators make **faster, smarter, and data-driven operational decisions**.
