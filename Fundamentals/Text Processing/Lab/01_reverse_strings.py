while True:
    input_text = input()
    # reversed_text = ""
    if input_text == "end":
        break
    else:
        print(input_text, "=", input_text[::-1])
    #     for ch in reversed(input_text):
    #         reversed_text += ch
    # print(input_text + " = " + reversed_text)

