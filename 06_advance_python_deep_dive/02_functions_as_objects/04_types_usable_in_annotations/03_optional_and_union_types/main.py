def show_count(count: int, singular: str, plural: str | None = None) -> str:
    if count == 1:
        return f"{count} {singular}"
    else:
        return f"{count} {plural or singular + 's'}"

print(show_count(1, "apple"))  # Output: 1 apple
print(show_count(5, "apple"))  # Output: 5 apples
print(show_count(5, "apple", "apples"))  # Output: 5 apples


import builtins
from typing import Union

def ord(c: Union[str, bytes]) -> int:
    return builtins.ord(c)  # Just for illustration

print(ord('a'))  # Output: 97
print(ord(b'a'))  # Output: 97
print(type(ord('a')))  # Output: 97
print(type(ord(b'a')))  # Output: 97


from typing import Union

def parse_token(token: str) -> Union[str, float]:
    try:
        return float(token)
    except ValueError:
        return token

print(parse_token("123.45"))  # Output: 123.45
print(parse_token("abc"))     # Output: abc

print(type(parse_token("123.45")))  # Output: 123.45
print(type(parse_token("abc")))     # Output: abc

