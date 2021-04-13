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
cursor.execute("SHOW TABLES")

for i in result:
    try:
        name=input("enter the database name which you want to create")
        if i!=name:
            cursor.execute('CREATE DATABASE name')
            print("database create")
        else:
            print(i)
    except BaseException as msg:
        print(msg)
    
   