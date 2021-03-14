class X:
    a=10
    def __init__(self):
        self.b=100

    def m1(self):
        print("this is m1 from class X")

class Y:
    c=20
    def __init__(self):
        self.d=200
    def m2(self):
        x=X()
        print(x.a)
        print(x.b)
        x.m1()
        print(self.c)
        print(self.d)
        print("this is m2 from class y")
y=Y()
y.m2()