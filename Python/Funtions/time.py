def first(num):
    n = 0
    while n <= num:
        yield n
        n = n+1
a=first(5)
for i in a:
    print (i)
