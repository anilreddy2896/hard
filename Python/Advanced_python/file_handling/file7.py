data="all students who learn english are gems"
f=open('testfile.txt','w')
f.write(data)
with open('testfile.txt','r+') as f:
    print(f.tell())
    #text=f.read()
    print(f.read())
    print(f.tell())
    print(f.seek(22))
    f.write("Devops!!")
    f.seek(22)
    print(f.read())
   