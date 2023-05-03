import mysql.connector
from connection import connection
import datetime


def insertStudents(list):

    cursor = connection.cursor()
    sql = "INSERT INTO student(StudentNumber,Name,SurName,Birthdate,Gender,Class) VALUE (%s,%s,%s,%s,%s,%s)"
    values = list
    cursor.executemany(sql,values)
    try:
        connection.commit()
    except mysql.connector.errors as err:
        print("error",err)
    finally:
        connection.close()
        print("database bağlantisi kapatildi")

def getStudents():
    mycursor = connection.cursor()
    mycursor.execute("SELECT * FROM student ORDER BY StudentNumber")

    try:
        result = mycursor.fetchall()
        for x in result:
            print(f"Numara:{x[1]},\tİsim:{x[2]},\tSoyisim:{x[3]},\tDoğum günü:{x[4]},\tCinsiyet:{x[5]}\tSınıf:{x[6]}")
    except mysql.connector.errors as err:
        print("error",err)
    finally:
        connection.close()
        print("database bağlantisi kapatildi")


def searchname(name):
    mycursor = connection.cursor()
    sql = "SELECT * FROM student WHERE name=%s"
    params = (name,)
    mycursor.execute(sql,params)

    try:
        result = mycursor.fetchall()
        for x in result:
            print(f"Numara:{x[1]},\tİsim:{x[2]},\tSoyisim:{x[3]},\tDoğum günü:{x[4]},\tCinsiyet:{x[5]}\tSınıf:{x[6]}")
    except mysql.connector.errors as err:
        print("error",err)
    finally:
        connection.close()
        if len(result) == 0:
            print("Öğrenci kaydı yok")
        print("database bağlantisi kapatildi")

def searchnumber(number):
    mycursor = connection.cursor()
    sql = "SELECT * FROM student WHERE StudentNumber=%s"
    params = (number,)
    mycursor.execute(sql,params)
    try:
        result = mycursor.fetchall()
        for x in result:
            print(f"Numara:{x[1]},\tİsim:{x[2]},\tSoyisim:{x[3]},\tDoğum günü:{x[4]},\tCinsiyet:{x[5]}\tSınıf:{x[6]}")
    except mysql.connector.errors as err:
        print("error",err)
    finally:
        connection.close()
        if len(result) == 0:
            print("Öğrenci kaydı yok")
        print("database bağlantisi kapatildi")

def update():
    number = input("Güncellenecek öğrenci no: ")
    name = input("İsim: ")
    surname = input("Soyad: ")
    birthdate_str = input("Doğum tarihi(yyyy-mm-dd): ")
    birthdate = datetime.datetime.strptime(birthdate_str, "%Y-%m-%d").date()
    gender = input("Cinsiyet: ")
    classs = input("Sınıf:")

    mycursor = connection.cursor()
    sql = "UPDATE student SET name=%s, surname=%s,birthdate=%s, gender = %s, class=%s WHERE StudentNumber = %s"
    params = (name,surname,birthdate,gender,classs,number)
    mycursor.execute(sql,params)
    try:
        connection.commit()
    except mysql.connector.errors as err:
        print("error",err)
    finally:
        connection.close()
        print("database bağlantisi kapatildi")

def delete():
    number = input("Silmek istediğiniz öğrenci no:")
    mycursor = connection.cursor()
    sql = "DELETE FROM student WHERE StudentNumber=%s"
    params = (number,)
    mycursor.execute(sql,params)
    try:
        connection.commit()
    except mysql.connector.errors as err:
        print("error",err)
    finally:
        connection.close()
        print("database bağlantisi kapatildi")

list = []

menü = input("1. Öğrenci kaydı oluştur\n2.Öğrenci Kayıtlarını getir\n3.Öğrenci sorgulama\n4.Öğrenci bilgi güncelle\n5.Öğrenci kayıt sil\nSeçim: ")
if menü == "1":
    while True:
        studentNumber = input("Numara: ")
        name = input("İsim: ")
        surname = input("Soyad: ")
        birthdate_str = input("Doğum tarihi(yyyy-mm-dd): ")
        birthdate = datetime.datetime.strptime(birthdate_str, "%Y-%m-%d").date()
        gender = input("Cinsiyet: ")
        classs = input("Sınıf:")

        list.append((studentNumber,name,surname,birthdate,gender,classs))

        result = input("Devam etmek istiyor musunuz?(y/n): ")
        if result == "n":
            insertStudents(list)
            break

elif menü == "2":
    getStudents()

elif menü == "3":
    print("------------------------------------------")
    secim = input("1.Öğrenci no\n2.İsim\nSeçim: ")
    if secim == "1":
        number = input("Öğrenci no: ")
        searchnumber(number)
    elif secim == "2":
        isim1 = input("İsim: ")
        searchname(isim1)
    else:
        print("Geçersiz işlem")

elif menü == "4":
    print("--------------------------------------------")
    update()

elif menü == "5":
    print("--------------------------------------------")
    delete()

else:
    print("Geçersiz işlem")