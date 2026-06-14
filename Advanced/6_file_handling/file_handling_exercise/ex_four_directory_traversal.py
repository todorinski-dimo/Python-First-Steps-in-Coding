import os
from _abs_path import abs_path
from _logs_input import write_to_log

exercise_path = abs_path

files = {}

for element in os.listdir(exercise_path):
    f = os.path.join(exercise_path, element)
    if os.path.isfile(f):
        extension = element.split(".")[-1]
        if extension not in files:
            files[extension] = []
        files[extension].append(element)
    else:
        for sub_el in os.listdir(f):
            filename = os.path.join(f, sub_el)
            if os.path.isfile(filename):
                extension = sub_el.split(".")[-1]
                if extension not in files:
                    files[extension] = []
                files[extension].append(sub_el)

with open(os.path.join(exercise_path, "ex_four_directory_traversal", "report.txt"), "w") as report:
    for key, value in sorted(files.items()):
        report.write(f"{key}\n")
        for val in sorted(value):
            report.write(f"- - - {val}\n")
    write_to_log(__file__, os.path.join(exercise_path, "ex_four_directory_traversal", "report.txt"), "OK. File Opened(Overwritten)")