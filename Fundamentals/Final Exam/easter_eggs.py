import re
regex = r"(@|#)([a-z]{3,})(@|#)[^a-zA-Z0-9]*\/(\d+)\/"

input_string = input()
check = re.findall(regex, input_string)
for item in check:
    print(f"You found {item[3]} {item[1]} eggs!")