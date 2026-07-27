import sqlite3

con = sqlite3.connect("food.db")
cur = con.cursor()

# Create Table
cur.execute("""
CREATE TABLE IF NOT EXISTS Orders(
    order_id INT,
    restaurant TEXT,
    area TEXT,
    status TEXT
)
""")

# Insert Data
cur.execute("DELETE FROM Orders")

cur.executemany("INSERT INTO Orders VALUES(?,?,?,?)",[
    (101,"Pizza Hut","Area A","Pending"),
    (102,"KFC","Area B","Pending"),
    (103,"Dominos","Area C","Pending")
])

con.commit()

# Fetch Pending Orders
cur.execute("SELECT * FROM Orders WHERE status='Pending'")
orders = cur.fetchall()

print("Pending Orders:")
for i in orders:
    print(i)

# Graph
graph = {
    "Pizza Hut":["Area A"],
    "KFC":["Area B"],
    "Dominos":["Area C"],
    "Area A":[],
    "Area B":[],
    "Area C":[]
}

# BFS
def bfs(start):
    queue = [start]
    visited = []

    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(node, end=" -> ")
            visited.append(node)
            queue.extend(graph[node])

# Delivery Route
print("\nDelivery Route:")
for i in orders:
    bfs(i[1])
    print("Delivered")

# Update Status
cur.execute("UPDATE Orders SET status='Completed' WHERE status='Pending'")
con.commit()

# Display Updated Orders
print("\nUpdated Orders:")
cur.execute("SELECT * FROM Orders")
for i in cur.fetchall():
    print(i)

con.close()