# **Python’s Collections Module** 📦🐍

The **collections** module in Python offers specialized container data types that extend the functionality of Python’s built-in types. These containers provide powerful alternatives and enhancements for handling data in your applications. Let’s dive into how these containers work, and also review the fundamental concepts of modules, packages, and scripts.

---

## **Understanding Modules, Packages, and Scripts** 📜🔍

- **Module:**  
  A module is a Python file (with a `.py` extension) that contains functions, classes, and variables. It encapsulates reusable code.  
  ```python
  # Example of a simple module: my_module.py
  def greet(name):
      return f"Hello, {name}!"
  ```
  **Explanation:**  
  1. **`def greet(name):`**  
     👉 Defines a function `greet` that takes a parameter `name`.  
  2. **`return f"Hello, {name}!"`**  
     👉 Returns a greeting string using an f-string.

- **Package:**  
  A package is a directory containing a collection of modules. It must include an `__init__.py` file to be recognized as a package by the Python interpreter.  
  ```python
  # Directory structure:
  # my_package/
  # ├── __init__.py
  # └── module1.py
  ```
  **Explanation:**  
  1. **`__init__.py`**  
     👉 An empty or initialization file that tells Python this directory is a package.

- **Script:**  
  A script is a Python file that you execute. It can import modules and packages to utilize their functions and classes.  
  ```python
  # my_script.py
  import my_module  # Imports our custom module
  print(my_module.greet("Alice"))
  ```
  **Explanation:**  
  1. **`import my_module`**  
     👉 Imports the module so its functions and variables can be used in the script.  
  2. **`print(my_module.greet("Alice"))`**  
     👉 Calls the `greet` function from `my_module` and prints the result.

---

## The Collections Module: Enhancing Python’s Data Structures 📚💡

The collections module provides various container datatypes that are alternatives to Python’s general-purpose built-in types. These specialized data types include:

- **namedtuple:**  
  Creates a tuple with named fields, similar to a regular tuple, but with more readable field names.
  
- **deque:**  
  A double-ended queue (doubly-linked list) that supports fast appends and pops from both ends.
  
- **defaultdict:**  
  A dictionary subclass that provides default values for missing keys, avoiding key errors.
  
- **ChainMap:**  
  A class for creating a single view of multiple dictionaries, useful for merging them.
  
- **Counter:**  
  A dictionary subclass for counting hashable objects. It returns counts for each key.
  
- **UserDict, UserList, UserString:**  
  These are wrapper classes that make it easier to create custom dictionary, list, or string objects with additional features.

---

## Table of Container Data Types 📊✨

Below is a table summarizing the container data types available in the collections module along with their descriptions:

| **Container Data Type** | **Description**                                                                                  |
|-------------------------|--------------------------------------------------------------------------------------------------|
| **namedtuple**          | Creates a tuple with named fields similar to regular tuples.                                     |
| **deque**               | Doubly-linked lists providing efficient appending and popping from both ends.                     |
| **defaultdict**         | A dictionary subclass that returns default values for missing keys.                              |
| **ChainMap**            | A dictionary-like class that groups multiple dictionaries into a single view.                    |
| **Counter**             | A dictionary subclass for counting hashable objects (tracks the number of occurrences).           |
| **UserDict**            | A wrapper around the dictionary object for easier subclassing to create custom dictionaries.      |
| **UserList**            | A wrapper around the list object for creating custom list types.                                  |
| **UserString**          | A wrapper around the string object for creating custom string types.                              |

---


<div align="center">

# `New Section NameTuple`

</div>

# **Named Tuples in Python** ✨🐍

Named tuples are an enhancement of the built-in tuple type provided by the `collections` module. They combine the simplicity and immutability of regular tuples with the added benefit of accessing elements by name. This makes your code more readable and easier to maintain when dealing with structured data. 

---

## **Why Use Named Tuples?** 🤔

- **Improved Readability:**  
  Instead of referring to tuple items by their numeric index, you can use descriptive field names. This self-documenting feature improves code clarity, making it easier for you and others to understand what each field represents.  
- **Immutability:**  
  Just like regular tuples, named tuples are immutable. Once created, their values cannot be changed. This characteristic ensures data consistency throughout your program.  
- **Memory Efficiency:**  
  Named tuples provide a memory-efficient alternative to classes when you only need to store data attributes without additional methods or behavior.

