-- ============================================================
-- Urban Bike Rental Demand & Operations Analysis
-- PostgreSQL Business Queries
-- Team: Targaryens
-- Author: T. Karthikeyan
-- ============================================================


-- ============================================================
-- TABLE
-- ============================================================

CREATE TABLE IF NOT EXISTS bike_sharing (
    date DATE,
    rented_bike_count INTEGER,
    hour INTEGER,
    temperature NUMERIC,
    humidity NUMERIC,
    wind_speed NUMERIC,
    visibility NUMERIC,
    dew_point_temperature NUMERIC,
    solar_radiation NUMERIC,
    rainfall NUMERIC,
    snowfall NUMERIC,
    seasons VARCHAR(30),
    holiday VARCHAR(30),
    functioning_day VARCHAR(30),
    year INTEGER,
    month INTEGER,
    day INTEGER,
    day_of_week VARCHAR(20),
    is_weekend BOOLEAN,
    time_category VARCHAR(20),
    weather_category VARCHAR(20)
);


-- ============================================================
-- Q1. Top 5 hours with highest average bike demand
-- ============================================================

SELECT
    hour,
    ROUND(
        AVG(rented_bike_count),
        2
    ) AS average_rentals
FROM bike_sharing
GROUP BY hour
ORDER BY average_rentals DESC
LIMIT 5;


-- ============================================================
-- Q2. Season with highest total rentals
-- ============================================================

SELECT
    seasons,
    SUM(rented_bike_count) AS total_rentals
FROM bike_sharing
GROUP BY seasons
ORDER BY total_rentals DESC
LIMIT 1;


-- ============================================================
-- Q3. Holiday vs Non-Holiday average rentals
-- ============================================================

SELECT
    holiday,
    ROUND(
        AVG(rented_bike_count),
        2
    ) AS average_rentals
FROM bike_sharing
GROUP BY holiday
ORDER BY average_rentals DESC;


-- ============================================================
-- Q4. Rental demand by rainfall category
-- ============================================================

SELECT
    weather_category,
    COUNT(*) AS observations,
    SUM(rented_bike_count) AS total_rentals,
    ROUND(
        AVG(rented_bike_count),
        2
    ) AS average_rentals
FROM bike_sharing
GROUP BY weather_category
ORDER BY average_rentals DESC;


-- ============================================================
-- Q5. Highest-demand Season + Time Category combination
-- ============================================================

SELECT
    seasons,
    time_category,
    COUNT(*) AS observations,
    SUM(rented_bike_count) AS total_rentals,
    ROUND(
        AVG(rented_bike_count),
        2
    ) AS average_rentals
FROM bike_sharing
GROUP BY
    seasons,
    time_category
ORDER BY average_rentals DESC
LIMIT 1;


-- ============================================================
-- Additional useful query:
-- Monthly demand
-- ============================================================

SELECT
    year,
    month,
    SUM(rented_bike_count) AS total_rentals,
    ROUND(
        AVG(rented_bike_count),
        2
    ) AS average_rentals
FROM bike_sharing
GROUP BY
    year,
    month
ORDER BY
    year,
    month;


-- ============================================================
-- Additional useful query:
-- Holiday vs functioning day
-- ============================================================

SELECT
    holiday,
    functioning_day,
    ROUND(
        AVG(rented_bike_count),
        2
    ) AS average_rentals
FROM bike_sharing
GROUP BY
    holiday,
    functioning_day
ORDER BY average_rentals DESC;