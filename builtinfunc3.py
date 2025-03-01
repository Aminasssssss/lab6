#Write a Python program with builtin function that checks 
#whether a passed string is palindrome or not

n=input()
r=""

for i in reversed(n):
    r+=i

if n==r:
    print("it is palindrome")

else:
    print("it is not palindrome")