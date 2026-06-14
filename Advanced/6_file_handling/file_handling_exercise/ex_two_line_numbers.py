import os.path
from _abs_path import abs_path
from _logs_input import write_to_log
from string import punctuation

exercise_path = os.path.join(abs_path, "ex_two_line_numbers")

try:
    with open(os.path.join(exercise_path, "text.txt"), "r") as file:
        try:
            with open(os.path.join(exercise_path, "output.txt"), "w") as output:
                lines = file.readlines()
                for line in range(len(lines)):
                    lines[line] = lines[line].replace("\n", "")
                    letters = len([ch for ch in lines[line] if ch.isalpha()])
                    punctuations = len([ch for ch in lines[line] if ch in punctuation])
                    output.write(f"Line {line + 1}: {lines[line]} ({letters})({punctuations})\n")
            write_to_log(__file__, os.path.join(exercise_path, "output.txt"), "OK. Write")
        except FileNotFoundError:
            write_to_log(__file__, os.path.join(exercise_path, "output.txt"), "File not found")
    write_to_log(__file__, os.path.join(exercise_path, "text.txt"), "OK. ReadFile")
except FileNotFoundError:
    write_to_log(__file__, os.path.join(exercise_path, "text.txt"), "FileNotFoundError")