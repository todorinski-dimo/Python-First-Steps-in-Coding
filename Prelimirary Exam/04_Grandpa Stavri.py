days = int(input())

total_rakiq = 0
total_degrees = 0
average_degrees = 0

for i in range(days):
    rakiq = float(input())
    degrees = float(input())
    total_rakiq += rakiq
    total_degrees += (degrees * rakiq)

average_degrees = total_degrees / total_rakiq

print(f"Liter: {total_rakiq:.2f}")
print(f"Degrees: {average_degrees:.2f}")

if average_degrees < 38:
    print("Not good, you should baking!")
elif 38 <= average_degrees <= 42:
    print("Super!")
else:
    print("Dilution with distilled water!")