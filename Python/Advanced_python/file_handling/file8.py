import os
fname=input("enter the file name: ")
a=os.path.isfile(fname)
if a==True:
    f=open(fname,"r+")
    print(f.read())
else:
    print("sorry")
f.close()