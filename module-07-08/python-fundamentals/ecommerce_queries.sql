-- Query 1: Show all products with their category name

SELECT products.product_name, categories.name
FROM products
INNER JOIN categories ON categories.id = products.category_id

-- Query 2: Show all orders with the customer's full name and order status

SELECT users.first_name, users.last_name, orders.order_status
FROM users
INNER JOIN orders ON orders.customer_id = users.id

-- Query 3: Show all products with their seller's full name

SELECT products.product_name, users.first_name, users.last_name
FROM products
INNER JOIN users ON users.id = products.seller_id

-- Query 4: Show the total amount spent by each customer

SELECT first_name, last_name, SUM(total_price) AS total_spent
FROM users
INNER JOIN orders ON orders.customer_id = users.id
GROUP BY first_name, last_name

-- Query 5: Show all orders with the product name and quantity from order_items

SELECT product_name, quantity
FROM products
INNER JOIN order_items ON order_items.product_id = products.id
INNER JOIN orders ON order_items.order_id = orders.id

-- Query 6: Show only the delivered orders with customer full name and total price

SELECT first_name, last_name, total_price, order_status
FROM users
INNER JOIN orders ON orders.customer_id = users.id
WHERE orders.order_status = 'delivered'

-- Query 7: Show the most expensive product in each category

SELECT categories.name, MAX(products.price) AS max_price
FROM products
INNER JOIN categories ON categories.id = products.category_id
GROUP BY categories.name

-- Query 8: Show all payments with the customer's full name and payment status

SELECT first_name, last_name, amount, payment_status
FROM users
INNER JOIN orders ON orders.customer_id = users.id
INNER JOIN payments ON payments.order_id = orders.id

-- Query 9: Show total revenue from completed payments only

SELECT SUM(amount) AS total_revenue
FROM payments
WHERE payments.payment_status = 'completed'

-- Query 10: Show all users who have never placed an order

SELECT first_name, last_name
FROM users
LEFT JOIN orders ON orders.customer_id = users.id
WHERE orders.id IS NULL

-- Query 11 — Show products priced above the average using CTE

WITH avg_price AS (
    SELECT AVG(price) as average
    FROM products
)
SELECT product_name, price
FROM products, avg_price
WHERE price > avg_price.average

-- Query 12 — Number all products by price from highest to lowest using ROW_NUMBER()

SELECT product_name, price, ROW_NUMBER() OVER (ORDER BY price DESC) AS row_num
FROM products

-- Query 13 — Rank products by price. Using RANK()

SELECT product_name, price, RANK() OVER (ORDER BY price DESC) AS rank_no
FROM products

-- Query 14 — Show each product's price and the previous product's price using LAG()

SELECT product_name, price, LAG(price) OVER (ORDER BY price DESC) AS lag_no
FROM products

-- Query 15 — Write a transaction that inserts a new order and a payment together. If either fails, both should rollback

BEGIN;

INSERT INTO orders (customer_id, total_price, order_status) VALUES (1, 5000, 'pending');
INSERT INTO payments (order_id, amount, payment_method, payment_status) VALUES (1, 5000, 'credit_card', 'completed');

COMMIT;
