factor = int(input())
count_iterations = int(input())

new_list = [factor]

for item in range(0, count_iterations - 1):
    buff = new_list[item]
    new_list.append(buff + factor)

print(new_list)
