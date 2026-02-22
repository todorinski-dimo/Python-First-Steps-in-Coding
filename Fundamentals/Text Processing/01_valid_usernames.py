input_list = input().split(", ")
output_list = []


for item in input_list:
    ok_word = True
    if 3 <= len(item) <= 16:
        for ch in item:
            if not (ch.isalnum() or ch == "-" or ch == "_"):
                ok_word = False
        if ok_word:
            output_list.append(item)

for item in output_list:
    print(item)
