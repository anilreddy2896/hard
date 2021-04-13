from threading import *
print(current_thread().getName())
current_thread().setName("Anilreddy")
print(current_thread().getName())
def display():
    print("name:",current_thread().getName())
t=Thread(target=display,name="jack")
t.start()
t.setName("mac")
t.getName()