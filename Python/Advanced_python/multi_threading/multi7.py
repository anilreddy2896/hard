#with multithreading
from threading import *
import time
def double(numbers):
    for i in numbers:
        print("double: ",2*i)
def square(numbers):
    for i in numbers:
        print("square: ",i**i)
numbers=[1,2,3,4,5,6]
begintime=time.time()
t1=Thread(target=double,args=(numbers,))
t2=Thread(target=double,args=(numbers,))
t1.start()
t2.start()
t1.join()
t2.join()
endtime=time.time()
print("total time: ",endtime-begintime)