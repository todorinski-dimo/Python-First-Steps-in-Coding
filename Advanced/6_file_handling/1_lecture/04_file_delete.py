import os
from constant import path_to_dir

path = os.path.join(path_to_dir, "files", "file_for_delete.txt")
with open(path, "w+") as file:
    file.write("I just created a file for deletion.")
    file.seek(0)
    print(file.read())

try:
    os.remove(path)
    print(f"{path} was deleted.")
except FileNotFoundError:
    print(f"{path} was not found.")
