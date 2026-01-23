sequence_list = input().split()
sequence_list = [int(item) for item in sequence_list]

iterations = int(len(sequence_list)/2)
time_left = 0
time_right = 0
position = 0

while position < iterations:
    if sequence_list[position] == 0:
        time_left *= 0.8
    else:
        time_left += sequence_list[position]
    if sequence_list[-1*(position + 1)] == 0:
        time_right *= 0.8
    else:
        time_right += sequence_list[-1*(position + 1)]
    position += 1

if time_left < time_right:
    print(f"The winner is left with total time: {time_left:.1f}")
elif time_right < time_left:
    print(f"The winner is right with total time: {time_right:.1f}")
