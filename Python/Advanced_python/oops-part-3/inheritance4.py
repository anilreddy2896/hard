class P:
    a=10
    def __init__(self):
        self.b=100
    def m1(self):
        print("this is instance method")
    @classmethod
    def m2(cls):
        print("this is class method")
    @staticmethod
    def m3():
        print("it is a static method")
class C(P):
    pass
c=C():
print(c.a)
print(c.b)
print()