input_words = input().split()
output_words = [item for item in input_words if len(item) % 2 == 0]
print("\n".join(output_words))
