# Container Methods

In Python, container methods are special methods that provide container functionality, enabling objects to behave like containers such as lists, dictionaries, or sets. These methods allow for indexing, assignment, deletion, iteration, and membership testing. Below is a detailed explanation of each container method followed by a practical example.

#### __contains__(self, item)
- **Purpose**: Checks if a given item is present in the container.
- **Usage**: `item in container`
- **Returns**: `True` if the item is present, otherwise `False`.

When this method is implemented, it should return `True` if the item is found in the container. If not implemented, Python falls back to iterating through the container and checking each item for equality, which is less efficient.

#### __delitem__(self, key)
- **Purpose**: Deletes an item or slice from the container.
- **Usage**: `del container[key]`

This method is called when an item or slice is deleted from the container. It should be implemented only if the container is mutable.

#### __getitem__(self, key)
- **Purpose**: Retrieves an item or slice from the container.
- **Usage**: `container[key]`

This method is used to access an item or slice from the container. It is essential for all non-set-like containers.

#### __iter__(self)
- **Purpose**: Returns an iterator for the container.
- **Usage**: `iter(container)` or `for item in container`

This method returns an iterator that allows looping over the container's items. Implementing this method is highly recommended for all container classes.

#### __len__(self)
- **Purpose**: Returns the number of items in the container.
- **Usage**: `len(container)`

This method should return the total number of items in the container. It is also used to evaluate the container in a Boolean context, where the container is considered `False` if it is empty.

#### __setitem__(self, key, value)
- **Purpose**: Assigns a value to an item or slice in the container.
- **Usage**: `container[key] = value`

This method binds a value to a specific key in the container. It should be implemented only if the container is mutable.

### Practical Example

Let's create a custom container class, `CustomList`, which will implement these container methods. This class will mimic the behavior of a list.

```python
class CustomList:
    def __init__(self, *args):
        self._data = list(args)
    
    def __contains__(self, item):
        return item in self._data
    
    def __delitem__(self, index):
        del self._data[index]
    
    def __getitem__(self, index):
        return self._data[index]
    
    def __iter__(self):
        return iter(self._data)
    
    def __len__(self):
        return len(self._data)
    
    def __setitem__(self, index, value):
        self._data[index] = value
    
    def __repr__(self):
        return repr(self._data)

# Creating an instance of CustomList
clist = CustomList(1, 2, 3, 4, 5)

# Testing __contains__
print(3 in clist)  # Output: True
print(6 in clist)  # Output: False

# Testing __delitem__
del clist[1]
print(clist)  # Output: [1, 3, 4, 5]

# Testing __getitem__
print(clist[2])  # Output: 4

# Testing __iter__
for item in clist:
    print(item, end=' ')  # Output: 1 3 4 5
print()

# Testing __len__
print(len(clist))  # Output: 4

# Testing __setitem__
clist[1] = 10
print(clist)  # Output: [1, 10, 4, 5]
```

### Explanation

1. **Initialization**: `CustomList` is initialized with any number of elements, stored in a list called `_data`.
2. **Containment Check**: The `__contains__` method checks if an item exists in `_data`.
3. **Item Deletion**: The `__delitem__` method deletes an item at a specified index.
4. **Item Access**: The `__getitem__` method retrieves an item at a specified index.
5. **Iteration**: The `__iter__` method returns an iterator for `_data`.
6. **Length**: The `__len__` method returns the number of items in `_data`.
7. **Item Assignment**: The `__setitem__` method assigns a value to an item at a specified index.

---

