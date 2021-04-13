from threading import *
def job():
    print('child thread')
t=Thread(target=job)
print(t.daemon)
# but if we start the thread then we cannot change it and if we try to change
# we will get error
#t.start()

t.setDaemon(True)
print(t.daemon)