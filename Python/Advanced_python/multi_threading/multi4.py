# extending with the thread class
from threading import *
class Mythread(Thread):
    def run(self):
        for i in range(10):
            print("child thread-1")
t=Mythread()
t.start()
for i in range(10):
    print("main thread")
