class Student:
    def __init__(self,name,marks,id):
        self.name=name
        self.marks=marks
        self.id=id
    def  display(self):
        print("Student name: ",self.name)
        print("Student marks: ",self.marks)
        print("Student id: ",self.id)

class Modify:
    def mod(student):
        student.marks=student.marks * 1.50
        student.display()  
s=Student("anil",50,595)
s.display()
Modify.mod(s)
