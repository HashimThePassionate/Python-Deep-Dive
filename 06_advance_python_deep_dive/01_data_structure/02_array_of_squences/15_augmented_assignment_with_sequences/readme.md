# Augmented Assignment with Sequences

The augmented assignment operators `+=` and `*=` behave differently depending on the first operand. This document will focus on augmented addition (`+=`), but the concepts also apply to `*=` and other augmented assignment operators.

## In-Place Addition with `+=`

### How It Works
The special method that makes `+=` work is `__iadd__` (for "in-place addition"). If `__iadd__` is not implemented, Python falls back to calling `__add__`. Consider the following expression:
```python
a += b
```

### Scenarios
1. **If `a` Implements `__iadd__`:**
   - `__iadd__` is called.
   - For mutable sequences (e.g., list, bytearray, array.array), `a` is changed in place (similar to `a.extend(b)`).
   - The identity of `a` remains the same.

2. **If `a` Does Not Implement `__iadd__`:**
   - The expression `a += b` behaves like `a = a + b`.
   - A new object is created by evaluating `a + b` and is then bound to `a`.
   - The identity of `a` changes.

### General Rule
- For mutable sequences, `__iadd__` is usually implemented, and `+=` modifies the sequence in place.
- For immutable sequences, there is no way for in-place modification to happen.

### Example with Lists and Tuples

#### Mutable Sequence (List)
```python
l = [1, 2, 3]
print(id(l))  # Output: ID of the initial list

l *= 2
print(l)  # Output: [1, 2, 3, 1, 2, 3]
print(id(l))  # Output: Same ID as initial list
```
- **Explanation:** The list `l` is modified in place, and the identity remains the same.

#### Immutable Sequence (Tuple)
```python
t = (1, 2, 3)
print(id(t))  # Output: ID of the initial tuple

t *= 2
print(t)  # Output: (1, 2, 3, 1, 2, 3)
print(id(t))  # Output: Different ID from initial tuple
```
- **Explanation:** A new tuple is created, and the identity of `t` changes.

## Efficiency Considerations

- Repeated concatenation of immutable sequences is inefficient because the interpreter has to copy the entire target sequence to create a new one with the new items concatenated.
- **Note:** Strings (`str`) are an exception. CPython is optimized for string concatenation in loops by allocating memory with extra room to avoid copying the entire string each time.

## Summary

- `+=` and `*=` operators have different behaviors based on whether the sequence is mutable or immutable.
- Mutable sequences usually implement `__iadd__`, allowing in-place modification.
- Immutable sequences do not allow in-place modification, leading to the creation of new objects.
- Understanding these behaviors helps avoid unintended side effects and inefficiencies in your code.
