import sqlite3
import heapq

# Patient Class
class Patient:
    def __init__(self, pid, name, age, priority):
        self.pid = pid
        self.name = name
        self.age = age
        self.priority = priority

# Database
con = sqlite3.connect("hospital.db")
cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS patient(
    pid INTEGER,
    name TEXT,
    age INTEGER,
    priority INTEGER
)
""")

cur.execute("DELETE FROM patient")

data = [
    (1, "Ajay", 20, 2),
    (2, "Dhileep", 35, 1),
    (3, "Yasu babu", 28, 3),
    (4, "Lokesh", 40, 2)
]

cur.executemany("INSERT INTO patient VALUES(?,?,?,?)", data)
con.commit()

# Fetch Patients
cur.execute("SELECT * FROM patient")
patients = [Patient(*row) for row in cur.fetchall()]

# Create Priority Queue
pq = []
for p in patients:
    heapq.heappush(pq, (p.priority, p.pid, p))

print("Patients Attended:")

# Attend Patients
while pq:
    _, _, p = heapq.heappop(pq)

    print("ID:", p.pid)
    print("Name:", p.name)
    print("Age:", p.age)
    print("Priority:", p.priority)
    print()

    # Remove attended patient
    cur.execute("DELETE FROM patient WHERE pid=?", (p.pid,))
    con.commit()

# Display Remaining Patients
print("Remaining Patients:")

cur.execute("SELECT * FROM patient")
rows = cur.fetchall()

if rows:
    for r in rows:
        print(r)
else:
    print("No Patients Left")

con.close()
