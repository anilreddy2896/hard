"""try:
    name==int(input("emter your number"))
except BaseException as msg:
    print("your code is not crt",msg)
else:
    print("you code is perfect")
finally:
    print("Done")"""

"""class ToyoungException(Exception):
    def __init__(self,msg):
        self.msg=msg

class TooldException(Exception):
    def __init__(self,msg):
        self.msg=msg
def marry():
    age=int(input("enter your age"))
    if age>35:
        raise TooldException("its too old to mary ")
    elif age<25:
        raise ToyoungException("You need to grow")
    else:
        print("crt age to marry")

marry()"""

try:
    prin("try")
except:
    print("except")
else:
    print("else")
finally:
    print("finally")