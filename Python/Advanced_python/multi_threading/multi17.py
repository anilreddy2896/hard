# why rlock
from threading import *
# l=Lock()
l=RLock()
print("lock object is created")
l.acquire()
print("lock acquired")
l.acquire()
print("trying to acquire again")