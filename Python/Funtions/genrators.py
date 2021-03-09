l=( x*x for x in range(10000000000000000000000000000) )
"""for x in l:
    print(x)"""
# in generator i will not store in the memory
# it just return one by one 
#this what generators
print(type(l))