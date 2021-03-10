class Employees():
    def __init__(self,ename,eid,esal,eage):
        self.ename=ename
        self.eid=eid
        self.esal=esal
        self.eage=eage
    def details(self):
        print("Employee name:",self.ename)
        print("Employee id:",self.eid)
        print("employee sal: ", self.esal)
        print("employee age:",self.eage)
e1=Employees("Rock",1052,10000,26)
e1.details()