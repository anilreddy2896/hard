num=input("enter the number: ")
list=num.split('0')
list=[int(x) for x in list]
print(list)
count=0
k=0
for i in list:
    if i%2==0:
        count=count+i
        k=k+1
    else:
        i+=1
print(count/k)