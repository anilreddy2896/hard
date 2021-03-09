# calling the function again again by itself is called recurrsion
def fact(num):
    result=1
    if num==0:
        print(result)
    elif num >=1:
        result = num * fact(num-1)
    return result        
print(fact(5))