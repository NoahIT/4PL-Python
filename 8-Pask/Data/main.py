import os

# f = open("data.txt", "r")
# print(f.read())
# print(f.readline())
# print(f.readline())

# text = []
# for line in f:
#     print(line)
#     text.append(line)
#
# f.close()
# print(text)

# f = open("data2.txt", "a")
#
# for x in range(100):
#     f.write(f"[{x}] - This line is added from code")
#
# f.close()

# if os.path.exists("data2.txt"):
#     print("File exists")
#     os.remove("data2.txt")
# else:
#     print("File not found")

with open("data.txt") as file:
    print(file.read())
