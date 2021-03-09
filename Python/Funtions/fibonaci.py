# fibonacci sequence 0,1,1,2,3,5,8.......
def fib():
    a,b,c=0,0,1
    #a,b=0,1
    while True:
        yield a
        a,b,c=b,c,a+b+c
        #a,b=b,a+b
        
a=fib()
for i in a:
    if i > 100:
        break
    print(i)
