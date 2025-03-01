#Write a Python program to write a list to a file.

file = input()
l=["Amina", "Zhumatayeva", "Ganikyzy"]

f=open(file, "w")
for i in l:
    f.write(i+"\n")

f.close()