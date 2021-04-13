#without multithreading
import time
def double(numbers):
    for i in numbers:
        print("double: ",2*i)
def square(numbers):
    for i in numbers:
        print("square: ",i**i)
numbers=[1,2,3,4,5,6]
begintime=time.time()
double(numbers)
square (numbers)
endtime=time.time()
print("total time: ",endtime-begintime)