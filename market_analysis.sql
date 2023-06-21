# MArket_Analysis

SELECT
    u.user_id AS buyer_id,
    u.join_date,
    COUNT(o.order_id) AS orders_in_2019
FROM
    Users u
    LEFT JOIN Orders o ON u.user_id = o.buyer_id
WHERE
    YEAR(o.order_date) = 2019 OR o.order_date IS NULL
GROUP BY
    u.user_id,
    u.join_date;