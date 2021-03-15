class Account:
    def __init__(self,name,balance,minbal):
        self.name=name
        self.balance=balance
        self.minbal=minbal
    def deposit(self,amount):
        self.balance=self.balance+amount
        print("{} your balance is {}".format(self.name,self.balance))
    def withdraw(self,amount):
        if self.balance - amount > self.minbal:
            self.balance=self.balance-amount
            print("{} your balance is {}".format(self.name,self.balance))
        else:
            print("sorry insufficent funds you need to maintain minimum {} and your balance is {}".format(self.minbal,self.balance))
    def print_statement(self):
        print("{} your balance is {}".format(self.name,self.balance))

a=Account("Pavan",20000,5000)
a.deposit(20000)
a.withdraw(38000)