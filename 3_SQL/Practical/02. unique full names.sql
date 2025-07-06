-- unique full names

SELECT DISTINCT first_name || ' ' || last_name AS full_name 
FROM employees;

-- OR

SELECT DISTINCT CONCAT(first_name, ' ', last_name) AS full_name
FROM employees;
