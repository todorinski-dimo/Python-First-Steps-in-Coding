seq_a = input().split(", ")
seq_b = input().split(", ")
seq_result = []
seq_unique_results = []

for item_a in range(len(seq_a)):
    for item_b in range(len(seq_b)):
        if seq_a[item_a] in seq_b[item_b]:
            seq_result.append(seq_a[item_a])

for result in seq_result:
    if result not in seq_unique_results:
        seq_unique_results.append(result)

print(seq_unique_results)
