## passing one class to other
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print("name: ",self.name)
        print("marks: ",self.marks)

class Test:
    def m1(self):
        if self.marks==45:
            self.marks=self.marks * 1.5
        else:
            self.marks
        self.display()
s=Student("Anil",45)
Test.m1(s)
s=Student("mac",90)
Test.m1(s)