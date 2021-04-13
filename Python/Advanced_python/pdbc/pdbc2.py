import mariadb
import time
import sysconfig
con=mariadb.connect(
    user="root",
    password="password",
    host="127.0.0.1",
    port=3306,
    autocommit=True
)
  
cursor=con.cursor()
cursor.execute("SHOW DATABASES")
for x in cursor:
    print(x)
name=input("enter the database name ")
sql="CREATE DATABASE (name) VALUE (%s)"
cursor.execute(sql,name)

   