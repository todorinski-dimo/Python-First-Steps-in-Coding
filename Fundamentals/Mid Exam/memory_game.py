# https://alpha.judge.softuni.org/contests/01-programming-fundamentals-mid-exam-retake/2517/practice#3
# score 100

seq_elements = input().split()
seq_elements_len = len(seq_elements)
moves = 0


while True:
    cmd = input().split()
    if cmd[0] == "end":
        print("Sorry you lose :(")
        print(" ".join(seq_elements))
        break
    else:
        cmd = [int(item) for item in cmd]
        moves += 1
        if cmd[0] < 0 or cmd[1] < 0 or cmd[0] == cmd[1] or cmd[0] >= len(seq_elements) or cmd[1] >= len(seq_elements):
            print("Invalid input! Adding additional elements to the board")
            seq_elements.insert(int(len(seq_elements) / 2), f"-{moves}a")
            seq_elements.insert(int(len(seq_elements) / 2), f"-{moves}a")
            seq_elements_len += 2
        elif seq_elements[cmd[0]] == seq_elements[cmd[1]]:
            print(f"Congrats! You have found matching elements - {seq_elements[cmd[0]]}!")
            if cmd[0] > cmd[1]:
                seq_elements.pop(cmd[0])
                seq_elements.pop(cmd[1])
            else:
                seq_elements.pop(cmd[1])
                seq_elements.pop(cmd[0])
            seq_elements_len -= 2
        elif seq_elements[cmd[0]] != seq_elements[cmd[1]]:
            print("Try again!")
        # print(seq_elements)
        if seq_elements_len == 0:
            print(f"You have won in {moves} turns!")
            break

