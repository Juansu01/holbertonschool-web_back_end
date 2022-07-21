-- In and not out
-- Task 1

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT,
    PRIMARY KEY (id),
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN') NOT NULL

);