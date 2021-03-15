class Account:
    def __init__(self,name,balance,branch,minbal):
        self.name=name
        self.balance=balance
        self.branch=branch
        self.minbal=minbal

    def __str__(self):
        return "The Name of account holder is {} , is balance is {} at branch {} and he should maintain minimum balance {}".format(self.name,self.balance,self.branch,self.minbal)

a=Account("Pavan",10000000,"Dsnr","100000")
b=str(a)
print(b)
c=repr(a)
print(c)
d=repr(c)
print(d)