stack = []
no_commands = int(input())

for _ in range(no_commands):
    command = input().split()
    if command[0] == "1":
        stack.append(command[1])
    elif command[0] == "2" and len(stack) > 0:
        stack.pop()
    elif command[0] == "3" and len(stack) > 0:
        max = int(stack[0])
        for i in range(len(stack)):
            if max < int(stack[i]):
                max = int(stack[i])
        print(max)
    elif command[0] == "4" and len(stack) > 0:
        min = int(stack[0])
        for i in range(len(stack)):
            if min > int(stack[i]):
                min = int(stack[i])
        print(min)

if len(stack) > 1:
    for _ in range(len(stack)-1):
        print(f"{stack.pop()}, ", end="")
print(stack.pop(), end="")
