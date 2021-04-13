# why synchronization
from threading import *
import time
def wish(name):
    for i in range(10):    
         print("good morning: ",end='')
         time.sleep(3)
         print(name)
t1=Thread(target=wish,args=('dhoni',))
t2=Thread(target=wish,args=('anil',))
t1.start()
t1.join()
t2.start()
