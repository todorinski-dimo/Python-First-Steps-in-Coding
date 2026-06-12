import os
from constant import path_to_dir

path = os.path.join(path_to_dir, "files", "my_first_file.txt")
# file = open(path, "w")
# file.write("I just created my first file!")
# file.close()

with open(path, "w") as file:
    file.write("I just created my first file!")