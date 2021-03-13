class University:
    name="anil university"
    def __init__(self):
        print(University.name) 
        self.cse=self.Cse()
        studentname=input("enter your name: ")
        print("Hello ",self.studentname)
        print("Choose your preferred branch:")
        print("1.cse\n2.ece\n3.eee\n4.mech")
        d=int(input("enter your prefered branch: "))
        if d==1:
           
        elif d==2:
            self.Ece()
        elif d==3:
            self.Eee()
        elif d==4:
            self.Mech() 
   

    class Cse:
        def __init__(self):
            self.m1()
        def m1(self):
            print("hello",University.studentname)
            grade=int(input("Enter your grade"))
            if grade <= 50:
                print("sorry we cannot give you admission")
            else:
                print("congrats")
                self.next()
        def next(cls):
            print("this is the final Step:")
            
            
    class Ece:
        pass
    class Eee:
        pass
    class Mech:
        pass
s=University()       