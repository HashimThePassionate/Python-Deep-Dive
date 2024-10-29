# Trying to add a list and a dictionary will raise an error.
# print([] + {})  
# Output: TypeError: can only concatenate list (not "dict") to list

# def process_age(age):
#     return age + 1

# Using a string accidentally
# print(process_age("25"))
# Output: TypeError: can only concatenate str (not "int") to str


from typing import Union, List

def parse_input(data: Union[str, List[int]]) -> List[str]:
    if isinstance(data, str):
        return data.split(',')
    elif isinstance(data, list):
        return [str(item) for item in data]
    else:
        raise ValueError("Unsupported data type!")

# This function can handle both strings and lists
print(parse_input("apple,banana,cherry"))  # Output: ['apple', 'banana', 'cherry']
print(parse_input([1, 2, 3]))              # Output: ['1', '2', '3']
print(parse_input(123))                     # Output: ValueError: Unsupported data type!
