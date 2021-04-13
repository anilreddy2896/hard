import mariadb
con=mariadb.connect(
    user="root",
    password="password",
    host="127.0.0.1",
    port=3306,
    autocommit=True,
    database='schools'
)
cursor=con.cursor()
"""cursor.execute("SELECT * FROM COMPUTERS WHERE FACULTY_NAME='ANIL'")"""
'''cursor.execute("select * from computers where depart_id =1 ")
cursor.execute("SELECT * FROM COMPUTERS WHERE FACULTY_NAME LIKE '%ac'")'''
cursor.execute("SELECT * FROM COMPUTERS WHERE FACULTY_NAME LIKE '_a_%'")
'''cursor.execute("SELECT * FROM COMPUTERS ORDER BY  YEAR DESC LIMIT 2 OFFSET 1")''' # DEFAULT IS ASCENDING ORDER 
SELECT * FROM students;
SELECT s_id,s_name FROM students ORDER BY s_id;
SELECT s_year,COUNT(*) FROM students GROUP BY s_year DESC ;
SELECT * FROM students HAVING s_year=3;
a=cursor.fetchall()
print(a)
