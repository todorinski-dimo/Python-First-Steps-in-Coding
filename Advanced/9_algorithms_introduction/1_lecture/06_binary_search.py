def binary_search(arr, t):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        mid_el = arr[mid]
        if mid_el == t:
            return mid
        elif mid_el < t:
            left = mid + 1
        else:
            right = mid - 1

    return -1

input_data = [int(x) for x in input().split()]
target = int(input())
print(binary_search(input_data, target))
