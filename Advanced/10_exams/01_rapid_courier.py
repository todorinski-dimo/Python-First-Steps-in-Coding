from collections import deque

packages = list(map(int, input().split()))
couriers = deque(list(map(int, input().split())))
delivered_weight = 0


while packages and couriers:
    if couriers[0] >= packages[-1]:
        couriers[0] -= packages[-1] * 2
        if couriers[0] > 0:
            couriers.rotate(-1)
        else:
            couriers.popleft()
        delivered_weight += packages.pop()
    else:
        packages[-1] -= couriers[0]
        delivered_weight += couriers[0]
        couriers.popleft()

print(f"Total weight: {delivered_weight} kg")
if packages:
    print(f"Unfortunately, there are no more available couriers to deliver the following packages: {', '.join(map(str, packages))}")
elif couriers:
    print(f"Couriers are still on duty: {', '.join(map(str, couriers))} but there are no more packages to deliver.")
else:
    print("Congratulations, all packages were delivered successfully by the couriers today.")