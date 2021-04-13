from threading import *
import time
def job():
    for i in range(10):
        print("lazy thread")
        time.sleep(2)
t=Thread(target=job)
t.setDaemon(True)
print(t.isDaemon())
t.start()
print(current_thread().name,"is end of execution")