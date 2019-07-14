import mysql.connector # pip install mysql-connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "Sql Statements here"

mycursor.execute(sql)

mydb.commit()
