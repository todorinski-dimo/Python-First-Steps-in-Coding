from time import sleep
import os


def typewrite(text: str):
    lines = text.split('\n')
    for line in lines:
        display = ''
        for char in line:
            display += char
            print()
            print(f'╭─ SOME MESSAGE OR SOMEONES NAME ────────────────────────────────────────────╮')
            print(f'│ {display:74} │')  # :74 is the same as ' ' * 74
            print(f'╰────────────────────────────────────────────────────────────────────────────╯')

            sleep(0.05)
            os.system("")
            print('\033[5A')


typewrite("DimoTodorinski")
print()
print()
print()
