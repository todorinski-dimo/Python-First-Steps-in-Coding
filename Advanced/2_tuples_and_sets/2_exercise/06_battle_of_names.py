odd_set = set()
even_set = set()

for i in range(int(input())):
    # name = input()
    # name_value = 0
    # for ch in name:
    #     name_value += ord(ch)
    # name_value //= i + 1

    name_value = sum(ord(ch) for ch in input()) // (i + 1)

    if name_value % 2 != 0:
        odd_set.add(name_value)
    else:
        even_set.add(name_value)

if sum(odd_set) == sum(even_set):
    # union_set = list(odd_set.union(even_set))
    # print(", ".join([str(item) for item in union_set]))
    print(*odd_set.union(even_set), sep=", ")
elif sum(odd_set) > sum(even_set):
    # diff_set = list(odd_set.difference(even_set))
    # print(", ".join([str(item) for item in diff_set]))
    print(*odd_set.difference(even_set), sep=", ")
else:
    # symmetric_set = list(even_set.symmetric_difference(odd_set))
    # print(", ".join([str(item) for item in symmetric_set]))
    print(*odd_set.symmetric_difference(even_set), sep=", ")