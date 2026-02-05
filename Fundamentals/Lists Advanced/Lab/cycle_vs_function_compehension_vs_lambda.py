"""
[bc] cycle in main body - can not be used as attribute in other functions, function needs to be implemented in the cycle
[fc] cycle as function - can be used as attribute in other functions
[co] comprehension  - can not be used as attribute in other functions, function needs to be implemented in the cycle
[lf] lambda function - can be used as attribute in other functions
"""

# ###input transformation
# happiness_score = input().split()
# happiness_score = [int(item) for item in happiness_score]
# =
# happiness_score = [int(item) for item in input().split()]
# =
# happiness_score = list(map(int, input().split()))
#
# ###multiply each item
# score_factored = [item * 3 for item in happiness_score]
# =
# score_factored = list(map(lambda item: item * 3, happiness_score))
#
# ###filter each item
# happy_employees = [item for item in happiness_score if item >= (sum(factored_score)/len(factored_score))]
# =
# happy_employees = list(filter(lambda item: item >= (sum(factored_score)/len(factored_score)), factored_score))

# ### comparison between diff list
# for index_a in range(len(seq_a)):
#     for index_b in range(len(seq_b)):
#         if seq_a[index_a] in seq_b[index_b]:
#             seq_result.append(seq_a[index_a])
#
# for result in seq_result:
#     if result not in seq_unique_results:
#         seq_unique_results.append(result)
# =
# seq_unique_result = [item_a for item_a in seq_a if any((item_a in item_b) for item_b in seq_b)]

# numbers = [1, 2, 3, 4, 5, 6]
# squares = [item ** 2 for item in numbers]
# print(squares)
# squares_odd = [item ** 2 for item in numbers if item % 2 == 1]
# print(squares_odd)
# squares_even_and_others = [item ** 2 if item % 2 == 0 else item ** 0.5 for item in numbers]
# print(squares_even_and_others)
#
# numbers.append([3, 4, 5])
# print(numbers)
# numbers.extend([3, 4, 5])
# print(numbers)
# numbers += [3, 4, 5]
# print(numbers)
# numbers.pop(6)
# # numbers_new = [int(item) for item in input().split()]
# even_indices = [idx for idx in range(len(numbers)) if numbers[idx] % 2 == 0]
# print(even_indices)

numbers = [1, 2, 3, 4, 5, 6]
numbers1 = numbers[0:]
print(numbers1)

numbers2 = numbers[:0]
print(numbers2)

numbers3 = numbers[8:]
print(numbers3)

numbers4 = numbers[:8]
print(numbers4)

numbers5 = numbers[1:]
print(numbers5)

numbers6 = numbers[:1]
print(numbers6)

numbers7 = numbers[5:]
print(numbers7)

numbers8 = numbers[:5]
print(numbers8)