---

## **Syntax and Creatio**n 🔧📝

The basic syntax for creating a named tuple is as follows:

```python
nt = namedtuple(typename, field_names)
```

- **`typename`:**  
  This is a string that defines the name of the new tuple subclass. It acts as a label for the structure.  
- **`field_names`:**  
  This can be a list of strings or a single string with space-separated field names. These names become the accessible attributes of the named tuple.

---

## **Creating and Using a Named Tupl**e 📖✨

Below is a code example that demonstrates how to define a named tuple for representing a book, create an instance, and access its fields using both index and key methods.

```python
from collections import namedtuple  # Import the namedtuple function from the collections module 📦

# Define a named tuple 'Book' with three fields: 'name', 'ISBN', and 'quantity'
Book = namedtuple('Book', ['name', 'ISBN', 'quantity'])  # Creates a new class 'Book'
# Explanation:
# - 'Book': This is the typename for the new tuple subclass.
# - ['name', 'ISBN', 'quantity']: These are the fields for our Book records.
#   Each field is accessible by name (e.g., Book.name) and by index.

# Create an instance of the Book named tuple
Book1 = Book('Hands on Data Structures', '9781788995573', '50')
# Explanation:
# - 'Hands on Data Structures': Assigned to the 'name' field.
# - '9781788995573': Assigned to the 'ISBN' field.
# - '50': Assigned to the 'quantity' field.
# The order of values corresponds directly to the order of fields specified.

# Accessing data items using index
print('Using index ISBN: ' + Book1[1])
# Explanation:
# - Book1[1] accesses the second element in the tuple (indexing starts at 0).
#   Here, it retrieves the ISBN value.
# - The result is concatenated with the string 'Using index ISBN: ' and printed.

# Accessing data items using key (attribute)
print('Using key ISBN: ' + Book1.ISBN)
# Explanation:
# - Book1.ISBN accesses the field 'ISBN' by name.
# - This makes the code more intuitive and easier to understand.
# - The result is concatenated with the string 'Using key ISBN: ' and printed.
```

### Detailed Explanation of Each Step:

1. **Importing namedtuple:**
   - `from collections import namedtuple`
     - **What it does:**  
       Imports the `namedtuple` factory function from the `collections` module.  
     - **Why it's important:**  
       This function is used to create the new tuple subclass that supports named fields, giving us a clean and efficient way to handle structured data.

2. **Defining the Named Tuple:**
   - `Book = namedtuple('Book', ['name', 'ISBN', 'quantity'])`
     - **What it does:**  
       Defines a new subclass of tuple named `Book` with fields `name`, `ISBN`, and `quantity`.  
     - **Why it's useful:**  
       Instead of using an ordinary tuple where you'd access elements by indices (e.g., `book[0]`), you can now access data by attribute (e.g., `book.name`). This improves readability and reduces errors related to misindexed data.

3. **Creating an Instance:**
   - `Book1 = Book('Hands on Data Structures', '9781788995573', '50')`
     - **What it does:**  
       Instantiates the `Book` named tuple by providing values for each of its fields.  
     - **Detailed Breakdown:**  
       - The first argument `'Hands on Data Structures'` corresponds to the `name` field.
       - The second argument `'9781788995573'` corresponds to the `ISBN` field.
       - The third argument `'50'` corresponds to the `quantity` field.
     - **Why it's useful:**  
       This allows you to create structured data objects quickly without having to define a full class.

4. **Accessing Data by Index:**
   - `print('Using index ISBN: ' + Book1[1])`
     - **What it does:**  
       Accesses the second element in the named tuple using its index (remember, indexing starts at 0).  
     - **Why it's useful:**  
       Even though named tuples provide named access, they still behave like regular tuples. This means you can use indexing if needed.

5. **Accessing Data by Key:**
   - `print('Using key ISBN: ' + Book1.ISBN)`
     - **What it does:**  
       Accesses the `ISBN` field directly by its name.  
     - **Why it's useful:**  
       This is the primary advantage of using named tuples. The field names act as self-documenting code, making it clear what each element represents, thus reducing potential errors and enhancing maintainability.

**Expected Output:**
```plaintext
Using index ISBN: 9781788995573
Using key ISBN: 9781788995573
```

---