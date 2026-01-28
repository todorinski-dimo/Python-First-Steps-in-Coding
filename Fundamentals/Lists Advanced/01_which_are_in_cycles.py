seq_a = input().split(", ")
seq_b = input().split(", ")
seq_result = []
seq_unique_results = []

for index_a in range(len(seq_a)):
    for index_b in range(len(seq_b)):
        if seq_a[index_a] in seq_b[index_b]:
            seq_result.append(seq_a[index_a])

for result in seq_result:
    if result not in seq_unique_results:
        seq_unique_results.append(result)

print(seq_unique_results)
