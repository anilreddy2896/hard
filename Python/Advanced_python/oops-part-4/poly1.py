class P:
    def __init__(self):
        print("property in all forms")
    def marriage(self):
        print("marry appalamma | laskhmi")
class C(P):
    def marriage(self):
        print("marry sunny| anushka")
        super().marriage()

c=C()
c.marriage()