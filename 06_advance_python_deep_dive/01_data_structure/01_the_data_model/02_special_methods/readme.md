# Special Methods
1. Special Methods Are for the Python Interpreter

   - **Intended Use**:
       - Special methods (also known as "magic methods" or "dunder methods") are designed to be called by the Python interpreter, not directly by the user.
       - For example, you should not call `my_object.__len__()`. Instead, you should use the built-in `len(my_object)`. This makes your code more readable and leverages Python’s design.

   - **Implicit Calls**:
       - When you use Python’s built-in functions (like `len()`, `iter()`, `str()`), these functions internally call the corresponding special methods (`__len__`, `__iter__`, `__str__`).

2. Optimization for Built-in Types

   . **Performance Shortcut**:
     - For built-in types like `list`, `str`, `bytearray`, and extensions like NumPy arrays, Python takes shortcuts to enhance performance.
     - These built-in types are implemented in C and include a structure called `PyVarObject`, which contains an `ob_size` field that stores the number of items.
     - When you call `len()` on these types, Python directly accesses the `ob_size` field, making the operation much faster than invoking a method.

3. Implicit Special Method Calls

   - **Loop Example**:
       - Consider the loop `for i in x:`. This statement implicitly calls `iter(x)`, which in turn may call `x.__iter__()`. If `__iter__` is not available, it may use `x.__getitem__()`, as seen in the `FrenchDeck` example.

   - **Avoid Direct Calls**:
       - Generally, you should avoid direct calls to special methods. Instead, use the related built-in functions. These functions not only call the special methods but also provide additional functionalities and optimizations.
       - The exception is `__init__`, which is frequently called directly in user code, especially to invoke the initializer of a superclass.

4. Implementing Special Methods

   - **Implementation Over Invocation**:
       - Focus more on implementing special methods in your custom classes rather than invoking them explicitly. This makes your classes integrate better with Python’s built-in functions and idioms.

   - **Built-in Functions**:
       - Use built-in functions like `len()`, `iter()`, and `str()` instead of directly calling `__len__()`, `__iter__()`, and `__str__()`. These functions are optimized for performance, especially for built-in types.

---

# General Purpose Special methods
#### Understanding `__new__` and `__init__`

#### `__new__` Method

- **Purpose**: The `__new__` method is responsible for creating a new instance of a class. It is called before the `__init__` method.
- **Usage**: It is used when subclassing immutable types like `int`, `str`, or `tuple`. It returns a new instance of the class.
- **Syntax**: `def __new__(cls, *args, **kwargs)`

#### `__init__` Method

- **Purpose**: The `__init__` method initializes the instance created by `__new__`. It is called after the instance has been created.
- **Usage**: It is used to set the initial state of the instance.
- **Syntax**: `def __init__(self, *args, **kwargs)`

#### Differences

- `__new__` is a static method, while `__init__` is an instance method.
- `__new__` is responsible for creating an instance, whereas `__init__` is responsible for initializing the created instance.
- `__new__` returns a new instance of the class, while `__init__` does not return anything (returns `None`).

### Example without Arguments

```python
class MyClassWithoutArgs:
    def __new__(cls):
        # Creating a new instance
        print("Creating instance (in __new__)")
        instance = super(MyClassWithoutArgs, cls).__new__(cls)
        return instance

    def __init__(self):
        # Initializing the instance
        print("Initializing instance (in __init__)")
        self.data = "Some data"

# Creating an instance of MyClassWithoutArgs
obj = MyClassWithoutArgs()
print(obj.data)
```

#### Explanation:
- `__new__` method creates the instance and prints a message.
- `__init__` method initializes the instance and sets the `data` attribute.

### Example with Arguments (`*args` and `**kwargs`)

```python
class MyClassWithArgs:
    def __new__(cls, *args, **kwargs):
        # Creating a new instance with arguments
        print("Creating instance (in __new__) with arguments:", args, kwargs)
        instance = super(MyClassWithArgs, cls).__new__(cls)
        return instance

    def __init__(self, *args, **kwargs):
        # Initializing the instance with arguments
        print("Initializing instance (in __init__) with arguments:", args, kwargs)
        self.args = args
        self.kwargs = kwargs

# Creating an instance of MyClassWithArgs with arguments
obj = MyClassWithArgs(1, 2, a=3, b=4)
print("Positional arguments:", obj.args)
print("Keyword arguments:", obj.kwargs)
```

#### Explanation:
- `__new__` method creates the instance and prints the provided arguments.
- `__init__` method initializes the instance with the provided arguments and sets `args` and `kwargs` attributes.

These examples illustrate how `__new__` and `__init__` work together to create and initialize instances, with and without arguments.

--- 

#### Understanding `__bytes__` and `__str__` Methods

The `__bytes__` method in Python is used to define how an object is converted to a byte string (i.e., an instance of the `bytes` class). This method is called when you use the `bytes()` function on an object.

Similarly, the `__str__` method defines how an object is converted to a string (i.e., an instance of the `str` class). This method is called when you use the `str()` function or `print()` function on an object.

When a class defines both `__bytes__` and `__str__`, they should return equivalent representations of the object, but in different formats: `__bytes__` should return a bytes object, and `__str__` should return a string object.

### Example with `__bytes__` and `__str__` Methods

Here's an example that demonstrates how to implement both `__bytes__` and `__str__` methods in a class.

```python
class DataPacket:
    def __init__(self, data):
        self.data = data

    def __bytes__(self):
        # Convert the data to a bytes object
        return bytes(self.data, encoding='utf-8')

    def __str__(self):
        # Convert the data to a string object
        return str(self.data)

# Creating an instance of DataPacket
packet = DataPacket("Hello, World!")

# Calling __bytes__ method
print(bytes(packet))  # Output: b'Hello, World!'

# Calling __str__ method
print(str(packet))  # Output: Hello, World!
```

#### Explanation:

- **`__init__` Method**: Initializes the `DataPacket` instance with the provided data.
- **`__bytes__` Method**: Converts the data to a bytes object using UTF-8 encoding.
- **`__str__` Method**: Converts the data to a string object.

### Example with Additional Arguments (`*args` and `**kwargs`)

Let's expand the example to include handling additional arguments using `*args` and `**kwargs`.

Got it! If you want the `__bytes__` and `__str__` methods to incorporate the additional positional and keyword arguments, we can modify these methods to include this information in their outputs. Here's an updated example that includes positional and keyword arguments in the `__bytes__` and `__str__` methods.

### Updated Example with Additional Arguments in `__bytes__` and `__str__`

