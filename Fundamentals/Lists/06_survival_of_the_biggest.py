list_of_ints = input().split()
list_of_ints = [int(item) for item in list_of_ints]

ints_to_remove = int(input())

removed_list = []
working_list = list_of_ints.copy()
working_list.sort(reverse=True)

for _ in range(0, ints_to_remove):
    removed_list.append(working_list.pop())

for item in removed_list:
    list_of_ints.remove(item)

final_result = ", ".join(map(str, list_of_ints))
print(final_result)




