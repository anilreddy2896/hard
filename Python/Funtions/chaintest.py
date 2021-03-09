def decor1(func):
    def inner(name):
        print("decor1")
        s=input("enter your favourite animal: ")
        print("Favorite animal:",s)
        func(name)
    return inner
def decor2(func):
    def inner(name):
        print("decor2")
        q=input("enter your favorite food : ")
        print("Food i like is :" , q)
        func(name)
    return inner
"""@decor2
@decor1"""
@decor1
@decor2
def wish(name):
    print("hello",name,"how are you")
l = ["anil","pavan"]
for i in l:
    wish(i)