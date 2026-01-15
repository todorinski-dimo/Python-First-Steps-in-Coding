
route_len = int(input())
route_type = input()

cost = 0

if route_len < 20:
    if route_type == "day":
        cost = 0.7 + route_len * 0.79
    elif route_type == "night":
        cost = 0.7 + route_len * 0.9
elif 20 <= route_len < 100:
    cost = route_len * 0.09
else:
    cost = route_len * 0.06

print(f"{cost:.2f}")
