raw_position = input().split()
raw_position = [int(pos) for pos in raw_position]
#print(raw_position)
#transforms first input in list with indexes
positions = []
for pos in range(len(raw_position)):
    temp = raw_position[pos]
    sum_digits = 0
    while temp > 0:
        sum_digits += temp % 10 #takes last position
        temp //= 10 #removes/cuts last position
    positions.append(sum_digits)
#print(positions)

raw_string = input()
new_message = ""

#build new string, select and remove chars from the string
for numb in positions:
    #print(numb)
    #check if input string is empty
    if not raw_string:
        break
    if numb >= len(raw_string):
        #getting the index in range of the string length
        numb %= len(raw_string)
    new_message += raw_string[numb]
    raw_string = raw_string[:numb] + raw_string[numb + 1:]
    #print(raw_string)

print(new_message)
