class Student():
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    def speak(self):
        print("My name is: ",self.name)
        print("My age is :",self.age)
        print("My marks are:",self.marks)

## creating object
s1=Student("Anil",25,90)

#calling the method
s1.speak()

#calling the instance variable
print(s1.age)