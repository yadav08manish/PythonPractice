# Q1: Print Number 1 to10

# a=1
# while(a<=10):
#     print(a)
#     a=a+1


# Q2: Print Number from 100 to 1

# a =100
# while(a>=1):
#     print(a)
#     a=a-1
# print("End of printing")

# Q3: Print a Multiplication table of number

# num= int(input("Please enter a number: "))
# mulFactor=1
# while(mulFactor<=10):
#     multipleRet= num*mulFactor
#     print(multipleRet)
#     mulFactor=mulFactor+1

# Q4: Print the element of the following list using a loop
# [1,4,9,16,25,36,49,64,81,100]

# lst= [1,4,9,16,25,36,49,64,81,100]
# print(type(lst))
# lenLst= len(lst)
# print(lenLst)
# i=0
# while(i<lenLst):
#     print(lst[i])
#     i=i+1

# Q5: Search of a number x in this tuple using loop
#[1,4,9,16,25,36,49,64,81,100]

# tup=(1,4,9,16,25,36,49,64,81,100)
# searchNum=int(input("please enter valueto serch: "))
# print(type(tup))
# lenTup= len(tup)
# i=0
# while(i<lenTup):
#     # print(tup[i])
#     if (searchNum == tup[i]):
#         print(searchNum, " Found at index ",i)
#         break
#     # else:
#     #     print("Not avalable in tuple ", searchNum)
#     i=i+1


# CONTINUE   #skip--> it skips the iteration

# i=0
# while(i<=5):
#     # print(i)
#     if(i==3):
#         # break;
#         i=i+1
#         continue
#     print("Value of i ",i)
#     i=i+1

# Print only odd numbers from 1 to 10 using continue keyword

i=1
while i <= 10:
    if(i%2==0):
        i=i+1
        continue
    print(i)
    i=i+1

 


