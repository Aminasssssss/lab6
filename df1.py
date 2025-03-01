#Write a Python program to list only directories,
# files and all directories, files in a specified path.

import os 
n=input()

if os.n.exists(n):
    items=os.listdir(n)

    for i in items:
        r=os.n.join(n,i)
        if os.n.isdir(r):
            print(i)

    for i in items:
        r=os.n.join(n,i)
        if os.n.isfile(r):
            print(i)

    for i in items:
        print (i)  

