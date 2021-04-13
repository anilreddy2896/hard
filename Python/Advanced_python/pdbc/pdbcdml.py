import mariadb
con=mariadb.connect(
    user="root",
    password="password",
    host="127.0.0.1",
    port=3306,
    autocommit=True,
    database='test'
)
cursor=con.cursor()
## SELECT
"""cursor.execute("SELECT * FROM computers")
result=cursor.fetchall()
for i in result:
    print(i)"""
#cursor.execute("SHOW DATABASES")
"""cursor.execute("SHOW TABLES")
result=cursor.fetchall()
for i in result:
    print(i)"""
"""cursor.execute("SHOW COLUMNS FROM computers")
result=cursor.fetchall()
for i in result:
    print(i)"""
"""cursor.execute("SELECT EMPID,SUBJECT FROM computers WHERE EMPID=2")
result=cursor.fetchall()
for i in result:
    print(i)"""

## INSERT:
"""sql="INSERT INTO COMPUTERS(FACULTY_NAME,SUBJECT,YEAR) VALUES(%s,%s,%s)"
record=('bac','es',3)
cursor.execute(sql,record)
cursor.execute("INSERT INTO COMPUTERS(FACULTY_NAME,SUBJECT,YEAR) VALUES('sac','daa',2)")"""

## update 

"""cursor.execute("UPDATE COMPUTERS SET FACULTY_NAME='ANIL' WHERE EMPID=6")"""
