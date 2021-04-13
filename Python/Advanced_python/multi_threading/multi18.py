from threading import *
import time
s=Semaphore(2)
#s=BoundedSemaphore(2)
s.acquire()
s.acquire()
s.release()
s.release()
s.release()