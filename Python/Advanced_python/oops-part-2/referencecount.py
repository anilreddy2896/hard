import sys
class Car:
    def __init__(self):
        print("program started...")
    def __del__(self):
        print("end of variable")
t=Car()
t1=t
t3=t
t4=t

print(sys.getrefcount(t))