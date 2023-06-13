/*

CustID                        Dates
1111                              202212
1111                              202210
1111                              202209
1111                              202301
2222                           202201
2222                           202205
2222                           202204

Assignment: The required out put is 

CUSTID                        DATES                Differenceinmonths
                                      202209                0
                                      202210                1
                                      202212                3
                                      202301                4


                                     202201                0
                                     202204                3
                                     202205                4


*/




CREATE TABLE cust_1 (
  cust_id INT,
  prod_name ARRAY<STRING>,
  price ARRAY<INT>
)
STORED AS ORC;


INSERT INTO TABLE cust_1
SELECT 111, array("a", "b", "c"), array(10, 20, 30)
UNION ALL
SELECT 112, array("d", "e", "f"), array(30, 20, 40);


SELECT
  c.cust_id,
  p.product_name,
  t.price
FROM
  cust_1 c
LATERAL VIEW posexplode(c.prod_name) p AS pos, product_name
LATERAL VIEW posexplode(c.price) t AS pos,price
WHERE
  t.pos = p.pos;