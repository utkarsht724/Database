import mysql.connector
mydb = mysql.connector.connect(host='localhost', user='root',database="DB5")
cur = mydb.cursor()
S="UPDATE book SET price=price+100 WHERE Price>200"
cur.execute(S)
mydb.commit()
