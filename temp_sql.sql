SELECT t1.id
FROM RisingTemperature t1
JOIN RisingTemperature t2 ON t1.recordDate = DATE_ADD(t2.recordDate, INTERVAL 1 DAY)
WHERE t1.temperature > t2.temperature;
