import os
from _abs_path import abs_path
from _logs_input import write_to_log

exercise_path = abs_path

files = {}

def get_dir_elements(dir_path, level):
    if level == -1:
        return
    for element in os.listdir(dir_path):
        f = os.path.join(dir_path, element)
        if os.path.isfile(f):
            extension = os.path.splitext(f)[1]
            if extension not in files:
                files[extension] = []
            files[extension].append(element)
        else:
            get_dir_elements(f, level - 1)

get_dir_elements(exercise_path, 1)

with open(os.path.join(exercise_path, "ex_four_directory_traversal", "report.txt"), "w") as report:
    for key, value in sorted(files.items()):
        report.write(f".{key}\n")
        for val in sorted(value):
            report.write(f"- - - {val}\n")
    write_to_log(__file__, os.path.join(exercise_path, "ex_four_directory_traversal", "report.txt"), "OK. File Opened(Overwritten)")