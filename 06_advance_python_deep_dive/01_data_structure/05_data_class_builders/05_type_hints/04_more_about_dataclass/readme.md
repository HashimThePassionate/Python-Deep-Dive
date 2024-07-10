# More About `@dataclass`

## Introduction
We have seen simple examples of using `@dataclass`. The decorator accepts several keyword arguments that allow for more customization. The signature of `@dataclass` is:

```python
@dataclass(*, init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False)
```

The `*` in the first position means the remaining parameters are keyword-only. The following sections describe these parameters and provide examples.

## Keyword Parameters Accepted by the `@dataclass` Decorator
| Option       | Meaning                         | Default | Notes                                                                                                           |
|--------------|---------------------------------|---------|-----------------------------------------------------------------------------------------------------------------|
| `init`       | Generate `__init__`             | `True`  | Ignored if `__init__` is implemented by the user.                                                               |
| `repr`       | Generate `__repr__`             | `True`  | Ignored if `__repr__` is implemented by the user.                                                               |
| `eq`         | Generate `__eq__`               | `True`  | Ignored if `__eq__` is implemented by the user.                                                                 |
| `order`      | Generate `__lt__`, `__le__`, `__gt__`, `__ge__` | `False` | If `True`, raises exceptions if `eq=False`, or if any of the comparison methods that would be generated are defined or inherited. |
| `unsafe_hash`| Generate `__hash__`             | `False` | Complex semantics and several caveats—see: dataclass documentation.                                             |
| `frozen`     | Make instances “immutable”      | `False` | Instances will be reasonably safe from accidental change, but not really immutable.                             |

> **Note**: `@dataclass` emulates immutability by generating `__setattr__` and `__delattr__`, which raise `dataclass.FrozenInstanceError`—a subclass of `AttributeError`—when the user attempts to set or delete a field.

## Default Settings
The default settings are useful for most common use cases. However, there are options you might want to change:

- **`frozen=True`**: Protects against accidental changes to class instances.
- **`order=True`**: Allows sorting of instances of the data class.

## Notes on `frozen` and `hash`
Given the dynamic nature of Python objects, a nosy programmer can bypass the protection afforded by `frozen=True`. However, such actions are easy to spot in a code review.

If both `eq` and `frozen` are `True`, `@dataclass` produces a suitable `__hash__`  [See Hash Example](./00_hash/readme.md) method, making the instances hashable. The generated `__hash__` will use data from all fields that are not individually excluded. If `frozen=False` (the default), `@dataclass` sets `__hash__` to `None`, signaling that the instances are unhashable, overriding `__hash__` from any superclass.

## Unsafe Hash
PEP 557—Data Classes states:

> Although not recommended, you can force Data Classes to create a `__hash__` method with `unsafe_hash=True`. This might be necessary if your class is logically immutable but can still be mutated. This is a specialized use case and should be considered carefully.

Use `unsafe_hash` cautiously. For more information, refer to the [dataclass documentation](https://docs.python.org/3/library/dataclasses.html).

## Customization at the Field Level
Further customization of the generated data class can be done at a field level.

## Examples

### Example: Custom `__init__`
By default, `@dataclass` generates an `__init__` method. If you implement your own `__init__`, it will be ignored.

```python
from dataclasses import dataclass

@dataclass(init=False)
class Person:
    name: str
    age: int

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

p = Person("Hashim", 30)
print(p)
```

**Explanation**:
- The `Person` class is defined with `init=False`, so `@dataclass` does not generate an `__init__` method.
- The custom `__init__` method is used to initialize the `Person` instance.
- Output: `Person(name='Hashim', age=30)`

### Example: Custom `__repr__`
By default, `@dataclass` generates a `__repr__` method. If you implement your own `__repr__`, it will be ignored.

```python
from dataclasses import dataclass

@dataclass(repr=False)
class Person:
    name: str
    age: int

    def __repr__(self):
        return f"Person({self.name}, {self.age})"

p = Person("Hashim", 30)
print(p)
```

**Explanation**:
- The `Person` class is defined with `repr=False`, so `@dataclass` does not generate a `__repr__` method.
- The custom `__repr__` method is used to represent the `Person` instance.
- Output: `Person(Hashim, 30)`

### Example: Custom `__eq__`
By default, `@dataclass` generates an `__eq__` method. If you implement your own `__eq__`, it will be ignored.

```python
from dataclasses import dataclass

@dataclass(eq=False)
class Person:
    name: str
    age: int

    def __eq__(self, other):
        return self.name == other.name

p1 = Person("Hashim", 30)
p2 = Person("Hashim", 25)
print(p1 == p2)
```

**Explanation**:
- The `Person` class is defined with `eq=False`, so `@dataclass` does not generate an `__eq__` method.
- The custom `__eq__` method compares `Person` instances based on the `name` attribute.
- Output: `True` (since `p1` and `p2` have the same name)

### Example: Ordering
You can enable ordering of instances by setting `order=True`. This generates methods like `__lt__`, `__le__`, `__gt__`, and `__ge__`.

```python
from dataclasses import dataclass

@dataclass(order=True)
class Person:
    name: str
    age: int

p1 = Person("Hashim", 30)
p2 = Person("Ali", 25)
print(p1 > p2)
```

**Explanation**:
- The `Person` class is defined with `order=True`, so `@dataclass` generates comparison methods.
- Instances of `Person` can be compared based on the fields in the order they are defined.
- Output: `True` (since "Hashim" > "Ali" alphabetically)

### Example: Unsafe Hash
You can force `@dataclass` to create a `__hash__` method with `unsafe_hash=True`.

```python
from dataclasses import dataclass

@dataclass(unsafe_hash=True)
class Person:
    name: str
    age: int

p = Person("Hashim", 30)
print(hash(p))
```

**Explanation**:
- The `Person` class is defined with `unsafe_hash=True`, so `@dataclass` generates a `__hash__` method.
- The `Person` instance `p` can be hashed, allowing it to be used in hash-based collections like sets and dictionaries.
- Output: The hash value of `p` (a unique integer)

### Example: Frozen Instances
Setting `frozen=True` makes instances of the data class immutable.

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Person:
    name: str
    age: int

p = Person("Hashim", 30)
try:
    p.name = "Ali"
except FrozenInstanceError as e:
    print(e)
```

**Explanation**:
- The `Person` class is defined with `frozen=True`, making its instances immutable.
- Attempting to modify the `name` attribute of the `Person` instance `p` raises a `FrozenInstanceError`.
- Output: `cannot assign to field 'name'`

## Conclusion
- The `@dataclass` decorator in Python provides a convenient way to create data classes with various customization options.
- Default settings cover common use cases, but options like `frozen=True` and `order=True` offer additional functionality.
- Custom methods can override the generated ones unless specified otherwise.
- Careful consideration is needed when using options like `unsafe_hash`.

For more detailed information, refer to the [dataclass documentation](https://docs.python.org/3/library/dataclasses.html).
