print("hello ")
try:
    print(10/0)
except BaseException as m :
    print("it is not divided by 0",m)
    
print("hi")