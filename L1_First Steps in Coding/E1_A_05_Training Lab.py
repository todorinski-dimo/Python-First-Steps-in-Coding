side_w = float(input())
side_h = float(input())

real_h = side_h - 1
columns = real_h // 0.7
rows = side_w // 1.2

print(f"{rows*columns-3}")