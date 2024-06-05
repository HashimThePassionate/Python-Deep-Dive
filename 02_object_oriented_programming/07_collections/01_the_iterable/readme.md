
# The Iterable

1. **Define the `GenericList` Class:**
   - The `GenericList` class has an initializer (`__init__`) that initializes an empty list `items` and a count `count` set to 0.
   - It provides an `add` method to add items to the list and increment the count.
   - It provides a `get` method to retrieve an item by its index.

2. **Implement the `__iter__` Method:**
   - The `__iter__` method is defined in the `GenericList` class to return an iterator object. In this case, it returns an instance of the nested `ListIterator` class, passing the current `GenericList` instance to it.

3. **Define the `ListIterator` Class:**
   - The `ListIterator` class is nested within the `GenericList` class. It is responsible for implementing the iterator protocol.
   - The `__init__` method of `ListIterator` takes a `GenericList` instance and initializes an index `_index` to 0.
   - The `__iter__` method of `ListIterator` returns `self`, indicating that the iterator object is also iterable.
   - The `__next__` method of `ListIterator` checks if the current index `_index` is less than the count of items in the `GenericList`. If so, it retrieves the item at the current index, increments the index, and returns the item. If the index is out of bounds, it raises a `StopIteration` exception to signal the end of the iteration.

4. **Usage Example:**
   - An instance of `GenericList` is created and two items ("Muhammad" and "Hashim") are added to it.
   - A for loop is used to iterate over the `GenericList` instance. This loop internally calls the `__iter__` method to get the iterator and then repeatedly calls the `__next__` method to get each item until a `StopIteration` exception is raised.

Here's the full code with some comments to highlight the important parts:

```python
class GenericList:
    def __init__(self):
        self.items = []
        self.count = 0

    def add(self, item):
        self.items.append(item)
        self.count += 1

    def get(self, index):
        return self.items[index]

    # This method returns an iterator object
    def __iter__(self):
        return self.ListIterator(self)

    # Nested class implementing the iterator protocol
    class ListIterator:
        def __init__(self, generic_list):
            self._generic_list = generic_list
            self._index = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self._index < self._generic_list.count:
                item = self._generic_list.items[self._index]
                self._index += 1
                return item
            else:
                raise StopIteration

# Create an instance of GenericList
list = GenericList()
list.add('Muhammad')
list.add('Hashim')

# Iterate over the list
for item in list:
    print(item)
```

Output:
```
Muhammad
Hashim
```

In summary, the iterator behavior is achieved by defining the `__iter__` and `__next__` methods within the nested `ListIterator` class, and making sure the `GenericList` class returns an instance of this iterator class when its `__iter__` method is called.