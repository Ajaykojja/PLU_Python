import sqlite3

class Transaction:
    def __init__(self, tid, acc, amount, date, ttype):
        self.tid = tid
        self.acc = acc
        self.amount = amount
        self.date = date
        self.ttype = ttype

# Database
con = sqlite3.connect("bank.db")
cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS transaction_table(
tid INT,
acc INT,
amount INT,
date TEXT,
type TEXT)
""")

cur.execute("DELETE FROM transaction_table")

data = [
    (101,1001,5000,"2025-07-01","Credit"),
    (102,1002,2000,"2025-07-02","Debit"),
    (103,1003,8000,"2025-07-03","Credit"),
    (104,1004,1500,"2025-07-04","Debit"),
    (105,1005,10000,"2025-07-05","Credit"),
    (106,1006,7000,"2025-07-06","Debit")
]

cur.executemany("INSERT INTO transaction_table VALUES(?,?,?,?,?)", data)
con.commit()

# Fetch Data
cur.execute("SELECT * FROM transaction_table")
transactions = [Transaction(*row) for row in cur.fetchall()]

# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x.amount <= pivot.amount]
    right = [x for x in arr[1:] if x.amount > pivot.amount]
    return quick_sort(left) + [pivot] + quick_sort(right)

transactions = quick_sort(transactions)

print("Transactions Sorted by Amount:")
for t in transactions:
    print(t.tid, t.acc, t.amount, t.ttype)

# Binary Search
search = sorted(transactions, key=lambda x: x.tid)

def binary_search(arr, tid):
    l, h = 0, len(arr)-1
    while l <= h:
        m = (l+h)//2
        if arr[m].tid == tid:
            return arr[m]
        elif arr[m].tid < tid:
            l = m+1
        else:
            h = m-1
    return None

tid = int(input("\nEnter Transaction ID: "))
t = binary_search(search, tid)

if t:
    print("Found:", t.tid, t.acc, t.amount, t.ttype)
else:
    print("Transaction Not Found")

# Total Credit and Debit
credit = 0
debit = 0

for t in transactions:
    if t.ttype == "Credit":
        credit += t.amount
    else:
        debit += t.amount

print("\nTotal Credit =", credit)
print("Total Debit =", debit)

# Top 5 Transactions
print("\nTop 5 Highest Transactions:")
for t in sorted(transactions, key=lambda x: x.amount, reverse=True)[:5]:
    print(t.tid, t.acc, t.amount, t.ttype)

con.close() 