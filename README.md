# Python-Deep-Dive

Welcome to **Python Deep Dive**, a comprehensive repository designed to take you on a journey through the entire spectrum of Python programming. This repository is structured to guide you from the fundamentals, through object-oriented programming (OOP), into data structures and algorithms, advanced Python concepts, and finally to the 23 classic design patterns. Additionally, it includes insights into CPython compilation to help you become a Python contributor.

## Table of Contents
1. [Fundamentals](#fundamentals)
2. [Object-Oriented Programming (OOP)](#object-oriented-programming-oop)
3. [Data Structures](#data-structures)
4. [Algorithms](#algorithms)
5. [Design Patterns](#design-patterns)
6. [Advanced Python Deep Dive](#advanced-python-deep-dive)
7. [Compiling CPython](#compiling-cpython)
8. [Contributing](#contributing)
9. [Credit](#Credits)
10. [License](#license)

## Fundamentals
In this section, you'll learn the basics of Python, including:
- Syntax and structure
- Data types and variables
- Control flow (loops and conditionals)
- Functions and modules
- Error handling and exceptions

Start here if you're new to Python or need a refresher on the basics.

## Object-Oriented Programming (OOP)
This section dives into OOP concepts in Python. You'll explore:
- Classes and objects
- Inheritance and polymorphism
- Encapsulation and abstraction
- Dependency injection
- Class-level and instance-level attributes

Learn how to design robust object-oriented applications in Python.

## Data Structures
Here, you'll discover the built-in and custom data structures used in Python, including:
- Lists, tuples, sets, and dictionaries
- Stacks and queues
- Linked lists
- Trees and graphs
- Heaps and hash tables

Understanding these structures is crucial for building efficient and scalable applications.

## Algorithms
In this section, you'll find various algorithms implemented in Python, covering:
- Sorting algorithms (bubble sort, quicksort, mergesort, etc.)
- Searching algorithms (binary search, linear search, etc.)
- Recursion and iterative solutions
- Graph traversal algorithms (DFS, BFS, Dijkstra's algorithm, etc.)
- Dynamic programming and greedy algorithms

These algorithms form the backbone of many computer science problems and interview questions.

## Design Patterns
Finally, explore the 23 classic design patterns from the "Gang of Four," with Python implementations, including:
- Creational patterns (Singleton, Factory, Builder, Prototype, Abstract Factory)
- Structural patterns (Adapter, Composite, Bridge, Decorator, Facade, Flyweight, Proxy)
- Behavioral patterns (Chain of Responsibility, Command, Interpreter, Iterator, Mediator, Memento, Observer, State, Strategy, Template Method, Visitor)

Learn how these patterns can be applied to solve common software design challenges.

## Advanced Python Deep Dive
In this section, you'll delve into advanced topics to deepen your understanding of Python:
### Part I. Data Structures
1. The Python Data Model
   - A Pythonic Card Deck
   - How Special Methods Are Used
   - Emulating Numeric Types
   - String Representation
   - Boolean Value of a Custom Type
   - Collection API
   - Overview of Special Methods
   - Why `len` Is Not a Method
2. An Array of Sequences
   - Overview of Built-In Sequences
   - List Comprehensions and Generator Expressions
   - Tuples as Records and Immutable Lists
   - Pattern Matching with Sequences
   - Slicing
   - Arrays, Memory Views, and NumPy
   - Deques and Other Queues
3. Dictionaries and Sets
   - Modern `dict` Syntax
   - Pattern Matching with Mappings
   - Practical Consequences of How `dict` and Sets Work
4. Unicode Text Versus Bytes
   - Character Issues
   - Byte Essentials
   - Handling Text Files
   - Normalizing Unicode for Reliable Comparisons
5. Data Class Builders
   - Overview of Data Class Builders
   - Classic Named Tuples and Typed Named Tuples
   - More About `@dataclass`
6. Object References, Mutability, and Recycling
   - Variables Are Not Boxes
   - Identity, Equality, and Aliases
   - Shallow and Deep Copies
   - Garbage Collection

### Part II. Functions as Objects
7. Functions as First-Class Objects
   - Treating a Function Like an Object
   - Higher-Order Functions
   - Modern Replacements for `map`, `filter`, and `reduce`
   - Anonymous Functions
   - User-Defined Callable Types
8. Type Hints in Functions
   - About Gradual Typing
   - Starting with Mypy
   - Types Usable in Annotations
   - Static Protocols
9. Decorators and Closures
   - Decorators 101
   - Variable Scope Rules
   - Closures and the `nonlocal` Declaration
   - Implementing a Simple Decorator
   - Memoization with `functools.cache`
10. Design Patterns with First-Class Functions
    - Case Study: Refactoring Strategy
    - Function-Oriented Strategy
    - The Command Pattern

### Part III. Classes and Protocols
11. A Pythonic Object
    - Object Representations
    - Formatted Displays
    - A Hashable Vector2d
    - Saving Memory with `__slots__`
12. Special Methods for Sequences
    - Vector: A User-Defined Sequence Type
    - Protocols and Duck Typing
    - Vector Take #4: Hashing and a Faster `==`
13. Interfaces, Protocols, and ABCs
    - Two Kinds of Protocols
    - Defensive Programming and “Fail Fast”
    - Structural Typing with ABCs
14. Inheritance: For Better or for Worse
    - The `super()` Function
    - Multiple Inheritance and Method Resolution Order
    - Coping with Inheritance
15. More About Type Hints
    - Overloaded Signatures
    - Variance and Generic Types
16. Operator Overloading
    - Operator Overloading 101
    - Rich Comparison Operators

### Part IV. Control Flow
17. Iterators, Generators, and Classic Coroutines
    - Using `iter` with a Callable
    - Generator Functions in the Standard Library
    - Classic Coroutines
18. with, match, and else Blocks
    - Context Managers and `with` Blocks
    - Pattern Matching in lis.py: A Case Study
19. Concurrency Models in Python
    - Processes, Threads, and Python’s Infamous GIL
    - Spinner with Threads, Processes, and Coroutines
20. Concurrent Executors
    - Concurrent Web Downloads
    - Launching Processes with `concurrent.futures`
21. Asynchronous Programming
    - An asyncio Example: Probing Domains
    - Downloading with asyncio and HTTPX

### Part V. Metaprogramming
22. Dynamic Attributes and Properties
    - Data Wrangling with Dynamic Attributes
    - Flexible Object Creation with `__new__`
    - Using a Property for Attribute Validation
23. Attribute Descriptors
    - Descriptor Example: Attribute Validation
    - Overriding Descriptors
24. Class Metaprogramming
    - Classes as Objects
    - type: The Built-In Class Factory
    - Metaclasses

## Compiling CPython
In this section, you'll learn about contributing to Python by compiling CPython:
1. Compiling CPython
   - Compiling CPython on macOS
   - Compiling CPython on Linux
   - Installing a Custom Version
   - A Quick Primer on Make
   - CPython’s Make Targets
   - Compiling CPython on Windows
   - Profile-Guided Optimization
2. The Python Language and Grammar
   - Why CPython Is Written in C and Not Python
   - The Python Language Specification
   - The Parser Generator
   - Regenerating Grammar
3. Configuration and Input
   - Configuration State
   - Build Configuration
   - Building a Module From Input
4. Lexing and Parsing With Syntax Trees
   - Concrete Syntax Tree Generation
   - The CPython Parser-Tokenizer
   - Abstract Syntax Trees
   - Example: Adding an Almost-Equal Comparison Operator
5. The Compiler
   - Instantiating a Compiler
   - Core Compilation Process
   - Assembly
   - Creating a Code Object
   - Example: Implementing the Almost-Equal Operator
6. The Evaluation Loop
   - Constructing Thread State
   - Frame Execution
   - The Value Stack
   - Example: Adding an Item to a List
7. Memory Management
   - Memory Allocation in C
   - The CPython Memory Allocator
   - Reference Counting
   - Garbage Collection
8. Parallelism and Concurrency
   - Models of Parallelism and Concurrency
   - Multiprocess Parallelism
   - Multithreading
   - Asynchronous Programming
9. Objects and Types
   - Built-in Types
   - Object and Variable Object Types
   - The `type` Type
   - The Unicode String Type
   - The Dictionary Type
10. The Standard Library
    - Python Modules
    - Python and C Modules
11. The Test Suite
    - Running the Test Suite on Various OS
    - Test Flags and Utilities
12. Debugging
    - Using the Crash Handler
    - Compiling Debug Support
    - Using Debuggers (LLDB, GDB, Visual Studio, CLion)
13. Benchmarking, Profiling, and Tracing
    - Using `timeit` for Microbenchmarks
    - Using

 the Python Benchmark Suite for Runtime Benchmarks
    - Profiling Python Code with `cProfile`
    - Profiling C Code with `DTrace`
14. Next Steps
    - Writing C Extensions for CPython
    - Improving Your Python Applications
    - Contributing to the CPython Project
15. Appendix: Introduction to C for Python Programmers
    - The C Preprocessor
    - Basic C Syntax

## Contributing
Contributions are welcome! If you'd like to contribute to this repository, please follow these steps:
1. Fork this repository.
2. Create a new branch with your changes.
3. Open an issue first to discuss the changes you want to make.
4. After the discussion, submit a pull request with a detailed explanation of your contribution.

For major changes, please ensure that the issue is thoroughly discussed before starting the implementation.

## Credits
Some examples and inspiration in this repository are taken from the book *Fluent Python* by Luciano Ramalho.

- **Book Title**: Fluent Python
- **Author**: Luciano Ramalho
- **Copyright**: © 2022 Luciano Ramalho. All rights reserved.
- **Publisher**: O’Reilly Media, Inc.
For more information, you can visit the [O'Reilly website](http://oreilly.com).


## License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

Thank you for exploring Python Deep Dive! If you have any questions, suggestions, or feedback, feel free to open an issue or contact. </br>
Regards: **Muhammad Hashim**
