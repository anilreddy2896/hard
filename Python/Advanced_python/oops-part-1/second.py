class Test():
    def __init__(self):
        print("trying to find the things on without the argumrnts")
    def __init__(self,x):
        print("with one arg")
        print(id(self))
t=Test(100)

### in this case 2 constructors are defined but if method overloading concept is not valid in the python so the recently
## decleared constructor will be executed and the first decleared ones will be ignored

## we can constructor explicity
t.__init__(10)
print(id(t))