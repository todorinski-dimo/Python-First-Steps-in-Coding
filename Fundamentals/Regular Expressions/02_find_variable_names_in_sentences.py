import re

string = input()
regex = r"\b_([a-zA-Z0-9]+)\b"
matches = re.findall(regex, string)
print(",".join(matches))