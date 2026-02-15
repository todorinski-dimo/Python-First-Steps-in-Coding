max_capacity = 4
current_capacity = 0
total_capacity = 0

waiting_people = int(input())
lift_state = [int(item) for item in input().split()]

for item in range(len(lift_state)):
    current_capacity = max_capacity - lift_state[item]
    if current_capacity <= waiting_people:
        waiting_people -= current_capacity
        lift_state[item] += current_capacity
    else:
        lift_state[item] += waiting_people
        waiting_people = 0

total_capacity = len(lift_state) * max_capacity
total_people_in_lift = sum(lift_state)
lift_state = [str(item) for item in lift_state]

if waiting_people > 0:
    print(f"There isn't enough space! {waiting_people} people in a queue!")
elif waiting_people == 0 and total_capacity > total_people_in_lift:
    print("The lift has empty spots!")

print(" ".join(lift_state))