class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self,other):
        return self.pages+other.pages
    def __mul__(self,other):
        return self.pages*other.pages
b=Book(200)
b1=Book(300)
b2=Book(400)
print(b+b1+b2)