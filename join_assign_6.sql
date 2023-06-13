create database hw06;

show databases;

CREATE TABLE table_a (
column1 int);

insert into table_a(column1)
values (1), (2), (Null), (3), (2), (4), (4), (6), (10);

select * from table_a;

CREATE TABLE table_b (
column1 int);

insert into table_b(column1)
values (7), (Null), (Null), (3), (4), (4), (2), (2), (8);

select * from table_b;

-- Inner join 9
SELECT table_a.column1
FROM table_a
INNER JOIN table_b
ON table_a.column1 = table_b.column1;

-- Left Join    13		
SELECT table_a.column1
FROM table_a
LEFT JOIN table_b
ON table_a.column1 = table_b.column1;

-- right join    13
SELECT table_a.column1
FROM table_a
right JOIN table_b
ON table_a.column1 = table_b.column1;

-- full outer join
SELECT table_a.column1
FROM table_a
fullouter JOIN table_b
ON table_a.column1 = table_b.column1;

SELECT table_a.column1 FROM table_a
right JOIN table_b
ON table_a.column1 = table_b.column1
UNION
SELECT table_a.column1 FROM table_a
LEFT outer JOIN table_b
ON table_a.column1 = table_b.column1;
