memory_list = [item for item in input().split()]
moves = 0

while True:
    cmd = input()
    if cmd == "end":
        print(f"Sorry you lose :(\n{' '.join(memory_list)}")
        break
    index_list = [int(item) for item in cmd.split()]
    moves += 1
    if index_list[0] < 0 or index_list[1] < 0 or index_list[0] >= len(memory_list) or index_list[1] >= len(memory_list) \
            or index_list[0] == index_list[1]:
        print("Invalid input! Adding additional elements to the board")
        memory_list.insert(int(len(memory_list) / 2), f"-{moves}a")
        memory_list.insert(int(len(memory_list) / 2), f"-{moves}a")
    elif memory_list[index_list[0]] == memory_list[index_list[1]]:
        print(f"Congrats! You have found matching elements - {memory_list[index_list[0]]}!")
        if index_list[0] < index_list[1]:
            memory_list.pop(index_list[1])
            memory_list.pop(index_list[0])
        else:
            memory_list.pop(index_list[0])
            memory_list.pop(index_list[1])
    elif memory_list[index_list[0]] != memory_list[index_list[1]]:
        print("Try again!")
    if len(memory_list) == 0:
        print(f"You have won in {moves} turns!")
        break


