-- Creates table second_table in the database and add multiple rows
-- if the table already exists, it will not fail
CREATE TABLE_IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

-- Insert 4 records into second _table
INSERT INTO second_table (id, name, score) VALUES
(1, 'John',10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4, 'George', 8);
