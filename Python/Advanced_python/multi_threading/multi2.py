from threading import *
import time
def display():
    print("hello everyone we are implementing multiple threads")
    print("thread name:",current_thread().getName())
t=Thread(target=display)
t.start()