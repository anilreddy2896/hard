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
"""cursor.execute("SELECT * FROM cse")
result=cursor.fetchall()
for i in result:
    print(i)"""

### rename:
"""cursor.execute("ALTER TABLE cse RENAME COLUMN FNAME TO FACULTY_NAME ")"""
## renaming table:
"""cursor.execute("ALTER TABLE cse RENAME TO COMPUTERS")"""
"""cursor.execute("ALTER TABLE COMPUTERS RENAME PRIMARY KEY EMPID TO EID ")"""
# ADDING column
"""cursor.execute("ALTER TABLE COMPUTERS ADD COLUMN YEAR INT")"""
# modify
"""cursor.execute("ALTER TABLE COMPUTERS MODIFY YEAR VARCHAR(10) ")"""
"""cursor.execute("ALTER TABLE COMPUTERS ADD COLUMN SUBJECTS INT")"""
"""cursor.execute("ALTER TABLE COMPUTERS DROP  SUBJECTS")"""
"""cursor.execute("ALTER TABLE COMPUTERS SET UNUSED COLUMN (SUBJECTS)")
cursor.execute("ALTER TABLE COMPUTERS DROP SUBJECTS")"""
#truncate
'''cursor.execute("TRUNCATE TABLE MECH")'''
