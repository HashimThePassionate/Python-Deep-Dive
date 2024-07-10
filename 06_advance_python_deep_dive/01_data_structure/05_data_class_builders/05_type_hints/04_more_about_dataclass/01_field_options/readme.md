# Field Options in `@dataclass`

## Introduction
We've already seen the most basic field option: providing (or not) a default value with the type hint. The instance fields you declare will become parameters in the generated `__init__`. Python does not allow parameters without defaults after parameters with defaults, so after you declare a field with a default value, all remaining fields must also have default values.

## Explanation of Default Values and Field Options in `@dataclass`

### Providing Default Values
When you define a field in a `@dataclass`, you can provide a default value for that field. This is similar to setting default values for function parameters.

### Order of Parameters with Default Values
Python enforces a rule in function definitions that parameters without default values cannot follow parameters with default values. This rule applies to the generated `__init__` method in `@dataclass`. Therefore, if you declare a field with a default value in a data class, all subsequent fields must also have default values. 

### Example Without Default Values
Consider the following example where fields do not have default values:

```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
```

In this case, the generated `__init__` method will be:

```python
def __init__(self, name: str, age: int):
    self.name = name
    self.age = age
```

### Example With Default Values
Now consider the following example where fields have default values:

```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int = 30
    country: str = "Unknown"
```

In this case, the generated `__init__` method will be:

```python
def __init__(self, name: str, age: int = 30, country: str = "Unknown"):
    self.name = name
    self.age = age
    self.country = country
```

### Enforcing Order in Default Values
If you mix fields with and without default values and put a non-default field after a default field, Python will raise an error:

```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str = "Unknown"
    age: int
```

This will raise a `TypeError` because `age` does not have a default value but follows `name`, which has a default value.

### Correct Order
To fix this, ensure that all non-default fields come before any fields with default values:

```python
from dataclasses import dataclass

@dataclass
class Person:
    age: int
    name: str = "Unknown"
```

## Mutable Default Values
Mutable default values are a common source of bugs for beginning Python developers. In function definitions, a mutable default value can be easily corrupted when one invocation of the function mutates the default, changing the behavior of further invocations. 

### Example of Incorrect Usage
Example 5-13 shows a `dataclass` that raises a `ValueError` due to a mutable default value:

```python
@dataclass
class ClubMember:
    name: str
    guests: list = []
```

If you load the module with that `ClubMember` class, you get:
</br></br> **[What is mutable default values](./00_mutable_default_values/readme.md)**

```plaintext
type_hints/04_more_about_dataclass/01_field_options/main.py
Traceback (most recent call last):
  File "C:\Users\aaaa\AppData\Local\Programs\Python\Python312\Lib\dataclasses.py", line 852, in 
_get_field
    raise ValueError(f'mutable default {type(f.default)} for field '
ValueError: mutable default <class 'list'> for field guests is not allowed: use default_factory 
```

The `ValueError` message explains the problem and suggests a solution: use `default_factory`.

### Correct Usage with `default_factory`
Example 5-14 shows how to correct `ClubMember`:

```python
from dataclasses import dataclass, field

@dataclass
class ClubMember:
    name: str
    guests: list = field(default_factory=list)
```

In the `guests` field, instead of a literal list, the default value is set by calling the `dataclasses.field` function with `default_factory=list`.

## Explanation
The `default_factory` parameter lets you provide a function, class, or any other callable, which will be invoked with zero arguments to build a default value each time an instance of the data class is created. This way, each instance of `ClubMember` will have its own list—instead of all instances sharing the same list from the class, which is rarely what we want and is often a bug.

> **Note**: While `@dataclass` rejects class definitions with a list default value in a field, it only applies to `list`, `dict`, and `set`. Other mutable values used as defaults will not be flagged by `@dataclass`. It's up to you to understand the problem and remember to use a default factory to set mutable default values. [See Custom Mutable Default Solution](./00_note/readme.md)

## Using Generic Types 
If you browse the `dataclasses` module documentation, you'll see a list field defined with a novel syntax, as in Example 5-15:

**[What is Generic Type?](./00_generic/readme.md)**

```python
from dataclasses import dataclass, field

@dataclass
class ClubMember:
    name: str
    guests: list[str] = field(default_factory=list)
```

The new syntax `list[str]` is a parameterized generic type: since Python 3.9, the `list` built-in accepts that bracket notation to specify the type of the list items.

> **Note**: Prior to Python 3.9, the built-in collections did not support generic type notation. If you need a parameterized list type hint in Python 3.8 or earlier, you must import the `List` type from `typing` and use it: `List[str]`.

Both examples 5-14 and 5-15 are correct, and the Mypy type checker does not complain about either of those class definitions. The difference is that `guests: list` means that `guests` can be a list of objects of any kind, while `guests: list[str]` says that `guests` must be a list in which every item is a `str`. This will allow the type checker to find (some) bugs in code that puts invalid items in the list, or that reads items from it.

## Field Function Options
The `default_factory` is likely to be the most common option of the `field` function, but there are several others, listed in Table 5-3.

## Table 5-3: Keyword Arguments Accepted by the `field` Function

| Option          | Meaning                                    | Default                                 |
|-----------------|--------------------------------------------|-----------------------------------------|
| `default`       | Default value for field                    | `_MISSING_TYPE`                         |
| `default_factory`| 0-parameter function used to produce a default | `_MISSING_TYPE`                         |
| `init`          | Include field in parameters to `__init__`  | `True`                                  |
| `repr`          | Include field in `__repr__`                | `True`                                  |
| `compare`       | Use field in comparison methods `__eq__`, `__lt__`, etc. | `True`                                  |
| `hash`          | Include field in `__hash__` calculation    | `None` (used in `__hash__` only if `compare=True`) |
| `metadata`      | Mapping with user-defined data; ignored by the `@dataclass` | `None`                                  |

