-- Categories
INSERT INTO categories (name, parent_id) VALUES
('Electronics', NULL),
('Mobile Phones', 1),
('Laptops', 1),
('Clothing', NULL);

-- Users
INSERT INTO users (first_name, last_name, email, password, phone_number, address, date_of_birth, date_joined, sex) VALUES
('Arafat', 'Hossain', 'arafat@gmail.com', 'hashed123', '01711111111', 'Khulna', '1995-03-12', '2024-01-01', 'Male'),
('Nusrat', 'Jahan', 'nusrat@gmail.com', 'hashed456', '01722222222', 'Dhaka', '1998-07-25', '2024-02-15', 'Female'),
('Tanvir', 'Ahmed', 'tanvir@gmail.com', 'hashed789', '01733333333', 'Chittagong', '1997-11-08', '2024-03-10', 'Male');

-- Products
INSERT INTO products (product_name, description, price, stock, rating, category_id, seller_id) VALUES
('iPhone 15', 'Apple smartphone', 120000.00, 50, 4.8, 2, 1),
('Samsung Galaxy', 'Android smartphone', 80000.00, 30, 4.5, 2, 2),
('Dell Laptop', 'Business laptop', 95000.00, 20, 4.3, 3, 1),
('T-Shirt', 'Cotton t-shirt', 500.00, 200, 4.0, 4, 3);

-- Orders
INSERT INTO orders (customer_id, total_price, order_status) VALUES
(2, 120000.00, 'delivered'),
(3, 80000.00, 'shipped'),
(2, 95000.00, 'pending');

-- Order Items
INSERT INTO order_items (order_id, product_id, quantity, price_at_purchase) VALUES
(1, 1, 1, 120000.00),
(2, 2, 1, 80000.00),
(3, 3, 1, 95000.00);

-- Payments
INSERT INTO payments (order_id, amount, payment_method, payment_status) VALUES
(1, 120000.00, 'mobile_banking', 'completed'),
(2, 80000.00, 'cash_on_delivery', 'pending'),
(3, 95000.00, 'credit_card', 'pending');