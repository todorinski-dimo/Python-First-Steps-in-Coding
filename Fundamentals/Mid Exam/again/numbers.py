numbers = [int(item) for item in input().split()]

average = sum(numbers) / len(numbers)
above_average = list(filter(lambda item: item > average, numbers))

if len(above_average) == 0:
    print("No")
else:
    above_average.sort(reverse=True)
    above_average = [str(item) for item in above_average]
    print(" ".join(above_average[:5]))
