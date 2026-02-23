inputs = int(input())

for _ in range(inputs):
    write = False
    string = list(input())
    name = string[string.index("@") + 1:string.index("|")]
    age = string[string.index("#") + 1:string.index("*")]
    print(f"{''.join(name)} is {''.join(age)} years old.")



