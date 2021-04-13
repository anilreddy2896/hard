## for finding identification number
from threading import *
def display():
    print("i am child thread")
t=Thread(target=display)
t.start()
print(active_count())
print("identification of main thread: ",current_thread().ident)
print("identification of child thread: ",t.ident)
## number of threads that are in active state
print(active_count())