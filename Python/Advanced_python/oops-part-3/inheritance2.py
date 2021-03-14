class Car:
    def __init__(self,name,model,color):
        self.name=name
        self.model=model
        self.color=color
        self.getinfo()
    def getinfo(self):
        print("car information")
        print("Name of car: ",self.name)
        print("Model of the car: ",self.model)
        print("Color of the car: ",self.color)
class Employee:
    def __init__(self,ename,eno,car):
        self.ename=ename
        self.eno=eno
        self.car=car
        self.fullinfo()
    def fullinfo(self):
        print("Name: ",self.ename)
        print("Id: ",self.eno)
        self.car.getinfo()
c=Car("alto",2008,"black")
e=Employee("Anil",120,c)
