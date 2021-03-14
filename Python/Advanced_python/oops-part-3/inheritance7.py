#setters and getters
class Student:
    def setName(self,name):
        self.name=name
    def setMarks(self,marks):
        self.marks=marks
    def getName(self):
        return self.name
    def getMarks(self):
        return self.marks
n = int(input("enter number of students: "))
for i in range(n):
    s=Student()
    name=input("Enter the name: ")
    marks=input("Enter the marks: ")
    s.setName(name)
    s.setMarks(marks)
    print("Name of the student",s.getName())
    print("Marks of ",s.getName(),"is" ,s.getMarks())
    


