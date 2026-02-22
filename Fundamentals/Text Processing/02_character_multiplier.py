input_list = input().split()
result = 0

for idx in range(min(len(input_list[0]), len(input_list[1]))):
    result += ord(input_list[0][idx]) * ord(input_list[1][idx])

# print(idx)
# print(result)

if len(input_list[0]) > idx + 1:
    for idx_ in range (idx + 1, len(input_list[0])):
        result += ord(input_list[0][idx_])
else:
    for idx_ in range (idx + 1, len(input_list[1])):
        result += ord(input_list[1][idx_])

# print(idx_)
print(result)