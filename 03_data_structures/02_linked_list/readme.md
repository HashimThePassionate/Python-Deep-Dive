# **Linked Lists** 📘🔗

Python’s list implementation is quite powerful and can encompass several different use cases.
We have discussed the built-in data structures of lists in Python in section, Python Data Types and Structures. Most of the time, Python’s built-in implementation of a list data structure is used to store data using a linked list. In this section, we will understand how linked lists work along with their internals.

A linked list is a data structure where the data elements are stored in a linear order. Linked lists provide efficient storage of data in linear order through pointer structures. Pointers are used to store the memory address of data items. They store the data and location, and the location stores the position of the next data item in the memory.

## 🎯 Section Objectives

* **Differentiate** between arrays and linked lists in terms of memory and performance.
* **Explain** how nodes and pointers collaborate to build dynamic lists.
* **Implement** singly, doubly, and circular linked lists with clarity.
* **Recognize** real-world scenarios where linked lists excel.


## 📚 Key Topics

### 1. Arrays vs. Linked Lists 🔄

* **Array**: Contiguous memory, fast index access (O(1)), but costly mid-list insertions/deletions (O(n)).
* **Linked List**: Non-contiguous nodes linked by pointers, flexible size, efficient insert/delete at known positions.

### 2. Node & Pointer Fundamentals 🧩

* **Node Structure**: Stores data and pointer(s).
* **Pointers**: References to next (and/or previous) nodes.

### 3. Singly Linked Lists ➡️

* Forward-only links.
* O(1) insert/delete at head, O(n) traversal.

### 4. Doubly Linked Lists ↔️

* Bidirectional navigation.
* Fast removal given a node pointer (O(1)).

### 5. Circular Linked Lists 🔄

* Tail connects back to head.
* Ideal for round-robin tasks and cyclic buffers.

### 6. Practical Applications 💼

* **Stacks & Queues**
* **Graph Adjacency Lists**
* **Undo/Redo Buffers**


