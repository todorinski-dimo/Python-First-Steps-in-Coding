from sre_parse import SPECIAL_CHARS


class PasswordTooShortError(Exception):
    pass

class PasswordTooCommonError(Exception):
    pass

class PasswordNoSpecialCharactersError(Exception):
    pass

class PasswordContainsSpacesError(Exception):
    pass

def passwd_common_check(pwd, spec):
    only_digits = pwd.isdigit()
    only_letters = pwd.isalpha()
    only_specials = all(ch in spec for ch in pwd)
    return only_digits or only_letters or only_specials


PASSWD_MIN_LENGTH = 8
SPEC= ["@", "*", "&", "%"]

while True:
    passwd = input()
    if passwd == 'Done':
        break

    if len(passwd) < PASSWD_MIN_LENGTH:
        raise PasswordTooShortError("Password must contain at least 8 characters")

    if passwd_common_check(passwd, SPEC):
        raise PasswordTooCommonError("Password must be a combination of digits, letters, and special characters")

    if not any(ch in SPEC for ch in passwd):
        raise PasswordNoSpecialCharactersError("Password must contain at least 1 special character")

    if " " in passwd:
        raise PasswordContainsSpacesError("Password must not contain empty spaces")

    print("Password is valid")