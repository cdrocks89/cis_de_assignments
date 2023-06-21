#SCD2 - slowly changing dimension type 2

SELECT SerialNo, productname, cost, Date as "Start Date" ,
	CASE WHEN Date < LEAD(date) OVER(PARTITION BY productname ORDER BY date) THEN LEAD(date) OVER(PARTITION BY productname ORDER BY date)
	ELSE "9999-12-31" END AS "End Date"
FROM products


CREATE TABLE products (
  SerialNo INT,
  ProductName VARCHAR(255),
  Cost DECIMAL(10, 2),
  Date DATE
);


INSERT INTO products (SerialNo, ProductName, Cost, Date)
VALUES
  (1, 'S22', 800, '2021-01-01'),
  (2, 'S23', 1000, '2023-01-01'),
  (3, 'S22', 600, '2022-07-01'),
  (4, 'S23', 1200, '2022-06-01'),
  (5, 'S20', 400, '2018-06-01');