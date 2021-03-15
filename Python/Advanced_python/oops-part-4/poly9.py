class Poly:
    def m1(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print("The sum of numbers is : ",a+b+c)
        elif a!=None and b!=None:
            print("The sum of numbers is : ",a+b)
        elif a!=None:
            print("The sum of numbers is : ",a)
        else:
            print("enter atleast one argument")

a=Poly()
a.m1()
a.m1(2)
a.m1(10,19)
a.m1(10,28,29)