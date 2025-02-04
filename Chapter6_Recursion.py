# When a funtion calls itself repeatedly

# def show(n):
#     if(n==0):  #Base Case
#         return
#     print(n)
#     show(n-1)

# show(5)

## #Recurrence Relation

# factorial of 5 = 1*2*3*4*5
# or we can say that factorial of 5 = factorial of 4 * 5
# 5!=4! *5

# n!=(n-1)!*n


# def fact(n):
#     if(n==1 or n==0):
#         return n
#     return fact(n-1)*n

# print(fact(5))

# Q1. Write a recursive function to calculate the sum of first n natural numbers

# def getSumOfNatuaralNumber(n):
#     if(n==1):
#         return 1
#     return getSumOfNatuaralNumber(n-1)+n
    

# print(getSumOfNatuaralNumber(5))

# Q2. Write a recursive funtion to print all elements in list.
# use list & index as parameter:

lst=[1,2,34,67,89]
print(lst)
print(type(lst))
print(lst[0])

def getListElement(n, idx):
    if(len(n)==idx):
        return 
    print(lst[idx])
    getListElement(n, idx+1)

getListElement(lst,0)
    
