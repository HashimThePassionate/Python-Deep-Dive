# Abstract Base Classes (ABCs) and Their Inheritance

<p align="center">
  <img src="./Collection.PNG" width="70%" alt="Collection interface">
</p>


## **Examples** 

#### 1. Iterable
- **Method**: `__iter__`
- **Purpose**: To provide an iterator for looping over the container.
- **Inheritance**: Directly inherited by classes that need to support iteration.

#### 2. Sized
- **Method**: `__len__`
- **Purpose**: To return the number of items in the container.
- **Inheritance**: Directly inherited by classes that need to report their size.

#### 3. Container
- **Method**: `__contains__`
- **Purpose**: To check if an item exists in the container using the `in` keyword.
- **Inheritance**: Directly inherited by classes that need to support membership testing.

#### 4. Collection
- **Methods**: Inherits `__iter__`, `__len__`, and `__contains__`
- **Purpose**: To combine the functionalities of Iterable, Sized, and Container.
- **Inheritance**: Inherits from Iterable, Sized, and Container.

#### 5. Reversible
- **Method**: `__reversed__`
- **Purpose**: To provide a reverse iterator.
- **Inheritance**: Inherits from Iterable.

#### 6. Sequence
- **Methods**: `__getitem__`, `__contains__`, `__iter__`, `__reversed__`, `index`, `count`
- **Purpose**: To support indexed access, iteration, reverse iteration, and other sequence operations.
- **Inheritance**: Inherits from Collection and Reversible.

#### 7. Mapping
- **Methods**: `__getitem__`, `__contains__`, `__eq__`, `__ne__`, `get`, `items`, `keys`, `values`
- **Purpose**: To provide a mapping interface like a dictionary.
- **Inheritance**: Inherits from Collection.

#### 8. Set
- **Methods**: `isdisjoint`, `__le__`, `__lt__`, `__gt__`, `__ge__`, `__eq__`, `__ne__`, `__and__`, `__or__`, `__sub__`, `__xor__`
- **Purpose**: To support set operations.
- **Inheritance**: Inherits from Collection.

### Practical Examples of Each ABC Implementation

Let's implement each ABC separately with practical examples:

### 1. Iterable

```python
from collections.abc import Iterable

class MyIterable(Iterable):
    def __init__(self, data):
        self._data = data
    
    def __iter__(self):
        return iter(self._data)

# Example usage
iterable = MyIterable([1, 2, 3])
for item in iterable:
    print(item)
```

**Output**:
```sh
1
2
3
```

### 2. Sized

```python
from collections.abc import Sized

class MySized(Sized):
    def __init__(self, data):
        self._data = data
    
    def __len__(self):
        return len(self._data)

# Example usage
sized = MySized([1, 2, 3])
print(len(sized))
```

**Output**:
```sh
3
```

### 3. Container

```python
from collections.abc import Container

class MyContainer(Container):
    def __init__(self, data):
        self._data = data
    
    def __contains__(self, item):
        return item in self._data

# Example usage
container = MyContainer([1, 2, 3])
print(2 in container)
print(4 in container)
```

**Output**:
```sh
True
False
```

### 4. Collection

```python
from collections.abc import Collection

class MyCollection(Collection):
    def __init__(self, data):
        self._data = data
    
    def __iter__(self):
        return iter(self._data)
    
    def __len__(self):
        return len(self._data)
    
    def __contains__(self, item):
        return item in self._data

# Example usage
collection = MyCollection([1, 2, 3])
print(2 in collection)
print(len(collection))
for item in collection:
    print(item)
```

**Output**:
```sh
True
3
1
2
3
```

### 5. Reversible

```python
from collections.abc import Reversible

class MyReversible(Reversible):
    def __init__(self, data):
        self._data = data
    
    def __iter__(self):
        return iter(self._data)
    
    def __reversed__(self):
        return reversed(self._data)

# Example usage
reversible = MyReversible([1, 2, 3])
for item in reversed(reversible):
    print(item)
```

**Output**:
```sh
3
2
1
```

### 6. Sequence

