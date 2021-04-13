import mariadb
import time
import sys
con=mariadb.connect(
    user="root",
    password="password",
    host="127.0.0.1",
    port=3306,
    autocommit=True,
    database='test'
)
cursor=con.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Gurunanak(DEPART_ID INT AUTO_INCREMENT PRIMARY KEY,DEPARTMENT_NAME VARCHAR(4),HOD_NAME VARCHAR(15))")
#cursor.execute("CREATE TABLE IF NOT EXISTS cse(EMPID INT AUTO_INCREMENT PRIMARY KEY ,EMPNAME VARCHAR(15),SUBJECT VARCHAR(10), DEPART_ID INT FOREIGN KEY REFERENCES Gurunanak(DEPART_ID))")
DEPARTMENT_NAME=input("Enter the name of the Department: ")
HOD_NAME=input("Enter name of the hod: ")
sql="insert into Gurunanak(DEPARTMENT_NAME,HOD_NAME) VALUES(%s,%s)"
record=(DEPARTMENT_NAME,HOD_NAME)
cursor.execute(sql,record)
print("entered into the database successfully")
cursor.close()

    


