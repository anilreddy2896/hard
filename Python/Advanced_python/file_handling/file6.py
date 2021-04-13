# using with statement
with open("file.md","r") as f:
    print(f.readline(),end='')
    print(f.readline(),end='')
print(f.closed)
