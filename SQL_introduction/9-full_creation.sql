-- Creates full table in the database
CREATE TABLE IF NOT EXISTS second_table (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    score INT NOT NULL,
    PRIMARY KEY (id)
);

-- Inserts a new row in the table
INSERT INTO second_table (id, name, score) VALUES
(1, 'John', 10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4, 'George', 8);