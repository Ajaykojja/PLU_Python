
CREATE TABLE Student (StudentID INT PRIMARY KEY,Name VARCHAR(50),CourseID INT);

CREATE TABLE Course (CourseID INT PRIMARY KEY,CourseName VARCHAR(50));

INSERT INTO Student VALUES
(1, 'Rahul', 201),
(2, 'Neha', 202),
(3, 'Aman', NULL);

INSERT INTO Course VALUES
(201, 'Python'),
(202, 'SQL');

SELECT Student.StudentID,Student.Name,Course.CourseName
FROM StudentLEFT JOIN Course
ON Student.CourseID = Course.CourseID;