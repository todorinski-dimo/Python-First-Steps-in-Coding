version = input().split(".")
version = "".join(version)
version = int(version)
version += 1
version = str(version)
version = list(version)
version.insert(1, ".")
version.insert(3, ".")
print("".join(version))
