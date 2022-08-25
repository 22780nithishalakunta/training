class Account(Exception):
    def __init__(self,acno,acname,atype,bal):
        self.accountnumber=acno
        self.accountname=acname
        self.accounttype=atype
        self.balance=bal
    def withdraw(self,amount):
        self.amt=amount
        if(self.balance<self.amt):
            raise 'LowBalanceException'
