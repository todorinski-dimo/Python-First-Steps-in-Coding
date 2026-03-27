import re

buff = []
text = input()
regex = r"(w{3}\.[0-9a-z-]+(\.[a-z]+)+)"

while text:
    check = re.search(regex, text, re.IGNORECASE)
    if check:
        buff.append(check.group(1))
    text = input()

for item in buff:
    print(item)