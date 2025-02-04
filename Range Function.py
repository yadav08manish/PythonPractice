# Range is an important function which returns a sequence of numbers starting from 0 by default, and increments by 1 by default and stops before a specified number

# range(start?, stop, step?)

# print(range(5))  # it has 5 values starting from 0 to 4 

# seq = range(5)  
# print(seq[0])
# print(seq[1])
# print(seq[2])
# print(seq[3])
# print(seq[4])
# # print(seq[5]) #IndexError: range object index out of range

# for m in range(10):   # range(stop)
#     print(m)

# for m in range(2,10): # range(start?, stop)
#     print(m)

# for m in range(2,10,2):  #range(start?, stop, step?)
#     print(m)

# Print even numbers from 1 to 100
# for m in range(2,101,2):
#     print(m)


# PRACTICE using for and range
# 1. Print numbers from 1 to 100

# for m in range(1,101,1):
#     print(m)

# 2. print numbers from 100 to 1
# for m in range(100,0,-1):
#     print(m)

# 3. print a multiplication table of a number
# x = int(input("Enter a number to make table of it : "))
# for m in range(1,11,1):
#     print(x*m)

# using while loop  linear search
# x = int(input("Enter a number"))
# i=1
# while i <=10:
#     print(x*i)
#     i +=1


# Pass Statement: pass is a null statement that does nothing. It is used as a placeholder for future code
# geenerally in python we use pass in Excetion handelling in try catch block
# for el in range(10):
#     pass

# Q1. WAP to find the sum of first n numbers. (using while)
# x=5
# y=1
# sum=0
# while y<=x:
#     # print(x)
#     sum=sum+y
#     y=y+1
# print(sum)

# x=0
# for m in range(1,6,1):
#     x=x+m
# print(x)

# Q2. WAP a program to find the facorial of first n numbers:
# n = int(input("Enter number"))
# fact=1
# for m in range(1,n+1,1):
#     print(m)
#     fact=fact*m
# print(fact)

n = int(input("Enter number"))
i=1
fact=1
while i<=n:
    fact=fact*i
    i=i+1
print(fact)





