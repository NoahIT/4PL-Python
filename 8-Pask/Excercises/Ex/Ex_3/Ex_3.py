# 3. Write a Python program to read a file line by line and store it into a list.

def file_read(test):
    with open("../test.txt", "r") as f:
        content_list = f.readlines()
        print(content_list)

file_read('test.txt')
