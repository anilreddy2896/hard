import time
class Test:
    def __init__(self):
        print("object is created ....")
    def __del__(self):
        print("object is deleted.......")

t=Test()
t1=t
t2=t1
print("using t to check")
time.sleep(5)
print("no use of t")
t=None
del t1
del t
del t2
time.sleep(10)
print("End of application.......")