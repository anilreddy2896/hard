## uses only static variables 
# static method should have the first argument as cls 
# and it has a decorator @class method

"""@classmethod 
def m1(cls):"""

class Student:
    a=20
    b=30
    @classmethod
    def method(cls):
        c=cls.a+cls.b
        print(c)

"""s1=Student()
s1.method()"""
Student.method()