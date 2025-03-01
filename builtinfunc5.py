#Write a Python program with builtin function
# that returns True if all elements of the tuple are true.

n=tuple(map(int, input().split()))
r=all(n)
print(r)