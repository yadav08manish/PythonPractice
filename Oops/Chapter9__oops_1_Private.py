class Account:
    def __init__(self, acc_no, acc_pass):
        self.__acc_no=acc_no
        self.__acc_pass=acc_pass
        # print("accountNO ",acc_no ,"and pwd is ",acc_pass)
    
    def __Hello(self):
        print(self.__acc_no)
        print(self.__acc_pass)

    def Hello1(self):
        self.__Hello()
acc1= Account(12345,'@dd44')
acc1.Hello1()
# print(acc1.__acc_no)
# print(acc1.__acc_pass)


