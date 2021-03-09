def decor(func):
    def inner(a,b):
        if b==0:
            print("please enter non zero number")
        else:
           return func(a,b)
    return inner

@decor
def div(a,b):
    return a/b
print(div(10,2))
div(10,0)