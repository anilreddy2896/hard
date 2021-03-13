class Test:
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
    def setAge(self,age):
        self.age=age
    def getAge(self):
        return self.age
l=[]
n=int(input("enter the number of studemts:"))
for i in range(n):
    t=Test()
    name=input("Enter the name: ")
    age=int(input("enter the age"))
    t.setName(name)
    t.setAge(age)
    l.append(t)
for i in l:
    print(t.getName())
    print(t.getAge())