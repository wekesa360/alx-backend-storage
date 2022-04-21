-- SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans

-- Requirements:
-- Import the table dump: metal_bands.sql.zip
-- Column name must be: oriin and nb_fans
-- Your scripts can be executed on any databse

SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands GROUP BY 1 ORDER BY 2 DESC;