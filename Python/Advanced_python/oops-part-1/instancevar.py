#instance variable: if every object require seperate value
class Person():
    def __init__(self,name):
        self.name=name # inside constructor
    def about(self,age):
        self.age=age #(inside method)
        print("My Name:",self.name)
        print("age:",self.age)
p=Person("anil")
p.number=9849574040 # outside the class
# check by commenting this 
p.about(35) 
print(p.number)

# to get the instance variables present in a class
print(p.__dict__)

# accessing the instance variables
print(p.name)
print(p.age)
print(p.number)

# to delete instance variable
# outside
del p.name
# inside [del self.<name of var>]