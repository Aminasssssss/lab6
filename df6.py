#Write a Python program to generate 26 text files 
# named A.txt, B.txt, and so on up to Z.txt

for i in range(65,91):
    letter= chr(i)
    name=letter+".txt"

    with open(name, "w") as file:
        file.write("")

    print(name)