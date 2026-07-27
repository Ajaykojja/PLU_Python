import sqlite3
class Sale:
    def __init__(self,id,product,qty,revenue,region,incentive):
        self.id=id
        self.product=product
        self.qty=qty
        self.revenue=revenue
        self.region=region
        self.incentive=incentive

con=sqlite3.connect("sales.db")
cur=con.cursor()

# Single Table
cur.execute("""
CREATE TABLE IF NOT EXISTS Sales(
id INT,
product TEXT,
qty INT,
revenue INT,
region TEXT,
incentive TEXT
)
""")

cur.execute("DELETE FROM Sales")

cur.executemany("INSERT INTO Sales VALUES(?,?,?,?,?,?)",[
(101,"Laptop",5,50000,"North","No"),
(102,"Mobile",8,70000,"South","No"),
(103,"TV",4,45000,"East","No"),
(104,"AC",6,80000,"North","No"),
(105,"Fridge",3,60000,"West","No"),
(106,"Fan",10,30000,"South","No")
])

con.commit()

# Fetch Records
cur.execute("SELECT * FROM Sales")
sales=[Sale(*i) for i in cur.fetchall()]

# Sort by Revenue
sales=sorted(sales,key=lambda x:x.revenue,reverse=True)

print("Sales Records:")
for i in sales:
    print(i.id,i.product,i.revenue)

# Binary Search
s=sorted(sales,key=lambda x:x.id)

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

x=int(input("\nEnter Salesperson ID: "))
e=bs(s,x)

if e:
    print("Found:",e.id,e.product,e.revenue)
else:
    print("Not Found")

# Top 5 Salespersons
print("\nTop 5 Salespersons:")
for i in sales[:5]:
    print(i.id,i.revenue)

# Highest Revenue Region
d={}
for i in sales:
    d[i.region]=d.get(i.region,0)+i.revenue

r=max(d,key=d.get)
print("\nHighest Revenue Region:",r,d[r])

# Update Incentive
cur.execute("UPDATE Sales SET incentive='Yes' WHERE revenue>=60000")
con.commit()

print("\nUpdated Records:")
cur.execute("SELECT * FROM Sales")
for i in cur.fetchall():
    print(i)

con.close()