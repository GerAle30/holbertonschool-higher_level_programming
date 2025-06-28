-- Lists all records from second_table with a non-empty name, orderd by score (descending)
SELECT score, name FROM  second_table
WHERE name is NOT NULL AND name != ''
ORDER BY score DESC;    