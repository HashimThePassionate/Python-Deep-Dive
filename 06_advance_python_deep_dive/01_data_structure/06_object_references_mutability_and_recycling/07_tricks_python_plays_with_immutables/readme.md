# Tricks Python Plays with Immutables

## Introduction

This section discusses some Python details that are not critical for everyday Python use but can be interesting to know. These details may not apply to other Python implementations or future versions of CPython. However, understanding these corner cases can prevent misuse of the `is` operator.

## Tuples and Immutability

### Copying Tuples

Surprisingly, for a tuple `t`, `t[:]` does not create a copy but returns a reference to the same object. Similarly, using `tuple(t)` also returns a reference to the same tuple.

### Example

```python
t1 = (1, 2, 3)
t2 = tuple(t1)
print(t2 is t1)  # Output: True

t3 = t1[:]
print(t3 is t1)  # Output: True
```

- **Binding**: `t1` and `t2` are bound to the same object.
- **Slicing**: `t3` is also the same object as `t1`.

### Other Immutables

The same behavior can be observed with instances of `str`, `bytes`, and `frozenset`. Note that a `frozenset` is not a sequence, so `fs[:]` does not work if `fs` is a `frozenset`. However, `fs.copy()` behaves similarly, returning a reference to the same object rather than creating a copy.

### Example with frozenset

```python
fs1 = frozenset([1, 2, 3])
fs2 = fs1.copy()
print(fs2 is fs1)  # Output: True
```

### String Literals

String literals may create shared objects through a process called interning, an optimization technique. CPython uses interning for small integers as well, such as 0, 1, -1, etc.

### Example with Strings and Integers

```python
s1 = 'ABC'
s2 = 'ABC'
print(s2 is s1)  # Output: True

i1 = 100
i2 = 100
print(i2 is i1)  # Output: True
```

- **Interning**: `s1` and `s2` refer to the same string object due to interning.
- **Small Integers**: Similar interning happens with small integers.

## Best Practices

### Using == Instead of is

- **Comparison**: Always use `==` to compare strings or integers for equality, not `is`. Interning is an internal optimization and should not be relied upon for program logic.

### Harmless "Lies"

- **Memory and Speed**: The tricks discussed, such as the behavior of `frozenset.copy()`, save memory and make the interpreter faster. These behaviors are harmless because they only apply to immutable types.

## Conclusion

Understanding these Python quirks can help you avoid unexpected behavior and misuse of the `is` operator. These details are more of trivia and do not impact the general use of Python. They can be fun facts to share with fellow Python enthusiasts.
!