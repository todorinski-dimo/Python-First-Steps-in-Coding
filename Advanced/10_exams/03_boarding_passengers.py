def boarding_passengers(ship_capacity, *passengers):
    waiting_passengers = 0
    boarded_passengers = {}
    remaining_capacity = ship_capacity
    for bp_passengers, bp_group in passengers:
        if bp_passengers <= remaining_capacity:
            if bp_group not in boarded_passengers:
                boarded_passengers[bp_group] = 0
            boarded_passengers[bp_group] += bp_passengers
            remaining_capacity -= bp_passengers
        else:
            waiting_passengers += bp_passengers

    result = ["Boarding details by benefit plan:"]
    for b_group, b_passengers in sorted(boarded_passengers.items(), key=lambda x: (-x[1], x[0])):
        result.append(f"## {b_group}: {b_passengers} guests")
    if waiting_passengers == 0 and remaining_capacity == 0:
        result.append("All passengers are successfully boarded!")
    elif waiting_passengers > 0 and remaining_capacity == 0:
        result.append("Boarding unsuccessful. Cruise ship at full capacity.")
    elif waiting_passengers > 0 and remaining_capacity > 0:
        result.append(f"Partial boarding completed. Available capacity: {remaining_capacity}.")

    return f'\n'.join(result)



print(boarding_passengers(150, (35, 'Diamond'), (55, 'Platinum'), (35, 'Gold'), (25, 'First Cruiser')))
print(boarding_passengers(100, (20, 'Diamond'), (15, 'Platinum'), (25, 'Gold'), (25, 'First Cruiser'), (15, 'Diamond'), (10, 'Gold')))
print(boarding_passengers(120, (30, 'Gold'), (20, 'Platinum'), (30, 'Diamond'), (10, 'First Cruiser'), (31, 'Platinum'), (20, 'Diamond')))