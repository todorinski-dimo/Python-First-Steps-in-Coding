data = input().split()

stock = {}

for item in range(0, len(data), 2):
    key = data[item]
    value = int(data[item + 1])
    stock[key] = value

print(stock)