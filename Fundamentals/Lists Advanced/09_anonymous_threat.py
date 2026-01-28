def merge(words: list, act: list) -> list:
    start_index, end_index = int(act[1]), int(act[2])
    if start_index not in range(len(words)):
        start_index = 0
    if end_index not in range(len(words)):
        end_index = len(words) - 1
    words[start_index] = "".join(words[start_index:end_index + 1])
    words = words[:start_index + 1] + words[end_index + 1:]
    return words


def divide(words: list, act: list) -> list:
    index, partitions = int(act[1]), int(act[2])
    word = words[index]
    partition_size = len(word) // partitions
    partitioned = []
    partition_numb = 0
    for idx in range(0, len(word), partition_size):
        partition_numb += 1
        if partition_numb == partitions:
            partitioned.append(word[idx:])
            break
        else:
            partitioned.append(word[idx:idx + partition_size])
    words = words[:index] + partitioned + words[index + 1:]
    return words


seq_words = input().split()

while True:
    cmd = input()
    if cmd == "3:1":
        break
    cmd = cmd.split()
    action = cmd[0]
    if action == "merge":
        seq_words = merge(seq_words, cmd)
    elif action == "divide":
        seq_words = divide(seq_words, cmd)

print(" ".join(seq_words))
