-- Lists all records wiht score >= 10 from second_table by score (top first)
SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC;
