# The Nine Flavors of Callable Objects

## Introduction
In Python, the call operator `()` can be applied to various types of objects, not just functions. To determine whether an object is callable, use the `callable()` built-in function. As of Python 3.9, the data model documentation lists nine callable types.

## List of Callable Types

### 1. User-Defined Functions
- **Description:** Created with `def` statements or lambda expressions.
- **Example:**
  ```python
  def my_function():
      return "Hello, World!"

  lambda_function = lambda x: x + 1
  ```

### 2. Built-In Functions
- **Description:** Functions implemented in C (for CPython), such as `len` or `time.strftime`.
- **Example:**
  ```python
  len("example")
  ```

### 3. Built-In Methods
- **Description:** Methods implemented in C, like `dict.get`.
- **Example:**
  ```python
  my_dict = {'key': 'value'}
  my_dict.get('key')
  ```

### 4. Methods
- **Description:** Functions defined in the body of a class.
- **Example:**
  ```python
  class MyClass:
      def method(self):
          return "This is a method."
  ```

### 5. Classes
- **Description:** When invoked, a class runs its `__new__` method to create an instance, then `__init__` to initialize it, and finally returns the instance to the caller. Because there is no `new` operator in Python, calling a class is like calling a function.
- **Example:**
  ```python
  class MyClass:
      def __init__(self, value):
          self.value = value

  instance = MyClass(10)
  ```

### 6. Class Instances
- **Description:** If a class defines a `__call__` method, then its instances may be invoked as functions.
- **Example:**
  ```python
  class CallableClass:
      def __call__(self, x):
          return x + 10

  callable_instance = CallableClass()
  callable_instance(5)  # Returns 15
  ```

### 7. Generator Functions
- **Description:** Functions or methods that use the `yield` keyword in their body. When called, they return a generator object.
- **Example:**
  ```python
  def generator_function():
      yield 1
      yield 2
      yield 3

  gen = generator_function()
  next(gen)  # Returns 1
  ```

### 8. Native Coroutine Functions
- **Description:** Functions or methods defined with `async def`. When called, they return a coroutine object.
- **Example:**
  ```python
  async def coroutine_function():
      return "Hello, Coroutine!"

  coro = coroutine_function()
  ```

### 9. Asynchronous Generator Functions
- **Description:** Functions or methods defined with `async def` that have `yield` in their body. When called, they return an asynchronous generator for use with `async for`.
- **Example:**
  ```python
  async def async_generator_function():
      yield 1
      yield 2
      yield 3

  async_gen = async_generator_function()
  ```

## Special Characteristics of Generators and Coroutines
Generators, native coroutines, and asynchronous generator functions differ from other callables as their return values are not application data but objects requiring further processing to yield application data or perform useful work.

### Summary
- **Generators:** Return iterators.
- **Native Coroutines and Asynchronous Generators:** Work with asynchronous programming frameworks like `asyncio`.

## Using `callable()` to Determine Callability
Given the variety of callable types, the safest way to check if an object is callable is to use the `callable()` built-in function.

### Example:
```python
>>> abs, str, 'Ni!'
(<built-in function abs>, <class 'str'>, 'Ni!')
>>> [callable(obj) for obj in (abs, str, 'Ni!')]
[True, True, False]
```

### Explanation:
1. **Objects:** We have three objects: `abs` (a built-in function), `str` (a class), and `'Ni!'` (a string).
2. **Checking Callability:** Using a list comprehension, we check if each object is callable with `callable(obj)`.
3. **Results:** The output is `[True, True, False]`, indicating that `abs` and `str` are callable, but `'Ni!'` is not.

## Moving Forward
We now move on to building class instances that work as callable objects.