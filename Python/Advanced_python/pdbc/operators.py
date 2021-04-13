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
'''cursor.execute("select depart_id,subject,year from computers where depart_id=1 AND year=2")'''
'''cursor.execute("select depart_id,subject,year from computers where depart_id=1 OR year=2")'''
cursor.execute("select depart_id,subject,year from computers where NOT year=2")
b=cursor.fetchall()
print(b)