
## unziping
from zipfile import *
f=ZipFile("file1.zip","r",ZIP_STORED)

# if you the file name
f1=open("names.txt","r")
data=f1.read()
print(data)

# if you don't know the file names
names=f.namelist()
for i in names:
    print("file name: ",i)
    print("content of file is ")
    f1=open(i,"r")
    data=f1.read()
    print(data)