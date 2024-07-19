# Getting Started With Mypy 

## Introduction
This section demonstrates how gradual typing works in practice, starting with a simple function and gradually adding type hints to it, guided by Mypy. Mypy is one of several Python type checkers compatible with PEP 484, alongside Google’s pytype, Microsoft’s Pyright, and Facebook’s Pyre. These type checkers are also embedded in IDEs such as PyCharm.

## Choosing a Type Checker
While Mypy is chosen for the examples due to its popularity, other type checkers might be a better fit for some projects or teams. For instance:
- **Pytype**: Designed to handle codebases with no type hints, it provides useful advice, is more lenient than Mypy, and can generate annotations for your code.
- **Pyright**
- **Pyre**

## Example Function: `show_count`
We will annotate the `show_count` function, which returns a string with a count and a singular or plural word depending on the count.

### Usage Examples
```python
>>> show_count(99, 'bird')
'99 birds'
>>> show_count(1, 'bird')
'1 bird'
>>> show_count(0, 'bird')
'no birds'
```

### Source Code of `show_count` Without Annotations
Below is the source code of the `show_count` function from `main.py`, without type hints:

```python
def show_count(count, word):
    if count == 1:
        return f'1 {word}'
    count_str = str(count) if count else 'no'
    return f'{count_str} {word}s'
```

### Explanation
The `show_count` function takes two parameters:
- `count`: The number of items.
- `word`: The word to be used for the items.

The function returns a formatted string based on the value of `count`:
- If `count` is 1, it returns "1 word".
- If `count` is 0, it returns "no words".
- For any other value of `count`, it returns "count words".

## Starting with Mypy
To begin type checking, run the mypy command on the `main.py` module:

```sh
$ pip install mypy
$ mypy main.py
Success: no issues found in 1 source file
```

Mypy with default settings finds no problem with the initial `show_count` function.

### Adding Type Hints
To gradually add type hints, use Mypy to check the types and ensure our annotations are correct.

1. **Initial Function**:
   ```python
   def show_count(count, word):
       if count == 1:
           return f'1 {word}'
       count_str = str(count) if count else 'no'
       return f'{count_str} {word}s'
   ```

2. **Add Type Hints**:
   ```python
   def show_count(count: int, word: str) -> str:
       if count == 1:
           return f'1 {word}'
       count_str = str(count) if count else 'no'
       return f'{count_str} {word}s'
   ```

### Explanation of Type Hints
- `count: int` indicates that `count` should be an integer.
- `word: str` indicates that `word` should be a string.
- `-> str` indicates that the function returns a string.

### Complete Example with Annotations
Here is the complete `show_count` function with type hints:

```python
def show_count(count: int, word: str) -> str:
    if count == 1:
        return f'1 {word}'
    count_str = str(count) if count else 'no'
    return f'{count_str} {word}s'
```

## Making Mypy More Strict
The command-line option `--disallow-untyped-defs` makes Mypy flag any function definition that does not have type hints for all its parameters and for its return value.

Using `--disallow-untyped-defs` on the test file produces three errors and a note:

```sh
$ mypy --disallow-untyped-defs main_test.py
main.py:14: error: Function is missing a type annotation
main_test.py:10: error: Function is missing a type annotation
main_test.py:15: error: Function is missing a return type annotation
main_test.py:15: note: Use "-> None" if function does not return a value
Found 3 errors in 2 files (checked 1 source file)
```

For the first steps with gradual typing, use another option: `--disallow-incomplete-defs`. Initially, it tells nothing:

```sh
$ mypy --disallow-incomplete-defs main_test.py
Success: no issues found in 1 source file
```

Now add just the return type to `show_count` in `main.py`:

```python
def show_count(count, word) -> str:
```

Using the same command line as before to check `main_test.py` will lead Mypy to look at `main.py` again:

```sh
$ mypy --disallow-incomplete-defs main_test.py
main.py:14: error: Function is missing a type annotation for one or more arguments
Found 1 error in 1 file (checked 1 source file)
```

Now you can gradually add type hints function by function, without getting warnings about functions that haven’t been annotated. This is a fully annotated signature that satisfies Mypy:

```python
def show_count(count: int, word: str) -> str:
```

## Mypy Configuration
Instead of typing command-line options like `--disallow-incomplete-defs`, save your favorite options as described in the Mypy configuration file documentation. You can have global settings and per-module settings. Here is a simple `mypy.ini` to get started:

```ini
[mypy]
python_version = 3.9
warn_unused_configs = True
disallow_incomplete_defs = True
```

## A Default Parameter Value
The `show_count` function in the initial example only works with regular nouns. If the plural can’t be spelled by appending an 's', let the user provide the plural form:

```python
>>> show_count(3, 'mouse', 'mice')
'3 mice'
```

### Type-Driven Development
First, add a test that uses the third argument. Don’t forget to add the return type hint to the test function, otherwise Mypy will not check it.

```python
def test_irregular() -> None:
    got = show_count(2, 'child', 'children')
    assert got == '2 children'
```

Mypy detects the error:

```sh
$ mypy main_test.py
main_test.py:22: error: Too many arguments for "show_count"
Found 1 error in 1 file (checked 1 source file)
```

Now edit `show_count`, adding the optional plural parameter:

```python
def show_count(count: int, singular: str, plural: str = '') -> str:
    if count == 1:
        return f'1 {singular}'
    count_str = str(count) if count else 'no'
    if not plural:
        plural = singular + 's'
    return f'{count_str} {plural}'

# Example calls:
print(show_count(99, 'bird'))          # Output: '99 birds'
print(show_count(1, 'bird'))           # Output: '1 bird'
print(show_count(0, 'bird'))           # Output: 'no birds'
print(show_count(3, 'mouse', 'mice'))  # Output: '3 mice'
print(show_count(2, 'child', 'children')) # Output: '2 children'
```

Now Mypy reports “Success.”

### Best Practices for Type Hints
- No space between the parameter name and the `:`
- One space after the `:`
- Spaces on both sides of the `=` that precedes a default parameter value

## Using `None` as a Default
In the modified `show_count`, the parameter `plural` is annotated as `str`, and the default value is `''`, so there is no type conflict. In other contexts, `None` is a better default, especially if the optional parameter expects a mutable type. To have `None` as the default for the `plural` parameter:

```python
from typing import Optional

def show_count(count: int, singular: str, plural: Optional[str] = None) -> str:
```

### Explanation
- `Optional[str]` means `plural` may be a `str` or `None`.
- You must explicitly provide the default value `= None`.

Remember: at runtime, type hints are ignored. You need to import `Optional` from the `typing` module. When importing types, it’s good practice to use `from typing import X` to reduce the length of the function signatures.

