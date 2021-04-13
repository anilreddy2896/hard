from threading import *
import time
def display():
    print("i am child thread")
    time.sleep(4)
print('active count',active_count())
t1=Thread(target=display,name="child1 ")
t2=Thread(target=display,name="child2 ")
t3=Thread(target=display,name="child3 ")
t4=Thread(target=display,name="child4 ")
t1.start()
print('active count',active_count())
t2.start()
print('active count',active_count())
t3.start()
print('active count',active_count())
t4.start()
l=enumerate()
for t in l:
    print("name",t.name)
    print("identity number",t.ident)
time.sleep(10
])
print('active count',active_count())
