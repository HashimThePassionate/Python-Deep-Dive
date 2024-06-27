# Assigning to Slices

Mutable sequences can be modified in place using slice notation on the left-hand side of an assignment statement or as the target of a `del` statement. The following examples demonstrate the power of this notation:

## Examples

### Initial List
```python
l = list(range(10))
print(l)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### Modify a Slice
Replace elements from index 2 to 4 with `[20, 30]`:
```python
l[2:5] = [20, 30]
print(l)  # Output: [0, 1, 20, 30, 5, 6, 7, 8, 9]
```

### Delete a Slice
Remove elements from index 5 to 6:
```python
del l[5:7]
print(l)  # Output: [0, 1, 20, 30, 5, 8, 9]
```

### Modify with Step
Replace every second element starting from index 3:
```python
l[3::2] = [11, 22]
print(l)  # Output: [0, 1, 20, 11, 5, 22, 9]
```

### Incorrect Assignment
Attempting to assign a single integer value results in an error:
```python
try:
    l[2:5] = 100
except TypeError as e:
    print(e)  # Output: can only assign an iterable
```

### Correct Assignment
Assign a list with a single integer value:
```python
l[2:5] = [100]
print(l)  # Output: [0, 1, 100, 22, 9]
```

When the target of the assignment is a slice, the right-hand side must be an iterable object, even if it has just one item.