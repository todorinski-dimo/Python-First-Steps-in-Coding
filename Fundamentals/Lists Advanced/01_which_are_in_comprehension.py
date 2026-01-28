seq_a = input().split(", ")
seq_b = input().split(", ")

seq_unique_results = [item_a for item_a in seq_a if any((item_a in item_b) for item_b in seq_b)]

print(seq_unique_results)