n = int(input())
reservations = set()

for _ in range(n):
    reservations.add(input())

reservation = input()

while reservation != "END":
    if reservation in reservations:
        reservations.remove(reservation)
    reservation = input()

print(len(reservations))
for reservation in sorted(reservations):
    print(reservation)