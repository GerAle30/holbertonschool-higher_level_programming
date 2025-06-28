-- Lists the number of records for each scroe in second in second_table
SELECT score, COUNT (*) AS number
FROM second_table
GROUP BY score <order by number DESC;