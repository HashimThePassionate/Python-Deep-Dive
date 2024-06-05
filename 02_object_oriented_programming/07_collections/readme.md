# Collection module
**collection module** generally refers to a set of built-in data structures that allow you to store and manipulate collections of items. These data structures are highly optimized and provide a range of functionalities to handle different types of collections. Here are the primary components of the collection module   in Python:

1. **Lists**: Ordered and mutable collections of items. They can hold heterogeneous items (i.e., items of different types).
   ```python
   my_list = [1, 2, 3, 'a', 'b', 'c']
   ```

2. **Tuples**: Ordered and immutable collections of items. Once created, the items in a tuple cannot be changed.
   ```python
   my_tuple = (1, 2, 3, 'a', 'b', 'c')
   ```

3. **Sets**: Unordered collections of unique items. Sets are mutable and can be used to perform mathematical set operations like union, intersection, and difference.
   ```python
   my_set = {1, 2, 3, 'a', 'b', 'c'}
   ```

4. **Dictionaries**: Unordered collections of key-value pairs. Dictionaries are mutable and allow for fast retrieval of values based on their keys.
   ```python
   my_dict = {'key1': 'value1', 'key2': 'value2'}
   ```

In addition to these basic types, Python's `collections` module provides specialized data structures that are alternatives to the above:

1. **namedtuple()**: Factory function for creating tuple subclasses with named fields.
   ```python
   from collections import namedtuple
   Point = namedtuple('Point', ['x', 'y'])
   p = Point(1, 2)
   ```

2. **deque**: List-like container with fast appends and pops on either end.
   ```python
   from collections import deque
   d = deque([1, 2, 3])
   d.appendleft(0)
   ```

3. **Counter**: Dictionary subclass for counting hashable items.
   ```python
   from collections import Counter
   count = Counter(['a', 'b', 'a', 'c', 'b', 'a'])
   ```

4. **OrderedDict**: Dictionary subclass that remembers the order in which its contents are added.
   ```python
   from collections import OrderedDict
   od = OrderedDict()
   od['one'] = 1
   od['two'] = 2
   ```

5. **defaultdict**: Dictionary subclass that calls a factory function to supply missing values.
   ```python
   from collections import defaultdict
   dd = defaultdict(int)
   dd['one'] += 1
   ```

6. **ChainMap**: Class for creating a single view of multiple mappings.
   ```python
   from collections import ChainMap
   dict1 = {'a': 1, 'b': 2}
   dict2 = {'b': 3, 'c': 4}
   chain = ChainMap(dict1, dict2)
   ```

These data structures are part of Python’s standard library and are designed to provide more powerful and flexible ways to manage collections of items.