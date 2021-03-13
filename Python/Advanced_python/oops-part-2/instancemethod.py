## any method with instance variables is called instance method
# for instance method first arg is self thisis must
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        self.display()
    def display(self):
        print("student name is:",self.name)
        print("marks:",self.marks)
        self.grade()
        
    def grade(self):
        if self.marks>=70:
            print("you got 1st class")
        elif self.marks>=50:
            print("you got 2nd class")
        elif self.marks>=36:
            print("you got 3rd class")    
        else:
            print("you are failed ")
s1=Student("anil",90)
#s1.display()
#s1.grade()
