import mysql.connector
mydb = mysql.connector.connect(host='localhost', user='root',database="DB5")
cur = mydb.cursor()

S="Select * from book"              #for printing data
cur.execute(S)
result=cur.fetchall()
for rec in result:
   print(rec)

