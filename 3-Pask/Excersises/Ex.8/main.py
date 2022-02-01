# 8. Write a Python program to check whether a specified value is contained in
# a group of values.
# Test Data :
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False

group = [1, 5, 8, 3]
print(group)

num = int(input("Enter your number: "))
if num in group:
    print("True")
else:
    print("False")
