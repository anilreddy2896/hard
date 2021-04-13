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
cursor.execute('create table if not exists students(s_name varchar(15),s_id int(5) ,s_year int(10),marks int(10))')
sql="insert into students values(%s,%s,%s,%s)"
value=[('sampath',2,4,500),('rakesh',6,3,570),('teja',8,2,580),('rohith',7,4,420),('lokesh',3,3,400)]
cursor.executemany(sql,value)