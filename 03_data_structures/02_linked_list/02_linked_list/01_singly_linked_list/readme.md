#  What is a Singly Linked List 🧱

A **singly linked list** is a linear data structure where:

* Each element is stored inside a **node**
* Every node points to the **next node**
* The **last node points to None** (signifying the end) ❌

## 🖼️ **Figure 4.6**: An Example of a Singly Linked List

<div align="center">
  <img src="./images/01.jpg" alt="" width="600px"/>
</div>

This figure illustrates a **singly linked list** that stores a sequence of integers:

```
1 → 5 → 2 → 8 → None
```

📌 The first node (`1`) is called the **head** of the list.
Each node:

* Stores a **data value**
* Points to the **next node** in the sequence
  The **last node (8)** points to `None`, marking the **end of the list**.

## 🛠️ Defining a Node in Python

```python
class Node:
    def __init__(self, data=None):
        self.data = data      # Stores the actual data
        self.next = None      # Reference to the next node
```

### 📌 Explanation:

* `data`: Stores the value (like `'eggs'`, `'ham'`, etc.)
* `next`: Initially set to `None`, meaning no link until we explicitly connect it


## 🧰 Creating a Singly Linked List

Let’s create a simple linked list using **three nodes**:

```python
n1 = Node('eggs')
n2 = Node('ham')
n3 = Node('spam')
```

Now link them together:

```python
n1.next = n2
n2.next = n3
# n3.next remains None (automatically set during initialization)
```

This results in the following list:

```
"eggs" → "ham" → "spam" → None
```

## 🚶 Traversing the Linked List

Traversal means going through **each node** from the head to the last.

### 🔁 Traversal Code:

```python
current = n1
while current:
    print(current.data)
    current = current.next
```

### 🖨️ Output:

```
eggs
ham
spam
```

### 🔎 How it works:

* `current` starts at `n1` (head)
* In each loop:

  * Print current node's data
  * Move to the next node using `current = current.next`
* Loop ends when `current` becomes `None` (end of list)


## ⚠️ Problems with This Basic Implementation

Although this structure works, it has some **major limitations**:

### ❌ Too Much Manual Work:

* You must **manually link every node**
* You manually manage node connections (`n1.next = n2`, etc.)

### ❌ Overexposure of Details:

* The inner mechanics (`.next` pointers) are exposed to the user
* Makes the code **error-prone** and **hard to manage** in large applications

There are, however, several problems with this simplistic list implementation:
- It requires too much manual work by the programmer
- Too much of the inner workings of the list is exposed to the programmer

---
 
#  **Improving Traversal** 🚀

In earlier examples, we **manually traversed** a linked list by directly accessing `.data` and `.next` from each node:

```python
while current:
    print(current.data)
    current = current.next
```

🔍 **Issue:**
This approach **exposes the inner structure** (`Node`) to the **user/client**, which is considered **bad practice** in software design.

### ⚠️ Why It's a Problem:

* Client code is too **dependent on implementation details**
* Harder to maintain or extend
* Not very elegant or Pythonic 😬

## ✅ The Solution: Encapsulation + Generators

We can **hide the internals** and make list traversal much more **user-friendly** by:

1. Defining an `iter()` method inside the Node class
2. Using the `yield` keyword to build a **generator** 🔄


### 🧪 Improved Traversal Code Using a Generator

```python
def iter(self):
    current = self
    while current:
        val = current.data
        current = current.next
        yield val
```

### 📌 Explanation:

* `yield` works like `return`, but **remembers** the current position/state of the function
* This function becomes a **generator**, meaning:

  * It produces a **sequence of values one at a time**
  * It doesn't return all values at once
  * It is **memory efficient** for large lists

## 🔁 Updated Usage — Cleaner & Safer Traversal

Now your client code is cleaner:

```python
for word in words.iter():
    print(word)
```

### 🎉 Benefits:

* No more direct use of `.data` or `.next`
* Cleaner, more elegant API
* Follows **encapsulation** principle


## 🧱 Complete Working Code

```python
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def iter(self):
        current = self
        while current:
            val = current.data
            current = current.next
            yield val

# Creating linked list nodes
n1: Node = Node('eggs')
n2: Node = Node('ham')
n3: Node = Node('spam')

# Linking the nodes
n1.next = n2
n2.next = n3

# Traversing using generator
for value in n1.iter():
    print(value)
```
---

#  **Singly Linked List Appending with append method** 📝

### 🖼️ **Figure 4.7**: Inserting a node at the end of a singly linked list

<div align="center">
  <img src="./images/02.jpg" alt="" width="600px"/>
</div>

