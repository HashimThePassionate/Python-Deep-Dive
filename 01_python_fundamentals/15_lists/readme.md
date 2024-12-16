# 📚 Python Lists

### 📜 Table of Contents
1. [Introduction to Lists](#introduction-to-lists)
   - [What is a List?](#what-is-a-list)
   - [Key Points](#key-points)
2. [🛠️ Common List Methods](#-common-list-methods)
   - [📌 `append(x)` Method](#-appendx-method)
   - [📌 `clear()` Method](#-clear-method)
   - [📌 `copy()` Method](#-copy-method)
   - [📌 `count(x)` Method](#-countx-method)
   - [📌 `extend(iterable)` Method](#-extenditerable-method)
   - [📌 `index(x, start=0, end=len(list))` Method](#-indexx-start0-endlenlist-method)
   - [📌 `insert(i, x)` Method](#-inserti-x-method)
   - [📌 `pop(i=-1)` Method](#-popi-1-method)
   - [📌 `remove(x)` Method](#-removex-method)
   - [📌 `reverse()` Method](#-reverse-method)
   - [📌 `sort(key=None, reverse=False)` Method](#-sortkeynone-reversefalse-method)
3. [🔄 Checking List Equality](#-checking-list-equality)
4. [📊 List Indexing and Slicing](#-list-indexing-and-slicing)
5. [➕ Concatenation and Modification](#-concatenation-and-modification)
6. [🧩 Nested Lists](#-nested-lists)
7. [✏️ Modifying List Values](#-modifying-list-values)
8. [➕ Python List Operations](#-python-list-operations)
9. [🔄 Iterating Through a List](#-iterating-through-a-list)
10. [➕ Adding Elements to a List](#-adding-elements-to-a-list)
11. [❌ Removing Elements from a List](#-removing-elements-from-a-list)
12. [⚙️ Modifying and Deleting List Items](#-modifying-and-deleting-list-items)
13. [🔀 Sorting a List](#-sorting-a-list)

## Introduction to Lists

A list in Python is a versatile and mutable data structure used to store a sequence of various types of data. Lists allow for dynamic and flexible manipulation of data, making them one of the most commonly used data types in Python.

### What is a List?

A list is a collection of items (elements) that are ordered and mutable (i.e., you can change the items in the list). Lists are created by placing the items inside square brackets `[]`, separated by commas.

```python
L1 = ["John", 102, "USA"]    
L2 = [1, 2, 3, 4, 5, 6]

print(type(L1))  # Output: <class 'list'>
print(type(L2))  # Output: <class 'list'>
```

### Key Points:
- **Ordered:** Lists maintain the order of elements.
- **Mutable:** Items in a list can be changed.
- **Flexible:** Lists can store elements of different types.

## 🛠️ Common List Methods

Python lists come with a variety of methods that allow for a wide range of operations, such as adding, removing, and sorting elements. Let's dive into each method with detailed explanations and examples.

### 📌 `append(x)` Method
- **Description:** Appends an item `x` to the end of the list.
- **Use Case:** Useful when you want to add a single item to a list without modifying any of the existing elements.

```python
cubes = [1, 8, 27, 65, 125]
cubes.append(216)  # Adds 216 to the end of the list
print(cubes)  # Output: [1, 8, 27, 65, 125, 216]
```

### 📌 `clear()` Method
- **Description:** Removes all items from the list, resulting in an empty list.
- **Use Case:** When you need to reset a list and remove all its elements.

```python
lst = [1, 2, 3, 4, 5]
lst.clear()
print(lst)  # Output: []
```

### 📌 `copy()` Method
- **Description:** Returns a shallow copy of the list.
- **Use Case:** When you need a copy of a list that is independent of the original list.

```python
original_list = [1, 2, 3]
copied_list = original_list.copy()
copied_list.append(4)
print(original_list)  # Output: [1, 2, 3]
print(copied_list)    # Output: [1, 2, 3, 4]
```

### 📌 `count(x)` Method
- **Description:** Returns the number of times the item `x` appears in the list.
- **Use Case:** Useful for counting occurrences of an element in a list.

```python
lst = [1, 2, 2, 3, 2, 4]
print(lst.count(2))  # Output: 3
```

### 📌 `extend(iterable)` Method
- **Description:** Extends the list by appending all the items from the `iterable` (e.g., another list, tuple).
- **Use Case:** To combine multiple lists or add elements from an iterable to the current list.

```python
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
lst1.extend(lst2)
print(lst1)  # Output: [1, 2, 3, 4, 5, 6]
```

### 📌 `index(x, start=0, end=len(list))` Method
- **Description:** Returns the index of the first occurrence of item `x`. Optional `start` and `end` arguments define a range to search within the list.
- **Use Case:** To find the position of an item in the list.

```python
lst = [1, 2, 3, 4, 2]
print(lst.index(2))  # Output: 1
print(lst.index(2, 2))  # Output: 4 (search starts at index 2)
```

### 📌 `insert(i, x)` Method
- **Description:** Inserts item `x` at index `i`. Shifts the element currently at that position (if any) and subsequent elements to the right.
- **Use Case:** To insert an item at a specific position in the list.

```python
lst = [1, 2, 4, 5]
lst.insert(2, 3)  # Insert 3 at index 2
print(lst)  # Output: [1, 2, 3, 4, 5]
```

### 📌 `pop(i=-1)` Method
- **Description:** Removes and returns the item at index `i`. If `i` is not specified, `pop()` removes and returns the last item in the list.
- **Use Case:** Useful for both removing an item from a specific position and for stack-like behavior (LIFO).

```python
lst = [1, 2, 3, 4]
print(lst.pop())  # Output: 4 (removes and returns the last item)
print(lst.pop(0))  # Output: 1 (removes and returns the first item)
```

### 📌 `remove(x)` Method
- **Description:** Removes the first occurrence of item `x` from the list. Raises a `ValueError` if the item is not found.
- **Use Case:** To remove a specific item from a list.

```python
lst = [1, 2, 3, 2, 4]
lst.remove(2)
print(lst)  # Output: [1, 3, 2, 4] (first 2 is removed)
```

### 📌 `reverse()` Method
- **Description:** Reverses the elements of the list in place.
- **Use Case:** To reverse the order of elements in a list.

```python
lst = [1, 2, 3, 4, 5]
lst.reverse()
print(lst)  # Output: [5, 4, 3, 2, 1]
```

### 📌 `sort(key=None, reverse=False)` Method
- **Description:** Sorts the list in place. The optional `key` argument specifies a function of one argument that is used to extract a comparison key from each list element. The optional `reverse` argument is a boolean value; if set to `True`, the list elements are sorted as if each comparison were reversed.
- **Use Case:** To sort elements in a list either in ascending or descending order.

```python
lst = [3, 1, 4, 2, 5]
lst.sort()
print(lst)  # Output: [1, 2, 3, 4, 5]

lst.sort(reverse=True)
print(lst)  # Output: [5, 4, 3, 2, 1]

# Sorting by a key
words = ['apple', 'banana', 'cherry']
words.sort(key=len)
print(words)  # Output: ['apple', 'banana', 'cherry'] (sorted by length)
```

## 🔄 Checking List Equality

You can check if two lists are the same object using the `is` operator. However, even if two lists have the same elements, they are not the same object unless explicitly assigned.

```python
a = [1, 2, "Peter", 4.50, "Ricky", 5, 6]  
b = [1, 2, "Peter", 4.50, "Ricky", 5, 6]  

print(a is b)  # Output: False (Different objects)
print(a == b)  # Output: True (Same elements)

b = a  # Now b refers to the same object as a
print(a is b)  # Output: True (Same object)
```

## 📊 List Indexing and Slicing

Lists support indexing and slicing, which allows you to access specific elements or a range of elements.

```python
squares = [1, 4, 9, 16, 25]
print(squares[0])  # Output: 1
print(squares[-1])  # Output: 25
print(squares[-3:])  # Output: [9, 16, 25]
```

### Visual Representation of List Indexing:
```
 +---+---+---+---+---+
 | 1 | 4 | 9 | 16 | 25|
 +---+---+---+---+---+
   0   1   2   3   4     
  -5  -4  -3  -2  -1  
```

## ➕ Concatenation and Modification

Lists can be concatenated using the `+` operator, and you can modify elements by assigning new values.

```python
squares = [1, 4, 9, 16, 25]
squares += [36, 49, 64, 81, 100]  # Concatenation
print(squares)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

c

ubes = [1, 8, 27, 65, 125]
cubes[3] = 64  # Correcting an incorrect value
print(cubes)  # Output: [1, 8, 27, 64, 125]
```

## 🧩 Nested Lists

Lists can contain other lists, allowing for complex data structures.

```python
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)  # Output: [['a', 'b', 'c'], [1, 2, 3]]
print(x[0][1])  # Output: 'b'
print(x[1][2])  # Output: 3
```

## ✏️ Modifying List Values

Lists are mutable, meaning their values can be updated using slice assignments.

```python
lst = [1, 2, 3, 4, 5, 6]
lst[2] = 10  # Update the value at index 2
print(lst)  # Output: [1, 2, 10, 4, 5, 6]

lst[1:3] = [89, 78]  # Update a slice of the list
print(lst)  # Output: [1, 89, 78, 4, 5, 6]

lst[-1] = 25  # Update the last element
print(lst)  # Output: [1, 89, 78, 4, 5, 25]
```

## ➕ Python List Operations

The concatenation `+` and repetition `*` operators work with lists just as they do with strings.

```python
l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]
print(l1 * 2 + l2)  # Output: [1, 2, 3, 4, 1, 2, 3, 4, 5, 6, 7, 8]
print(len(l1))  # Output: 4
```

## 🔄 Iterating Through a List

You can iterate through a list using a `for` loop.

```python
lst = ["John", "David", "James", "Jonathan"]
for name in lst:
    print(name)  # Output: John, David, James, Jonathan (each on a new line)
```

## ➕ Adding Elements to a List

You can add elements to a list using the `append()` method.

```python
l = []
n = int(input("Enter the number of elements in the list: "))  
for i in range(n):  
    l.append(input("Enter the item: "))  
print("Printing the list items...")  
for item in l:  
    print(item, end="  ")  
```

### Output:
```
Enter the number of elements in the list: 5
Enter the item: 25
Enter the item: 46
Enter the item: 12
Enter the item: 75
Enter the item: 42
Printing the list items...
25  46  12  75  42
```

## ❌ Removing Elements from a List

Use the `remove()` method to delete an element from a list.

```python
lst = [0, 1, 2, 3, 4]
print("Original list: ", lst)
lst.remove(2)
print("List after removal: ", lst)
```

### Output:
```
Original list: [0, 1, 2, 3, 4]
List after removal: [0, 1, 3, 4]
```

## ⚙️ Modifying and Deleting List Items

You can modify items in a list using indexing and slicing, and you can delete items using the `del` keyword.

```python
x = [1, 2, 3, 4]
x[1] = 42  # Modify single item
print(x)  # Output: [1, 42, 3, 4]

x[1:3] = [22, 33, 44]  # Modify a slice
print(x)  # Output: [1, 22, 33, 44, 4]

del x[1]  # Delete an item
print(x)  # Output: [1, 33, 44, 4]
```

## 🔀 Sorting a List

Python’s `sort()` method sorts a list in place, and it is guaranteed to be stable (elements that compare equal are not exchanged).

```python
mylist = ['alpha', 'Beta', 'GAMMA']
mylist.sort()  # Sorts alphabetically
print(mylist)  # Output: ['Beta', 'GAMMA', 'alpha']

mylist.sort(key=str.lower)  # Sorts case-insensitively
print(mylist)  # Output: ['alpha', 'Beta', 'GAMMA']
```
