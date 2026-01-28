def remove_chars(from_: list, what_: list) -> list:
    """
    takes a list(or string) to have chars to be removed from;
    takes a list with defined chars to be removed;
    returns a list with the initial list(string) with removed chars
    """
    return [item for item in from_ if item.lower() not in what_]

input_text = input()
chr_for_removal = ['a', 'o', 'u', 'e', 'i']
new_list = remove_chars(input_text, chr_for_removal)
print("".join(new_list))