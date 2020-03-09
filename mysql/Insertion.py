import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root',database="DB5")

S = "INSERT INTO book(book_id,title,price) VALUES (%s, %s, %s)"
books=[(1,'CS',400),(2,'ML',300),(3,'DATA SCIENCE',200)]
cur = mydb.cursor()
cur.executemany(S,books)
mydb.commit()
print("table created")
