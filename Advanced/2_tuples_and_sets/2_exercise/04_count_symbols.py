string = input()
# dictionary = {}
#
# for el in string:
#     if el not in dictionary.keys():
#         dictionary[el] = 0
#     dictionary[el] += 1
#
# for key in sorted(dictionary):
#     print(f"{key}: {dictionary[key]} time/s")

symbols = set()
for ch in string:
    symbols.add(ch)

for ch in sorted(symbols):
    print(f"{ch}: {string.count(ch)} time/s")