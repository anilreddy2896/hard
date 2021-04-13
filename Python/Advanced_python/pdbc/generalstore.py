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
cursor.execute("select * from general_store")
result=cursor.fetchall()
for i in result:
    print(i)
a=int(input("enter the item number "))
b=int(input("Enter the quantity you want "))
cursor.execute("SELECT @c:= item_quantity FROM general_store WHERE item_id={}".format(a))
"""cursor.execute("SELECT item_name FROM general_store WHERE @c>={}".format(b))
x=cursor.fetchall()
print(x)"""
cursor.execute("SELECT @d:= item_name FROM general_store WHERE item_id={}".format(a))
cursor.execute("CREATE or replace TRIGGER quantity BEFORE UPDATE  ON general_store FOR EACH ROW SET NEW.item_quantity=@c-{}".format(b))
cursor.execute("UPDATE general_store SET item_name=@d WHERE item_id={}".format(a))
cursor.execute("select * from general_store")
r=cursor.fetchall()
for i in r:
    print(i)

