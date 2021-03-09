def fact(num):
    a=1
    while num > 1:
        a=a*num
        num=num-1
    return a
#fact(5)
for i in range(7):
    print("factorial of {} is {}".format(i,fact(i)))