class P:
    def __init__(self):
        self.name="Anil"
        self.a=10
        # try removing the multiline comments 
    def __str__(self):
        return self.name
    # magic method
    def __add__(self,other):
        return self.a+other.b
class C:
    def __init__(self):
        self.b=20
    def __add__(self,other):
        return self.b+other.a

p=P()
c=C()
print(p)
print(p+c)
print(c+p)