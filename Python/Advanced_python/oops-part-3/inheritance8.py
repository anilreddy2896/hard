class A:
    def m1(self):
        print("this A class method")

class B(A):
    def m1(self):
        print("this b class method")
class C(B):
    def m1(self):
        print("this c class method")

class D(C):
    def m1(self):
        print("this d class method")

class E(D):
    def m1(self):
        # B.m1(self) [This is one method of using]

        # second method of using super class method
        super(C,self).m1()

e=E()
e.m1()