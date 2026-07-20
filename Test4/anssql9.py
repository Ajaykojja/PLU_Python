CREATE DATABASE Book;
USE Book;

CREATE TABLE Book(BookID INT PRIMARY KEY,BookName VARCHAR(100),Author VARCHAR(50),Price INT);

INSERT INTO Book VALUES
(1, 'Python Basics', 'John', 500),
(2, 'Learning SQL', 'David', 700);
