# 4. Write a Python program to read a file line by line and store it into a
# variable.

def file_read(test):
    with open("../test.txt", "r") as myfile:
        data = myfile.readlines()
        print(data)

file_read('test.txt')
