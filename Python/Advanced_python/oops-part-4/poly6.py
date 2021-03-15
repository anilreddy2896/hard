class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self,other):
        print("magic add method is calling")
        total= self.pages+other.pages
        return Book(total)
    def __str__(self):
        print("Str method is calling ")
        return str(self.pages)
b=Book(200)
b1=Book(300)
b2=Book(400)
b3=Book(500)
print(b+b1+b2+b3)
# number of times magic method  called is equal to number of number of opertator symbols
# like (+,-,*)