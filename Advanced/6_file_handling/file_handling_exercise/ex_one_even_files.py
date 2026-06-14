import os.path
from _abs_path import abs_path
from _logs_input import write_to_log

exercise_path = os.path.join(abs_path, "ex_one_even_files")
chars = ["-", ",", ".", "!", "?"]

try:
    with open(os.path.join(exercise_path,"text.txt")) as file:
        text = file.readlines()
    write_to_log(f"{__file__}", f"{os.path.join(exercise_path, 'text.txt')}", "OK: ReadLines")
except FileNotFoundError:
    write_to_log(f"{__file__}", f"{os.path.join(exercise_path, 'text.txt')}", "Error: FileNotFoundError")

text = [text[line] for line in range(len(text)) if line % 2 != 1]
text = ["".join("@" if char in chars else char for char in line) for line in text]

try:
    with open(os.path.join(exercise_path, "output.txt"), "w") as output:
        for line in text:
            print(" ".join(reversed(line.split())))
            output.write(line)
    write_to_log(f"{__file__}", f"{os.path.join(exercise_path, 'output.txt')}", "OK: Write")
except FileNotFoundError:
    write_to_log(f"{__file__}", f"{os.path.join(exercise_path, 'output.txt')}", "Error: FileNotFoundError")
