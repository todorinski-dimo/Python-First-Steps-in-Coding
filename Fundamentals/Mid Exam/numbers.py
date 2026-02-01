sequence = [int(item) for item in input().split()]
average_value = sum(sequence) / len(sequence)
new_sequence = list(filter(lambda item: item > average_value, sequence))
new_sequence = sorted(new_sequence, reverse=True)
if len(new_sequence) > 5:
    new_sequence = new_sequence[:5]

if len(new_sequence) == 0:
    print("No")
else:
    new_sequence = [str(item) for item in new_sequence]
    print(" ".join(new_sequence))
