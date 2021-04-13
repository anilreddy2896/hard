f=open("testfile.txt","w") ## if the file is not present it will create it
print("Name of the file: ",f.name)
print("mode of the file: ",f.mode)
print("Is file is readable: ",f.readable())
print("Is file is writable: ",f.writable())
print("is file is closed: ",f.closed)
f.close()
print("is file is closed: ",f.closed)
