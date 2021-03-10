from random import *
def dice():
    a=randint(1,6)
    return a
a=dice()
print(a)
if a==6:
    print("you got one more chance")
    b=dice()
    print(b)