-- We are all unique!
-- Task 0

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    PRIMARY KEY (id)
);
