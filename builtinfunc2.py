#Write a Python program with builtin function that accepts
#a string and calculate the number of upper case letters and lower case letters

n=input()
upperc=sum(c.isupper() for c in n)
lowerc=sum(c.islower() for c in n)

print(upperc)
print(lowerc)