import sqlite3
import heapq

class Student:
    def __init__(self, roll, name, cgpa, skills, status):
        self.roll = roll
        self.name = name
        self.cgpa = cgpa
        self.skills = skills
        self.status = status

# Database
con = sqlite3.connect("college.db")
cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS student(
    roll INT,
    name TEXT,
    cgpa REAL,
    skills TEXT,
    status TEXT
)
""")

cur.execute("DELETE FROM student")

cur.executemany("INSERT INTO student VALUES(?,?,?,?,?)", [
    (101,"Ajay",8.5,"Python","No"),
    (102,"Rahul",7.2,"Java","No"),
    (103,"Sneha",9.1,"C++","No"),
    (104,"Priya",7.8,"Python","No")
])

con.commit()

# Fetch Students
cur.execute("SELECT * FROM student")
students = [Student(*i) for i in cur.fetchall()]

# Heap Sort
heap = []
for s in students:
    heapq.heappush(heap, (s.cgpa, s.roll, s))

print("Students Sorted by CGPA:")
while heap:
    _, _, s = heapq.heappop(heap)
    print(s.roll, s.name, s.cgpa, s.status)

# Binary Search
students = sorted(students, key=lambda x: x.roll)

def binary_search(arr, roll):
    l, h = 0, len(arr)-1
    while l <= h:
        m = (l+h)//2
        if arr[m].roll == roll:
            return arr[m]
        elif arr[m].roll < roll:
            l = m+1
        else:
            h = m-1
    return None

roll = int(input("\nEnter Roll Number: "))
s = binary_search(students, roll)

if s:
    print("Found:", s.roll, s.name, s.cgpa, s.status)
else:
    print("Student Not Found")

# Eligible Students
print("\nEligible Students (CGPA > 7.5):")
for s in students:
    if s.cgpa > 7.5:
        print(s.roll, s.name, s.cgpa)

# Update Placement Status
roll = int(input("\nEnter Selected Roll Number: "))
cur.execute("UPDATE student SET status='Placed' WHERE roll=?", (roll,))
con.commit()

print("\nUpdated Student Records:")
cur.execute("SELECT * FROM student")
for row in cur.fetchall():
    print(row)

con.close()