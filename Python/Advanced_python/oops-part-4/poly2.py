class Duck:
    def talk(self):
        print("quack quack......")
class Dog:
    def bark(self):
        print("bow bow.......")

def f(obj):
    if hasattr(obj,"talk"):
        obj.talk()
    elif hasattr(obj,"bark"):
        obj.bark()
d=Duck()
f(d)
k=Dog()
f(k)