```python
class DataPacketWithArgs:
    def __init__(self, data, *args, **kwargs):
        # Initializing the instance with provided data and additional arguments
        self.data = data
        self.args = args
        self.kwargs = kwargs

    def __bytes__(self):
        # Convert the data and additional arguments to a bytes object
        args_bytes = b', '.join([bytes(str(arg), encoding='utf-8') for arg in self.args])
        kwargs_bytes = b', '.join([bytes(f"{key}={value}", encoding='utf-8') for key, value in self.kwargs.items()])
        combined_bytes = bytes(self.data, encoding='utf-8') + b'; ' + args_bytes + b'; ' + kwargs_bytes
        return combined_bytes

    def __str__(self):
        # Convert the data and additional arguments to a string object
        args_str = ', '.join(map(str, self.args))
        kwargs_str = ', '.join([f"{key}={value}" for key, value in self.kwargs.items()])
        combined_str = f"{self.data}; {args_str}; {kwargs_str}"
        return combined_str

    def additional_info(self):
        # Print additional arguments
        if self.args:
            print(f"Additional positional arguments: {self.args}")
        if self.kwargs:
            print(f"Additional keyword arguments: {self.kwargs}")

# Creating an instance of DataPacketWithArgs with additional arguments
packet_with_args = DataPacketWithArgs("Hello, World!", 42, key="value")

# Calling __bytes__ method
print(bytes(packet_with_args))  
# Output: b'Hello, World!; 42; key=value'

# Calling __str__ method
print(str(packet_with_args))  
# Output: Hello, World!; 42; key=value

# Printing additional arguments
packet_with_args.additional_info()
# Output:
# Additional positional arguments: (42,)
# Additional keyword arguments: {'key': 'value'}
```

### Explanation

1. **`__init__` Method**:
   - Initializes the instance with the provided `data` and any additional positional (`*args`) and keyword arguments (`**kwargs`).

2. **`__bytes__` Method**:
   - Converts the `data` attribute and additional arguments to a bytes object.
   - Positional arguments (`args`) are converted to bytes and joined with a comma.
   - Keyword arguments (`kwargs`) are converted to bytes in the form of `key=value` pairs and joined with a comma.
   - All parts are combined into a single bytes object with semicolons separating the sections.

3. **`__str__` Method**:
   - Converts the `data` attribute and additional arguments to a string object.
   - Positional arguments (`args`) are converted to strings and joined with a comma.
   - Keyword arguments (`kwargs`) are converted to strings in the form of `key=value` pairs and joined with a comma.
   - All parts are combined into a single string with semicolons separating the sections.

4. **`additional_info` Method**:
   - Prints any additional positional and keyword arguments provided during initialization.

### Usage and Output

- **Creating an Instance**: `DataPacketWithArgs("Hello, World!", 42, key="value")` initializes the instance with the provided arguments.
- **Converting to Bytes**: `bytes(packet_with_args)` calls the `__bytes__` method, which returns the bytes representation of the data and additional arguments (`b'Hello, World!; 42; key=value'`).
- **Converting to String**: `str(packet_with_args)` or `print(packet_with_args)` calls the `__str__` method, which returns the string representation of the data and additional arguments (`'Hello, World!; 42; key=value'`).
- **Printing Additional Arguments**: `packet_with_args.additional_info()` prints any additional positional and keyword arguments provided during initialization.

This example demonstrates how to implement and use `__bytes__` and `__str__` methods along with handling additional arguments in the class.

--- 

#### Understanding `__dir__` Method in Python

The `__dir__` method is a special method in Python that allows you to customize the behavior of the `dir()` function. When you call `dir(x)`, Python translates this operation into a call to `x.__dir__()`. This method should return a sorted list of the object's attributes. If a class does not define a `__dir__` method, the default implementation of `dir()` performs introspection to return a list of attributes, aiming to provide relevant information.

### When and Why to Use `__dir__`

You might want to implement `__dir__` in a class when:
1. **Customization**: You want to control the list of attributes and methods that are displayed when `dir()` is called on an instance of your class.
2. **Security**: You need to hide certain attributes or methods from being listed.
3. **Simplification**: You want to simplify the output of `dir()` to show only the most relevant attributes and methods.

Let's create a more practical and comprehensive example of using the `__dir__` method in a class.

### Practical Example: Customizing `__dir__` in a Configuration Class

Imagine you have a configuration class that loads settings from a file. You want to customize the output of `dir()` to show only the most relevant configuration options, hiding internal attributes and methods.

#### Step-by-Step Implementation

1. **Define the Class**:
   Create a `Config` class that loads settings from a file.

2. **Implement the `__dir__` Method**:
   Customize the `__dir__` method to list only the public configuration options.

3. **Add Methods and Attributes**:
   Include methods to load settings and some internal attributes.

#### Example Code

```python
class Config:
    def __init__(self, filepath):
        self.filepath = filepath
        self._settings = {}
        self._load_settings()

    def _load_settings(self):
        # Simulate loading settings from a file
        self._settings = {
            'host': 'localhost',
            'port': 8080,
            'debug': True
        }

    def get_setting(self, key):
        return self._settings.get(key, None)

    def __dir__(self):
        # Customize the list of attributes and methods shown by dir()
        public_attributes = ['filepath', 'get_setting', 'host', 'port', 'debug']
        return public_attributes

    @property
    def host(self):
        return self._settings['host']

    @property
    def port(self):
        return self._settings['port']

    @property
    def debug(self):
        return self._settings['debug']

# Creating an instance of Config
config = Config("config.yaml")

# Calling dir() on the instance
print(dir(config))
```

### Output Explanation

```python
['debug', 'filepath', 'get_setting', 'host', 'port']
```

In this example, the `__dir__` method of the `Config` class returns a list containing only the `filepath`, `get_setting` method, and the properties `host`, `port`, and `debug`. When you call `dir(config)`, it displays this customized list instead of the default list that would include internal attributes and methods.

By customizing the `__dir__` method, you control what information is revealed when introspecting an instance of the class, making it more user-friendly and focused on relevant details.

--- 

#### Understanding `__delattr__` Method in Python

The `__delattr__` method is a special method in Python that is called when you try to delete an attribute from an object using the `del` statement. When you write `del x.y`, Python translates this into a call to `x.__delattr__('y')`.

### Key Points About `__delattr__`

- **Purpose**: Customize the deletion of attributes from an object.
- **Invocation**: Called automatically when `del` is used on an attribute.
- **Fallback**: If `__delattr__` is not defined, Python defaults to deleting the attribute directly from the instance's `__dict__`.

### Example: Custom Attribute Deletion

Here is a practical example demonstrating how to use `__delattr__` to customize attribute deletion in a class:

#### Step-by-Step Implementation

1. **Define the Class**:
   Create a class and override the `__delattr__` method.
   
2. **Customize Attribute Deletion**:
   Implement logic in `__delattr__` to control how attributes are deleted.

#### Example Code

