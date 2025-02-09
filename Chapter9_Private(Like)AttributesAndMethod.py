# Private

# Private methods and attributes are meant to be used only with in the class and are not accessible out side the class
# To declare private property we user __ (2 underscore before the property name)
# __name

class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass
    def reset_pwd(self):
        print(self.__acc_pass)
    def __Hello(self):
        print("Hello")
    def Welcome(self):
        self.Hello();

acc1= Account("12345","Pwad1")
print("Account No is ",acc1.acc_no)
acc1.reset_pwd()
# print("Account Pwd is ", acc1.__acc_pass)  # This will give Error
# acc1.__Hello()  # This will give Error AttributeError: 'Account' object has no attribute '__Hello'

#BUT
acc1.Welcome()
