n = int(input())
elements = set()

for _ in range(n):
    buff = input().split()
    for element in buff:
        elements.add(element)

for element in elements:
    print(element)