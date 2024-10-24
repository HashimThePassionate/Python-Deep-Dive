from typing import Union

def parse_user_input(value: str) -> int | str:
    if value.isdigit():
        return int(value)
    return value

result1: Union[int, str] = parse_user_input("hello")
print(f'Result1 type is {type(result1)} and its value is {result1}')  # Output: "hello" (as a str)
result2: Union[int, str] = parse_user_input("42")
print(f'Result2 type is {type(result2)} and its value is {result2}')  # Output: "hello" (as a str)