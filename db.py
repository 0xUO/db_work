CREATE DATABASE onlineShop;
USE onlineShop;

CREATE TABLE users(
user_id INT NOT NULL AUTO_INCREMENT,
user_fname varchar(50) NOT NULL,
user_sname varchar(50) NOT NULL,
user_age int NOT NULL,
user_house_no int NOT NULL,
user_postcode varchar(8) NOT NULL,
PRIMARY KEY (user_id)
);

CREATE TABLE products(
prod_id INT NOT NULL AUTO_INCREMENT,
prod_name varchar(100) NOT NULL,
prod_quantity INT NOT NULL,
prod_price decimal(10) NOT NULL,
PRIMARY KEY(prod_id)
);

CREATE TABLE orders(
order_id int NOT NULL AUTO_INCREMENT,
fk_user_id int NOT NULL,
order_total decimal(10) NOT NULL,
PRIMARY KEY (order_id),
FOREIGN KEY (fk_user_id) REFERENCES users(user_id)
);

CREATE TABLE orderline(
orderline_id INT NOT NULL AUTO_INCREMENT,
fk_order_id int NOT NULL,
fk_prod_id int NOT NULL,
PRIMARY KEY(orderline_id),
FOREIGN KEY(fk_order_id) REFERENCES orders(order_id),
FOREIGN KEY(fk_prod_id) REFERENCES products(prod_id)
);

INSERT INTO users (user_fname, user_sname, user_age, user_house_no, user_postcode) VALUES 
("john", "doe", 20, 10, "HA9 6BE"),
("mary", "moles", 20, 50, "HA3 0VL"),
("harry", "potter", 25, 140, "NW10 9AB"),
("tom", "jones", 23, 103, "W1 5HP"),
("Dan", "theMan", 19, 4, "SE9 3HW"),
("Dave", "Sir", 29, 19, "HA9 0GW");

INSERT INTO products (prod_name, prod_quantity, prod_price) VALUES 
("pen", "50", 1.00),
("pencil", "80", 2.00),
("notebook", "100", 3.00),
("tablet", "30", 50.00),
("calculator", "50", 5.00),
("ferrari", "2", 150000.00);

INSERT INTO orders (fk_user_id, order_total) VALUES 
(2, 6.00),
(5, 50.00),
(3, 3.00),
(4, 100.00),
(1, 9.00),
(1, 150000.00);

INSERT INTO orderline (fk_order_id, fk_prod_id) VALUES 
(1, 3),
(2, 1),
(3, 1),
(4, 1),
(5, 1),
(6, 1);

UPDATE users
SET user_postcode = "HA8 6BY"
WHERE user_id = 1;

UPDATE users
SET user_age= 23
WHERE user_id = 2;

UPDATE products
SET prod_price = 45.00
WHERE prod_price = 50.00;

UPDATE products
SET prod_quantity = 20
WHERE prod_name = "tablet";

UPDATE orders
SET order_total = order_total - 20
WHERE orders_total = 100;

#UPDATE orderline
#SET ?

/*
UPDATE orderline
*/

SELECT * FROM users;
SELECT * FROM products;
SELECT * FROM products WHERE price > 20;
SELECT * FROM users WHERE age > 30;
SELECT * FROM  users WHERE user_postcode LIKE "HA%";
SELECT COUNT(user_id) FROM users;
SELECT MAX(prod_price) FROM products;
SELECT MIN(prod_price) FROM products;
SELECT AVG(prod_price) FROM products;

SELECT user_id, user_fname
FROM users
WHERE user_id=(
	SELECT user_id
    FROM orders
    WHERE order_id=1
);

DELETE FROM users WHERE user_id = 6;
DELETE FROM products WHERE product_id = 6;
DELETE FROM orders WHERE order_id = 6;
DELETE FROM orderline WHERE orderline_id = 6;

/////////////////////////////////////////////////////////////


USE sakila;
#1
SELECT * FROM actor;
#2
SELECT last_name FROM actor WHERE first_name = "John";
#3
SELECT * FROM actor WHERE last_name = "Neeson";
#4
SELECT * FROM actor WHERE actor_id LIKE "%0";
#5
SELECT description FROM film WHERE film_id = 100;
#6
SELECT * FROM film WHERE rating = "R";
#7
SELECT * FROM film WHERE rating != "R";
#8
SELECT length FROM film LIMIT 10 ; #not sure if correct 
#9
SELECT MAX(length) FROM film ORDER BY length DESC;
#10
SELECT * FROM film WHERE special_features LIKE "deleted scenes";
#11
SELECT last_name FROM actor GROUP BY last_name HAVING COUNT(last_name) =1 ORDER BY last_name DESC;
#12
SELECT last_name FROM actor GROUP BY last_name HAVING COUNT(last_name) >1 ORDER BY COUNT(last_name) DESC; #not sure if correct
#13
SELECT actor_id FROM actor GROUP BY films HAVING COUNT;
#14
select * from rental;
select return_date FROM rental WHERE last_update LIKE "Academy Dinosaur";
select rental_duration FROM film WHERE title = "Academy Dinosaur";
#15
SELECT AVG(length) FROM film;
#16
SELECT AVG(length) FROM film_category;
#17
describe film;
#18
SELECT film_id, title FROM film WHERE release_year LIKE "2010"; #not working
#19
SELECT COUNT(film_id) from film_category WHERE category_id LIKE "11"; #horror category id == 11