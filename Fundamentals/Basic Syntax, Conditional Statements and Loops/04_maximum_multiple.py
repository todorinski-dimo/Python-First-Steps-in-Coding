devisor = int(input())
boundary = int(input())
for boundary in range(boundary, devisor - 1, -1):
    if boundary % devisor == 0:
        print(boundary)
        break