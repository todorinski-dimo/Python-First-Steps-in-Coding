nums_tuple = tuple([float(item) for item in input().split()])

data = {}

for el in nums_tuple:
    if el not in data:
        data[el] = nums_tuple.count(el)

for key, value in data.items():
    print(f"{key:.1f} - {value} times")