# https://alpha.judge.softuni.org/contests/01-programming-fundamentals-mid-exam-retake/2517/practice#2
# score 100

waiting_people = int(input())
lift_status = [int(item) for item in input().split()]

max_people_in_wagon = 4
wagon_capacity = 0

for wagon in range(len(lift_status)):
    if lift_status[wagon] >= 4:
        continue
    elif lift_status[wagon] < 4 and waiting_people > 0:
        wagon_capacity = max_people_in_wagon - lift_status[wagon]
        if wagon_capacity < waiting_people:
            lift_status[wagon] += wagon_capacity
            waiting_people -= wagon_capacity
        else:
            lift_status[wagon] += waiting_people
            waiting_people -= waiting_people
            break
    # print(lift_status)
    # print(waiting_people)
# lift_status = [str(wagon) for wagon in lift_status]
if waiting_people <= 0 and sum(lift_status) < len(lift_status) * max_people_in_wagon:
    print("The lift has empty spots!")
    lift_status = [str(wagon) for wagon in lift_status]
    print(" ".join(lift_status))
elif waiting_people > 0 and sum(lift_status) == len(lift_status) * max_people_in_wagon:
    print(f"There isn't enough space! {waiting_people} people in a queue!")
    lift_status = [str(wagon) for wagon in lift_status]
    print(" ".join(lift_status))
elif waiting_people <= 0 and sum(lift_status) == len(lift_status) * max_people_in_wagon:
    lift_status = [str(wagon) for wagon in lift_status]
    print(" ".join(lift_status))
