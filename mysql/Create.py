import mysql.connector
mydb = mysql.connector.connect(host='localhost', user='root',database="DB5")

S = "CREATE TABLE book(book_id integer(4),title varchar(20),price float(5,2))"
cur = mydb.cursor()
cur.execute(S)