> **Note**: `dataclass._MISSING_TYPE` is a sentinel value indicating the option was not provided. It exists so we can set `None` as an actual default value, a common use case.
## Example: Using field Function
```python
from dataclasses import dataclass, field
from typing import Any, Dict

@dataclass
class ClubMember:
    name: str
    guests: list = field(default_factory=list)

@dataclass
class ExampleDataClass:
    # Non-default argument
    unique_id: int

    # default: Provide a default value for the field
    name: str = "Unknown"

    # default_factory: Provide a function to generate a default value for the field
    ids: Dict[int, str] = field(default_factory=dict)

    # init: Exclude this field from the __init__ method parameters
    computed_value: int = field(init=False, default=42)

    # repr: Exclude this field from the __repr__ method
    password: str = field(repr=False, default="1234")

    # compare: Exclude this field from comparison methods (__eq__, __lt__, etc.)
    secret_code: str = field(compare=False, default="SECRET")

    # hash: Include this field in the __hash__ method calculation
    unique_id: int = field(hash=True)

    # metadata: Attach additional information to the field (ignored by the dataclass itself)
    description: str = field(default="No description", metadata={"info": "This is a description field"})

    def __post_init__(self):
        # computed_value is not included in __init__, so we can compute it after initialization
        self.computed_value = len(self.name) * 10

# Example usage
example = ExampleDataClass(unique_id=123)
print(example)  # __repr__ method output
print(example.name)  # Output: Unknown
print(example.ids)  # Output: {}
print(example.computed_value)  # Output: 70 (computed in __post_init__)
print(example.password)  # Not displayed in __repr__
print(example.secret_code)  # Output: SECRET
print(example.unique_id)  # Output: 123
print(example.description)  # Output: No description
print(example.__dataclass_fields__["description"].metadata)  # Output: {'info': 'This is a description field'}

# Comparison example
example2 = ExampleDataClass(unique_id=123, name="Different")
print(example == example2)  # Output: True (secret_code is excluded from comparison)
print(hash(example))  # Hash value includes unique_id
```

### Detailed Explanation

### Fields and Parameters in `ExampleDataClass`

1. **unique_id: int**
   - **Position**: Non-default argument, placed before all default arguments.
   - **Purpose**: Unique identifier for each instance. Included in hash calculations due to `field(hash=True)`.

2. **name: str = "Unknown"**
   - **default**: Provides a default value "Unknown" for the `name` field.

3. **ids: Dict[int, str] = field(default_factory=dict)**
   - **default_factory**: Generates a new dictionary for each instance, preventing shared default values.

4. **computed_value: int = field(init=False, default=42)**
   - **init**: Excludes `computed_value` from the `__init__` method parameters. The value is computed after initialization in `__post_init__`.

5. **password: str = field(repr=False, default="1234")**
   - **repr**: Excludes `password` from the `__repr__` method output for security reasons.

6. **secret_code: str = field(compare=False, default="SECRET")**
   - **compare**: Excludes `secret_code` from comparison methods (`__eq__`, `__lt__`, etc.).

7. **description: str = field(default="No description", metadata={"info": "This is a description field"})**
   - **metadata**: Attaches additional information to the `description` field, which can be accessed using the `__dataclass_fields__` attribute.

### `__post_init__` Method
The `__post_init__` method is called after the `__init__` method. It is useful for performing additional initialization that depends on the values of other fields.

In this example, `__post_init__` computes the `computed_value` based on the length of the `name`:

```python
def __post_init__(self):
    self.computed_value = len(self.name) * 10
```

### Example Usage
```python
example = ExampleDataClass(unique_id=123)
print(example)  # __repr__ method output
```

This prints the `__repr__` output of the `example` instance. Fields excluded from `__repr__` (like `password`) are not displayed.

```python
print(example.name)  # Output: Unknown
print(example.ids)  # Output: {}
print(example.computed_value)  # Output: 70 (computed in __post_init__)
print(example.password)  # Not displayed in __repr__
print(example.secret_code)  # Output: SECRET
print(example.unique_id)  # Output: 123
print(example.description)  # Output: No description
print(example.__dataclass_fields__["description"].metadata)  # Output: {'info': 'This is a description field'}
```

These lines print the values of various fields, demonstrating how default values, `default_factory`, and computed values work.

### Comparison Example
```python
example2 = ExampleDataClass(unique_id=123, name="Different")
print(example == example2)  # Output: True (secret_code is excluded from comparison)
print(hash(example))  # Hash value includes unique_id
```

- **Comparison**: `example` and `example2` are considered equal because `secret_code` is excluded from comparison.
- **Hash**: The hash value includes the `unique_id` field, making the instances hashable and allowing them to be used in hash-based collections like sets and dictionaries.

### Summary
- **Order of Fields**: Non-default fields must come before default fields to avoid `TypeError`.
- **Mutable Defaults**: Use `default_factory` to prevent shared default values.
- **Customization**: Various field options (`init`, `repr`, `compare`, `hash`, `metadata`) allow customization of field behavior.
- **Post Initialization**: Use `__post_init__` for additional initialization.

## Conclusion
- Field options in `@dataclass` provide powerful customization for default values and how fields are handled.
- Using `default_factory` is essential for mutable default values to avoid common bugs.
- The `field` function offers multiple options for customizing field behavior, such as including fields in `__init__`, `__repr__`, comparisons, and hash calculations.
- Generic types in field annotations allow for more precise type checking.



For more detailed information, refer to the [dataclass documentation](https://docs.python.org/3/library/dataclasses.html).

