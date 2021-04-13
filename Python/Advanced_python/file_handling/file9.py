import os
fname=input("enter the file name: ")
a=os.path.isfile(fname)
if a==True:
    f=open(fname,"r+")
    list=f.readlines()
    lcount=0
    wcount=0
    ccount=0
    for i in list:
        lcount=lcount+len(list)
        ccount=ccount+len(i)

        words=i.split()
        wcount=wcount+len(words) 
        
    print("number of lines",lcount)
    print("number of words",wcount)
    print("number of char",ccount)
else:
    print("sorry")
f.close()