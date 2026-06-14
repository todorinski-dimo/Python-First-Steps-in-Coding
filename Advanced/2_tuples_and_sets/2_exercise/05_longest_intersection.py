def create_set_from_range(input_range):
    start, end = input_range.split(",")
    return set(range(int(start), int(end) + 1))

intersection = set()

for _ in range(int(input())):
    first_range, second_range = input().split("-")
    first_set = create_set_from_range(first_range)
    second_set = create_set_from_range(second_range)

    curr_intersection = first_set & second_set

    if len(curr_intersection) > len(intersection):
        intersection = curr_intersection

print(f"Longest intersection is {list(intersection)} with length {len(intersection)}")