# 2. Write a Python program to append text to a file and display the text.

f = open("test.txt", "a")

for x in range(10):
    f.write(f"[{x}] - This line is added from code")

f.close()
