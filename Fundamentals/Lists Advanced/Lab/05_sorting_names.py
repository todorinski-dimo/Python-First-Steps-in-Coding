names_list = input().split(", ")
names_list.sort()
names_list.sort(key=len, reverse=True)
print(names_list)
