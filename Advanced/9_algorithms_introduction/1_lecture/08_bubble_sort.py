def bubble_sort(arr):
    is_sorted = False
    sorted_elements = 0
    while not is_sorted:
        is_sorted = True
        for j in range(1, len(arr) - sorted_elements):
            i = j - 1
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                is_sorted = False
        sorted_elements += 1
    return arr

input_data = [int(x) for x in input().split()]
print(*bubble_sort(input_data))