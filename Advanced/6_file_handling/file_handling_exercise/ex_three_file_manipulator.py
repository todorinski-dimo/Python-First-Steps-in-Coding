import os
from _abs_path import abs_path
from _logs_input import write_to_log

exercise_path = os.path.join(abs_path, "ex_three_file_manipulator")

while True:
    command = input().split("-")
    if command[0] == "Create":
        file = open(os.path.join(exercise_path, f"{command[1]}"), "w")
        write_to_log(__file__, os.path.join(exercise_path, f"{command[1]}"), "OK. File Opened(empty/ed)")
        file.close()
        write_to_log(__file__, os.path.join(exercise_path, f"{command[1]}"), "OK. File closed")
    elif command[0] == "Add":
        file = open(os.path.join(exercise_path, f"{command[1]}"), "a")
        write_to_log(__file__, os.path.join(exercise_path, f"{command[1]}"), "OK. File Opened(append)")
        file.write(f"{command[2]}\n")
        write_to_log(__file__, os.path.join(exercise_path, f"{command[1]}"), "OK. Text appended")
        file.close()
        write_to_log(__file__, os.path.join(exercise_path, f"{command[1]}"), "OK. File closed")
    elif command[0] == "Replace":
        if os.path.exists(os.path.join(exercise_path, f"{command[1]}")):
            with open(os.path.join(exercise_path, f"{command[1]}"), "r") as file:
                text = file.read()
                new_text = text.replace(command[2], command[3])
                write_to_log(__file__, os.path.join(exercise_path, f"{command[1]}"), "OK. File Opened(read)")
            with open(os.path.join(exercise_path, f"{command[1]}"), "w") as file:
                file.write(new_text)
                write_to_log(__file__, os.path.join(exercise_path, f"{command[1]}"), "OK. File Opened(Overwritten)")
        else:
            print("An error occurred")
            write_to_log(__file__, os.path.join(exercise_path, f"{command[1]}"), "Error. File does not exist")
    elif command[0] == "Delete":
        if os.path.isfile(os.path.join(exercise_path, f"{command[1]}")):
            os.remove(os.path.join(exercise_path, f"{command[1]}"))
            write_to_log(__file__, os.path.join(exercise_path, f"{command[1]}"), "OK. File deleted")
        else:
            print("An error occurred")
            write_to_log(__file__, os.path.join(exercise_path, f"{command[1]}"), "Error. File does not exist")
    elif command[0] == "End":
        break