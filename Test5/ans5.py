import sqlite3

class Movie:
    def __init__(self,id,title,genre,rating,watch):
        self.id=id
        self.title=title
        self.genre=genre
        self.rating=rating
        self.watch=watch

con=sqlite3.connect("movie.db")
cur=con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS movie(id INT,title TEXT,genre TEXT,rating REAL,watch INT)")
cur.execute("DELETE FROM movie")

cur.executemany("INSERT INTO movie VALUES(?,?,?,?,?)",[
(1,"KGF","Action",9.2,500),
(2,"RRR","Action",8.8,700),
(3,"Jawan","Action",8.5,600),
(4,"3 Idiots","Comedy",9.5,900),
(5,"Bhool Bhulaiyaa","Comedy",8.2,400),
(6,"Interstellar","SciFi",9.8,800),
(7,"Avatar","SciFi",9.0,950),
(8,"Inception","SciFi",9.4,850),
(9,"Titanic","Romance",8.7,1000),
(10,"DDLJ","Romance",9.1,750)
])
con.commit()

# Fetch Movies
cur.execute("SELECT * FROM movie")
movies=[Movie(*i) for i in cur.fetchall()]

# Sort by Rating
movies=sorted(movies,key=lambda x:x.rating)

print("Movies Sorted by Rating:")
for m in movies:
    print(m.id,m.title,m.rating)

# Binary Search
search=sorted(movies,key=lambda x:x.id)

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

x=int(input("\nEnter Movie ID: "))
m=bs(search,x)

if m:
    print("Found:",m.id,m.title,m.genre,m.rating,m.watch)
else:
    print("Movie Not Found")

# Top 10 Movies
print("\nTop Rated Movies:")
for m in sorted(movies,key=lambda x:x.rating,reverse=True)[:10]:
    print(m.id,m.title,m.rating)

# Most Watched Movie in Each Genre
print("\nMost Watched Movie in Each Genre:")
cur.execute("""
SELECT genre,title,MAX(watch)
FROM movie
GROUP BY genre
""")

for row in cur.fetchall():
    print(row)

con.close()