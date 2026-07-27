import sqlite3
from datetime import datetime

class Employee:
    def __init__(self,id,name,cin,cout):
        self.id=id
        self.name=name
        self.cin=cin
        self.cout=cout
        self.hours=(datetime.strptime(cout,"%H:%M")-datetime.strptime(cin,"%H:%M")).seconds/3600*5

con=sqlite3.connect("employee.db")
cur=con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS emp(id INT,name TEXT,cin TEXT,cout TEXT)")
cur.execute("DELETE FROM emp")

cur.executemany("INSERT INTO emp VALUES(?,?,?,?)",[
(101,"Ajay","09:00","18:00"),
(102,"Rahul","09:30","17:30"),
(103,"Sneha","08:30","18:30"),
(104,"Priya","09:00","19:00")
])
con.commit()

# Fetch Records
cur.execute("SELECT * FROM emp")
emp=[Employee(*i) for i in cur.fetchall()]

# Sort by Working Hours
emp=sorted(emp,key=lambda x:x.hours,reverse=True)

print("Employees:")
for i in emp:
    print(i.id,i.name,i.hours)

# Binary Search
s=sorted(emp,key=lambda x:x.id)

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

x=int(input("\nEnter Employee ID: "))
e=bs(s,x)

if e:
    print("Found:",e.id,e.name,e.hours)
else:
    print("Employee Not Found")

# Employees Working More Than 45 Hours
print("\nEmployees Working More Than 45 Hours:")
for i in emp:
    if i.hours>45:
        print(i.id,i.name,i.hours)

con.close()