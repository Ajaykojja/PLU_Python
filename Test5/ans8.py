import sqlite3

con = sqlite3.connect("ride.db")
cur = con.cursor()

# Single Table
cur.execute("""
CREATE TABLE IF NOT EXISTS Ride(
    booking_id INT,
    customer TEXT,
    driver TEXT,
    city TEXT,
    available TEXT,
    status TEXT
)
""")

cur.execute("DELETE FROM Ride")

cur.executemany("INSERT INTO Ride VALUES(?,?,?,?,?,?)",[
    (1001,"Amit","Ajay","A","Yes","Pending"),
    (1002,"Sneha","Rahul","B","Yes","Pending"),
    (1003,"Rohan","Ravi","C","No","Pending")
])

con.commit()

# Fetch Available Drivers
cur.execute("SELECT * FROM Ride WHERE available='Yes'")
rides = cur.fetchall()

print("Available Drivers:")
for i in rides:
    print(i)

# Graph
graph = {
    "A":["B"],
    "B":["A","C"],
    "C":["B"]
}

# BFS
def bfs(start):
    q=[start]
    v=[]

    while q:
        x=q.pop(0)
        if x not in v:
            print(x,end=" ")
            v.append(x)
            q.extend(graph[x])

print("\nNearest Driver Route:")
for i in rides:
    bfs(i[3])
    print()

# Assign Booking
cur.execute("UPDATE Ride SET status='Assigned' WHERE available='Yes'")
cur.execute("UPDATE Ride SET available='No' WHERE available='Yes'")
con.commit()

print("\nUpdated Records:")
cur.execute("SELECT * FROM Ride")
for i in cur.fetchall():
    print(i)

con.close()