import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",database="DB5")
cur=mydb.cursor()
S="DELETE FROM book WHERE title='CS'"
cur.execute(S)
mydb.commit()

