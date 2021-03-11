class Test():
    a=10
    def __init__(self):
        Test.b=20
        print(Test.a)
        print(self.a)
    def m1(self):
        Test.c=30
        
    @classmethod
    def m2(cls):
        Test.d=40
        cls.e=50
        print(cls.c)
        #del cls.e
    @staticmethod
    def m3():
        Test.f=60
t=Test()
#print(Test.__dict__)
Test.g=600
#print(Test.__dict__)
t.m1()
#print(Test.__dict__)
t.m2()
#print(Test.__dict__)
t.m3()
# del Test.e
#print(Test.__dict__)

#accesssing the static variables
print(t.f)
print(Test.d)
