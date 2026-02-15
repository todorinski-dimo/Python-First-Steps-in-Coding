input_stock = input().split()
stock = {}

for idx in range(0, len(input_stock), 2):
    key = input_stock[idx]
    value = int(input_stock[idx + 1])
    stock[key] = value

check_items = input().split()

for item in check_items:
    if item in stock:
        print(f"We have {stock[item]} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")
