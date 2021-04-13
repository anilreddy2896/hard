# reading the file

f=open('file.md',"r")
# data=f.read() 
#data=f.read(100)
# data=f.readline()
# data1=f.readline()
#data2=f.readline()
#print(data,data1,data2)
# by doing this one extra new line character is going to be added 
"""print(f.readline())
print(f.readline())
print(f.readline())"""

# this will slove the problem 
print(f.readline(),end='')
## tell is used to loctae the file pointer index position
print(f.tell())
print(f.readline(),end='')

print(f.readline(),end='')


f.close()