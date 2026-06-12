import os
from constant import path_to_dir

path = os.path.join(path_to_dir, "files", "numbers.txt")
file = open(path)
print(file.read())
file.seek(0)
contents = list(file.read().split())
print(contents)
contents = [int(item) for item in contents if item.isnumeric()]
print(sum(contents))
file.close()