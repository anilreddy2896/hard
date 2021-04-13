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
#cursor.execute("drop table eee")
cursor.execute("CREATE TABLE IF NOT EXISTS eee(EMPID INT AUTO_INCREMENT PRIMARY KEY ,FNAME VARCHAR(15),SUBJECT VARCHAR(10),DEPART_ID INT DEFAULT 3,FOREIGN KEY(DEPART_ID ) REFERENCES Gurunanak(DEPART_ID))")
a=input("Faculty name: ")
b=input("subject: ")
sql="INSERT INTO eee(FNAME,SUBJECT) VALUES(%s,%s)"
record=(a,b)
cursor.execute(sql,record)