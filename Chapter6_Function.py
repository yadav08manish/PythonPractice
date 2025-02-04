# Function is a block of statement to perform  specific task and returns some value

# def func_name(param1, param2,....):
    #some work
    #return val

# def getsum(a,b):
#     return a+b

# print(getsum(4,3))

# # write a function which calculates avarage of 3 numbers

# def average(a,b,c):
#     ave=(a+b+c)/3
#     return ave
   

# calAve=average(2,5,8)
# print(calAve)

# TYPES of Function:

# Built-in Function 
# print()
# len()
# range()
# type()
# UserDefined Function

# print("Manish")
# print("Manish","Yadav")
# print("Manish", end="$")
# print("Yadav")


# Default Parameters
# we start giving default values from last 
# def cal_prod(a=3,b):  # This will give error since it should start from last
#     print(a*b)
#     return a*b


# def cal_prod(a,b=4):  # This will give error since it should start from last
#     print(a*b)
#     return a*b
# cal_prod(3)


# Let's Patrctice:

# Q1. WAF to print the length of a list (list in the parameter)

# lst = [1,2,3,4,5]
# print(type(lst))
# def cal_LengthOfList(a):
#     print(len(a))
#     return len(a)

# cal_LengthOfList(lst)

# Q2. WAF to print the elements of a list in a single line. (list is the parameter)

# lst= [10,20,30,40,50]
# print(lst)
# def elementInaLine(a):
#     x=""
#     for m in range(0,len(lst)):
#         x=x+str(lst[m])+","
#     print(x)
# elementInaLine(lst)


# def elementInaLineUsing(a):
#     for m in lst:
#         print(m, end=",")

# lst=[1,6,3,4,5,2]
# elementInaLineUsing(lst)

# Q3. WAF to find factorial of n
# def getFactNumber(n):
#     x=1
#     for m in range(1,n+1,1):
#         x=x*m
#     print(x)

# getFactNumber(int(input("Enter value for factorial: ")))

# Q4. WAF to Convert USD to InR

# def getINRFromUSD(n):
#     return n*80

# usd= input("USD value: ")
# rupees= getINRFromUSD(int(usd))
# print(usd, "dollar in rupees ", rupees)

# Q5. 

# def getString(n):
#     if(n%2==0):
#         print("String")
#     else:
#         print("Odd")
# nn= input("Please Enter a value: ")
# getString(int(nn))