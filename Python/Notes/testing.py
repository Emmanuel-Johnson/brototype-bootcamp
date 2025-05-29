try:
    with open("my_file.txt", "x") as f:
        f.write("This is my File")
    print("File created successfully")
except FileExistsError:
    print("File already exists")

import os

file_path = "my_file.txt"

if os.path.exists(file_path):
    os.remove(file_path)
    print("File removed successfully")
else:
    print("File does not exist")