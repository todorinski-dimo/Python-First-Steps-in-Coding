txt = input()
try:
    multy = int(input())
except ValueError:
    print("Please enter an integer")
else:
    print(txt * multy)
