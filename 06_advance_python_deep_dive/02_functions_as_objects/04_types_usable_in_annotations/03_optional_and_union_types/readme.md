# Optional and Union Types

## Introduction
Optional and Union types in Python provide a way to specify that a variable, function argument, or return value can be one of several types. These types are particularly useful when dealing with cases where values might be `None` or when a function can return different types based on certain conditions.

## Optional Type
The `Optional` type is used to indicate that a variable can be of a specified type or `None`. It is a shortcut for `Union[type, None]`.

### Example: Using Optional
```python
from typing import Optional

def show_count(count: int, singular: str, plural: Optional[str] = None) -> str:
    if count == 1:
        return f"{count} {singular}"
    else:
        return f"{count} {plural or singular + 's'}"

print(show_count(1, "apple"))  # Output: 1 apple
print(show_count(5, "apple"))  # Output: 5 apples
print(show_count(5, "apple", "apples"))  # Output: 5 apples
```

In this example, `plural: Optional[str]` means that the `plural` parameter can be a `str` or `None`. If it is `None`, the function uses the default plural form.

## Better Syntax for Optional and Union in Python 3.10
Since Python 3.10, you can use the `|` operator as a shorthand for `Union`. This simplifies the syntax and removes the need to import `Optional` or `Union`.

### Example: Using New Syntax
```python
def show_count(count: int, singular: str, plural: str | None = None) -> str:
    if count == 1:
        return f"{count} {singular}"
    else:
        return f"{count} {plural or singular + 's'}"

print(show_count(1, "apple"))  # Output: 1 apple
print(show_count(5, "apple"))  # Output: 5 apples
print(show_count(5, "apple", "apples"))  # Output: 5 apples
```

## Union Type
The `Union` type is used to indicate that a variable can be one of several types.

### Example: Using Union
The `ord` function can take either a `str` or `bytes` and returns an `int`.

```python
from typing import Union

def ord(c: Union[str, bytes]) -> int:
    return builtins.ord(c)  # Just for illustration

print(ord('a'))  # Output: 97
print(ord(b'a'))  # Output: 97
```

Here is a function that takes a `str` but may return a `str` or a `float`:

```python
from typing import Union

def parse_token(token: str) -> Union[str, float]:
    try:
        return float(token)
    except ValueError:
        return token

print(parse_token("123.45"))  # Output: 123.45
print(parse_token("abc"))     # Output: abc
```

### Why Avoid Functions Returning Union Types
Functions that return `Union` types can be more difficult for users to work with because they must check the type of the returned value at runtime to know how to handle it. However, there are reasonable use cases, such as in simple expression evaluators.

### When Union Is Not Accurate
In some cases, functions accept arguments of multiple types but return a type based on the input type. For such functions, using `Union` is not accurate. Instead, you can use type variables or overloading.

### Example: Using TypeVar for Dual-Mode APIs
```python
from typing import TypeVar

T = TypeVar('T', str, bytes)

def process(value: T) -> T:
    if isinstance(value, str):
        return value.upper()
    elif isinstance(value, bytes):
        return value.upper()

print(process("hello"))  # Output: HELLO
print(process(b"hello"))  # Output: b'HELLO'
```

## Flattening Nested Unions
Nested `Union` types have the same effect as a flattened `Union`.

### Example: Nested Union
```python
from typing import Union

# Nested Union
NestedUnionType = Union[A, B, Union[C, D, E]]
# Flattened Union
FlattenedUnionType = Union[A, B, C, D, E]
```

### Explanation
- **Nested Union**: `NestedUnionType = Union[A, B, Union[C, D, E]]` means that the type can be `A`, `B`, `C`, `D`, or `E`. The inner `Union[C, D, E]` is nested within the outer `Union[A, B, ...]`.
- **Flattened Union**: `FlattenedUnionType = Union[A, B, C, D, E]` is equivalent to the nested union. This means that when you use `Union`, all the nested unions are flattened into a single union type.

Using `Union[int, float]` is redundant because `int` is already consistent with `float`. This means that you can use `float` to annotate the parameter, and it will accept `int` values as well.

## Conclusion
Using `Optional` and `Union` types in Python provides flexibility in handling cases where variables can have multiple types. With the new syntax introduced in Python 3.10, it's easier and more concise to use these types. However, it's important to use them judiciously to avoid making the code harder to understand and work with.