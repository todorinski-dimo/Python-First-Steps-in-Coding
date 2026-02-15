from math import ceil

rec_1 = int(input())
rec_2 = int(input())
rec_3 = int(input())

students_per_hour = rec_3 + rec_2 + rec_1
total_students = int(input())


working_time =  ceil(total_students / students_per_hour)
rest_hours = working_time // 3
if working_time <= 3:
    rest_hours = 0
elif working_time % 3 == 0:
    rest_hours = (working_time // 3) - 1
else:
    rest_hours = working_time // 3


print(f"Time needed: {working_time + rest_hours}h.")