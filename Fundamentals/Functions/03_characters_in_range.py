def chr_in_range(chr_one: str, chr_two: str) -> list:
    """takes 2 characters; returns a list with characters between(excluding) the 2 characters by ASCII table"""
    list_of_integers = []
    for code in range(ord(chr_one) + 1, ord(chr_two)):
        list_of_integers.append(chr(code))
    return list_of_integers


input_chr_first = input()
input_chr_second = input()
list_in_between = chr_in_range(input_chr_first, input_chr_second)
print(" ".join(list_in_between))
