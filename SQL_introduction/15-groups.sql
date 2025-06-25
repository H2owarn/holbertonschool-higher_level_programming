--  lists the number of records with the same score (counts how many times each score appears)
SELECT score, COUNT(*) AS count
FROM second_table
GROUP BY score
ORDER BY score DESC;
