def list_roman_emperors(*status, **length):
    status_dict = {key: value for key, value in sorted(status, key=lambda item: item[1], reverse=True)}
    result = [f"Total number of emperors: {len(status_dict)}"]
    result1 = ["Successful emperors:"]
    result2 = ["Unsuccessful emperors:"]
    for length_name, length_length in sorted(length.items(), key=lambda item: (-item[1], item[0])):
        for status_name, status_status in status_dict.items():
            if status_status:
                if status_name == length_name:
                    result1.append(f"****{status_name}: {length_length}")
    for length_name, length_length in sorted(length.items(), key=lambda item: (item[1], item[0])):
        for status_name, status_status in status_dict.items():
            if not status_status:
                if status_name == length_name:
                        result2.append(f"****{status_name}: {length_length}")
    if len(result1) > 1:
        result.extend(result1)
    if len(result2) > 1:
        result.extend(result2)
    return "\n".join(result)





print(list_roman_emperors(("Augustus", True), ("Nero", False), Augustus=40, Nero=14,))
print(list_roman_emperors(("Augustus", True), ("Trajan", True), ("Nero", False), ("Pertinax", False), ("Caligula", False), ("Vespasian", True), Augustus=40, Trajan=19, Nero=14, Caligula=4, Pertinax=4, Vespasian=19,))
print(list_roman_emperors(("Augustus", True), ("Trajan", True), ("Claudius", True), Augustus=40, Trajan=19, Claudius=13,))