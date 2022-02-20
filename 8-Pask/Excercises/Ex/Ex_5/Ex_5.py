# 5. Write a Python program to read a file line by line and store each word into
# an array.

with open("../test.txt", "r") as f:
    for line in f:
        for word in line.split():
            content_arr = word
            print(content_arr)
