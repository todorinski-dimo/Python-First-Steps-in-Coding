from collections import deque

FOR_GOAL = 100
STR_DEC = -10

strength = list(map(int, input().split()))
accuracy = deque(list(map(int, input().split())))
goals = 0

while strength and accuracy:
    if strength[-1] + accuracy[0] == FOR_GOAL:
        goals += 1
        strength.pop()
        accuracy.popleft()
    elif strength[-1] + accuracy[0] < FOR_GOAL:
        if strength[-1] == accuracy[0]:
            str_pop = strength.pop()
            acc_pop = accuracy.popleft()
            strength.append(str_pop + acc_pop)
        elif strength[-1] > accuracy[0]:
            accuracy.popleft()
        elif strength[-1] < accuracy[0]:
            strength.pop()
    elif strength[-1] + accuracy[0] > FOR_GOAL:
        strength[-1] += STR_DEC
        accuracy.rotate(-1)

if goals > 3:
    print("Paul performed remarkably well!")
elif goals == 3:
    print("Paul scored a hat-trick!")
elif 0 < goals < 3:
    print("Paul failed to make a hat-trick.")
elif goals == 0:
    print("Paul failed to score a single goal.")
if goals > 0:
    print(f"Goals scored: {goals}")
if strength:
    print(f"Strength values left: {', '.join(map(str, strength))}")
if accuracy:
    print(f"Accuracy values left: {', '.join(map(str, accuracy))}")




