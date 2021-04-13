import mariadb
import time
import sysconfig
con=mariadb.connect(
    user="root",
    password="password",
    host="127.0.0.1",
    port=3306,
    database="test",
    autocommit=True
)   
cursor=con.cursor()
while True:
    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"    
    name=input("Enter your name: ")
    address=input("Enter your address: ")
    val = (name, address)
    cursor.execute(sql,val)
    


