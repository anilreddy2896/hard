## trying to cover all the oops-part1

# creation of class
class Employee:
    company="crazy infotech"
    #creation of constructor
    def __init__(self,name,id):
        self.name=name
        self.id=id
        self.display() 

    def display(self):
        print("Name: ",self.name)
        print("Id: ",self.id)
        print(Employee.company,"employee")
        self.a=self.Modify()
        self.f=self.a
        self.f.m1()
        self.k=self.f.sal
        print("hello",self.name,self.f.exp)
        print("your salary fixed is:",self.k)
        Increament.m2(self)
        print("for every 2 years the increament will be",self.sal-self.k)  
        print("before:",self.k)
        print("after",self.sal) 
        
    class Modify:
        n=1999
        def m1(self):
            print(Employee.company)
            self.sal=0
            self.exp=int(input("how many years of experience do you have: "))
            if self.exp >= 2:
                self.sal=int(input("enter your expected salary: "))
                if self.sal <= 100:
                    print("sorry")
                else:
                    print("congrats")
                    self.day=int(input("how many day you wanna work")) 
                    if self.day == 5:
                        print("full timer")
                        Full()
                    elif self.day <=4:
                        Part()
                    elif self.day  ==1 :
                        Cas()
                    else:
                        print()
            else:
                print("sorry")
class Increament:
    def m2(self):
        self.sal=self.k * 1.25

class Full:
    def __init__(self):
        print("Welcome to full time job")
        self.details()
    def details(self):
        print("you will get Annual leaves")
        print("you will be having fixed hours of job")
        a=22.5
        print("your pay rate is:",a)
        print("pay during public holidays is",a*2.5)
class Part:
    def __init__(self):
        print("Welcome to part time job")
        self.details()
    def details(self):
        print("you will less Annual leaves")
        print("you will be having fixed 20 hours of job")
        a=22.5
        print("your pay rate is:",a)
        print("pay during public holidays is",a*2.1)
class Cas:
    def __init__(self):
        print("Welcome to  job")
        self.details()
    def details(self):
        print("you will not Annual leaves")
        print("you will not fixed hours of job")
        a=22.5
        print("your pay rate is:",a)
        print("pay during public holidays is",a*3.5)

#creating the object
e=Employee("Mike",1050051)
#Increament.m2(e)



