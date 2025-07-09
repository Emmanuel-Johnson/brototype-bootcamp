-- -------------------------------------------------------------------------
-- 🧱 Sample Database Schema - USERS TABLE
-- -------------------------------------------------------------------------
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100)
);

-- Sample data for users table
INSERT INTO users (id, name) VALUES
(1, 'Alice'),
(2, 'Bob');

-- -------------------------------------------------------------------------
-- 📦 Sample Database Schema - ORDERS TABLE  
-- -------------------------------------------------------------------------
CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    product_id INTEGER
);

-- Sample data for orders table
INSERT INTO orders (id, user_id, product_id) VALUES
(1, 1, 2),
(2, 2, 3);

-- -------------------------------------------------------------------------
-- 🛒 Sample Database Schema - PRODUCTS TABLE
-- -------------------------------------------------------------------------
CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    title VARCHAR(100)
);

-- Sample data for products table
INSERT INTO products (id, title) VALUES
(2, 'Keyboard'),
(3, 'Monitor');

-- =========================================================================
-- ✅ PSQL QUERY WITH MULTIPLE JOINS
-- =========================================================================

-- Join all three tables to see which user ordered which product
SELECT 
    users.name AS user_name,
    products.title AS product_title
FROM 
    users 
JOIN 
    orders ON users.id = orders.user_id 
JOIN 
    products ON orders.product_id = products.id;

-- =========================================================================
-- 🔤 STRING FUNCTIONS
-- =========================================================================

-- -------------------------------------------------------------------------
-- 1. UPPER() and LOWER() - Converts text to uppercase or lowercase
-- -------------------------------------------------------------------------
SELECT 
    name, 
    UPPER(name) AS upper_name, 
    LOWER(name) AS lower_name 
FROM users;

-- -------------------------------------------------------------------------
-- 2. SUBSTRING() - Extracts part of a string
-- -------------------------------------------------------------------------
SELECT 
    email, 
    SUBSTRING(email FROM 1 FOR 5) AS first_five 
FROM users;

-- -------------------------------------------------------------------------
-- 3. TRIM(), LTRIM(), RTRIM() - Removes spaces or characters from strings
-- -------------------------------------------------------------------------

-- Remove spaces from both ends
SELECT TRIM('   hello   ') AS trimmed; -- Output: 'hello'

-- Remove specific characters from left
SELECT LTRIM('---hello', '-') AS left_trimmed; -- Output: 'hello'

-- Remove specific characters from right
SELECT RTRIM('hello***', '*') AS right_trimmed; -- Output: 'hello'

-- -------------------------------------------------------------------------
-- 4. POSITION() - Find the position of a substring
-- -------------------------------------------------------------------------
SELECT POSITION('@' IN email) AS at_pos 
FROM users;

-- -------------------------------------------------------------------------
-- 5. REPLACE() - Replaces occurrences of a substring
-- -------------------------------------------------------------------------
SELECT REPLACE(email, '@', '[at]') AS safe_email 
FROM users;

-- -------------------------------------------------------------------------
-- 6. CONCAT() and || - Joins strings together
-- -------------------------------------------------------------------------

-- Using CONCAT function
SELECT CONCAT(first_name, ' ', last_name) AS full_name 
FROM users;

-- Using || concatenation operator
SELECT first_name || ' ' || last_name AS full_name 
FROM users;

-- -------------------------------------------------------------------------
-- 7. LENGTH() - Gets the number of characters in a string
-- -------------------------------------------------------------------------
SELECT 
    name, 
    LENGTH(name) AS name_length 
FROM users;

-- -------------------------------------------------------------------------
-- 8. REPEAT() - Repeats a string a given number of times
-- -------------------------------------------------------------------------
SELECT REPEAT('Hi ', 3) AS repeated; -- Output: 'Hi Hi Hi '

-- =========================================================================
-- 📊 AGGREGATE FUNCTIONS
-- =========================================================================

-- -------------------------------------------------------------------------
-- 1. ✅ COUNT() - Count rows
-- -------------------------------------------------------------------------
-- Counts all users in the users table
SELECT COUNT(*) AS total_users 
FROM users;

-- -------------------------------------------------------------------------
-- 2. 💰 SUM() - Total of a column
-- -------------------------------------------------------------------------
-- Adds all prices in the orders table
SELECT SUM(price) AS total_revenue 
FROM orders;

-- -------------------------------------------------------------------------
-- 3. 📈 AVG() - Average value
-- -------------------------------------------------------------------------
-- Calculates the average price of all orders
SELECT AVG(price) AS average_order_price 
FROM orders;

-- -------------------------------------------------------------------------
-- 4. 🔼 MAX() - Highest value
-- -------------------------------------------------------------------------
-- Finds the most expensive product
SELECT MAX(price) AS highest_price 
FROM products;

-- -------------------------------------------------------------------------
-- 5. 🔽 MIN() - Lowest value
-- -------------------------------------------------------------------------
-- Finds the cheapest product
SELECT MIN(price) AS lowest_price 
FROM products;

-- -------------------------------------------------------------------------
-- 6. 📂 With GROUP BY - Aggregate values grouped by a column
-- -------------------------------------------------------------------------
-- Counts how many products exist per category
SELECT 
    category, 
    COUNT(*) AS total_products 
FROM products 
GROUP BY category;

-- -------------------------------------------------------------------------
-- 7. 🚨 With HAVING - Filter groups after aggregation
-- -------------------------------------------------------------------------
-- Shows only categories with an average price greater than 100
SELECT 
    category, 
    AVG(price) AS avg_price 
FROM products 
GROUP BY category 
HAVING AVG(price) > 100;

-- -------------------------------------------------------------------------
-- 8. 🧠 Multiple aggregates in one query
-- -------------------------------------------------------------------------
-- Get multiple statistics in a single query
SELECT 
    COUNT(*) AS total_orders,
    SUM(price) AS total_revenue,
    AVG(price) AS average_price 
FROM orders;

-- =========================================================================
-- 📋 AGGREGATE FUNCTIONS REFERENCE TABLE
-- =========================================================================
/*
| Function | Description             |
|----------|-------------------------|
| COUNT()  | Counts rows            |
| SUM()    | Adds values            |
| AVG()    | Calculates average     |
| MAX()    | Finds maximum value    |
| MIN()    | Finds minimum value    |
*/

---

