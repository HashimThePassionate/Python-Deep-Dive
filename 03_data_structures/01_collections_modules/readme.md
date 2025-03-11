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

<div align="center">

# `New Section Deque`

</div>



# **Deque: Double-Ended Queue in Python** ⏩⏪

A **deque** (pronounced "deck") is a double-ended queue that allows you to append and pop elements from both the front and the back. Deques are implemented as doubly-linked lists, making operations like inserting and deleting elements highly efficient—typically in O(1) time complexity. This makes deques a powerful tool when you need a flexible and fast data structure for queue-like operations.

---

## What is a Deque? 🧐

- **Definition:**  
  A deque is a list-like container with fast appends and pops from both ends.
  
- **Key Characteristics:**  
  - **Double-Ended:** Supports operations on both ends (left and right). ⏩⏪  
  - **Efficiency:** Insertion and deletion operations are executed in constant time, O(1). ⚡  
  - **Implementation:** Built using a doubly-linked list for optimal performance. 🔗

---

## Creating and Using a Deque 🛠️💡

Below is an enhanced example demonstrating how to create an empty deque, initialize one with elements, and perform basic operations:

```python
from collections import deque  # Import deque from the collections module 📦

# Create an empty deque
s = deque()  # Initializes an empty deque, ready to be used 🆕
print("Empty deque:", s)  # Expected output: deque([])

# Create a deque with initial elements
my_queue = deque([1, 2, 'Name'])  # Initializes deque with a mix of integers and a string 🔢🔤
print("Initial deque:", my_queue)  # Expected output: deque([1, 2, 'Name'])
```

**Line-by-Line Explanation:**

1. **`from collections import deque`**  
   👉 This line imports the `deque` class from Python's built-in `collections` module.  
   👉 **Why?** The `collections` module provides alternative container types that offer more flexibility and performance for specific tasks.

2. **`s = deque()`**  
   👉 Creates an empty deque named `s`.  
   👉 **What happens?**  
      - An empty deque is initialized.
      - Ready to be populated with elements later.
      
3. **`print("Empty deque:", s)`**  
   👉 Prints the empty deque, which should output: `deque([])`.  
   👉 **Why?**  
      - To verify that the deque has been created and is currently empty.

4. **`my_queue = deque([1, 2, 'Name'])`**  
   👉 Initializes a new deque called `my_queue` with the elements `1`, `2`, and `'Name'`.  
   👉 **What happens?**  
      - The deque now contains three items.
      - It supports various operations at both ends.
      
5. **`print("Initial deque:", my_queue)`**  
   👉 Prints the initialized deque, expected to output: `deque([1, 2, 'Name'])`.

---

## Common Deque Operations 🚀🔧

Deques offer several built-in functions to manipulate data efficiently. The following table summarizes the most common operations along with their descriptions:

| **Function**               | **Description**                                                                  |
|----------------------------|----------------------------------------------------------------------------------|
| `my_queue.append('age')`   | Inserts `'age'` at the right end of the deque. ➕                                 |
| `my_queue.appendleft('age')` | Inserts `'age'` at the left end of the deque. ⬅️                                 |
| `my_queue.pop()`           | Removes and returns the rightmost element of the deque. ➖                        |
| `my_queue.popleft()`       | Removes and returns the leftmost element of the deque. ⬅️                        |

*Table 1.8: Description of different deque functions*

---

## Enhanced Example: Using Deque Operations 🔄💥

Let’s see a more detailed example demonstrating several deque operations:

