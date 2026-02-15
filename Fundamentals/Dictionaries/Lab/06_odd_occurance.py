init_input = input().split()
init_input = [item.lower() for item in init_input]
output = {}
for item in init_input:
    if item in output:
        output[item] += 1
    else:
        output[item] = 1

for key, value in output.items():
    if value % 2 == 1:
        print(f"{key}", end=" ")
