input_key = int(input())
input_lines = int(input())

new_message = ""

for _ in range(input_lines):
    character = input()
    new_message += chr(ord(character)+input_key)

print(new_message)