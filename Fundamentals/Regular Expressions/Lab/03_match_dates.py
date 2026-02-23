import re
dates = input()
regex = r"\b(?P<day>\d{2})([/.-])(?P<month>[A-Z][a-z]{2})\2(?P<year>\d{4})\b"
matches = re.findall(regex, dates)
for item in matches:
    print(f"Day: {item[0]}, Month: {item[2]}, Year: {item[3]}")
