#Write a Python program to count the number of lines in a text file.

file=input()

f=open(file , "r")
r=f.readlines()
print(len(r))
f.close()
    