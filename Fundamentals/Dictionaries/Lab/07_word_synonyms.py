count = int(input())
dictionary = {}
for _ in range(count):
    word = input()
    synonym = input()
    if word in dictionary:
        dictionary[word].append(synonym)
    else:
        dictionary[word] = [synonym]

for word in dictionary:
    print(f"{word} - {', '.join(dictionary[word])}")
