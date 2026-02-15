courses = {}

while True:
    cmd = input().split(" : ")
    if cmd[0] == "end":
        break
    else:
        course_name = cmd[0]
        student_name = cmd[1]
        if course_name in courses:
            courses[course_name].append(student_name)
        else:
            courses[course_name] = [student_name]

for course in courses:
    print(f"{course}: {len(courses[course])}")
    for name in courses[course]:
        print(f"-- {name}")
