-- Join table 

-- INNER JOIN - Only rows with matching values in both tables are returned.


SELECT s.name, sc.id FROM students s
INNER JOIN scores sc ON s.id = sc.student_id;

-- LEFT JOIN (LEFT OUTER JOIN) - All rows from the left table are returned, with NULLs if no match in right.

SELECT s.name, sc.score
FROM students s
LEFT JOIN scores sc ON s.id = sc.student_id;

-- RIGHT JOIN (RIGHT OUTER JOIN) - All rows from the right table are returned, with NULLs if no match in left.

SELECT s.name, sc.score
FROM students s
RIGHT JOIN scores sc ON s.id = sc.student_id;

-- FULL JOIN (FULL OUTER JOIN) - All rows from both tables are returned, with NULLs where there's no match.

SELECT s.name, sc.score
FROM students s
FULL JOIN scores sc ON s.id = sc.student_id;

-- CROSS JOIN - Returns the Cartesian product (every row in A × every row in B).

SELECT students.name, scores.score
FROM students
CROSS JOIN scores;

-- NATURAL JOIN - A NATURAL JOIN automatically performs an INNER JOIN using all columns with the same name in both tables.

SELECT *
FROM students
NATURAL JOIN scores;

-- SELF JOIN - A SELF JOIN is a regular join where a table is joined with itself to compare rows within the same table.

SELECT A.name AS employee, B.name AS manager
FROM employees A
JOIN employees B ON A.manager_id = B.id;
