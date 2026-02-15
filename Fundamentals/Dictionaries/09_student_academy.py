students = {}
cycles = int(input())

for _ in range(cycles):
    name = input()
    grade = float(input())
    if name not in students:
        students[name] = []
    students[name].append(grade)

for name, grades in students.items():
    average_score = sum(students[name]) / len(students[name])
    if average_score >= 4.5:
        print(f"{name} -> {average_score:.2f}")
