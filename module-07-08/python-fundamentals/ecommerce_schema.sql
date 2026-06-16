-- Active: 1780698603913@@127.0.0.1@5432@ecommerce_db
CREATE DATABASE ecommerce_db;
\c ecommerce_db

CREATE TABLE categories (
    id SERIAL NOT NULL,
    name VARCHAR(50) NOT NULL,
    parent_id INT REFERENCES categories(id),
    PRIMARY KEY (id)
)

CREATE TABLE users (
    id SERIAL NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    phone_number VARCHAR(50) NOT NULL,
    address VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    date_joined DATE NOT NULL,
    sex VARCHAR(50) NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
)

CREATE TABLE products (
    id SERIAL NOT NULL,
    product_name VARCHAR(50) NOT NULL,
    description VARCHAR(100) NOT NULL,
    price NUMERIC(10,2) NOT NULL,
    stock INT NOT NULL DEFAULT 0,
    rating NUMERIC(3,2) NOT NULL,
    category_id INT REFERENCES categories(id),
    seller_id INT REFERENCES users(id),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
)

CREATE TABLE orders (
    id SERIAL NOT NULL,
    customer_id INT REFERENCES users(id),
    total_price NUMERIC(10,2) NOT NULL,
    order_status VARCHAR(50) NOT NULL CHECK (order_status IN ('pending', 'processing', 'shipped', 'delivered', 'cancelled')),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
)

CREATE TABLE order_items (
    id SERIAL NOT NULL,
    order_id INT REFERENCES orders(id),
    product_id INT REFERENCES products(id),
    quantity INT NOT NULL,
    price_at_purchase NUMERIC(10,2) NOT NULL,
    PRIMARY KEY (id)
)

CREATE TABLE payments (
    id SERIAL NOT NULL,
    order_id INT REFERENCES orders(id),
    amount NUMERIC(10,2) NOT NULL,
    payment_method VARCHAR(50) NOT NULL CHECK(payment_method IN ('credit_card', 'mobile_banking', 'cash_on_delivery')),
    payment_status VARCHAR(50) NOT NULL CHECK(payment_status IN ('pending', 'completed', 'failed', 'refunded')),
    payment_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
)

SELECT table_name FROM information_schema.tables 
WHERE table_schema = 'public';