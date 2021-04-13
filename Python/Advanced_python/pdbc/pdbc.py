import mariadb
con=mariadb.connect(
    user="root",
    password="password",
    host="127.0.0.1",
    port=3306,
    database="test",
    autocommit=True
)   
cursor=con.cursor()
try:
    cursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
    cursor.execute("CREATE TABLE students (name VARCHAR(255), address VARCHAR(255))")
except BaseException as msg:
    print(msg)
    cursor.execute('SHOW TABLES')
    for x in cursor:
        print (x)
    try:
         sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
         val = ("John", "Highway 21")
         cursor.execute(sql, val)
    except BaseException:
        print("already")
    #cursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
    #cursor.execute("DELETE FROM customers WHERE address = 'Highway 21'")
    cursor.fetchall()
    

finally:
    cursor.close()

