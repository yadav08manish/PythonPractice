# Open(name of file, mode)
# modes are read, Write and Close
# bydefault it takes read mode if we dont pass any mode parameter 

# 'r' --> open for reading(default)
# 'w' --> open for writing, truncating thr file first
# 'x' ==> Create a new file and open it for writing
# 'a' ==> open for writitng , appending to the end of the file if it exists
# 'b' ==> binary mode
# 't' ==> text mode (default)
# '+' ==> open a disk file for updating (reading or writing)


# f= open("C:\\Python Practice\\Manish\\test.txt",'r')
# data=f.read()
# print(data)
# print(type(f))
# f.close()

#readLine

f=open("C:\\Python Practice\\Manish\\test.txt",'r')
line1= f.readline()
print(line1)

line2= f.readline()
print(line2)