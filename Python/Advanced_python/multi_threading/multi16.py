
from threading import *
import time
l=Lock()
def wish(name):
    l.acquire()
    for i in range(10):    
         print("good morning: ",end='')
         time.sleep(3)
         print(name)
    l.release()
t1=Thread(target=wish,args=('dhoni',))
t2=Thread(target=wish,args=('anil',))
t1.start()
t2.start()