```python
from collections import deque  # Import deque from the collections module

# Initialize a deque with some initial elements
my_queue = deque([1, 2, 'Name'])
print("Original deque:", my_queue)  # Expected: deque([1, 2, 'Name'])

# Append an element at the right end
my_queue.append('age')  
print("After append:", my_queue)  # Expected: deque([1, 2, 'Name', 'age'])

# Append an element at the left end
my_queue.appendleft('start')
print("After appendleft:", my_queue)  # Expected: deque(['start', 1, 2, 'Name', 'age'])

# Remove an element from the right end
removed_right = my_queue.pop()
print("After pop (removed from right):", my_queue, "| Removed:", removed_right)
# Expected: deque(['start', 1, 2, 'Name']) and removed element 'age'

# Remove an element from the left end
removed_left = my_queue.popleft()
print("After popleft (removed from left):", my_queue, "| Removed:", removed_left)
# Expected: deque([1, 2, 'Name']) and removed element 'start'
```

**Detailed Explanation of the Enhanced Example:**

1. **`from collections import deque`**  
   👉 Imports the `deque` class, which is necessary for creating deque objects.

2. **`my_queue = deque([1, 2, 'Name'])`**  
   👉 Initializes `my_queue` with three items: `1`, `2`, and `'Name'`.

3. **`print("Original deque:", my_queue)`**  
   👉 Prints the original state of the deque.  
   👉 **Output:** `deque([1, 2, 'Name'])`

4. **`my_queue.append('age')`**  
   👉 Appends the string `'age'` to the right end of the deque.  
   👉 **Why?**  
      - Use `append` when you want to add an element at the end of the deque.

5. **`print("After append:", my_queue)`**  
   👉 Prints the state of the deque after the append operation.  
   👉 **Output:** `deque([1, 2, 'Name', 'age'])`

6. **`my_queue.appendleft('start')`**  
   👉 Inserts the string `'start'` at the left end of the deque.  
   👉 **Why?**  
      - Use `appendleft` when you need to add an element at the beginning.

7. **`print("After appendleft:", my_queue)`**  
   👉 Prints the deque after inserting `'start'` at the beginning.  
   👉 **Output:** `deque(['start', 1, 2, 'Name', 'age'])`

8. **`removed_right = my_queue.pop()`**  
   👉 Removes and returns the rightmost element from the deque.  
   👉 **Why?**  
      - The `pop` operation is useful when you want to process or remove the last element.
   👉 **Output:** The removed element is stored in `removed_right`.

9. **`print("After pop (removed from right):", my_queue, "| Removed:", removed_right)`**  
   👉 Prints the deque after the `pop` operation along with the removed element.  
   👉 **Expected Output:**  
      - Deque: `deque(['start', 1, 2, 'Name'])`  
      - Removed element: `'age'`

10. **`removed_left = my_queue.popleft()`**  
    👉 Removes and returns the leftmost element from the deque.  
    👉 **Why?**  
       - The `popleft` operation is used when you need to process or remove the first element.
    👉 **Output:** The removed element is stored in `removed_left`.

11. **`print("After popleft (removed from left):", my_queue, "| Removed:", removed_left)`**  
    👉 Prints the deque after the `popleft` operation along with the removed element.  
    👉 **Expected Output:**  
       - Deque: `deque([1, 2, 'Name'])`  
       - Removed element: `'start'`


---

<div align="center">

# `New Section OrderedDict`

</div>


# **OrderedDict: Preserving Key Order in Dictionaries** 🗂️✨

An **OrderedDict** is a subclass of the regular Python dictionary available in the `collections` module. Unlike standard dictionaries (especially in Python versions prior to 3.7), an OrderedDict maintains the order in which keys are inserted. This means that when you iterate over an OrderedDict, keys are returned in the same order as they were added. This predictable order can be very useful for many applications.  

---

## How Does OrderedDict Maintain Order? 🔍

- **Internal Doubly-Linked List:**  
  OrderedDict uses a doubly-linked list to store the keys. Each time a key is inserted, it is added at the end of this list, preserving the order of insertion.

- **Insertion Order:**  
  The order of the key-value pairs in an OrderedDict is exactly the same as the order in which they were added. This means if you create an OrderedDict with a list of tuples, the keys will remain in that sequence.

- **Iteration:**  
  When you iterate over an OrderedDict (using a for loop, for example), it traverses the internal linked list in order, so the keys are returned in the insertion order.