```python
class MyClass:
    def __init__(self):
        self.name = "Example"
        self.value = 42
    
    def __delattr__(self, name):
        if name == 'value':
            print("You are trying to delete a protected attribute!")
        else:
            # Use the default behavior to delete the attribute
            object.__delattr__(self, name)

# Creating an instance of MyClass
obj = MyClass()

# Trying to delete the 'value' attribute
del obj.value  # Output: You are trying to delete a protected attribute!

# Trying to delete the 'name' attribute
del obj.name

# Checking the remaining attributes
print(dir(obj))  # Output will not include 'name', but 'value' remains
```
### Summary

- **Purpose of `__delattr__`**: To customize the deletion of attributes from an object.
- **Common Use Cases**: Preventing deletion of critical attributes, logging attribute deletions, or enforcing specific business rules.
- **Implementation**: Override the `__delattr__` method to control the behavior when an attribute is deleted.

### Key Considerations

- **Security**: You can use `__delattr__` to prevent the deletion of important attributes that should remain intact for the object's integrity.
- **Logging and Debugging**: Useful for logging attribute deletions or raising exceptions when certain attributes are deleted.

By customizing the `__delattr__` method, you gain control over the deletion of attributes, which can help in maintaining the integrity and security of your objects.

--- 

#### Understanding Special Methods for Comparisons in Python

In Python, special methods are used to define the behavior of comparison operators. These methods allow you to customize how objects of your class are compared with each other.

### Special Methods for Comparisons

- `__eq__(self, other)`: Defines behavior for the equality operator `==`.
- `__ne__(self, other)`: Defines behavior for the inequality operator `!=`.
- `__lt__(self, other)`: Defines behavior for the less than operator `<`.
- `__le__(self, other)`: Defines behavior for the less than or equal to operator `<=`.
- `__gt__(self, other)`: Defines behavior for the greater than operator `>`.
- `__ge__(self, other)`: Defines behavior for the greater than or equal to operator `>=`.

Each of these methods should return `True` or `False` based on the comparison. They can also return `NotImplemented` if the comparison is not supported.

### Best Practice: Using `functools.total_ordering`

The `functools.total_ordering` decorator can help simplify the implementation of these methods. You only need to define `__eq__` and one other method (typically `__lt__`), and `total_ordering` will automatically provide the rest of the comparison methods.

### Example Implementation

Let's create a `Person` class that compares people based on their age using `__eq__` and `__lt__`, and then use `functools.total_ordering` to provide the other comparison methods.

#### Step-by-Step Implementation

1. **Import `total_ordering`**:
   Import `total_ordering` from the `functools` module.

2. **Define the Class**:
   Create a `Person` class with `__eq__` and `__lt__` methods.

3. **Use the `total_ordering` Decorator**:
   Decorate the class with `@total_ordering`.

#### Example Code

```python
from functools import total_ordering

@total_ordering
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return self.age == other.age

    def __lt__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return self.age < other.age

    def __str__(self):
        return f"{self.name}, Age: {self.age}"

# Creating instances of Person
alice = Person("Alice", 30)
bob = Person("Bob", 25)
charlie = Person("Charlie", 30)

# Using comparison operators
print(alice == bob)      # Output: False
print(alice == charlie)  # Output: True
print(alice > bob)       # Output: True
print(alice < bob)       # Output: False
print(alice >= charlie)  # Output: True
print(bob <= charlie)    # Output: True
print(alice != bob)      # Output: True
```
### Summary

- **Special Methods**: Use special methods like `__eq__`, `__lt__`, etc., to define custom comparison behavior.
- **Best Practice**: Use `functools.total_ordering` to minimize boilerplate code and avoid logical contradictions.
- **Implementation**: Define `__eq__` and one other comparison method (e.g., `__lt__`), and use `@total_ordering` to generate the rest.

By following these practices, you can create classes with robust and easy-to-maintain comparison behaviors.

--- 

#### Understanding `__getattr__` Method in Python

The `__getattr__` method is a special method in Python that is called when an attribute is not found in the usual places, such as the instance’s `__dict__` or the class itself. This method allows you to define custom behavior for attribute access that would otherwise result in an `AttributeError`.

### Key Points About `__getattr__`

- **Invocation**: `__getattr__` is called only when an attribute is not found by the usual means.
- **Return Value**: Should return a value for the attribute or raise an `AttributeError`.
- **Fallback Mechanism**: Acts as a fallback mechanism for undefined attributes.

### Use Cases for `__getattr__`

1. **Dynamic Attribute Handling**: Useful for cases where you need to dynamically generate or retrieve attributes.
2. **Proxy Objects**: When creating proxy objects that delegate attribute access to another object.
3. **Default Values**: Providing default values for missing attributes.

### Example Implementation

Let's create an example where a class uses `__getattr__` to provide default values for attributes that are not explicitly defined.

#### Step-by-Step Implementation

1. **Define the Class**:
   Create a class and override the `__getattr__` method.

2. **Implement Custom Attribute Handling**:
   In the `__getattr__` method, provide a default value or raise an `AttributeError` if the attribute is not found.

#### Example Code

```python
class MyClass:
    def __init__(self):
        self.name = "Example"
        self.value = 42

    def __getattr__(self, name):
        if name == 'default':
            return "This is a default value"
        else:
            raise AttributeError(f"'MyClass' object has no attribute '{name}'")

# Creating an instance of MyClass
obj = MyClass()

# Accessing an existing attribute
print(obj.name)  # Output: Example

# Accessing a non-existing attribute that triggers __getattr__
print(obj.default)  # Output: This is a default value

# Accessing a non-existing attribute that raises AttributeError
try:
    print(obj.non_existent)
except AttributeError as e:
    print(e)  # Output: 'MyClass' object has no attribute 'non_existent'
```

### Summary

- **Purpose of `__getattr__`**: To provide custom behavior for attribute access when an attribute is not found.
- **Common Use Cases**: Dynamic attribute handling, proxy objects, providing default values.
- **Implementation**: Override the `__getattr__` method to return a value or raise an `AttributeError`.

By using `__getattr__`, you can add flexibility to your class, allowing it to handle missing attributes dynamically and gracefully. This can be particularly useful in cases where attributes are generated on-the-fly or when creating proxy objects.

--- 

#### Understanding `__getattribute__` Method in Python

The `__getattribute__` method is a special method in Python that is called every time an attribute of an object is accessed. This includes attribute access through dot notation (`x.y`) and functions like `getattr(x, 'y')`. This method provides a way to intercept all attribute accesses and define custom behavior for them.

### Key Points About `__getattribute__`

- **Invocation**: Called on every attribute access, whether the attribute exists or not.
- **Return Value**: Must return the value of the attribute or raise an `AttributeError`.
- **Default Implementation**: The default implementation handles normal attribute access, including looking up the attribute in the instance’s `__dict__`, class attributes, and calling `__getattr__` if the attribute is not found.

