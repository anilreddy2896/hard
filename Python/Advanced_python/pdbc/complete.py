import mariadb
import time
import sysconfig
con=mariadb.connect(
    user="root",
    password="password",
    host="127.0.0.1",
    port=3306,
    autocommit=True,
    database='test'
)
cursor=con.cursor()
try:
    cursor.execute("CREATE TABLE IF NOT EXISTS employee(eno INT(5) ,ename VARCHAR(10),esal INT(10),eadd VARCHAR(10))")
    sql="INSERT INTO employee(eno,ename,esal,eadd) VALUES(%s,%s,%s,%s)"
    eno=int(input("enter your id: "))
    ename=input("enter your name: ")
    esal=int(input("enter your sal: "))
    eadd=input("enter your add: ")
    record=(eno,ename,esal,eadd)
    cursor.execute(sql,record)
   
except BaseException as msg:
    print(msg) 
else:
     print("table created successfully") 
finally:
    cursor.close()