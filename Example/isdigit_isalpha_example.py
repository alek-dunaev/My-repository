"""Пример использования isdigit_isalpha"""
"""In this mission you need to create a password verification function.
The verification conditions are:
the length should be bigger than 6;
should contain at least one digit, but it cannot consist of just digits;
if the password is longer than 9 - previous rule (about one digit), is not required.
Input: A string (str).
Output: A logic value (bool). """


def is_acceptable_password(password: str) -> bool:
    return (len(password) > 6 and not password.isdigit() and not password.isalpha()) or len(password) > 9


print("Example:")
print(is_acceptable_password("short"))
