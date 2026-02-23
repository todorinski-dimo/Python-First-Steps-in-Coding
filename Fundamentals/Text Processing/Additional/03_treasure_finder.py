key = [int(item) for item in input().split()]


while True:
    code = input()
    decoded = ""
    new_key = []
    # treasure = ""
    # coordinates = ""
    if code == "find":
        break
    for _ in range((len(code) // len(key)) + 1):
        new_key += key
    for idx in range(len(code)):
        decoded += chr(ord(code[idx]) - new_key[idx])
    treasure = decoded[decoded.index("&") + 1:decoded.index("&") + 1 + decoded[decoded.index("&") + 1:].index("&")]
    coordinates = decoded[decoded.index("<") + 1:decoded.index(">")]
    print(f"Found {treasure} at {coordinates}")