---

## Example: Creating and Iterating Over an OrderedDict 📖✨

Let's look at a sample code snippet that creates an OrderedDict and then iterates over it using a for loop to print the keys in the expected order:

```python
from collections import OrderedDict  # Import OrderedDict from collections module 📦

# Creating an OrderedDict with keys and values
od = OrderedDict([
    ('my', 2),
    ('name', 4),
    ('is', 2),
    ('Mohan', 5),
    ('hello', 4)
])
# Explanation:
# - The OrderedDict is initialized with a list of tuples.
# - Each tuple represents a key-value pair.
# - The keys are stored in the order: 'my', 'name', 'is', 'Mohan', 'hello'.

# Printing the entire OrderedDict
print("OrderedDict:", od)
# Expected output:
# OrderedDict([('my', 2), ('name', 4), ('is', 2), ('Mohan', 5), ('hello', 4)])

# Using a for loop to iterate over the OrderedDict and print each key in order
print("\nIterating over OrderedDict keys:")
for key in od:
    print(key, "->", od[key])
# Expected output:
# my -> 2
# name -> 4
# is -> 2
# Mohan -> 5
# hello -> 4
```

**Line-by-Line Explanation:**

1. **`from collections import OrderedDict`**  
   👉 Imports the OrderedDict class from the `collections` module.  
   👉 **Why?**  
      - To use a dictionary-like structure that preserves the order of key insertion.

2. **Creating the OrderedDict:**
   ```python
   od = OrderedDict([
       ('my', 2),
       ('name', 4),
       ('is', 2),
       ('Mohan', 5),
       ('hello', 4)
   ])
   ```
   👉 **What it does:**  
      - An OrderedDict named `od` is created using a list of tuples.
      - Each tuple represents a key-value pair.
      - The order of the tuples in the list determines the order of keys in the OrderedDict.
   👉 **Internal Mechanism:**  
      - The OrderedDict maintains a doubly-linked list to store keys in the order they were inserted.

3. **`print("OrderedDict:", od)`**  
   👉 Prints the entire OrderedDict to show that the keys appear in the insertion order.  
   👉 **Expected Output:**  
      - `OrderedDict([('my', 2), ('name', 4), ('is', 2), ('Mohan', 5), ('hello', 4)])`

4. **Using a For Loop to Iterate Over Keys:**
   ```python
   print("\nIterating over OrderedDict keys:")
   for key in od:
       print(key, "->", od[key])
   ```
   👉 **What it does:**  
      - The for loop iterates over the OrderedDict `od`.
      - In each iteration, the variable `key` holds the next key in the insertion order.
      - `od[key]` accesses the corresponding value.
   👉 **Why it's useful:**  
      - This loop demonstrates that the keys are retrieved in the same order they were added.
   👉 **Expected Output:**  
      - The output will display:
        ```
        my -> 2
        name -> 4
        is -> 2
        Mohan -> 5
        hello -> 4
        ```

---

<div align="center">

# `New Section DefaultDict`

</div>

# **defaultdict: A Convenient Dictionary with Default Values** 🛠️🐍

The **defaultdict** is a subclass of the built-in dictionary class (`dict`) from Python’s `collections` module. It works like a normal dictionary, but it provides a default value for a key that does not exist, thus never raising a `KeyError`. This makes it especially useful for tasks like counting, grouping, or accumulating data.

---

## How Normal Dictionaries and KeyError Work ⚠️🔑

- **Normal Dictionary Behavior:**
  When you try to access a key that does not exist in a normal dictionary, Python raises a `KeyError`. For example:
  
  ```python
  normal_dict = {}
  print(normal_dict['missing'])  # Raises KeyError because 'missing' is not in the dictionary
  ```
  
  **Explanation:**
  - A standard dictionary does not have a predefined value for non-existent keys.
  - Attempting to access such a key results in a runtime error (`KeyError`).

