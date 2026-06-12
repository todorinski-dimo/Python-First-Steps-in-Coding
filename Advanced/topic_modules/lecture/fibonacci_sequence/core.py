from Advanced.topic_modules.lecture.fibonacci_sequence.main import create_fibonacci_sequence, find_n

sequence = []

while True:
    command = input().split()
    if command[0] == "Create":
        sequence = create_fibonacci_sequence(int(command[2]))
        print(*sequence)
    elif command[0] == "Locate":
        print(find_n(int(command[1]), sequence))
    elif command[0] == "Stop":
        break