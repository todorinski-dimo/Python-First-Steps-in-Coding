hour = int(input())
minutes = int(input())

new_minutes = minutes + 15

if new_minutes - 60 >= 0:
    new_minutes = new_minutes - 60
    hour += 1

if hour - 24 >= 0:
    hour = hour - 24

print(f"{hour}:{new_minutes:02d}")