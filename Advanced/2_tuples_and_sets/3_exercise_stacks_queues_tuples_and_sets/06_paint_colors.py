from collections import deque

main_colors = ("red", "yellow", "blue")
secondary_colors = {"orange":("red", "yellow"),
                    "purple":("red", "blue"),
                    "green":("yellow", "blue")
                    }
colors = []

input_text = deque(input().split())
while input_text:
    first_text = input_text.popleft()
    last_text = input_text.pop() if input_text else ""
    for color in (first_text + last_text, last_text + first_text):
        if color in main_colors or color in secondary_colors:
            colors.append(color)
            break
    else:
        if len(first_text) > 1:
            input_text.insert(len(input_text) // 2, first_text[:-1])
        if len(last_text) > 1:
            input_text.insert(len(input_text) // 2, last_text[:-1])

valid_colors = []
for color in colors:
    if color in main_colors:
        valid_colors.append(color)
    elif color in secondary_colors:
        for c in secondary_colors[color]:
            if c not in colors:
                break
        else:
            valid_colors.append(color)

print(valid_colors)
