# Understanding Names and Objects

This chapter delves into the distinction between objects and their names in Python. It explores the concept that a name is not the object itself but a separate entity. Here's a breakdown of what we'll cover:

## Table of Contents
1. **Introduction**
2. **Variables as Labels, Not Boxes**
3. **Object Identity, Value, and Aliasing**
4. **Immutability and Mutable Values in Tuples**
5. **Shallow and Deep Copies**
6. **References and Function Parameters**
7. **Garbage Collection and the `del` Command**
8. **Tricks with Immutable Objects**

## 1. Introduction
The chapter starts with a metaphor illustrating that variables in Python are like labels, not containers. This metaphor helps explain the concept of aliasing, where multiple names refer to the same object.

## 2. Variables as Labels, Not Boxes
In Python, variables act as labels that point to objects, rather than boxes that contain objects. This analogy is useful for understanding how Python handles references and memory management.

### Example:
```python
a = [1, 2, 3]
b = a  # Both a and b reference the same list object
b.append(4)
print(a)  # Output: [1, 2, 3, 4]
```

## 3. Object Identity, Value, and Aliasing
We discuss the concepts of object identity (`id()`), value, and aliasing. Understanding these concepts is crucial for managing objects and references in Python.

### Example:
```python
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)  # Output: True (values are equal)
print(x is y)  # Output: False (different objects)
```

## 4. Immutability and Mutable Values in Tuples
Tuples are immutable, meaning their structure cannot be changed. However, they can contain mutable objects, leading to potentially unexpected behavior.

### Example:
```python
t = ([1, 2], 3)
t[0].append(4)
print(t)  # Output: ([1, 2, 3, 4], 3)
```

## 5. Shallow and Deep Copies
We explain the difference between shallow and deep copies, which is important when duplicating complex objects.

### Example:
```python
import copy

original = [1, [2, 3], 4]
shallow_copy = copy.copy(original)
deep_copy = copy.deepcopy(original)

original[1].append(5)
print(shallow_copy)  # Output: [1, [2, 3, 5], 4]
print(deep_copy)     # Output: [1, [2, 3], 4]
```

## 6. References and Function Parameters
This section covers how Python handles references with function parameters, focusing on mutable default arguments and safe handling of mutable arguments.

### Example:
```python
def append_to_list(value, my_list=[]):
    my_list.append(value)
    return my_list

print(append_to_list(1))  # Output: [1]
print(append_to_list(2))  # Output: [1, 2] (unexpected)

# Correct way:
def append_to_list(value, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(value)
    return my_list

print(append_to_list(1))  # Output: [1]
print(append_to_list(2))  # Output: [2]
```

## 7. Garbage Collection and the `del` Command
We discuss Python's garbage collection mechanism and the use of the `del` command to manage memory.

### Example:
```python
import gc

a = [1, 2, 3]
b = a
del a  # a is deleted but b still references the list
gc.collect()  # Forces garbage collection
print(b)  # Output: [1, 2, 3]
```

## 8. Tricks with Immutable Objects
The chapter concludes with a selection of interesting tricks and behaviors Python exhibits with immutable objects.

### Example:
```python
a = 256
b = 256
print(a is b)  # Output: True (small integers are cached)

a = 257
b = 257
print(a is b)  # Output: False (larger integers are not cached)
```