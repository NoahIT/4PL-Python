# 9. Write a Python program to get the file size of a plain file.
import os

def file_size(fname):
    statinfo = os.stat(fname)
    return statinfo.st_size

print("File size in bytes of a plain file: ", file_size("plain.txt"))
print("File size in bytes of a not plain file: ", file_size(f"./Excercises/test.txt"))
