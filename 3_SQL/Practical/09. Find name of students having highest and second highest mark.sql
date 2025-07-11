-- Highest mark

SELECT name
FROM students
WHERE marks = (SELECT MAX(marks) FROM students);

-- OR

SELECT name
FROM students
ORDER BY marks DESC
LIMIT 1;

-- Second highest mark

SELECT name
FROM students
WHERE marks = (
    SELECT MAX(marks)
    FROM students
    WHERE marks < (SELECT MAX(marks) FROM students)
);

-- OR

SELECT DISTINCT marks
FROM students
ORDER BY marks DESC
LIMIT 1
OFFSET 1;

-- To get names of students with second highest mark using Option 2:

SELECT name
FROM students
WHERE marks = (
    SELECT DISTINCT marks
    FROM students
    ORDER BY marks DESC
    LIMIT 1 OFFSET 1
);

---

WITH ranked_students AS (
  SELECT
    name,
    marks,
    RANK() OVER (ORDER BY marks DESC) AS rnk
  FROM students
)
SELECT name, marks
FROM ranked_students
WHERE rnk IN (1, 2);

---
