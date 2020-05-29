import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="prince", passwd="9695")

mycursor = mydb.cursor()

mycursor.execute("Show databases")

for db in mycursor:
    print(db)