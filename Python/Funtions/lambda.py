
s=lambda x: x * x  
print(s(20))

l=[1,6,9,4,6,8]
b=list(filter(lambda x:x%2==0,l))
print(b)

c=[85,96,8,4,2,98,20,21,23,97]
d=list(map(lambda x:x*2,c ))
print(d)

from functools import *
f=[10,20,30,40,50,60]
a=reduce(lambda x,y:x+y,f)
print(type(a))
print(a) 