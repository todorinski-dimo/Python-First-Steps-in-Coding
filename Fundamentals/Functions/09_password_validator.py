def is_length(phrase: str) -> bool:
    """takes a string; returns True if string is long between 6 and 10 chars"""
    if 6 <= len(phrase) <= 10:
        return True
    return False


def is_only_digits_letters(phrase: str) -> bool:
    """takes a string; returns True if string has only chars and digits"""
    return phrase.isalnum()


def is_has_two_digits(phrase: str) -> bool:
    """takes a string; returns True if string has 2 or more digits"""
    digits = 0
    for char in phrase:
        if char.isdigit():
            digits += 1
    if digits >= 2:
        return True
    return False


def is_valid(phrase: str) -> str:
    """takes a string; returns list with messages on new line related to validity check"""
    exit_string = []
    if is_length(phrase) and is_only_digits_letters(phrase) and is_has_two_digits(phrase):
        return "Password is valid"
    if not is_length(phrase):
        exit_string.append("Password must be between 6 and 10 characters")
    if not is_only_digits_letters(phrase):
        exit_string.append("Password must consist only of letters and digits")
    if not is_has_two_digits(phrase):
        exit_string.append("Password must have at least 2 digits")
    return "\n".join(exit_string)


input_pass = input()
print(is_valid(input_pass))
