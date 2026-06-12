import os
import re

from constant import path_to_dir

file_words_path = os.path.join(path_to_dir, "files", "words.txt")
file_text_path = os.path.join(path_to_dir, "files", "text.txt")

with open(file_words_path, "w") as file:
    file.write("quick is fault")

with open(file_text_path, "w") as file:
    file.write("-I was quick to judge him, but it wasn't his fault.\n-Is this some kind of joke?! Is it?\n-Quick, hide here…It is safer")

with open(file_words_path, "r") as file:
    words = file.read().lower().split()

with open(file_text_path, "r") as file:
    text = file.read().lower()

result = {}
for word in words:
    pattern = rf"\b{word}\b"
    matches = re.findall(pattern, text)
    result[word] = len(matches)

ordered_result = sorted(result.items(), key=lambda x: -x[1])

with open(os.path.join(path_to_dir, "files", "output.txt"), "w") as file:
    for word, count in ordered_result:
        file.write(f"{word} - {count}\n")