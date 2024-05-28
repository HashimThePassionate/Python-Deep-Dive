### Access Modifiers in OOP

Access modifiers in Object-Oriented Programming (OOP) are keywords used to set the accessibility of classes, methods, and other members. They control how the members of a class can be accessed from outside the class. The most common access modifiers are:

1. **Public:** Members are accessible from anywhere.
2. **Protected:** Members are accessible within the same class and by derived class instances.
3. **Private:** Members are accessible only within the same class.

### Why We Use Private Access Modifier

The **private** access modifier is used to restrict access to certain members of a class. This encapsulation provides several benefits:

1. **Encapsulation:** It hides the internal state and requires all interaction to be performed through an object's methods, improving the modularity and maintainability of the code.
2. **Data Integrity:** By restricting direct access to class variables, it ensures that data is not modified directly, thereby protecting the integrity of the data.
3. **Controlled Access:** It allows the class to control how its data is accessed and modified, ensuring that changes occur in a controlled manner.

### Private Access Modifier in Python

In Python, private members are denoted by prefixing the member name with double underscores (`__`). This name mangling makes it harder (but not impossible) to access private members from outside the class.

Here is the provided Python code illustrating the use of private access modifiers:

```python
class PrivateAccessError(Exception):
    pass


class UIControl:
    def __init__(self, is_enabled=True):
        self.__is_enabled = is_enabled

    def enable(self):
        self.__is_enabled = True
        return f'Dynamically Call to Enable Method with attribute : {self.__is_enabled}'

    def __disable(self):
        self.__is_enabled = False
        return f'Dynamically Call to __disable Method with attribute : {self.__is_enabled}'

    def __is_enabled(self):
        return self.__is_enabled

    def access_private(self, attribute):
        if attribute == "__is_enabled":
            raise PrivateAccessError(f"Access to private attribute '{attribute}' is not allowed.")
        else:
            return getattr(self, attribute)

    def call_private(self, method):
        if method == "__disable" or method == "__is_enabled":
            raise PrivateAccessError(f"Access to private method '{method}' is not allowed.")
        else:
            return getattr(self, method)()


class TextBox(UIControl):
    def __init__(self):
        super().__init__(True)
        self.__text = ""

    def set_text(self, text):
        self.__text = text

    def clear(self):
        self.__text = ""

    def access_private(self, attribute):
        if attribute == "__text":
            raise PrivateAccessError(f"Access to private attribute '{attribute}' is not allowed.")
        else:
            return super().access_private(attribute)


# Creating an instance of TextBox
control = TextBox()
c = UIControl()
access = c.access_private('enable')
print(access())

# Attempting to access private method and raising an error
try:
    control._UIControl__disable()  # Forcefully accessing private method
except AttributeError:
    print("Direct access to private methods is not allowed.")

# Attempting to access private method using call_private method
try:
    control.call_private("__disable")
except PrivateAccessError as e:
    print(e)

# Attempting to access private attribute and raising an error
try:
    control.access_private("__is_enabled")
except PrivateAccessError as e:
    print(e)

# Checking if control is enabled
# Access private member indirectly
print(control.access_private("_UIControl__is_enabled"))
```

### Explanation of the Code

1. **PrivateAccessError:** Custom exception for handling access to private members.
2. **UIControl Class:**
   - `__init__`: Initializes the private attribute `__is_enabled`.
   - `enable`: Public method to enable the control.
   - `__disable`: Private method to disable the control.
   - `__is_enabled`: Private method to check if the control is enabled.
   - `access_private` and `call_private`: Methods to safely access private attributes and methods, raising exceptions if access to private members is attempted.
3. **TextBox Class:**
   - Inherits from `UIControl`.
   - Adds a private attribute `__text`.
   - Overrides `access_private` to handle `__text` attribute specifically.
4. **Main Execution:**
   - Creates instances of `UIControl` and `TextBox`.
   - Demonstrates safe access to public methods.
   - Attempts to access private methods and attributes both directly and via provided methods, catching and printing exceptions.

### Explanation of `getattr(self, method)()`

In Python, `getattr` can be used to dynamically access methods and attributes of an object. Let's break down `getattr(self, method)()` step by step:

1. **`getattr(self, method)`**:
   - `self`: Refers to the current instance of the class.
   - `method`: A string representing the name of the method you want to access dynamically.
   - `getattr(self, method)`: Retrieves the method from the instance `self` by its name `method`. If `method` is the name of a method defined in the class, `getattr` will return a reference to that method.

2. **`getattr(self, method)()`**:
   - After retrieving the method using `getattr`, adding `()` immediately after it calls the method. This is because the parentheses `()` in Python are used to call functions and methods.

### Detailed Breakdown with Example

Here’s a simplified example to illustrate this:

```python
class MyClass:
    def greet(self):
        return "Hello, World!"

    def farewell(self):
        return "Goodbye, World!"

    def dynamic_call(self, method_name):
        # Use getattr to retrieve the method by name and then call it
        method = getattr(self, method_name)
        return method()

# Create an instance of MyClass
obj = MyClass()

# Call the dynamic_call method with different method names
print(obj.dynamic_call('greet'))     # Output: Hello, World!
print(obj.dynamic_call('farewell'))  # Output: Goodbye, World!
```

### Explanation of the Example

1. **Class Definition**:
   - `MyClass` has two methods: `greet` and `farewell`.
   - `dynamic_call` method takes `method_name` as a parameter, which is a string representing the name of the method to call.

2. **Using `getattr`**:
   - `method = getattr(self, method_name)`: This line dynamically retrieves the method from the instance `self` using the name provided in `method_name`.
   - If `method_name` is `'greet'`, then `method` will be a reference to `self.greet`.
   - If `method_name` is `'farewell'`, then `method` will be a reference to `self.farewell`.

3. **Calling the Method**:
   - `method()`: Calls the retrieved method. Since `method` is a reference to either `greet` or `farewell`, calling `method()` will execute the corresponding method.

### Application to Our  `call_private`

In the provided `UIControl` class, the `call_private` method demonstrates dynamic method access using `getattr`:

```python
def call_private(self, method):
    if method == "__disable" or method == "__is_enabled":
        raise PrivateAccessError(f"Access to private method '{method}' is not allowed.")
    else:
        return getattr(self, method)()
```

1. **Parameter Check**:
   - The method name is checked to see if it matches any private method names that are restricted.
   - If it matches `__disable` or `__is_enabled`, a `PrivateAccessError` is raised.

2. **Dynamic Method Access**:
   - `getattr(self, method)`: Retrieves the method from the instance `self` using the name provided in `method`.
   - `()`: Immediately calls the retrieved method.
   - For example, if `method` is `'enable'`, `getattr(self, method)` retrieves `self.enable`, and `getattr(self, method)()` calls `self.enable()`.

### Summary

Using `getattr(self, method)()`, you can dynamically access and call methods on an object. This approach is particularly useful when the method names are determined at runtime, making your code more flexible and dynamic.