# Urban Bike Demand Operations Dashboard

## Recommended KPI cards
- Total Rentals
- Average Hourly Rentals
- Peak Hour
- Peak Season
- Rainfall / Snowfall impact

## Recommended visuals
1. Line chart: rentals by hour
2. Column chart: rentals by season
3. Line/column chart: monthly rentals
4. Scatter: temperature vs rentals
5. Column chart: holiday vs non-holiday
6. Matrix: hour × day of week
7. Slicers: Season, Holiday, Functioning Day, Month

## Suggested measures
Total Rentals = SUM(bike_sharing[Rented_Bike_Count])
Average Rentals = AVERAGE(bike_sharing[Rented_Bike_Count])
Peak Hour = TOPN(1, VALUES(bike_sharing[Hour]), [Average Rentals], DESC)
