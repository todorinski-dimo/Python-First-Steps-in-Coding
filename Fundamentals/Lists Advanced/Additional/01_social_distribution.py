def is_dtr_possible(wealth: list, lv: int) -> bool:
    diff_list = [item - lv for item in wealth]
    # print(diff_list)
    if sum(diff_list) >= 0:
        return True
    return False


def distribute(wealth: list, lv: int) -> list:
    for index in range(len(wealth)):
        if wealth[index] < lv:
            wealth[wealth.index(max(wealth))] -= lv - wealth[index]
            wealth[index] = lv

    return wealth


wealth_levels = [int(item) for item in input().split(", ")]
level = int(input())

if not is_dtr_possible(wealth_levels, level):
    print("No equal distribution possible")
else:
    print(distribute(wealth_levels, level))
