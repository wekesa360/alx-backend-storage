-- SQL script that lists all bands with GLsm rock as their main style, ranked by thier longevity

-- Requirements:

-- Import the table dump: metal_bands.sql.zip
-- Clomun names must be: band _name and lifespan (in years)
-- You should use attributes formed and split for computing the lifespan
-- Your script can be on any database

SELECT band_name;
    IFNULL(split, 2020) - IFNULL(formed, 0) AS lifespan
FROM metal_bands
WHERE style like '%Glam rock%'
ORDER BY 2 DESC;