- **Avoiding KeyError with defaultdict:**
  defaultdict allows you to specify a default factory function that provides a default value for missing keys. For example, by using `int` as the default factory, any missing key will automatically be assigned a default value of `0` (since `int()` returns `0`).

---

## Example: Counting Words with defaultdict 🔢📖

Consider an example where we count the occurrences of each word in a string. Using defaultdict, we avoid the need to check whether a key exists before updating its count.

```python
from collections import defaultdict  # Import defaultdict from the collections module 📦

# Create a defaultdict with int as the default factory
dd = defaultdict(int)  # int() returns 0, so missing keys start with a default count of 0

# Split a string into words
words = str.split('data python data data structure data python')  # Splitting the string into a list of words 🔠

# Count each word using defaultdict
for word in words:
    dd[word] += 1  # If the word is missing, defaultdict automatically initializes it to 0 before adding 1 🔢

# Print the resulting defaultdict
print(dd)
# Expected output:
# defaultdict(<class 'int'>, {'data': 4, 'python': 2, 'structure': 1})
```

**Line-by-Line Explanation:**

1. **`from collections import defaultdict`**  
   👉 Imports the `defaultdict` class from the `collections` module.  
   👉 **Why?**  
      - To create a dictionary that returns a default value for missing keys.

2. **`dd = defaultdict(int)`**  
   👉 Creates a defaultdict named `dd` where the default factory is the `int` function.  
   👉 **How it works:**  
      - When a non-existent key is accessed, `int()` is called, which returns `0`.  
      - This means every new key starts with a value of 0.

3. **`words = str.split('data python data data structure data python')`**  
   👉 Splits the given string into a list of words.  
   👉 **Result:**  
      - `['data', 'python', 'data', 'data', 'structure', 'data', 'python']`

4. **`for word in words:`**  
   👉 Iterates over each word in the list.

5. **`dd[word] += 1`**  
   👉 Increments the count for each word.  
   👉 **Why it works:**  
      - If `word` is not already a key in `dd`, defaultdict calls `int()` to initialize it to `0` and then adds `1`.

6. **`print(dd)`**  
   👉 Prints the defaultdict, showing the counts of each word.  
   👉 **Expected Output:**  
      - `defaultdict(<class 'int'>, {'data': 4, 'python': 2, 'structure': 1})`

---

## Comparing Normal dict vs. defaultdict ⚖️

- **Normal dict:**
  ```python
  normal_dict = {}
  # Attempting to update a missing key without initialization:
  # This would cause a KeyError.
  # normal_dict['data'] += 1  # KeyError if 'data' is not present
  ```

- **defaultdict:**
  ```python
  from collections import defaultdict
  dd = defaultdict(int)
  dd['data'] += 1  # Works fine: 'data' is automatically initialized to 0, then incremented to 1
  ```

**Key Benefits:**
- **No KeyError:**  
  With defaultdict, you don't need to check if a key exists before updating it.
- **Cleaner Code:**  
  It reduces boilerplate code, making your code more concise and readable.
- **Efficient Counting:**  
  Ideal for counting occurrences or aggregating values.

---

<div align="center">

# `New Section ChainMap`

</div>

# **ChainMap: Combining Multiple Dictionaries into a Single View** 🔗🗂️

A **ChainMap** is a data structure in the `collections` module that groups multiple dictionaries (or other mappings) into a single, unified view. When you search for a key in a ChainMap, it checks each dictionary in order—returning the value from the first dictionary where the key is found. This makes it an excellent tool for scenarios like managing configurations or merging contexts.

---

## How ChainMap Works 🤔

- **Multiple Mappings:**  
  A ChainMap combines several dictionaries into one view. You can pass two or more dictionaries when creating a ChainMap.
  
- **Search Order:**  
  When you look up a key, the ChainMap searches each dictionary in the order they were provided. The first occurrence of the key is returned.
  
