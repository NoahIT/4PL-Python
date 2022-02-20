# 11. Write a Python program to copy the contents of a file to another file.

with open('test.txt', 'r') as firstfile, open('test2.txt', 'a') as secondfile:

    for line in firstfile:

        secondfile.write(line)

print(secondfile)