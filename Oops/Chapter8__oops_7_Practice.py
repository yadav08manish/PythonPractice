class Account:
    def __init__(self, accountNO,balance):
        self.accountNo=accountNO
        self.balance=balance
        print("Account No ", accountNO, " has balance ",balance)
    
    def Debit(self, amount):
        self.balance=self.balance-amount
        print("Rs ", amount, "deducted, balance amount is ", self.balance)

    def Credit(self,amount):
        self.balance=self.balance+amount
        print("Rs ", amount, "deposited, balance amount is ", self.balance)

a1 = Account(12345,100000)
a1.Debit(100)

a1.Credit(100000)