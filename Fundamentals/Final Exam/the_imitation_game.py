encrypted_message = input()
cmd = input().split("|")

while cmd[0] != "Decode":
    if cmd[0] == "ChangeAll":
        encrypted_message = encrypted_message.replace(cmd[1], cmd[2])
    elif cmd[0] == "Insert":
        first_half = encrypted_message[:int(cmd[1])]
        second_half = encrypted_message[int(cmd[1]):]
        # print(first_half, second_half)
        encrypted_message = first_half + cmd[2] + second_half
        # print(encrypted_message)
    elif cmd[0] == "Move" and int(cmd[1]) <= len(encrypted_message):
        buff = encrypted_message[:int(cmd[1])]
        encrypted_message += buff
        encrypted_message = encrypted_message[int(cmd[1]):]
        # print(encrypted_message)
    cmd = input().split("|")
print(f"The decrypted message is: {encrypted_message}")