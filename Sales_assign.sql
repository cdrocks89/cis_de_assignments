create table product(product_id int primary key, product_name varchar(50),product_category varchar(50));

create table sales(transaction_id int primary key, amount float, customer_id varchar(50),T_date Date,units int,product_id INT,
    ->     FOREIGN KEY (product_id) REFERENCES product(product_id));


-- Insert sample data into the sales table
INSERT INTO sales (transaction_id, amount, customer_id, T_date, units,product_id)
VALUES
    (1, 100, 1, '2023-05-15', 2, 2),
    (2, 150, 2, '2023-05-18', 3, 3),
    (3, 200, 1, '2023-05-20', 1, 1),
    (4, 120, 3, '2023-05-25', 2, 3),
    (5, 80, 2, '2023-05-26', 4, 1);

-- Insert sample data into the product table
INSERT INTO product (product_id, product_name, product_category)
VALUES
    (1, 'A', 'X'),
    (2, 'B', 'Y'),
    (3, 'C', 'X'),
    (4, 'D', 'Z');


select p. product_id,p.product_name,p.product_category from product p where p.product_id NOT IN(select s.product_id from sales s where exists( select 1 from sales s1 where s.pro
duct_id=s1.product_id and DATEDIFF(s1.T_date,s.T_date)=7));