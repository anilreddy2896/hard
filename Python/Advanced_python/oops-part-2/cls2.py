class M2:
    count=0
    def __init__(self):
        M2.count=M2.count+1
    @classmethod
    def m1(cls):
        print("Number of objects created is : ",cls.count)
t=M2()
t1=M2()
t2=M2()
M2.m1()
