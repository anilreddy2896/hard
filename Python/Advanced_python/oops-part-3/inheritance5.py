class P:
    def __init__(self):
        print("parent class constructor")
    def m1(self):
        print("instance method")

class C(P):
    def __init__(self):
        super().__init__()
        print("child constructor")
        self.m1()
    
c=C()