```python
from collections.abc import Sequence
class CustomSequence(Sequence):
    def __init__(self, *args):
        self._data = list(args)
    
    def __getitem__(self, index):
        return self._data[index]
    
    def __contains__(self, item):
        return item in self._data
    
    def __iter__(self):
        return iter(self._data)
    
    def __reversed__(self):
        return reversed(self._data)
    
    def __len__(self):
        return len(self._data)
    
    def index(self, value, start=0, stop=None):
        if stop is None:
            stop = len(self._data)
        for i in range(start, stop):
            if self._data[i] == value:
                return i
        raise ValueError(f'{value} is not in list')
    
    def count(self, value):
        return self._data.count(value)
    
    def __repr__(self):
        return repr(self._data)

# Example usage
cseq = CustomSequence(1, 2, 3, 4, 5, 3)
# Accessing elements
print(cseq[1])  # Output: 2
# Checking containment
print(3 in cseq)  # Output: True
print(6 in cseq)  # Output: False
# Iteration
for item in cseq:
    print(item, end=' ')  # Output: 1 2 3 4 5 3
print()
# Reversed iteration
for item in reversed(cseq):
    print(item, end=' ')  # Output: 3 5 4 3 2 1
print()
# Length
print(len(cseq))  # Output: 6
# Index
print(cseq.index(3))  # Output: 2
print(cseq.index(3, 3))  # Output: 5
# Count
print(cseq.count(3))  # Output: 2
```

**Output**:
```sh
2
True
False
1 2 3 4 5 3
3 5 4 3 2 1
6
2
5
2
```

### 7. Mapping

```python
from collections.abc import Mapping
class CustomMapping(Mapping):
    def __init__(self, **kwargs):
        self._data = kwargs
    def __getitem__(self, key):
        return self._data[key]
    def __iter__(self):
        return iter(self._data)
    def __len__(self):
        return len(self._data)
    def __contains__(self, key):
        return key in self._data
    def keys(self):
        return self._data.keys()
    def items(self):
        return self._data.items()
    def values(self):
        return self._data.values()
    def __eq__(self, other):
        if isinstance(other, Mapping):
            return self._data == other
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, Mapping):
            return self._data != other
        return NotImplemented
    def __repr__(self):
        return repr(self._data)

# Example usage
cmapping = CustomMapping(a=1, b=2, c=3)
# Accessing elements
print(cmapping['a'])  # Output: 1
# Checking containment
print('b' in cmapping)  # Output: True
print('d' in cmapping)  # Output: False
# Iteration
for key in cmapping:
    print(key, end=' ')  # Output: a b c
print()
# Length
print(len(cmapping))  # Output: 3
# Keys
print(list(cmapping.keys()))  # Output: ['a', 'b', 'c']
# Items
print(list(cmapping.items()))  # Output: [('a', 1), ('b', 2), ('c', 3)]
# Values
print(list(cmapping.values()))  # Output: [1, 2, 3]
# Equality
cmapping2 = CustomMapping(a=1, b=2, c=3)
cmapping3 = CustomMapping(a=1, b=2)
print(cmapping == cmapping2)  # Output: True
print(cmapping == cmapping3)  # Output: False
print(cmapping != cmapping3)  # Output: True
```

**Output**:
```sh
1
True 
False
a b c
3
['a', 'b', 'c']
[('a', 1), ('b', 2), ('c', 3)]
[1, 2, 3]
True
False
True
```

### 8. Set

```python
from collections.abc import Set

class MySet(Set):
    def __init__(self, data):
        self._data = set(data)
    
    def __contains__(self, item):
        return item in self._data
    
    def __iter__(self):
        return iter(self._data)
    
    def __len__(self):
        return len(self._data)
    
    def isdisjoint(self, other):
        return self._data.isdisjoint(other)
    
    def __le__(self, other):
        return self._data <= other
    
    def __lt__(self, other):
        return self._data < other
    
    def __ge__(self, other):
        return self._data >= other
    
    def __gt__(self, other):
        return self._data > other
    
    def __eq__(self, other):
        return self._data == other
    
    def __ne__(self, other):
        return self._data != other
    
    def __and__(self, other):
        return self._data & other
    
    def __or__(self, other):
        return self._data | other
    
    def __sub__(self, other):
        return self._data - other
    
    def __xor__(self, other):
        return self._data ^ other

# Example usage
set1 = MySet([1, 2, 3])
set2 = MySet([3, 4, 5])
print(set1 & set2)  # Intersection
print(set1 | set2)  # Union
print(set1 - set2)  # Difference
print(set1 ^ set2)  # Symmetric Difference
```

**Output**:
```sh
{3}
{1, 2, 3, 4, 5}
{1, 2}
{1, 2, 4, 5}
```

### Summary

- **Iterable**: Provides iteration support.
- **Sized**: Provides size reporting.
- **Container**: Provides membership testing.
- **Collection**: Combines Iterable, Sized, and Container functionalities.
- **Reversible**: Provides reverse iteration.
- **Sequence**: Provides indexed access and sequence operations.
- **Mapping**: Provides mapping interface like a dictionary.
- **Set**: Provides set operations.

