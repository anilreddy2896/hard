try:
    amount=float(input('enter the principal amount: '))
    interest=float(input("enter the rate of interest: "))
    year=int(input("enter the number of years "))
    c= amount * (pow(( 1 + interest /100),year))
    print(c)
except (ValueError,ZeroDivisionError) as msg:
    print("enter the correct values",msg)
finally:
    print("Thanks")