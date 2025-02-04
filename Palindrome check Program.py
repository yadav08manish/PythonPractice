# Q2. WAP to check if a list contains a palindrome of elements

pali=[1,2,3,2,1]
print(pali)

copyPal= pali.copy()
print(copyPal)

# revcopyPal=copyPal.reverse()
copyPal.reverse()
if(pali==copyPal):
    print("List is Palindrome")
else:
    print("Not a palindrome")



# cntPali=len(pali)
# print("count of list pali:- ", cntPali)

# cntcopyPal=len(copyPal)
# print("count of list copyPal:- ", cntcopyPal)

# if(cntPali=cntcopyPal)

