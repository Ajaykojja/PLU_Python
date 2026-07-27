import sqlite3

class Product:
    def __init__(self, pid, name, qty):
        self.pid = pid
        self.name = name
        self.qty = qty

# Create Database
con = sqlite3.connect("inventory.db")
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS products(pid INT, name TEXT, qty INT)")
cur.execute("DELETE FROM products")

data = [
    (101, "Laptop", 15),
    (102, "Mouse", 8),
    (103, "Keyboard", 20),
    (104, "Book", 5)
]

cur.executemany("INSERT INTO products VALUES(?,?,?)", data)
con.commit()

# Fetch Data
cur.execute("SELECT * FROM products")
products = [Product(*row) for row in cur.fetchall()]

# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    while left and right:
        if left[0].qty < right[0].qty:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    return result + left + right

# Binary Search
def binary_search(arr, pid):
    low, high = 0, len(arr)-1

    while low <= high:
        mid = (low + high)//2

        if arr[mid].pid == pid:
            return arr[mid]
        elif arr[mid].pid < pid:
            low = mid + 1
        else:
            high = mid - 1
    return None

# Sort by Quantity
products = merge_sort(products)

print("Products:")
for p in products:
    print(p.pid, p.name, p.qty)

# Search by Product ID
search_list = sorted(products, key=lambda x: x.pid)

pid = int(input("\nEnter Product ID: "))
p = binary_search(search_list, pid)

if p:
    print("Found:", p.pid, p.name, p.qty)
else:
    print("Product Not Found")

# Low Stock
print("\nLow Stock Products:")
for p in products:
    if p.qty < 10:
        print(p.pid, p.name, p.qty)

con.close()