import re
from math import floor
regex = r"(#|\|)([a-zA-Z\s]+)\1(\d{2}/\d{2}/\d{2})\1(\d+)\1"

ttl_calories = 0
food_to_last = 0
input_string = input()

food = re.findall(regex, input_string)
for item in food:
    ttl_calories += int(item[3])
food_to_last = floor(ttl_calories / 2000)
print(f"You have food to last you for: {food_to_last} days!")
for item in food:
    print(f"Item: {item[1]}, Best before: {item[2]}, Nutrition: {item[3]}")