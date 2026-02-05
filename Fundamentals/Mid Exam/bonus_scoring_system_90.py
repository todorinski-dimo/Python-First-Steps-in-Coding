# https://alpha.judge.softuni.org/contests/05-programming-fundamentals-mid-exam/2028/practice#1
# score 90

number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())

attendance = []
bonuses = []

for _ in range(number_of_students):
    attendance.append(int(input()))
bonuses = [(item / number_of_lectures * (5 + additional_bonus)) for item in attendance]

max_bonus_points = max(bonuses)
index = bonuses.index(max_bonus_points)
max_att = attendance[index]

print(f"Max Bonus: {max_bonus_points:.0f}.")
print(f"The student has attended {max_att:.0f} lectures.")
