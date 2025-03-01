#Write a Python program to test whether a given path exists or not. 
#If the path exist find the filename and directory portion of the given path.

import os

n=input()

if os.path.exists(n):
    print(os.path.basename(n))
    print(os.path.dirname(n))

else:
    print("no")