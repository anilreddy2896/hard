## banking operation
import sys
class Customer():
    Bankname="ANIL co-operate bank"
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount
        print("Balance after deposit",self.balance)
    def withdraw(self,amount):
        if amount > self.balance:
            print("insufficient balance")
            sys.exit()
        self.balance=self.balance-amount
        print("Balance after withdraw",self.balance)
print("welcome to the ",Customer.Bankname)
name=input("Enter your name: ")
c=Customer(name)
while True:
    print("d- Deposit \n w-Withdraw \n e-Exit")
    select=input("Select the operation which you want to perform:")
    option=select.lower()
    if option=="d":
        amount=float(input("Enter the amount: "))
        c.deposit(amount)
    elif option=="w":
        amount=float(input("Enter the amount: "))
        c.withdraw(amount)
    elif option=="e":
        break
    else:
        print("Please enter the correct and display options only")


    

