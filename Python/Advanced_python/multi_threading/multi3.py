#without using the thread class
from threading import *
def display():
    for i in range(10):
        print("child thread")
t=Thread(target=display)
t.start()
for i in range(10):
    print("main thread")