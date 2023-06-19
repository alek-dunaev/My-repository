"""In this mission you need to create a password verification function.
The verification conditions are:
the length should be bigger than 6;
should contain at least one digit, but cannot consist of just digits.
Input: A string (str).

Output: A logic value (bool)."""

is_acceptable_password = lambda p: 0 < sum(c.isdigit() for c in p) < len(p) > 6

print("Example:")
print(is_acceptable_password("short"))
