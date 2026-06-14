import os
import datetime as dt
from _abs_path import abs_path

def write_to_log(file, path, message):
    with open(os.path.join(abs_path, "_logs_exercises.txt"), "a") as log:
        log.write(f"{dt.datetime.now()} - {file} - {path} - {message}\n")

