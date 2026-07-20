CREATE DATABASE Orders;
USE Orders;
CREATE TABLE Orders (OrderID INT PRIMARY KEY,CustomerName VARCHAR(50),OrderDate DATE,Amount INT);
CREATE INDEX idx_OrderID
ON Orders(OrderID);