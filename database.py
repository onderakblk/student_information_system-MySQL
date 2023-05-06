import mysql.connector

def create():
    mydb = mysql.connector.connect(
        host = "localhost", 
        user = "root",
        password = "12345678",
    )

    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS schooldb")
    mydb.close()

def table():
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "12345678",
        database = "schooldb"
    )
    mycursor = connection.cursor()
    mycursor.execute("CREATE TABLE IF NOT EXISTS student (id INT AUTO_INCREMENT PRIMARY KEY , StudentNumber VARCHAR(45) NOT NULL, Name VARCHAR(45), SurName VARCHAR(45), Birthdate DATETIME, Gender VARCHAR(45), Class VARCHAR(45))")
    connection.close()

create()
table()
