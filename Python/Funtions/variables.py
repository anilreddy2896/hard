# global variable
a=10000
def test():
     
    # a = 20000 #local variable
     #print(globals()['a'])
     global a
     a = 2211
     print(a)
   
a=test ## function aliasing
a()
