
#trips_and_users


SELECT
    request_at AS Day,
    ROUND(
        COUNT(CASE WHEN status LIKE 'cancelled%' THEN 1 END) / COUNT(*)::numeric,
        2
    ) AS "Cancellation Rate"
FROM Trips t
JOIN Users u1 ON t.client_id = u1.users_id AND u1.banned = 'No'
JOIN Users u2 ON t.driver_id = u2.users_id AND u2.banned = 'No'
WHERE request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY request_at
ORDER BY request_at;