- **Unified View:**  
  Although the underlying dictionaries remain separate, the ChainMap provides a unified mapping interface. You can access keys, values, and iterate over the ChainMap just as you would with a regular dictionary.

---

## Example Code with Detailed Explanations

Below is an example that demonstrates how to create a ChainMap, access its keys and values, and retrieve items from it.

```python
from collections import ChainMap  # Import the ChainMap class from the collections module 📦

# Create two dictionaries
dict1 = {"data": 1, "structure": 2}      # First dictionary with two key-value pairs 🗃️
dict2 = {"python": 3, "language": 4}       # Second dictionary with two key-value pairs 📚

# Combine the dictionaries using ChainMap
chain = ChainMap(dict1, dict2)             # Creates a ChainMap that combines dict1 and dict2 🔗
# Explanation:
# - The ChainMap will first search in dict1; if the key is not found, it will search dict2.

# Print the ChainMap
print(chain)
# Expected output:
# ChainMap({'data': 1, 'structure': 2}, {'python': 3, 'language': 4})
# This shows that the ChainMap holds the two dictionaries.

# Get and print all keys from the ChainMap
print(list(chain.keys()))
# Explanation:
# - list(chain.keys()) collects keys from both dictionaries.
# Expected output (order depends on internal implementation):
# ['python', 'language', 'data', 'structure']

# Get and print all values from the ChainMap
print(list(chain.values()))
# Explanation:
# - list(chain.values()) collects values corresponding to the keys.
# Expected output:
# [3, 4, 1, 2]

# Access a key that exists in the first dictionary (dict1)
print(chain["data"])
# Explanation:
# - 'data' is found in dict1, and its value (1) is returned.
# Expected output: 1

# Access a key that exists in the second dictionary (dict2)
print(chain["language"])
# Explanation:
# - 'language' is not in dict1, so the ChainMap checks dict2, where it is found with value 4.
# Expected output: 4
```

**Line-by-Line Explanation:**

1. **`from collections import ChainMap`**  
   👉 Imports the `ChainMap` class, allowing you to combine multiple dictionaries into a single view.

2. **`dict1 = {"data": 1, "structure": 2}`**  
   👉 Creates the first dictionary, `dict1`, with keys `"data"` and `"structure"` and their corresponding values.

3. **`dict2 = {"python": 3, "language": 4}`**  
   👉 Creates the second dictionary, `dict2`, with keys `"python"` and `"language"`.

4. **`chain = ChainMap(dict1, dict2)`**  
   👉 Combines `dict1` and `dict2` into a single ChainMap called `chain`.  
   👉 **Internal Behavior:**  
      - The ChainMap maintains the order: it will first search in `dict1`, then in `dict2`.

5. **`print(chain)`**  
   👉 Displays the entire ChainMap, showing both dictionaries.  
   👉 **Output:**  
      - `ChainMap({'data': 1, 'structure': 2}, {'python': 3, 'language': 4})`

6. **`print(list(chain.keys()))`**  
   👉 Retrieves and prints a list of all keys in the ChainMap.  
   👉 **Note:**  
      - The order of keys may vary based on internal dictionary ordering.  
   👉 **Example Output:**  
      - `['python', 'language', 'data', 'structure']`

7. **`print(list(chain.values()))`**  
   👉 Retrieves and prints a list of all values in the ChainMap corresponding to the keys.  
   👉 **Example Output:**  
      - `[3, 4, 1, 2]`

8. **`print(chain["data"])`**  
   👉 Accesses the value associated with the key `"data"`.  
   👉 **Explanation:**  
      - `"data"` is found in `dict1`, so its value `1` is returned.  
   👉 **Output:**  
      - `1`

9. **`print(chain["language"])`**  
   👉 Accesses the value associated with the key `"language"`.  
   👉 **Explanation:**  
      - `"language"` is not found in `dict1`, so the ChainMap checks `dict2` where it is found with value `4`.  
   👉 **Output:**  
      - `4`

---