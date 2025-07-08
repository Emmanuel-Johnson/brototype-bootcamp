-- Add new column to a table 

ALTER TABLE table_name
ADD COLUMN column_name data_type;

ALTER TABLE students
ADD COLUMN email VARCHAR(100);

ALTER TABLE students
ADD COLUMN email VARCHAR(100) UNIQUE NOT NULL;
