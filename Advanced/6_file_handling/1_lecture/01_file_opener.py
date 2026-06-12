import os
from constant import path_to_dir

path = os.path.join(path_to_dir, "files", "text.txt")
try:
    file = open(path)
    file.close()
    print("File found")
except FileNotFoundError:
    print("File not found")