### Use Cases for `__getattribute__`

1. **Logging and Debugging**: Log every attribute access for debugging purposes.
2. **Attribute Access Control**: Implement custom access control for attributes.
3. **Dynamic Attributes**: Generate attributes dynamically or compute their values on the fly.

### Best Practices

- **Delegate to the Default Implementation**: When overriding `__getattribute__`, it's often useful to delegate to the default implementation using `object.__getattribute__` to maintain normal behavior for attributes that do not need special handling.
- **Use with Caution**: Since `__getattribute__` is called on every attribute access, it can easily introduce performance overhead and complexity if not used carefully.

### Example Implementation

Let’s create an example where we log every attribute access and provide custom behavior for certain attributes.

#### Step-by-Step Implementation

1. **Define the Class**:
   Create a class and override the `__getattribute__` method.
   
2. **Implement Custom Attribute Handling**:
   In the `__getattribute__` method, log attribute access and provide custom behavior for specific attributes.

#### Example Code

```python
class MyClass:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __getattribute__(self, name):
        # Log every attribute access
        print(f"Accessing attribute: {name}")
        
        # Custom behavior for specific attributes
        if name == 'name':
            return f"Name: {object.__getattribute__(self, name)}"
        elif name == 'value':
            return object.__getattribute__(self, name) * 2
        else:
            # Delegate to the default implementation for all other attributes
            return object.__getattribute__(self, name)

# Creating an instance of MyClass
obj = MyClass("Example", 42)

# Accessing attributes
print(obj.name)   # Output: Accessing attribute: name \n Name: Example
print(obj.value)  # Output: Accessing attribute: value \n 84
print(obj.__dict__)  # Output: Accessing attribute: __dict__ \n {'name': 'Example', 'value': 42}
```
By using `__getattribute__`, you can have fine-grained control over attribute access, making it a powerful tool for advanced use cases like debugging, logging, and implementing custom access policies. However, it should be used judiciously to avoid unnecessary complexity and performance overhead.

--- 

#### Understanding `__bool__` (formerly `__nonzero__`) Method in Python

In Python 2, the method `__nonzero__` is used to define the truth value of an object. In Python 3, this method has been renamed to `__bool__`, making it more readable and intuitive.

### Key Points About `__bool__` / `__nonzero__`

- **Invocation**: Called by `bool(x)` and in contexts where an object's truth value is needed, such as in conditionals (`if x:`).
- **Return Value**: Should return `True` or `False`.
- **Fallback**: If `__bool__`/`__nonzero__` is not defined, Python falls back to `__len__()`, considering the object `False` if its length is zero.
- **Default Behavior**: If neither `__bool__`/`__nonzero__` nor `__len__` is defined, the object is always considered `True`.

### Use Cases for `__bool__` / `__nonzero__`

1. **Custom Truth Values**: Define custom logic to determine the truth value of an object.
2. **Emulating Built-in Types**: Mimic the behavior of built-in types that have specific truth value semantics.
3. **Empty/Non-Empty Checks**: Implement truth value based on whether the object is empty or non-empty.

### Example Implementation

Let’s create an example where a `Box` class uses `__bool__` to define its truth value based on whether it contains any items.

#### Step-by-Step Implementation

1. **Define the Class**:
   Create a `Box` class with `__bool__` to define its truth value.
   
2. **Implement Custom Truth Value Logic**:
   In the `__bool__` method, return `True` if the box contains items, otherwise return `False`.

#### Example Code

```python
class Box:
    def __init__(self, items=None):
        self.items = items if items is not None else []

    def __bool__(self):
        # The box is considered True if it contains items
        return bool(self.items)

    def __len__(self):
        # Fallback for Python 2 if __nonzero__ is used instead of __bool__
        return len(self.items)

# Creating instances of Box
box1 = Box(['apple', 'banana'])
box2 = Box([])

# Checking truth value of boxes
print(bool(box1))  # Output: True (box1 contains items)
print(bool(box2))  # Output: False (box2 is empty)

# Using boxes in conditional statements
if box1:
    print("Box1 is not empty")  # Output: Box1 is not empty

if not box2:
    print("Box2 is empty")  # Output: Box2 is empty
```
### Summary

- **Purpose of `__bool__`/`__nonzero__`**: To define the truth value of an object.
- **Common Use Cases**: Custom truth values, emulating built-in types, empty/non-empty checks.
- **Implementation**: Override `__bool__` (or `__nonzero__` in Python 2) to return `True` or `False` based on custom logic.

By using `__bool__`, you can control how your objects are evaluated in boolean contexts, providing a clear and intuitive way to define their truth value based on their state or contents.

---
### Understanding `__repr__` Method in Python

The `__repr__` method in Python is a special method that is called by the `repr()` function and by the interactive interpreter when an object is the result of an expression statement. The purpose of `__repr__` is to provide a complete and unambiguous string representation of an object, which is useful for debugging and development.

### Key Points About `__repr__`

- **Invocation**: Called by `repr(x)` and by the interactive interpreter.
- **Return Value**: Should return a string that provides a complete and unambiguous representation of the object.
- **Goal**: Ideally, the string returned by `__repr__` should be an expression that, when passed to `eval()`, returns an object with the same state (though this is not always feasible).
- **Default Behavior**: If `__repr__` is not defined, Python uses a default string representation.

### Use Cases for `__repr__`

1. **Debugging**: Provides detailed information about the object for debugging purposes.
2. **Logging**: Useful for logging detailed information about objects.
3. **Interactive Interpreter**: Enhances the readability of objects when working in the interactive interpreter.

### Best Practices

- **Unambiguous Information**: Ensure that `__repr__` provides enough information to uniquely identify the object.
- **Eval Compatibility**: When feasible, make the string representation a valid Python expression that can recreate the object.
- **Clarity**: Make the representation clear and informative to aid in debugging.

```python
class Person:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def __repr__(self):
        return f"Person(name={repr(self.name)}, age={self.age}, occupation={repr(self.occupation)})"

# Creating instances of Person
alice = Person("Alice", 30, "Engineer")
bob = Person("Bob", 25, "Doctor")

# Using repr() to get the string representation
repr_alice = repr(alice)
repr_bob = repr(bob)
print(repr_alice)  # Output: Person(name='Alice', age=30, occupation='Engineer')
print(repr_bob)    # Output: Person(name='Bob', age=25, occupation='Doctor')

# Recreating objects using eval()
alice_copy = eval(repr_alice)
bob_copy = eval(repr_bob)

# Checking if the recreated objects are the same as the originals
print(alice == alice_copy)  # Output: False (different instances, same state)
print(bob == bob_copy)      # Output: False (different instances, same state)
print(alice.name == alice_copy.name)  # Output: True (same state)
print(bob.name == bob_copy.name)      # Output: True (same state)

# Showing the representation in the interactive interpreter
alice  # Output: Person(name='Alice', age=30, occupation='Engineer')
```

