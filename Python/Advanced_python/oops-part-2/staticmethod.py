## static method
# we need to use static method if we are using only local variables
# this are also called as method level variables
# general utility methods

class Fun:
    @staticmethod
    def add(a,b):
        print("sum: ",a+b)
    @staticmethod
    def sub(a,b):
        print("sub: ",a-b)
    @staticmethod
    def avg(a,b):
        print("avg: ",(a+b)/2)

Fun.add(10,52)
