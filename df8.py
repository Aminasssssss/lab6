#Write a Python program to delete file by specified path.
# Before deleting check for access and whether a given path exists or not.

import os

file_path = input()

if os.path.exists(file_path):
    if os.access(file_path, os.R_OK):
        print("reading")
    if os.access(file_path, os.W_OK):
        print("writing")
    if os.access(file_path, os.X_OK):
        print("doing")

    confirm = input("Delete it? (type 'yes' or 'да'): ").lower()

    if confirm == "yes" or confirm == "да":
        os.remove(file_path)
        print("deleted")

else:
    print("file does not exist")
