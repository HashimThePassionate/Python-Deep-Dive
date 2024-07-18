# Additional Information

## Object Identities and Values

The **[Data Model](https://docs.python.org/3/reference/datamodel.html)** chapter of The Python Language Reference provides a clear explanation of object identities and values.

### Recommended Resources

1. **Wesley Chun**: Presented **[Understanding Python’s Memory Model, Mutability, and Methods](https://www.youtube.com/watch?v=HHFCFJSPWrI&ab_channel=EuroPythonConference)** at EuroPython 2011, covering the themes of this chapter and the use of special methods.
2. **Doug Hellmann**: Wrote the posts **[copy – Duplicate Objects](https://pymotw.com/3/copy/)** and **[weakref—Garbage Collectable References to Objects](https://pymotw.com/3/weakref/)** covering some of the topics discussed.
3. **gc Module Documentation**: Provides information on the CPython generational garbage collector and starts with the sentence **[This module provides an interface to the optional garbage collector](https://docs.python.org/3/library/gc.html)**

## Garbage Collection in CPython

### Implementation Quality

The “Data Model” chapter states:
> An implementation is allowed to postpone garbage collection or omit it altogether—it is a matter of implementation quality how garbage collection is implemented, as long as no objects are collected that are still reachable.

### In-Depth Reading

- **Pablo Galindo**: Wrote **[Design of CPython’s Garbage Collector](https://devguide.python.org/internals/garbage-collector/index.html)** in the Python Developer’s Guide, aimed at new and experienced contributors to the CPython implementation.
- **PEP 442**: Describes improvements in handling objects with a `__del__` method in CPython 3.4.
- **Wikipedia**: Has articles on string interning and the Lewis Carroll song “Haddocks’ Eyes,” which is used to discuss the symbolic status of names.

## Equal Treatment to All Objects

### Java vs. Python

- **Equality in Java**: The `==` operator in Java compares references, not object values. For object comparison, Java uses the `.equals` method, which can lead to null pointer exceptions.
- **Equality in Python**: The `==` operator compares object values, while `is` compares references. Python's operator overloading makes `==` work sensibly with all objects in the standard library, including `None`.

### Custom Equality

You can define `__eq__` in your own classes to decide what `==` means for your instances. If you don’t override `__eq__`, the method inherited from `object` compares object IDs.

## Mutability

### Immutability and Functional Programming

- **Pure Functional Programming**: In languages like Elixir, all data is immutable, meaning appending to a collection creates a new collection.
- **Python**: Is not a pure functional language, and instances of user-defined classes are mutable by default.

### Thread Safety

Mutable objects are a primary reason why programming with threads is challenging. Threads mutating objects without proper synchronization can produce corrupted data, while excessive synchronization can cause deadlocks.

## Object Destruction and Garbage Collection

### No Direct Destruction

There is no mechanism in Python to directly destroy an object. Garbage collection in CPython is primarily done by reference counting, which immediately disposes of objects with zero references.

### Generational Garbage Collector

Introduced in CPython 2.0, it handles unreachable objects kept alive by reference cycles.

### Safe File Handling

In CPython, the reference count of a file object will be zero after its write method returns, allowing Python to close the file immediately. However, using the `with` statement is the best practice for file handling.

```python
with open('test.txt', 'wt', encoding='utf-8') as fp:
    fp.write('1, 2, 3')
```

## Parameter Passing: Call by Sharing

### Explanation

In Python, parameters are passed by value, but the values are references. The function gets a copy of the references, allowing modification of the referenced objects if they are mutable. However, rebinding the references within the function has no effect outside the function.

