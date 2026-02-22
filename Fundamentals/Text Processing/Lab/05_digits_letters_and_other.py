input_string = input()

numbers = ""
letters = ""
symbols = ""

for ch in input_string:
    if ch.isdigit():
        numbers += ch
    elif ch.isalpha():
        letters += ch
    else:
        symbols += ch

print(numbers)
print(letters)
print(symbols)
