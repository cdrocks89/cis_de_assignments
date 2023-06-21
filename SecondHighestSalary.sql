SecondHighestSalary


SELECT
    CASE
        WHEN COUNT(*) > 1 THEN MAX(salary)
        ELSE NULL
    END AS SecondHighestSalary
FROM
    Employee
WHERE
    salary < (SELECT MAX(salary) FROM Employee);