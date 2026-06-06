stu = int(input())
students = {}
for _ in range(stu):
    name, score = tuple(input().split())
    if name not in students:
        students[name] = []
    students[name].append(float(score))

for name, score in students.items():
    print(f"{name} -> {' '.join([f'{el:.2f}' for el in score])} (avg: {sum(score)/len(score):.2f})")
