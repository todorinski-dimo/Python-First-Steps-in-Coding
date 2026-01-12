start = int(input())
end = int(input())
new_string = ""

for num in range(start, end + 1):
    new_string += chr(num) + " "

print(new_string)
