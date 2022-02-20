# 10. Write a Python program to write a list content to a file.

color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
with open('Ex_10.txt', "w") as myfile:
        for c in color:
                myfile.write("%s\n" % c)

content = open('Ex_10.txt')
print(content.read())