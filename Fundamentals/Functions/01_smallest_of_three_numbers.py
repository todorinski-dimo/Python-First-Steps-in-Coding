def find_min_int(num_list: list) -> int:
    """takes: list of integers; returns min integer"""
    return min(num_list)


input_num_first = int(input())
input_num_second = int(input())
input_num_third = int(input())

list_input_nums = [input_num_first, input_num_second, input_num_third]
print(find_min_int(list_input_nums))
