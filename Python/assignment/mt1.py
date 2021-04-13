n=input("What is your name? ")
print("There are {} characters in your name".format(len(n)))
name=n.lower()
acount=0
ecount=0
icount=0
ocount=0
ucount=0
for i in name:
    if i == 'a':
        acount+=1
    
    elif i== 'e':
        ecount+=1
        
    elif i== 'i':
        icount+=1
    
    elif i== 'o':
        ocount+=1
    
    elif i== 'u':
        ucount+=1
    
print("Number of a is",acount)
print("Number of e is",ecount)
print("Number of i is",icount)
print("Number of o is",ocount)
print("Number of u is",ucount)

    
    