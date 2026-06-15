def calc_sum_recursive(arr, idx):
    if idx == len(arr) -1:
        return arr[idx]
    return arr[idx] + calc_sum_recursive(arr, idx + 1)

input_nums = [int(x) for x in input().split()]
print(calc_sum_recursive(input_nums, 0))