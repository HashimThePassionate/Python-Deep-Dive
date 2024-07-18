# User-Defined Callable Types

## Introduction
In Python, not only are functions real objects, but arbitrary objects can also be made to behave like functions. This is achieved by implementing the `__call__` method in a class.

## Example 7-8: Implementing a BingoCage Class

The `BingoCage` class is a user-defined callable type. An instance of this class is built from any iterable, stores an internal list of items in random order, and allows calling the instance to pop an item from the list.

### Implementation of BingoCage Class

```python
import random

class BingoCage:
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)
    
    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')
    
    def __call__(self):
        return self.pick()
```

#### Explanation of BingoCage Class

1. **Constructor (`__init__` Method):**
   - **Accepts Any Iterable:** The constructor accepts any iterable and converts it to a list.
   - **Building a Local Copy:** Building a local copy of the items prevents unexpected side effects on the original list passed as an argument.
   - **Shuffle:** The `random.shuffle` function is used to shuffle the items, ensuring they are in random order.

2. **Pick Method:**
   - **Main Method:** The `pick` method pops an item from the internal list.
   - **Exception Handling:** If the list is empty, it raises a `LookupError` with a custom message.

3. **Call Method (`__call__`):**
   - **Shortcut:** The `__call__` method allows the instance to be called as a function, acting as a shortcut to the `pick` method.

### Demonstration of BingoCage Class

```python
>>> bingo = BingoCage(range(3))
>>> bingo.pick()
1
>>> bingo()
0
>>> callable(bingo)
True
```

#### Explanation of the Demonstration

1. **Creating an Instance:**
   - An instance of `BingoCage` is created with a range of numbers from 0 to 2.

2. **Using the Pick Method:**
   - The `pick` method is called directly, returning an item from the shuffled list.

3. **Using the Call Method:**
   - The instance is called as a function, invoking the `__call__` method, which in turn calls the `pick` method.

4. **Checking Callability:**
   - The `callable()` function confirms that the `bingo` instance is callable.

## Use Cases for __call__ Method

1. **Function-Like Objects with Internal State:**
   - The `__call__` method is useful for creating function-like objects that need to maintain internal state across invocations. For example, the `BingoCage` class keeps track of the remaining items.

2. **Implementing Decorators:**
   - The `__call__` method is also useful for implementing decorators. Decorators must be callable, and using the `__call__` method allows them to "remember" something between calls, such as caching results for memoization or splitting complex implementations into separate methods.

## Functional Approach: Closures
The functional approach to creating functions with internal state is to use closures. Closures and decorators will be covered in more detail in upcoming section.

## Conclusion
The `__call__` method allows arbitrary Python objects to behave like functions, providing flexibility in creating function-like objects with internal state and implementing decorators. Understanding and utilizing this feature can enhance your Python programming skills.

Next, we will explore the powerful syntax Python offers to declare function parameters and pass arguments into them.