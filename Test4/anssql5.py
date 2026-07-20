CREATE DATABASE CompanyDB;
USE CompanyDB;

CREATE TABLE Employee (
    EmployeeID INT PRIMARY KEY,
    Name VARCHAR(50),
    DepartmentID INT
);

CREATE TABLE Department (
    DepartmentID INT PRIMARY KEY,
    DepartmentName VARCHAR(50)
);

INSERT INTO Employee VALUES
(1, 'Rahul', 101),
(2, 'Priya', 102),
(3, 'Aman', 101);

INSERT INTO Department VALUES
(101, 'IT'),
(102, 'HR');

SELECT E.Name, D.DepartmentName
FROM Employee E
JOIN Department D
ON E.DepartmentID = D.DepartmentID;