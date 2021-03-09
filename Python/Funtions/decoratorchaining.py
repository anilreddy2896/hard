def dec(funct):
    def inner(name):
        if name == "pavan":
            print("hello pavan you are thop")
        else:
            return funct(name)
    return inner
decorator=dec( "wish ")
def wish(name):
    print("hello",name,"good man")
wish("pavan")
decorator("pavan")