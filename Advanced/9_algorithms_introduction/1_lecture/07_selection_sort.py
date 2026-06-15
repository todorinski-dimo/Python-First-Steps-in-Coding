def selection_sort(arr):

    for i in range(len(arr)):
        min_val_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_val_index]:
                min_val_index = j
        arr[i], arr[min_val_index] = arr[min_val_index], arr[i]

    return arr

input_data = [int(x) for x in input().split()]
print(*selection_sort(input_data))
