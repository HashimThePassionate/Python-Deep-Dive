from typing import TypeVar

T = TypeVar('T', bound='Comparable')

class Comparable:
    def __lt__(self, other):
        return NotImplemented

def max_util(first: T, second: T) -> T:
    return second if first < second else first

max_value_int = max_util(1, 2)  # Using integers
print(max_value_int)  # Output: 2

max_value_float = max_util(1.5, 2.5)  # Using floats
print(max_value_float)  # Output: 2.5

max_value_str = max_util("apple", "banana")  # Using strings
print(max_value_str)  # Output: banana

