import re
output = []
string = input()
regex = r"(\d+)"
while string:
    matches = re.findall(regex, string)
    output += matches
    string = input()

for item in output:
    print(item, end=" ")