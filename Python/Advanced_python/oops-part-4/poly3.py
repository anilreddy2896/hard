## operator overloading
class Book:
    """def __init__(self,pages):
        self.pages=pages"""
    def setPages(self,pages):
        self.pages=pages
    def getPages(self):
        return self.pages
    def __add__(self,other):
        return self.pages + other.pages
def boook():
    b=Book()
    pages=int(input("Enter number of pages: "))
    b.setPages(pages)
    print(b.getPages())
    return pages

l=[]
for i in range(2):
    i=boook() 
    l.append(i)  
print(l)
