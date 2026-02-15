output = {}

while True:
    resource = input()
    if resource == "stop":
        break
    quantity = int(input())
    if resource in output:
        output[resource] += quantity
    else:
        output[resource] = quantity

for resource, quantity in output.items():
    print(f"{resource} -> {quantity}")
