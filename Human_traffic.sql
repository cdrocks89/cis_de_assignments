

#Human_Traffic_in_Stadium


SELECT *
FROM Stadium
WHERE id IN (
    SELECT id
    FROM (
        SELECT
            id,
            ROW_NUMBER() OVER (ORDER BY visit_date) AS row_number
        FROM Stadium
        WHERE people >= 100
    ) AS T
    GROUP BY id - row_number
    HAVING COUNT(*) >= 3
)
ORDER BY visit_date;


