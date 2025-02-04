# Abstraction: Hiding the implementation details from user and showing only the essential features to the user

#Encapsulation: wrapping data functions into a single unit (object)


# Create Account class with 2 attributes - balance and account no.
# Create methods for debit, credit and printing the balance

class Account:
    def __init__(self,accountNo, balance):
        self.accountNo=accountNo
        self.balance=balance
        print("For Account No ",accountNo," balance is ", balance)

    def Debit(self, amount):
        self.balance=self.balance-amount
        print("Rs.", amount, "was debitted")
        print("Total balance is ", self.balance)
    
    def Credit(self, amount):
        self.balance=self.balance+amount
        print("Rs.", amount," was Credited")
        print("Total balance is ", self.balance)
    
acc1= Account(10000,12345)
acc1.Debit(100)
acc1.Credit(200)


        
