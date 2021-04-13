x=input("Enter amount of money (in dollar) with 0,1 or 2 decimal places: ")
i=int(x[-1])
if(i==1 or i==2):
     j=0 #rounding off cents as per rules
elif(i==3 or i==4 or i==6 or i==7):
     j=5
elif(i==8 or i==9):
     j=10
else:
     j=i
x=str(x)
if(j==10):
      k=x[len(x)-2]
      k=int(k)+1
      x=x[:len(x)-2]+str(k)+"0"
else:
     l=len(x)-1
     x=x[:l]+str(j)
print(x)