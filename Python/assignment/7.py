
def adjust(cents):
    c=0
    for i in cents:
       x=cents.index(i)
       if(i==1 or i==2):
           j=0 #rounding off cents as per rules
       elif(i==3 or i==4 or i==6 or i==7):
           j=5
       elif(i==8 or i==9):
          j=10
      else:
         j=i
    cents.remove(i) #remove old value
    cents.insert(x,j) #insert new value
   return cents

n=int(input("Enter total number of cents: "))
print("Enter cents' value between 0 to 9 (inclusive): ")
for i in range(0,n):
    x=int(input()) #input of cents
    cents.append(x)
print("Resultant cents by rounding off to nearst 5 cents: "+str(adjust(cents)))




------
def roundOff(n):
x=round(n)
i=x%10
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

return x

n=eval(input("Enter amount of money (in dollar) with 0,1 or 2 decimal places: "))
print("Resultant amount: "+"$ "+roundOff(n))