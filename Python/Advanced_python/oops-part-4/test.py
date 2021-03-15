class Test:
    def m1(self,*a):
        total=0
        for i in a :
            total=total+i
        print(total)
t=Test()
t.m1()
t.m1(10,20)
t.m1(10,30,60)

