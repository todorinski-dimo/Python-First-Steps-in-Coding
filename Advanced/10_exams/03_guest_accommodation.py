def accommodate(*guest_groups, **rooms):
    a_rooms = {k: v for k,v in sorted(rooms.items(), key=lambda item: (item[1], item[0]))}
    empty_rooms = len(a_rooms)
    accommodated_guests = {}
    unaccommodated_guests = 0
    for group in guest_groups:
        for room_num, room_capacity in a_rooms.items():
            if group <= room_capacity:
                if room_num[-3:] not in accommodated_guests:
                    accommodated_guests[room_num[-3:]] = 0
                accommodated_guests[room_num[-3:]] = group
                a_rooms[room_num] = 0
                empty_rooms -= 1
                break
        else:
            unaccommodated_guests += group
    result = []
    if accommodated_guests:
        result.append(f"A total of {len(accommodated_guests)} accommodations were completed!")
        for room_num, room_capacity in sorted(accommodated_guests.items(), key=lambda item: item[0]):
            result.append(f"<Room {room_num} accommodates {room_capacity} guests>")
    else:
        result.append(f"No accommodations were completed!")
    if unaccommodated_guests:
        result.append(f"Guests with no accommodation: {unaccommodated_guests}")
    if empty_rooms:
        result.append(f"Empty rooms: {empty_rooms}")
    return "\n".join(result)






print(accommodate(5, 4, 2, room_305=6, room_410=5, room_204=2))
print(accommodate(10, 9, 8, room_307=6, room_802=5))
print(accommodate(1, 2, 4, 8, room_102=3, room_101=1, room_103=2))