CREATE DATABASE atm_system;

USE atm_system;

CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id VARCHAR(12) UNIQUE NOT NULL,
    user_name VARCHAR(100) NOT NULL,
    pin VARCHAR(4) NOT NULL,
    balance DECIMAL(10, 2) NOT NULL
);
INSERT INTO users (user_id,user_name, pin, balance) VALUES 
('123456','John Doe', '1234', 10000.0),
('123457','Alice', '1111', 5000.0),
('123458','Bob', '2222', 3000.0);

select * from users;