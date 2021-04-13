from threading import *
class Myclass():
    def display(slef):
        for i in range(10):
            print("child thread")
obj=Myclass()
t=Thread(target=obj.display)
t.start()
for i in range(10):
    print("parent thread")