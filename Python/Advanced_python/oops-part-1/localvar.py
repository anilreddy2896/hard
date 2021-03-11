# to meet temporary requirements of programmer ,local variables are used
class Test():
    def __init__(self):
        a=1000
        print(a)
    def m1(self):
        global a
        a=100
        print(a)
    def m2(self):
        b=200
        print(b)
    @classmethod
    def m3(cls):
        c=300
        print(c)
    @staticmethod
    def m4():
        d=400
        print(d)
        print(a) 

        # print(a) this is error we cannot Acess the local variable
        
t=Test()
t.m1()
t.m2()
t.m3()
t.m4()