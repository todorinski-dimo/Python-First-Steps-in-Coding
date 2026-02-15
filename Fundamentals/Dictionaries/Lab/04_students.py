students_dict = {}

while True:
    init_input = input().split(":")
    if len(init_input) == 1:
        course_list = init_input[0].split("_")
        course_list_str = f"{course_list[0]}"
        for idx in range(1, len(course_list)):
            course_list_str += f" {course_list[idx]}"
        for k, v in students_dict.items():
            for sub_k, sub_v in v.items():
                if course_list_str == sub_v:
                    print(f"{students_dict[k]['name']} - {k}")
        break
    else:
        key = int(init_input[1])
        value = {"name":init_input[0], "course":init_input[2]}
        students_dict[key] = value
