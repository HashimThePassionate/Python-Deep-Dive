# Types Usable in Annotations

## Introduction
In Python, you can use many types in type hints to indicate the expected type of a variable, function argument, or return value. However, there are some restrictions and recommendations to follow. Additionally, the `typing` module introduces special constructs that might have surprising semantics.

This section covers the major types you can use with annotations:

- `typing.Any`
- `Simple types and classes`
- `typing.Optional` and `typing.Union`
- `Generic collections`, including `tuples` and `mappings`
- `Abstract base classes`
- `Generic iterables`
- `Parameterized generics` and `TypeVar`
- `typing.Protocols`—the key to static duck typing
- `typing.Callable`
- `typing.NoReturn`—a good way to end this list

We’ll cover each of these in turn, starting with a type that is strange, apparently useless, but crucially important.

