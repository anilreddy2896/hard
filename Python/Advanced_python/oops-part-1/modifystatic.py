class Test():
    a=10
    def __init__(self):
        Test.a=100
    def m1(self):
        Test.a=200
    @classmethod
    def m2(cls):
        cls.a=300
        #Test.a=400
    @staticmethod
    def m3():
        Test.a=500

t=Test()
print(t.a)
t.m1()
print(t.a)
t.m2()
print(t.a)
t.m3()
print(t.a)

