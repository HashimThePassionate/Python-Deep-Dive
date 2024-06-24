### Why len is not a method?

The question "Why `len` is not a method?" addresses why `len` in Python is implemented as a built-in function rather than as a method of an object. The response draws from "The Zen of Python," a set of aphorisms that capture the philosophy of Python. The key point is practicality over purity: Python is designed to be practical and efficient, sometimes at the cost of strict adherence to object-oriented purity.

#### Key Points

1. **Efficiency**:
    - For built-in types in CPython (the standard implementation of Python), `len(x)` is implemented very efficiently. It directly reads the length from a field in a C struct without calling a method.
    - This ensures that the length calculation for common operations on types like `str`, `list`, and `memoryview` is extremely fast.

2. **Special Treatment**:
    - `len` is given special treatment as part of the Python Data Model, similar to other built-in functions like `abs`.
    - This special treatment allows `len` to operate very efficiently on built-in types.

3. **Consistency with Custom Objects**:
    - Despite its special treatment for efficiency, Python provides a way to make `len` work with custom objects using the special method `__len__`.
    - This ensures that user-defined objects can integrate seamlessly with Python's built-in functions, maintaining consistency across the language.

4. **Practicality Over Purity**:
    - The design choice reflects the principle from "The Zen of Python": "practicality beats purity." This means Python favors practical solutions that work well in common scenarios over strict adherence to theoretical principles.
    - Another principle from "The Zen of Python": "Special cases aren’t special enough to break the rules," indicates that while `len` is special-cased for efficiency, the language still provides a consistent and predictable way to extend its functionality to user-defined types.

### Example

Let's illustrate how `len` works with both built-in types and custom objects.

#### Built-In Types

For built-in types like `list` and `str`, `len` operates very efficiently:

```python
my_list = [1, 2, 3, 4, 5]
print(len(my_list))  # Output: 5

my_string = "Hello, World!"
print(len(my_string))  # Output: 13
```

For these built-in types, `len` reads the length directly from an internal field without calling a method, making it very fast.

#### Custom Objects

For custom objects, you can define the `__len__` method to make `len` work with your objects:

```python
class MyCollection:
    def __init__(self, items):
        self.items = items
    
    def __len__(self):
        return len(self.items)

# Example usage
my_collection = MyCollection([1, 2, 3, 4, 5])
print(len(my_collection))  # Output: 5
```

In this example:
- `MyCollection` is a custom class that implements the `__len__` method.
- When `len(my_collection)` is called, it internally calls the `__len__` method defined in `MyCollection`, returning the length of the `items` list.

### Summary

- `len` is implemented as a built-in function for efficiency, allowing it to quickly get the length of built-in types by directly accessing internal fields.
- To maintain consistency, Python allows custom objects to support `len` by implementing the `__len__` method.
- This design choice exemplifies Python's philosophy of favoring practical solutions that work well for common cases, even if it means deviating from pure object-oriented principles.