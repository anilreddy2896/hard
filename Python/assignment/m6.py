def adjust(n):
    if (n==1 or n==2):
        m=0
    elif(n==3 or n==4 or n==6 or n==7):
        m=5
    elif(n==8 or n==9):
        m=10
    else:
        m=n
    return m

n=int(input("enter the the number of centes: "))
k=adjust(n)
print(k)

    
    