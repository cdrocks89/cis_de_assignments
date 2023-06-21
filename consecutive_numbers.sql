


# consecutive_numbers.sql

SELECT DISTINCT num AS ConsecutiveNums
FROM (
    SELECT
        num,
        CASE
            WHEN num = lag(num, 1) OVER (ORDER BY id) AND num = lag(num, 2) OVER (ORDER BY id)
            THEN 1
            ELSE 0
        END AS isConsecutive
    FROM Logs
) AS T
WHERE isConsecutive = 1;
