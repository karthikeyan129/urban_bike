Urban Bike Demand Operations Dashboard

## Dashboard Objective

The dashboard analyzes Seoul bike rental demand and identifies the
best periods and conditions for fleet planning and operational
resource allocation.

---

## Dataset

Source:

Seoul Bike Sharing Demand Dataset

Main table:

`bike_sharing`

---

# KPI Cards

The dashboard should contain these four primary KPI cards:

1. Total Bike Rentals
2. Average Hourly Rentals
3. Peak Rental Hour
4. Highest-Demand Season

---

# Required Visuals

## 1. Rentals by Hour

Chart:
Line chart

Axis:
`Hour`

Values:
`Average Rentals`

Purpose:
Identify peak rental hours.

---

## 2. Rentals by Season

Chart:
Column chart

Axis:
`Seasons`

Values:
`Total Rentals`

Purpose:
Compare seasonal demand.

---

## 3. Temperature vs Bike Rentals

Chart:
Scatter chart

X-axis:
`Temperature`

Y-axis:
`Rented_Bike_Count`

Purpose:
Understand the relationship between temperature
and bike demand.

---

## 4. Rainfall vs Bike Rentals

Chart:
Scatter chart

X-axis:
`Rainfall`

Y-axis:
`Rented_Bike_Count`

Purpose:
Understand how rainfall affects demand.

---

## 5. Holiday vs Non-Holiday Usage

Chart:
Column chart

Axis:
`Holiday`

Values:
`Average Rentals`

Purpose:
Compare normal days and holidays.

---

## 6. Time Category vs Rentals

Chart:
Column chart

Axis:
`Time_Category`

Values:
`Average Rentals`

Purpose:
Compare Morning, Afternoon, Evening and Night demand.

---

# Required Slicers

Add the following slicers:

- Seasons
- Holiday
- Time_Category
- Weather_Category

Optional:

- Month
- Year
- Functioning_Day

---

# DAX Measures

## Total Bike Rentals

```DAX
Total Bike Rentals =
SUM(bike_sharing[Rented_Bike_Count])
```

## Average Hourly Rentals

```DAX
Average Hourly Rentals =
AVERAGE(bike_sharing[Rented_Bike_Count])
```

## Peak Rental Hour

```DAX
Peak Rental Hour =
VAR PeakTable =
    TOPN(
        1,
        SUMMARIZE(
            ALL(bike_sharing[Hour]),
            bike_sharing[Hour],
            "AverageDemand",
            CALCULATE(
                AVERAGE(bike_sharing[Rented_Bike_Count])
            )
        ),
        [AverageDemand],
        DESC
    )
RETURN
    FORMAT(
        MAXX(
            PeakTable,
            bike_sharing[Hour]
        ),
        "00"
    ) & ":00"
```

## Highest-Demand Season

```DAX
Highest-Demand Season =
VAR SeasonTable =
    TOPN(
        1,
        SUMMARIZE(
            ALL(bike_sharing[Seasons]),
            bike_sharing[Seasons],
            "TotalDemand",
            CALCULATE(
                SUM(bike_sharing[Rented_Bike_Count])
            )
        ),
        [TotalDemand],
        DESC
    )
RETURN
    MAXX(
        SeasonTable,
        bike_sharing[Seasons]
    )
```

# Dashboard Business Questions

The dashboard must answer:

When is bike demand highest?
Which season generates the most rentals?
Does rainfall reduce bike usage?
Does temperature influence demand?
Are holidays different from normal days?
Which time category has the highest demand?

Final Business Decision

The dashboard should identify:

Best season
Best time of day
Suitable weather conditions
Operational periods requiring maximum bike availability

Recommendations

Exactly three recommendations should be presented in the final report.

1. Optimize fleet availability before the highest-demand hours.
2. Use weather information to adjust operational planning during
   rainfall and adverse conditions.
3. Increase seasonal capacity during high-demand periods and reduce
   unnecessary resource allocation during low-demand periods.

---