### Summary

- **Purpose of `__repr__`**: To provide a complete and unambiguous string representation of an object.
- **Common Use Cases**: Debugging, logging, enhancing the interactive interpreter experience.
- **Implementation**: Override `__repr__` to return a string that includes all relevant information about the object.

By defining `__repr__`, you can make your objects easier to work with during development and debugging, providing clear and informative representations of their state.

---

#### Understanding `__setattr__` Method in Python

The `__setattr__` method in Python is a special method that is called whenever an attribute assignment is made on an object. This includes direct assignments like `x.y = value` as well as calls to `setattr(x, 'y', value)`. Unlike `__getattr__`, which is called only for missing attributes, `__setattr__` is invoked for all attribute assignments.

### Key Points About `__setattr__`

- **Invocation**: Called for every attribute assignment on an object.
- **Avoid Recursion**: When overriding `__setattr__`, you must avoid infinite recursion by directly modifying the object's `__dict__` or delegating the setting to the superclass.
- **Delegation**: It's often useful to delegate the setting to the superclass using `super().__setattr__(name, value)` to ensure that normal attribute setting behavior is maintained.

### Use Cases for `__setattr__`

1. **Attribute Validation**: Validate or transform values before setting them as attributes.
2. **Logging and Debugging**: Log attribute assignments for debugging purposes.
3. **Enforcing Read-Only Attributes**: Prevent certain attributes from being modified after they are set.

### Example Implementation

Let's create an example where a `Person` class uses `__setattr__` to log attribute assignments and enforce that the `name` attribute can only be set once.

#### Step-by-Step Implementation

1. **Define the Class**:
   Create a `Person` class and override the `__setattr__` method.
   
2. **Implement Custom Attribute Setting**:
   In the `__setattr__` method, log assignments and enforce that the `name` attribute is read-only after being set.

#### Example Code

```python
class Person:
    def __init__(self, name, age):
        self._name_set = False
        self.name = name
        self.age = age

    def __setattr__(self, name, value):
        # Log every attribute assignment
        print(f"Setting attribute {name} to {value}")
        
        if name == "name":
            if self._name_set:
                raise AttributeError("The 'name' attribute is read-only")
            else:
                self._name_set = True
        
        # Use the default behavior to set the attribute
        super().__setattr__(name, value)

# Creating an instance of Person
alice = Person("Alice", 30)

# Setting attributes
alice.age = 31  # Output: Setting attribute age to 31

# Attempting to set the name attribute again
try:
    alice.name = "Alicia"
except AttributeError as e:
    print(e)  # Output: The 'name' attribute is read-only

# Setting a new attribute
alice.occupation = "Engineer"  # Output: Setting attribute occupation to Engineer

# Checking the state of the object
print(alice.__dict__)  # Output: {'_name_set': True, 'name': 'Alice', 'age': 31, 'occupation': 'Engineer'}
```
### Summary

- **Purpose of `__setattr__`**: To provide custom behavior for attribute assignments.
- **Common Use Cases**: Attribute validation, logging, enforcing read-only attributes.
- **Implementation**: Override `__setattr__` and use `super().__setattr__(name, value)` to maintain normal behavior.

By using `__setattr__`, you can add additional logic to attribute assignments, such as validation or logging, making your classes more robust and easier to debug.


#### Understanding `__unicode__` Method in Python 2

In Python 2, the `__unicode__` method is used to define the behavior of the `unicode()` function, which converts an object to a Unicode string. This method is particularly useful for handling non-ASCII text and ensuring that objects can be represented correctly in Unicode.

### Key Points About `__unicode__`

- **Invocation**: Called by `unicode(x)` in Python 2.
- **Return Value**: Should return a Unicode string.
- **Compatibility with `__str__`**: If both `__unicode__` and `__str__` are defined, they should return equivalent strings, with `__unicode__` returning a Unicode string and `__str__` returning a plain string.

### Use Cases for `__unicode__`

1. **Non-ASCII Text Handling**: Ensure that objects containing non-ASCII characters can be correctly represented as Unicode strings.
2. **Consistency with `__str__`**: Provide a consistent string representation in both Unicode and plain string formats.

### Example Implementation

Let’s create an example where a `Person` class defines both `__unicode__` and `__str__` methods to provide consistent string representations.

#### Step-by-Step Implementation

1. **Define the Class**:
   Create a `Person` class with both `__unicode__` and `__str__` methods.
   
2. **Implement Custom Unicode and String Representations**:
   Ensure that the `__unicode__` method returns a Unicode string and the `__str__` method returns a plain string.

#### Example Code

```python
class Person:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def __unicode__(self):
        return u"Person(name=u'{name}', age={age}, occupation=u'{occupation}')".format(
            name=self.name, age=self.age, occupation=self.occupation)

    def __str__(self):
        return "Person(name='{name}', age={age}, occupation='{occupation}')".format(
            name=self.name, age=self.age, occupation=self.occupation)

# Creating instances of Person
alice = Person("Alice", 30, "Engineer")
bob = Person("Bob", 25, "Doctor")

# Using unicode() to get the Unicode string representation (Python 2)
print(unicode(alice))  # Output: Person(name=u'Alice', age=30, occupation=u'Engineer')
print(unicode(bob))    # Output: Person(name=u'Bob', age=25, occupation=u'Doctor')

# Using str() to get the plain string representation
print(str(alice))  # Output: Person(name='Alice', age=30, occupation='Engineer')
print(str(bob))    # Output: Person(name='Bob', age=25, occupation='Doctor')
```
### Summary

- **Purpose of `__unicode__`**: To provide a Unicode string representation of an object in Python 2.
- **Common Use Cases**: Handling non-ASCII text and providing consistent string representations.
- **Implementation**: Define `__unicode__` to return a Unicode string and `__str__` to return a plain string, ensuring consistency between the two.

By defining both `__unicode__` and `__str__`, you can ensure that your objects have consistent and correct string representations in both Unicode and plain string formats, which is especially important for handling non-ASCII text in Python 2.

---

#### Understanding `__format__` Method in Python

The `__format__` method in Python is a special method that is called by the `format()` function. This method allows you to define custom formatting for your objects using the format specification language. When you call `format(x)`, it calls `x.__format__()`, and when you call `format(x, format_string)`, it calls `x.__format__(format_string)`.

### Key Points About `__format__`

- **Invocation**: Called by `format(x)` and `format(x, format_string)`.
- **Return Value**: Should return a formatted string based on the provided format string.
- **Format Specification**: Each class can define its own "language" of format specifications inspired by those implemented by built-in types.

