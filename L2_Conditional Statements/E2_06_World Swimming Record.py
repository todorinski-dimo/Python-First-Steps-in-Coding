import math

record = float(input())
length = float(input())
tempo = float(input())

own_time = length * tempo
resistance = math.floor(length / 15)
resistance_time = resistance * 12.5

total_time = own_time + resistance_time

if total_time >= record:
    print(f"No, he failed! He was {abs(total_time - record):.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
