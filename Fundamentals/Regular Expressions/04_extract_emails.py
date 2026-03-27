import re

emails = input()

regex = r"\s([a-zA-Z0-9]+[\.\-\_]?[a-zA-Z0-9]+@[a-zA-Z0-9]+[\-]?[a-zA-Z0-9]+(\.[a-zA-Z]+)(\.[a-zA-Z]+)?)"
result = re.findall(regex, emails, re.IGNORECASE)
for item in result:
    print(item[0])