### Use Cases for `__format__`

1. **Custom Formatting**: Provide custom formatting options for your objects.
2. **Consistency with Built-in Types**: Implement similar format specifications to built-in types for consistency.
3. **Enhanced Readability**: Improve the readability and presentation of your object's string representation.

### Example Implementation

Let’s create an example where a `Person` class defines a `__format__` method to support custom formatting options for name and age.

#### Step-by-Step Implementation

1. **Define the Class**:
   Create a `Person` class with a `__format__` method.
   
2. **Implement Custom Formatting**:
   In the `__format__` method, interpret the format string and return a formatted string.

#### Example Code

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __format__(self, format_string=''):
        if format_string == '':
            return f"{self.name}, {self.age}"
        elif format_string == 'name':
            return self.name
        elif format_string == 'age':
            return str(self.age)
        elif format_string == 'name_upper':
            return self.name.upper()
        else:
            raise ValueError(f"Unknown format code '{format_string}' for object of type 'Person'")

# Creating an instance of Person
alice = Person("Alice", 30)

# Using format() with different format strings
print(format(alice))             # Output: Alice, 30
print(format(alice, 'name'))     # Output: Alice
print(format(alice, 'age'))      # Output: 30
print(format(alice, 'name_upper'))  # Output: ALICE

# Using f-strings with format specifications
print(f"{alice}")             # Output: Alice, 30
print(f"{alice:name}")        # Output: Alice
print(f"{alice:age}")         # Output: 30
print(f"{alice:name_upper}")  # Output: ALICE
```

### Summary

- **Purpose of `__format__`**: To provide custom formatting for objects based on a format string.
- **Common Use Cases**: Custom formatting, consistency with built-in types, enhanced readability.
- **Implementation**: Override `__format__` to interpret the format string and return a formatted string.

By defining `__format__`, you can customize how your objects are formatted using the `format()` function and f-strings, providing flexibility and enhancing the readability of your object's string representation.

---

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

### Special Methods for Numeric Objects

Special methods in Python allow instances to support numeric operations by overloading operators. These methods enable custom classes to handle arithmetic, bitwise, and conversion operations similarly to built-in numeric types. Below is a detailed explanation of each group of special methods, followed by practical examples for implementation.

### Table of Special Methods for Numeric Operations

1. **Unary Operations**
    - `__abs__(self)`: Called by `abs(x)`.
    - `__invert__(self)`: Called by `~x`.
    - `__neg__(self)`: Called by `-x`.
    - `__pos__(self)`: Called by `+x`.

2. **Binary Operations**
    - `__add__(self, other)`: Called by `x + y`.
    - `__sub__(self, other)`: Called by `x - y`.
    - `__mul__(self, other)`: Called by `x * y`.
    - `__mod__(self, other)`: Called by `x % y`.
    - `__div__(self, other)`: Called by `x / y` (Python 2 only).
    - `__floordiv__(self, other)`: Called by `x // y`.
    - `__truediv__(self, other)`: Called by `x / y` (Python 3).
    - `__pow__(self, other[, modulo])`: Called by `x ** y` and `pow(x, y[, z])`.

3. **Right Binary Operations**
    - `__radd__(self, other)`: Called by `y + x`.
    - `__rsub__(self, other)`: Called by `y - x`.
    - `__rmul__(self, other)`: Called by `y * x`.
    - `__rmod__(self, other)`: Called by `y % x`.
    - `__rdiv__(self, other)`: Called by `y / x` (Python 2 only).
    - `__rfloordiv__(self, other)`: Called by `y // x`.
    - `__rtruediv__(self, other)`: Called by `y / x` (Python 3).
    - `__rpow__(self, other)`: Called by `y ** x`.

4. **Bitwise Operations**
    - `__and__(self, other)`: Called by `x & y`.
    - `__or__(self, other)`: Called by `x | y`.
    - `__xor__(self, other)`: Called by `x ^ y`.
    - `__lshift__(self, other)`: Called by `x << y`.
    - `__rshift__(self, other)`: Called by `x >> y`.

5. **Right Bitwise Operations**
    - `__rand__(self, other)`: Called by `y & x`.
    - `__ror__(self, other)`: Called by `y | x`.
    - `__rxor__(self, other)`: Called by `y ^ x`.
    - `__rlshift__(self, other)`: Called by `y << x`.
    - `__rrshift__(self, other)`: Called by `y >> x`.

6. **In-place Operations**
    - `__iadd__(self, other)`: Called by `x += y`.
    - `__isub__(self, other)`: Called by `x -= y`.
    - `__imul__(self, other)`: Called by `x *= y`.
    - `__imod__(self, other)`: Called by `x %= y`.
    - `__idiv__(self, other)`: Called by `x /= y` (Python 2 only).
    - `__ifloordiv__(self, other)`: Called by `x //= y`.
    - `__itruediv__(self, other)`: Called by `x /= y` (Python 3).
    - `__iand__(self, other)`: Called by `x &= y`.
    - `__ior__(self, other)`: Called by `x |= y`.
    - `__ixor__(self, other)`: Called by `x ^= y`.
    - `__ilshift__(self, other)`: Called by `x <<= y`.
    - `__irshift__(self, other)`: Called by `x >>= y`.
    - `__ipow__(self, other)`: Called by `x **= y`.

7. **Conversion Operations**
    - `__complex__(self)`: Called by `complex(x)`.
    - `__float__(self)`: Called by `float(x)`.
    - `__int__(self)`: Called by `int(x)`.
    - `__index__(self)`: Called by `hex(x)`, `oct(x)`, and slicing operations.

### Implementation of a Custom Numeric Class

Let's implement a custom numeric class that supports various numeric operations:

