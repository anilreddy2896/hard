from threading import *
import time
def display():
    for i in range(5):
        print("sita thread")
        time.sleep(2)
t=Thread(target=display)
t.start()
#t.join()
#t.join(5)
for i in range(5):
    print("rama")