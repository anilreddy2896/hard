# without existing of outer class object there is no chance of existing inner class
class Outer:
    def __init__(self):
        print("this is outer class")
        print()
    class Inner:
        def __init__(self):
            print("this is inner class")
            print()
        def m1(self):
            print("inner method")
o=Outer()
i=o.Inner()
i.m1()
