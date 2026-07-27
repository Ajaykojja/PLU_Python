import sqlite3

class Book:
    def __init__(self,id,name,available,days):
        self.id=id
        self.name=name
        self.available=available
        self.days=days

con=sqlite3.connect("library.db")
cur=con.cursor()

# Single Table
cur.execute("""
CREATE TABLE IF NOT EXISTS Books(
id INT,
name TEXT,
available TEXT,
days INT
)
""")

cur.execute("DELETE FROM Books")

cur.executemany("INSERT INTO Books VALUES(?,?,?,?)",[
(101,"Python","Yes",0),
(102,"Java","Yes",0),
(103,"C++","No",20),
(104,"Data Science","Yes",0),
(105,"DBMS","No",18)
])

con.commit()

# Fetch Books
cur.execute("SELECT * FROM Books")
books=[Book(*i) for i in cur.fetchall()]

# Merge Sort
def merge(a):
    if len(a)>1:
        m=len(a)//2
        l=a[:m]
        r=a[m:]
        merge(l)
        merge(r)
        i=j=k=0
        while i<len(l) and j<len(r):
            if l[i].name<r[j].name:
                a[k]=l[i]
                i+=1
            else:
                a[k]=r[j]
                j+=1
            k+=1
        while i<len(l):
            a[k]=l[i]
            i+=1
            k+=1
        while j<len(r):
            a[k]=r[j]
            j+=1
            k+=1

merge(books)

print("Books:")
for i in books:
    print(i.id,i.name,i.available)

# Binary Search
s=sorted(books,key=lambda x:x.id)

def bs(a,id):
    l,h=0,len(a)-1
    while l<=h:
        m=(l+h)//2
        if a[m].id==id:
            return a[m]
        elif a[m].id<id:
            l=m+1
        else:
            h=m-1
    return None

x=int(input("\nEnter Book ID: "))
b=bs(s,x)

if b:
    print("Found:",b.id,b.name)
else:
    print("Book Not Found")

# Borrow Book
cur.execute("UPDATE Books SET available='No' WHERE id=?", (x,))
con.commit()

# Available Books
print("\nAvailable Books:")
cur.execute("SELECT * FROM Books WHERE available='Yes'")
for i in cur.fetchall():
    print(i)

# Overdue Books
print("\nOverdue Books:")
cur.execute("SELECT * FROM Books WHERE days>15")
for i in cur.fetchall():
    print(i)

con.close()