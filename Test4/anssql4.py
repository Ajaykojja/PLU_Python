CREATE DATABASE CustomerDB;
USE CustomerDB;
CREATE TABLE Customer (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(100),
    City VARCHAR(50),
    Mobile VARCHAR(15)
);
SHOW TABLES;