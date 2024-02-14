-- This script removes all records with a score <= 5 from the "second_table" in the "hbtn_0c_0" database

DELETE FROM hbtn_0c_0.second_table
WHERE score <= 5;
