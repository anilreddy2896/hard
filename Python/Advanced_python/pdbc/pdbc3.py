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
cursor.execute("CREATE TABLE IF NOT EXISTS student(sid INT(6),sname VARCHAR(10),fathername VARCHAR(15),mothername VARCHAR(15),snumber VARCHAR(10))")
cursor.execute("INSERT INTO student (sid,sname,fathername,mothername,snumber) VALUES (1,'siri','gova','sai','9553782')")
cursor.execute("SELECT sid,snumber FROM student")
result=cursor.fetchall()
for i in result:
    print(i)
