-- Old school band
-- Task 3

SELECT band_name, IFNULL(split, 2020) - IFNULL(formed, 0) AS years_ac
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY years_ac DESC;
