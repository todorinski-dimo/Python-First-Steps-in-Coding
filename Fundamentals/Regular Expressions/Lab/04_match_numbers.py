import re
string = input()
regex = r"((^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s)))"
matches = re.findall(regex, string)
for item in matches:
    print(item[0], end=" ")