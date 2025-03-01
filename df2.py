#Write a Python program to check for access to a specified path. 
# Test the existence, readability, writability and executability of the specified path

import os

n=input()
if os.path.exists(n):
    print(os.access(n, os.R_OK))
    print(os.access(n, os.W_OK))
    print(os.access(n, os.X_OK))