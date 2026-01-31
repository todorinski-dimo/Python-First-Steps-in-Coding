def take_even_index(init_list: list) -> list:
    evens_list = []
    for index in range(0, len(init_list), 2):
        evens_list.append(init_list[index])
    return evens_list


def take_odd_index(init_list: list) -> list:
    odds_list = []
    for index in range(1, len(init_list), 2):
        odds_list.append(init_list[index])
    return odds_list


def decode(init_list: list, take_lst: list, skip_lst: list) -> list:
    decoded_list = []
    index_start = 0
    index_end = 0
    for index in range(len(take_lst)):
        index_end += int(take_lst[index])
        decoded_list.extend(init_list[index_start: index_end])
        index_start += int(take_lst[index])
        index_start += int(skip_lst[index])
        index_end += int(skip_lst[index])
    return decoded_list


init_string = list(input())
nums_list = list(filter(lambda item: item.isnumeric(), init_string))
alphas_List = list(filter(lambda item: not item.isnumeric(), init_string))
take_list = take_even_index(nums_list)
skip_list = take_odd_index(nums_list)
decoded = decode(alphas_List, take_list, skip_list)
print("".join(decoded))
