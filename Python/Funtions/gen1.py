
import time
def countdown(num):
    print("this is generators")
    while num >= 0 :
        yield num
        time.sleep(2)
        num = num-1


t1=time.time()
a=countdown(200000000000000000000000000000)
t2=time.time()
print(t2-t1)
    