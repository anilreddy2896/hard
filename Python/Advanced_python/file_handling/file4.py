#f=open("file.md","r")
try:
    fname=input("enter the name of the file you want to open: ")
    mode=input("enter the mode in which you want to open the file")
    f=open(fname,mode)
    n=int(input("enter the number of line you want to print: "))
except ValueError as msg:
    print("enter the integers only ",msg)
except BaseException as msg:
    print("The number should be in limit: ",msg)
else:
    print("thanks for entering correct number")
    for i in range(n):
        data=f.readline()
        print(i,data)
finally:
    f.close()

