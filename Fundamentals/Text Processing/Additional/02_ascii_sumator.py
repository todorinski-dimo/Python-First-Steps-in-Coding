left = ord(input())
right = ord(input())
string = input()
value = 0

for ch in string:
    if left < ord(ch) < right:
        value += ord(ch)

print(value)