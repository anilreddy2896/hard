
# has-a and is-a relation
class Car:
    def __init__(self,name,model,color):
        self.name=name
        self.model=model
        self.color=color
    def getinfo(self):
        print("Name of car:",self.name)
        print("Model of the car: ",self.model)
        print("Color of the car: ",self.color)
        
class P:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def details(self):
        print("Name of employee: ",self.name)
        print("Age of the employee: ",self.age)
class C(P):
    def __init__(self,name,age,eid,sal,car):
        super().__init__(name,age)
        self.eid=eid
        self.sal=sal
        self.car=car
        self.fullbio()
    def fullbio(self):
        super().details()
        print("sal of employee: ",self.sal)
        print("eid of employee: ",self.eid)
        self.car.getinfo()

class Hero:
    def __init__(self,c):
        self.car=c
        name=input("Enter the name of the Hero: ")
        self.name=name
        print("Now we are going to ask the car details of : ",self.name)
        self.car.getinfo()

c=Car("innova",2008,"black")
h=Hero(c)
e=C("anil",25,1050051,8000,c)

