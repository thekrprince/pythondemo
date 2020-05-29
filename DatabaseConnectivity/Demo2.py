import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="prince", passwd="9695", database="tech")

mycursor = mydb.cursor()

mycursor.execute("Select * from device")

result = mycursor.fetchone()

for data in result:
    print(data)