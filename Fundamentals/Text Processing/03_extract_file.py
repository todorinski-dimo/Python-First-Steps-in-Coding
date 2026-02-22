path = input()
file = ""

for ch in range(len(path) - 1, -1, -1):
    if path[ch] != "\\":
        file += path[ch]
    else:
        break

file = file[::-1]
file = file.split(".")
print("File name:", file[0])
print("File extension:", file[1])
