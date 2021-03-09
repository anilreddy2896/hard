def test(a,b):
    print("a value:",a)
    print("b value:",b)
    return a*b
"""a=test(b=1,3)"""
a=test(b=1,a=3)
print(a)