```python
class CustomNumber:
    def __init__(self, value):
        self.value = value

    # Unary operations
    def __abs__(self):
        return CustomNumber(abs(self.value))
    
    def __invert__(self):
        return CustomNumber(~self.value)
    
    def __neg__(self):
        return CustomNumber(-self.value)
    
    def __pos__(self):
        return CustomNumber(+self.value)
    
    # Binary operations
    def __add__(self, other):
        return CustomNumber(self.value + other.value)
    
    def __sub__(self, other):
        return CustomNumber(self.value - other.value)
    
    def __mul__(self, other):
        return CustomNumber(self.value * other.value)
    
    def __mod__(self, other):
        return CustomNumber(self.value % other.value)
    
    def __floordiv__(self, other):
        return CustomNumber(self.value // other.value)
    
    def __truediv__(self, other):
        return CustomNumber(self.value / other.value)
    
    def __pow__(self, other):
        return CustomNumber(self.value ** other.value)
    
    # Right binary operations
    def __radd__(self, other):
        return CustomNumber(other.value + self.value)
    
    def __rsub__(self, other):
        return CustomNumber(other.value - self.value)
    
    def __rmul__(self, other):
        return CustomNumber(other.value * self.value)
    
    def __rmod__(self, other):
        return CustomNumber(other.value % self.value)
    
    def __rfloordiv__(self, other):
        return CustomNumber(other.value // self.value)
    
    def __rtruediv__(self, other):
        return CustomNumber(other.value / self.value)
    
    def __rpow__(self, other):
        return CustomNumber(other.value ** self.value)
    
    # Bitwise operations
    def __and__(self, other):
        return CustomNumber(self.value & other.value)
    
    def __or__(self):
        return CustomNumber(self.value | other.value)
    
    def __xor__(self):
        return CustomNumber(self.value ^ other.value)
    
    def __lshift__(self, other):
        return CustomNumber(self.value << other.value)
    
    def __rshift__(self, other):
        return CustomNumber(self.value >> other.value)
    
    # Right bitwise operations
    def __rand__(self, other):
        return CustomNumber(other.value & self.value)
    
    def __ror__(self, other):
        return CustomNumber(other.value | self.value)
    
    def __rxor__(self, other):
        return CustomNumber(other.value ^ self.value)
    
    def __rlshift__(self, other):
        return CustomNumber(other.value << self.value)
    
    def __rrshift__(self, other):
        return CustomNumber(other.value >> self.value)
    
    # In-place operations
    def __iadd__(self, other):
        self.value += other.value
        return self
    
    def __isub__(self, other):
        self.value -= other.value
        return self
    
    def __imul__(self, other):
        self.value *= other.value
        return self
    
    def __imod__(self, other):
        self.value %= other.value
        return self
    
    def __ifloordiv__(self, other):
        self.value //= other.value
        return self
    
    def __itruediv__(self, other):
        self.value /= other.value
        return self
    
    def __iand__(self, other):
        self.value &= other.value
        return self
    
    def __ior__(self, other):
        self.value |= other.value
        return self
    
    def __ixor__(self, other):
        self.value ^= other.value
        return self
    
    def __ilshift__(self, other):
        self.value <<= other.value
        return self
    
    def __irshift__(self, other):
        self.value >>= other.value
        return self
    
    def __ipow__(self, other):
        self.value **= other.value
        return self
    
    # Conversion operations
    def __complex__(self):
        return complex(self.value)
    
    def __float__(self):
        return float(self.value)
    
    def __int__(self):
        return int(self.value)
    
    def __index__(self):
        return self.value
    
    def __repr__(self):
        return f'CustomNumber({self.value})'

# Example usage
a = CustomNumber(10)
b = CustomNumber(3)

# Unary operations
print(abs(a))  # Output: CustomNumber(10)
print(~a)

      # Output: CustomNumber(-11)
print(-a)      # Output: CustomNumber(-10)
print(+a)      # Output: CustomNumber(10)

# Binary operations
print(a + b)   # Output: CustomNumber(13)
print(a - b)   # Output: CustomNumber(7)
print(a * b)   # Output: CustomNumber(30)
print(a % b)   # Output: CustomNumber(1)
print(a // b)  # Output: CustomNumber(3)
print(a / b)   # Output: CustomNumber(3.3333333333333335)
print(a ** b)  # Output: CustomNumber(1000)

# Right binary operations
print(b + a)   # Output: CustomNumber(13)
print(b - a)   # Output: CustomNumber(-7)
print(b * a)   # Output: CustomNumber(30)
print(b % a)   # Output: CustomNumber(3)
print(b // a)  # Output: CustomNumber(0)
print(b / a)   # Output: CustomNumber(0.3)
print(b ** a)  # Output: CustomNumber(59049)

# Bitwise operations
print(a & b)   # Output: CustomNumber(2)
print(a | b)   # Output: CustomNumber(11)
print(a ^ b)   # Output: CustomNumber(9)
print(a << b)  # Output: CustomNumber(80)
print(a >> b)  # Output: CustomNumber(1)

# In-place operations
a += b
print(a)       # Output: CustomNumber(13)
a -= b
print(a)       # Output: CustomNumber(10)
a *= b
print(a)       # Output: CustomNumber(30)
a //= b
print(a)       # Output: CustomNumber(10)
a /= b
print(a)       # Output: CustomNumber(3.3333333333333335)

# Conversion operations
print(float(a))  # Output: 3.3333333333333335
print(int(a))    # Output: 3
print(complex(a))# Output: (3.3333333333333335+0j)
print(hex(a))    # Output: 0x3
```

### Updated README

```markdown
# CustomNumber Class

The `CustomNumber` class is a custom implementation of numeric operations in Python. It leverages special methods to support arithmetic, bitwise, in-place, and conversion operations, enabling instances to behave similarly to built-in numeric types.

## Methods Implemented

1. **Unary Operations**
    - `__abs__(self)`: Called by `abs(x)`.
    - `__invert__(self)`: Called by `~x`.
    - `__neg__(self)`: Called by `-x`.
    - `__pos__(self)`: Called by `+x`.

2. **Binary Operations**
    - `__add__(self, other)`: Called by `x + y`.
    - `__sub__(self, other)`: Called by `x - y`.
    - `__mul__(self, other)`: Called by `x * y`.
    - `__mod__(self, other)`: Called by `x % y`.
    - `__floordiv__(self, other)`: Called by `x // y`.
    - `__truediv__(self, other)`: Called by `x / y`.
    - `__pow__(self, other[, modulo])`: Called by `x ** y`.

3. **Right Binary Operations**
    - `__radd__(self, other)`: Called by `y + x`.
    - `__rsub__(self, other)`: Called by `y - x`.
    - `__rmul__(self, other)`: Called by `y * x`.
    - `__rmod__(self, other)`: Called by `y % x`.
    - `__rfloordiv__(self, other)`: Called by `y // x`.
    - `__rtruediv__(self, other)`: Called by `y / x`.
    - `__rpow__(self, other)`: Called by `y ** x`.

4. **Bitwise Operations**
    - `__and__(self, other)`: Called by `x & y`.
    - `__or__(self, other)`: Called by `x | y`.
    - `__xor__(self, other)`: Called by `x ^ y`.
    - `__lshift__(self, other)`: Called by `x << y`.
    - `__rshift__(self, other)`: Called by `x >> y`.

5. **Right Bitwise Operations**
    - `__rand__(self, other)`: Called by `y & x`.
    - `__ror__(self, other)`: Called by `y | x`.
    - `__rxor__(self, other)`: Called by `y ^ x`.
    - `__rlshift__(self, other)`: Called by `y << x`.
    - `__rrshift__(self, other)`: Called by `y >> x`.

