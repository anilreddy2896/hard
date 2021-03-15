class Employee:
    def __init__(self,name,sal):
        self.name=name
        self.sal=sal
    def __mul__(self,other):
        return self.sal*other.time
class Time:
    def __init__(self,name,time):
        self.name=name
        self.time=time

e=Employee("anil",8000)
t=Time("ANIL",25)
print(e*t)

