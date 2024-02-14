-- This script lists all records of the "second_table" in the "hbtn_0c_0" database, excluding rows without a name value. The results will display the score and the name, ordered by descending score

SELECT score, name
FROM hbtn_0c_0.second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
