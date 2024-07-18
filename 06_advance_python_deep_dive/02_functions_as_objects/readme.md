# Functions as Objects

## In this section we will explore these topics
1. Functions as First-Class Objects
   - Treating a Function Like an Object
   - Higher-Order Functions
   - Modern Replacements for `map`, `filter`, and `reduce`
   - Anonymous Functions
   - The Nine Flavors of Callable Objects
   - User-Defined Callable Types
   - From Positional to Keyword-Only Parameters
   - Positional-Only Parameters
   - Packages for Functional Programming
   - The `operator` Module
   - Freezing Arguments with `functools.partial`
   - Section Summary
   - Further Reading
2. Type Hints in Functions
   - About Gradual Typing
   - Gradual Typing in Practice
   - Starting with Mypy
   - Making Mypy More Strict
   - A Default Parameter Value
   - Using None as a Default
   - Types Are Defined by Supported Operations
   - Types Usable in Annotations
   - The Any Type
   - Simple Types and Classes
   - Optional and Union Types
   - Generic Collections
   - Tuple Types
   - Generic Mappings
   - Abstract Base Classes
   - Iterable
   - Parameterized Generics and TypeVar
   - Static Protocols
   - Callable
   - NoReturn
   - Annotating Positional Only and Variadic Parameters
   - Imperfect Typing and Strong Testing
   - Section Summary
   - Further Reading
3. Decorators and Closures
   - Decorators 101
   - When Python Executes Decorators
   - Registration Decorators
   - Variable Scope Rules
   - Closures
   - The `nonlocal` Declaration
   - Variable Lookup Logic
   - Implementing a Simple Decorator
   - How It Works
   - Decorators in the Standard Library
   - Memoization with `functools.cache`
   - Using `lru_cache`
   - Single Dispatch Generic Functions
   - Parameterized Decorators
   - A Parameterized Registration Decorator
   - The Parameterized Clock Decorator
   - A Class-Based Clock Decorator
   - Section Summary
   - Further Reading
4. Design Patterns with First-Class Functions
   - Case Study: Refactoring Strategy
   - Classic Strategy
   - Function-Oriented Strategy
   - Choosing the Best Strategy: Simple Approach
   - Finding Strategies in a Module
   - Decorator-Enhanced Strategy Pattern
   - The Command Pattern
   - Section Summary
   - Further Reading

---

## Functions as First-Class Objects
### Treating a Function Like an Object
Functions in Python can be treated like objects. This means you can assign them to variables, pass them as arguments to other functions, and return them from other functions.

### Higher-Order Functions
A higher-order function is a function that takes one or more functions as arguments or returns a function as its result.

### Modern Replacements for `map`, `filter`, and `reduce`
Python provides modern alternatives to the `map`, `filter`, and `reduce` functions using list comprehensions, generator expressions, and the `functools.reduce` function.

#### List Comprehensions

#### Generator Expressions

#### `functools.reduce`

### Anonymous Functions
Anonymous functions in Python are defined using the `lambda` keyword.

### The Nine Flavors of Callable Objects
In Python, there are nine types of callable objects. These include:
1. User-defined functions
2. Built-in functions
3. Methods
4. Classes
5. Instances of classes with a `__call__` method
6. Generators
7. Coroutines
8. Asynchronous generators
9. Standard library callable objects like `functools.partial`

### User-Defined Callable Types
You can create your own callable objects by defining the `__call__` method in a class.

### From Positional to Keyword-Only Parameters
Python allows defining parameters that must be specified using keyword arguments.

### Positional-Only Parameters
Python 3.8 introduced positional-only parameters, which must be specified positionally and cannot be passed as keyword arguments.

### Packages for Functional Programming
Python provides several packages for functional programming, such as:
- `functools`
- `itertools`
- `operator`

### The `operator` Module
The `operator` module provides function equivalents for many arithmetic and comparison operators.

### Freezing Arguments with `functools.partial`
The `functools.partial` function allows you to fix a certain number of arguments of a function and generate a new function.

### Section Summary
This section covered various aspects of treating functions as first-class objects, including higher-order functions, anonymous functions, and callable objects. It also explored modern replacements for `map`, `filter`, and `reduce`, as well as packages and modules for functional programming.

### Further Reading
To deepen your understanding, consider exploring additional resources and documentation on functional programming and callable objects in Python.

---

## Type Hints in Functions
### About Gradual Typing
Gradual typing allows you to incrementally add type annotations to your Python code, which helps in catching errors early and improving code readability.

### Gradual Typing in Practice
You can start adding type annotations to your existing Python code without needing to annotate everything at once.

### Starting with Mypy
Mypy is a static type checker for Python. You can use it to check your type annotations.

### Making Mypy More Strict
Mypy can be configured to be more strict about type checking.

### A Default Parameter Value
You can provide default values for parameters in function definitions.

### Using None as a Default
Using `None` as a default value can be useful for optional parameters.