6. **In-place Operations**
    - `__iadd__(self, other)`: Called by `x += y`.
    - `__isub__(self, other)`: Called by `x -= y`.
    - `__imul__(self, other)`: Called by `x *= y`.
    - `__imod__(self, other)`: Called by `x %= y`.
    - `__ifloordiv__(self, other)`: Called by `x //= y`.
    - `__itruediv__(self, other)`: Called by `x /= y`.
    - `__iand__(self, other)`: Called by `x &= y`.
    - `__ior__(self, other)`: Called by `x |= y`.
    - `__ixor__(self, other)`: Called by `x ^= y`.
    - `__ilshift__(self, other)`: Called by `x <<= y`.
    - `__irshift__(self, other)`: Called by `x >>= y`.
    - `__ipow__(self, other)`: Called by `x **= y`.

7. **Conversion Operations**
    - `__complex__(self)`: Called by `complex(x)`.
    - `__float__(self)`: Called by `float(x)`.
    - `__int__(self)`: Called by `int(x)`.
    - `__index__(self)`: Called by `hex(x)`, `oct(x)`, and slicing operations.

## Example Usage

### Creating an Instance

```python
from custom_number import CustomNumber

a = CustomNumber(10)
b = CustomNumber(3)
```

### Unary Operations

```python
print(abs(a))  # Output: CustomNumber(10)
print(~a)      # Output: CustomNumber(-11)
print(-a)      # Output: CustomNumber(-10)
print(+a)      # Output: CustomNumber(10)
```

### Binary Operations

```python
print(a + b)   # Output: CustomNumber(13)
print(a - b)   # Output: CustomNumber(7)
print(a * b)   # Output: CustomNumber(30)
print(a % b)   # Output: CustomNumber(1)
print(a // b)  # Output: CustomNumber(3)
print(a / b)   # Output: CustomNumber(3.3333333333333335)
print(a ** b)  # Output: CustomNumber(1000)
```

### Right Binary Operations

```python
print(b + a)   # Output: CustomNumber(13)
print(b - a)   # Output: CustomNumber(-7)
print(b * a)   # Output: CustomNumber(30)
print(b % a)   # Output: CustomNumber(3)
print(b // a)  # Output: CustomNumber(0)
print(b / a)   # Output: CustomNumber(0.3)
print(b ** a)  # Output: CustomNumber(59049)
```

### Bitwise Operations

```python
print(a & b)   # Output: CustomNumber(2)
print(a | b)   # Output: CustomNumber(11)
print(a ^ b)   # Output: CustomNumber(9)
print(a << b)  # Output: CustomNumber(80)
print(a >> b)  # Output: CustomNumber(1)
```

### In-place Operations

```python
a += b
print(a)       # Output: CustomNumber(13)
a -= b
print(a)       # Output: CustomNumber(10)
a *= b
print(a)       # Output: CustomNumber(30)
a //= b
print(a)       # Output: CustomNumber(10)
a /= b
print(a)       # Output: CustomNumber(3.3333333333333335)
```

### Conversion Operations

```python
print(float(a))  # Output: 3.3333333333333335
print(int(a))    # Output: 3
print(complex(a))# Output: (3.3333333333333335+0j)
print(hex(a))    # Output: 0x3
```

## Class Implementation

```python
class CustomNumber:
    def __init__(self, value):
        self.value = value

    # Unary operations
    def __abs__(self):
        return CustomNumber(abs(self.value))
    
    def __invert__(self):
        return CustomNumber

(~self.value)
    
    def __neg__(self):
        return CustomNumber(-self.value)
    
    def __pos__(self):
        return CustomNumber(+self.value)
    
    # Binary operations
    def __add__(self, other):
        return CustomNumber(self.value + other.value)
    
    def __sub__(self, other):
        return CustomNumber(self.value - other.value)
    
    def __mul__(self, other):
        return CustomNumber(self.value * other.value)
    
    def __mod__(self, other):
        return CustomNumber(self.value % other.value)
    
    def __floordiv__(self, other):
        return CustomNumber(self.value // other.value)
    
    def __truediv__(self, other):
        return CustomNumber(self.value / other.value)
    
    def __pow__(self, other):
        return CustomNumber(self.value ** other.value)
    
    # Right binary operations
    def __radd__(self, other):
        return CustomNumber(other.value + self.value)
    
    def __rsub__(self, other):
        return CustomNumber(other.value - self.value)
    
    def __rmul__(self, other):
        return CustomNumber(other.value * self.value)
    
    def __rmod__(self, other):
        return CustomNumber(other.value % self.value)
    
    def __rfloordiv__(self, other):
        return CustomNumber(other.value // self.value)
    
    def __rtruediv__(self, other):
        return CustomNumber(other.value / self.value)
    
    def __rpow__(self, other):
        return CustomNumber(other.value ** self.value)
    
    # Bitwise operations
    def __and__(self, other):
        return CustomNumber(self.value & other.value)
    
    def __or__(self):
        return CustomNumber(self.value | other.value)
    
    def __xor__(self):
        return CustomNumber(self.value ^ other.value)
    
    def __lshift__(self, other):
        return CustomNumber(self.value << other.value)
    
    def __rshift__(self, other):
        return CustomNumber(self.value >> other.value)
    
    # Right bitwise operations
    def __rand__(self, other):
        return CustomNumber(other.value & self.value)
    
    def __ror__(self, other):
        return CustomNumber(other.value | self.value)
    
    def __rxor__(self, other):
        return CustomNumber(other.value ^ self.value)
    
    def __rlshift__(self, other):
        return CustomNumber(other.value << self.value)
    
    def __rrshift__(self, other):
        return CustomNumber(other.value >> self.value)
    
    # In-place operations
    def __iadd__(self, other):
        self.value += other.value
        return self
    
    def __isub__(self, other):
        self.value -= other.value
        return self
    
    def __imul__(self, other):
        self.value *= other.value
        return self
    
    def __imod__(self, other):
        self.value %= other.value
        return self
    
    def __ifloordiv__(self, other):
        self.value //= other.value
        return self
    
    def __itruediv__(self, other):
        self.value /= other.value
        return self
    
    def __iand__(self, other):
        self.value &= other.value
        return self
    
    def __ior__(self, other):
        self.value |= other.value
        return self
    
    def __ixor__(self, other):
        self.value ^= other.value
        return self
    
    def __ilshift__(self, other):
        self.value <<= other.value
        return self
    
    def __irshift__(self, other):
        self.value >>= other.value
        return self
    
    def __ipow__(self, other):
        self.value **= other.value
        return self
    
    # Conversion operations
    def __complex__(self):
        return complex(self.value)
    
    def __float__(self):
        return float(self.value)
    
    def __int__(self):
        return int(self.value)
    
    def __index__(self):
        return self.value
    
    def __repr__(self):
        return f'CustomNumber({self.value})'
```
