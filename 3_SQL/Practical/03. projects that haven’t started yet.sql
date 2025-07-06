-- projects that haven’t started yet

-- Option 1: If you use a start_date column:

SELECT *
FROM projects
WHERE start_date IS NULL;

-- Option 2: If you want projects starting in the future (after today):

SELECT *
FROM projects
WHERE start_date > CURRENT_DATE;

SELECT CURRENT_DATE; -- Returns current date (no time)
SELECT CURRENT_TIME; -- Returns current time (no date)
SELECT CURRENT_TIMESTAMP; -- Returns current date and time
SELECT NOW(); -- Same as CURRENT_TIMESTAMP 
SELECT TIMEOFDAY(); -- Returns current date and time as a text string

-- Option 3: If you use a status column (e.g., status = 'Not Started'):

SELECT *
FROM projects
WHERE status = 'Not Started';