## 🏗️ Building the `SinglyLinkedList` Class

We encapsulate all linked-list logic within a **single class** so that **clients never touch the `Node` class** directly.

```python
class SinglyLinkedList:
    def __init__(self):
        # The head of the list (first node). None means an empty list.
        self.head = None
        # Optional: track the number of nodes for O(1) size retrieval
        self.size = 0
```

* **`self.head`** points to the first node in the list (or `None` if empty)
* **`self.size`** keeps count of nodes (initially `0`) ✨


## ➕ Appending Items to the End

We hide the `Node` details by providing an **`append(data)`** method:

```python
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        # 1️⃣ Create a new Node to encapsulate the data
        node = Node(data)

        # 2️⃣ If the list is empty, new node becomes the head
        if self.head is None:
            self.head = node
        else:
            # 3️⃣ Otherwise, traverse to the end of the list
            current = self.head
            while current.next:
                current = current.next
            # 4️⃣ Link the last node to the new node
            current.next = node

        # 5️⃣ Update size counter
        self.size += 1
```

### 🔍 Step-by-Step Explanation

1. **Encapsulate**

   * Wrap the raw `data` in a `Node`, giving it a `.next` pointer.

2. **Empty List Check**

   * If `self.head` is `None`, the list has **no nodes**.
   * We set `self.head = node` to make our new node the **first element** 🥇.

3. **Traverse to Last Node**

   * Start at `self.head`.
   * Follow `.next` pointers until `current.next` is `None` (last node).

4. **Insert New Node**

   * Set `current.next = node`, linking the old last node to our new one ➡️.

5. **Maintain Size**

   * Increment `self.size` by 1 for quick length queries 📏.

## ⚙️ Using the `append()` Method

```python
words = SinglyLinkedList()
words.append('egg')   # List: egg → None
words.append('ham')   # List: egg → ham → None
words.append('spam')  # List: egg → ham → spam → None
```

* After three appends, `words.size == 3`
* The structure matches **Figure 4.7**

## 🔁 Traversing the List

You can traverse just like before (or use a generator if you implemented one):

```python
current = words.head
while current:
    print(current.data)
    current = current.next
```

**Output:**

```
egg
ham
spam
```

---

---

#  **Optimizing Append with a Tail Pointer** 🚀

### 🖼️ **Figure 4.8**: Inserting a Node at the End with a Tail Pointer

<div align="center">
  <img src="./images/03.jpg" alt="" width="600px"/>
</div>

## 🎯 Goal: O(1) Append Time

* **Problem**: Without a tail pointer, `append()` requires **O(n)** time to traverse to the end.
* **Solution**: Maintain both:

  * `self.head` → first node
  * `self.tail` → last node

With a tail pointer, we **directly link** the new node to the end in **constant time**.

## 🧱 Updated `SinglyLinkedList` Implementation

```python
class SinglyLinkedList:
    def __init__(self):
        self.head = None   # First node
        self.tail = None   # Last node
        self.size = 0      # Number of nodes

    def append(self, data):
        node = Node(data)  # 1️⃣ Wrap data in a new Node

        if self.tail:
            # 2️⃣ Link old tail to the new node
            self.tail.next = node
            # 3️⃣ Update tail to the new node
            self.tail = node
        else:
            # 📦 Empty list: both head & tail point to the new node
            self.head = node
            self.tail = node

        # 4️⃣ Increase size counter
        self.size += 1
```

### 🔍 Step-by-Step:

1. **Create** a new `Node(data)`.
2. **Non-empty list?**

   * **Yes**: Link `self.tail.next → node`, then update `self.tail = node`.
   * **No** (list empty): Set **both** `self.head` and `self.tail` to `node`.
3. **Increment** `self.size`.

## 🔄 Execution Flow (Figure 4.8)

1. **Step 1**: When list is **non-empty**,

   * `tail.next` jumps to the **new node**.
   * `tail` moves forward to that node.
2. **Step 2**: If the list is **empty**,

   * Both `head` and `tail` are initialized to the **first node**.


## ⚙️ Usage Example

```python
words = SinglyLinkedList()
words.append('eggs')
words.append('ham')
words.append('spam')

# Traverse & print
current = words.head
while current:
    print(current.data)
    current = current.next
```

**Output:**

```
eggs
ham
spam
```

* **Append** operations are now **O(1)** 🔥
* **Traverse** remains **O(n)**


## 🔑 Key Benefits

* **Efficiency**: Instant appends, no full-list traversal
* **Simplicity**: Client code still interacts only with `SinglyLinkedList`
* **Scalability**: Ideal for large, dynamic datasets

---
