## we will break the crux of inner class classes and compostion
# innerclass
# we will write same program using inner class and composition

class Car:
    def __init__(self,name,model,color):
        self.name=name
        self.model=model
        self.color=color
        self.display()
    def display(self):
        print('Name of car: ',self.name)              
        print("model: ",self.model)
        print("color: ",self.color)
        self.e=self.Engine("petrol","high")
    class Engine:
        def __init__(self,fuel,level):
            self.fuel=fuel
            self.level=level
            self.description()
        def description(self):
            if self.fuel=="petrol":
                print("it is high cost but low maintainence")
            elif self.fuel=="diesel":
                print("it is low cost and high maintance")
            else:
                print('select correct fuel type ')
c=Car("innova",2008,"black")
d=c.Engine("petrol","high")

class Car:
    def __init__(self,name,model,color):
        self.name=name
        self.model=model
        self.color=color
        self.display()
    def display(self):
        print('Name of car: ',self.name)
        print("model: ",self.model)
        print("color: ",self.color)
class Engine:
        def __init__(self,fuel,level):
            self.fuel=fuel
            self.level=level
            self.name=input("enter the nameof car ")
            self.model=int(input("enter the model of car "))
            self.color=input("enter the color of car ")
            self.car=c1=Car(self.name,self.model,self.color)
            self.description()
        def __str__(self):
            return self.name
        def description(self):
            if self.fuel=="petrol":
                print("it is high cost but low maintainence")
         
            elif self.fuel=="diesel":
                print("it is low cost and high maintance")
            else:
                print('select correct fuel type ')

e=Engine("petrol","high")
