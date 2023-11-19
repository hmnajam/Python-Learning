import mysql.connector


myDB = mysql.connector.connect(host = "localhost", user = "root", passwd ="8star@Mysql", database = 'employees')

myCur = myDB.cursor()
myCur.execute("INSERT INTO USER VALUES(1001, 'Najam', 'hmnajam@gmail.com', 'pro')")
myCur.execute("INSERT INTO USER VALUES(1002, 'Najam', 'hmnajam@gmail.com', 'pro')")
myCur.execute("INSERT INTO USER VALUES(1003, 'Najam', 'hmnajam@gmail.com', 'pro')")
myCur.execute("INSERT INTO USER VALUES(1004, 'Najam', 'hmnajam@gmail.com', 'pro')")
myCur.execute("INSERT INTO USER VALUES(1005, 'Najam', 'hmnajam@gmail.com', 'pro')")
myDB.commit()


myCur.execute("select * from USER")
result = myCur.fetchall()
for i in result:
    print(i)
myDB.close()


