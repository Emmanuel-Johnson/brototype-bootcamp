""" import os

with open("my_file.txt", "w") as f:
    f.write("New file Created Successfully, and this is the file.")

if os.path.exists("my_file.txt"):
    os.remove("my_file.txt")
    print("File Removed Successfully")
else:
    print("File not exists") """

limit = 5
print(limit)
for i in range(limit):
    print(i)
