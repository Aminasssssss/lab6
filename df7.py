#Write a Python program to copy the contents of a file to another file

first_file= input()
second_file=input()

with open(first_file, "r") as source:
    r=source.read()

with open(second_file, "w") as destination:
    destination.write(r)