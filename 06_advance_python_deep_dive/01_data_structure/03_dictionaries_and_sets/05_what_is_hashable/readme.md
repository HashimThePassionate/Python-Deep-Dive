# What Is Hashable
An object is hashable if it has a hash code which never changes during its lifetime (it needs a `__hash__()` method), and can be compared to other objects (it needs an `__eq__()` method). Hashable objects which compare equal must have the same hash code.

### Key Points
- **Hash Code**: An object needs a `__hash__()` method that provides a hash code.
- **Equality Comparison**: An object needs an `__eq__()` method to compare it to other objects.
- **Consistency**: Hashable objects which compare equal must have the same hash code.

### Hashable Types
- **Numeric Types**: All numeric types are hashable.
- **Flat Immutable Types**: `str` and `bytes` are hashable.
- **Container Types**: These are hashable if they are immutable and all contained objects are also hashable.
  - **frozenset**: Always hashable because every element it contains must be hashable.
  - **tuple**: Hashable only if all its items are hashable.

### Example: Hashing Tuples
```python
tt = (1, 2, (30, 40))
print(hash(tt))  # Output: 8027212646858338501

tl = (1, 2, [30, 40])
print(hash(tl))  # Output: TypeError: unhashable type: 'list'

tf = (1, 2, frozenset([30, 40]))
print(hash(tf))  # Output: -4118419923444501110
```

### Explanation
- **Immutable Items**: `tt` is hashable because it contains only immutable items.
- **Mutable Items**: `tl` is not hashable because it contains a list, which is mutable.
- **frozenset**: `tf` is hashable because it contains a `frozenset`, which is immutable.

## Hash Code Consistency

The hash code of an object may be different depending on the version of Python, the machine architecture, and because of a salt added to the hash computation for security reasons. The hash code of a correctly implemented object is guaranteed to be constant only within one Python process.

### User-Defined Types
User-defined types are hashable by default because their hash code is their `id()`, and the `__eq__()` method inherited from the `object` class simply compares the object IDs. If an object implements a custom `__eq__()` that takes into account its internal state, it will be hashable only if its `__hash__()` always returns the same hash code.

### Best Practices
To ensure that a user-defined object is hashable:
- Implement a `__hash__()` method that returns the same hash code as long as the object's state does not change.
- Ensure that `__eq__()` and `__hash__()` methods only take into account instance attributes that never change during the life of the object.

## Example: Custom Hashable Class
```python
class MyClass:
    def __init__(self, value):
        self.value = value
    
    def __eq__(self, other):
        if isinstance(other, MyClass):
            return self.value == other.value
        return False

    def __hash__(self):
        return hash(self.value)

# Instances of MyClass are hashable
obj1 = MyClass(10)
obj2 = MyClass(10)
print(hash(obj1))  # Output: hash value based on the value attribute
print(hash(obj2))  # Output: same hash value as obj1 if value is the same
print(obj1 == obj2)  # Output: True if value attributes are equal
```

## Summary
- **Hashable**: An object is hashable if it has a `__hash__()` method and an `__eq__()` method, and its hash code does not change during its lifetime.
- **Immutable Types**: Numeric types, `str`, `bytes`, and immutable containers like `frozenset` and `tuple` (with hashable items) are hashable.
- **User-Defined Types**: Default to being hashable via `id()`. Custom `__eq__()` and `__hash__()` implementations must ensure the hash code remains consistent.
