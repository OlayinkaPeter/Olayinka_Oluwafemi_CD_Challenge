## On which day of the week do we on average have the longest trip?

``` sql
SELECT
    DATE_FORMAT(start_time, '%W') AS day_of_week,
    AVG(duration_minutes) AS average_trip_duration
FROM
    bikerdatav2
GROUP BY
    day_of_week
ORDER BY
    average_trip_duration DESC
LIMIT 1;
```


## What month/year has the most bike trips and what is the count of the trips?

``` sql
SELECT
    DATE_FORMAT(start_time, '%Y-%m') AS month_year,
    COUNT(*) AS trip_count
FROM
    bikerdatav2
GROUP BY
    month_year
ORDER BY
    trip_count DESC
LIMIT 1;
```

####  We can use `EXTRACT` for year specifically

``` sql
SELECT
    EXTRACT(YEAR FROM start_time) AS year,
    COUNT(*) AS trip_count
FROM
    bikerdatav2
GROUP BY
    year
ORDER BY
    trip_count DESC
LIMIT 1;
```


## In the same table, return which particular trip has longest duration and the trip that has the shortest duration (return all the information(columns) on the table for this record)

``` sql
SELECT *
FROM bikerdatav2
WHERE start_station_id != end_station_id
  AND duration_minutes = (
    SELECT MAX(duration_minutes)
    FROM bikerdatav2
    WHERE start_station_id != end_station_id
  )
UNION ALL
SELECT *
FROM bikerdatav2
WHERE start_station_id != end_station_id
  AND duration_minutes = (
    SELECT MIN(duration_minutes)
    FROM bikerdatav2
    WHERE start_station_id != end_station_id
  );
```