### Types Are Defined by Supported Operations
Types in Python are defined by the operations they support, rather than their inheritance.

### Types Usable in Annotations
Python provides various types that can be used in annotations, including built-in types and those from the `typing` module.

### The Any Type
The `Any` type can be used when you do not want to impose any type restrictions.

### Simple Types and Classes
You can use simple types like `int`, `str`, and custom classes in type annotations.

### Optional and Union Types
The `Optional` and `Union` types allow specifying that a value can be one of multiple types.

### Generic Collections
You can specify types for elements within collections using generics.

### Tuple Types
Tuples can have their types specified for each element.

### Generic Mappings
Generic mappings allow specifying types for both keys and values in a mapping.

### Abstract Base Classes
Abstract Base Classes (ABCs) can be used to define interfaces that other classes must implement.

### Iterable
The `Iterable` type indicates that an object can be iterated over.

### Parameterized Generics and TypeVar
Parameterized generics and `TypeVar` allow creating functions and classes that can operate on a variety of types.

### Static Protocols
Static protocols define a set of methods that a class must implement.

### Callable
The `Callable` type indicates that an object can be called like a function.

### NoReturn
The `NoReturn` type indicates that a function does not return a value.

### Annotating Positional Only and Variadic Parameters
You can annotate positional-only and variadic parameters in functions.

### Imperfect Typing and Strong Testing
While type hints can help catch many errors, they are not a substitute for thorough testing.

### Section Summary
This section introduced type hints in Python, covering gradual typing, mypy, various types, and how to use them effectively to improve code quality and readability.

### Further Reading
For more information, explore additional resources on type hints, static type checking, and the `typing` module in Python.

---

## Decorators and Closures
### Decorators 101
Decorators are functions that modify the behavior of other functions or classes. They are often used to add functionality to existing code in a clean and readable manner.

### When Python Executes Decorators
Decorators are executed when the function they decorate is defined, not when it is called.

### Registration Decorators
Registration decorators can be used to register functions for later use.

### Variable Scope Rules
Python has specific rules for variable scope, which are important to understand when working with decorators and closures.

### Closures
A closure is a function that remembers the values from its enclosing lexical scope even when the program flow is no longer in that scope.

### The `nonlocal` Declaration
The `nonlocal` keyword allows you to assign values to variables in an outer (but not global) scope.

### Variable Lookup Logic
Python follows the LEGB (Local, Enclosing, Global, Built-in) rule for variable lookup.

### Implementing a Simple Decorator
You can implement your own decorators to add functionality to existing functions.

### How It Works
Decorators work by wrapping the original function with another function that adds the desired functionality.

### Decorators in the Standard Library
Python's standard library includes several useful decorators, such as `@staticmethod`, `@classmethod`, and `@property`.

### Memoization with `functools.cache`
Memoization is an optimization technique that stores the results of expensive function calls and returns the cached result when the same inputs occur again.

### Using `lru_cache`
The `lru_cache` decorator caches the results of a function based on the least recently used (LRU) strategy.

### Single Dispatch Generic Functions
Single dispatch allows you to define generic functions that perform different operations based on the type of the first argument.

### Parameterized Decorators
Parameterized decorators accept arguments that customize their behavior.

### A Parameterized Registration Decorator
You can create a parameterized decorator that registers functions with specific parameters.

### The Parameterized Clock Decorator
A clock decorator can be parameterized to measure the execution time of functions.

### A Class-Based Clock Decorator
You can implement a

 clock decorator using a class.

### Section Summary
This section introduced decorators and closures, covering their basic concepts, usage, and implementation. It also explored various types of decorators, including those in the standard library, and explained the concept of memoization and single dispatch generic functions.

### Further Reading
For additional information, consider exploring more resources on decorators, closures, and functional programming in Python.

---

## Design Patterns with First-Class Functions
### Case Study: Refactoring Strategy
This section explores a case study on refactoring a strategy pattern using first-class functions.

### Classic Strategy
The classic strategy pattern involves defining a family of algorithms, encapsulating each one, and making them interchangeable.

### Function-Oriented Strategy
The function-oriented strategy pattern simplifies the classic strategy pattern by using functions instead of classes.

### Choosing the Best Strategy: Simple Approach
Choosing the best strategy can be simplified using dictionaries or other data structures.

### Finding Strategies in a Module
You can dynamically find and execute strategies defined in a module.

### Decorator-Enhanced Strategy Pattern
The decorator pattern can enhance the strategy pattern by adding additional behavior.

### The Command Pattern
The command pattern encapsulates a request as an object, thereby allowing for parameterization of clients with queues, requests, and operations.

### Section Summary
This section explored various design patterns that leverage first-class functions, including strategy patterns and command patterns. It also demonstrated how decorators can enhance these patterns.

### Further Reading
For more detailed information, consider exploring resources on design patterns and functional programming in Python.
