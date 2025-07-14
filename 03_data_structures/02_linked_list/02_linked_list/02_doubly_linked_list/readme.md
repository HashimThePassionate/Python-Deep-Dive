#  **Doubly Linked Lists** 🔁

A **doubly linked list** extends the concept of a singly linked list by allowing **two-way traversal**. Each node contains:

1. **Data**: The value stored in the node.
2. **Next pointer**: Reference to the **next** node in the sequence.
3. **Previous pointer**: Reference to the **previous** node in the sequence.

## 🖼️ Figure 4.18: A Single Node in a Doubly Linked List

<div align="center">
  <img src="./images/01.jpg" alt="" width="400px"/>
</div>

* **Data field** holds the node’s value.
* **Next** points forward to another node (here, `None` because no successor exists).
* **Previous** points backward to another node (here, `None` because no predecessor exists).

## 🖼️ Figure 4.19: Two Nodes in a Doubly Linked List

<div align="center">
  <img src="./images/02.jpg" alt="" width="400px"/>
</div>

* **Node A**:

  * `Next` → Node B
  * `Previous` → `None` (no node before A)
* **Node B**:

  * `Previous` → Node A
  * `Next` → `None` (no node after B)

## 📋 Key Differences from Singly Linked List

| Aspect                   | Singly Linked List                                               | Doubly Linked List                                                |
| ------------------------ | ---------------------------------------------------------------- | ----------------------------------------------------------------- |
| **Pointers per node**    | 1 (`next`)                                                       | 2 (`next` and `previous`)                                         |
| **Traversal**            | Only forward                                                     | Forward **and** backward                                          |
| **Ease of backtracking** | Requires extra work (e.g., stack or re-traverse)                 | Immediate via `previous` pointer                                  |
| **Insertion/Deletion**   | At head: O(1) without tail; At tail or middle: O(n) forward-only | At both ends or middle: can use `previous` to simplify operations |

## 🧠 Why Use a Doubly Linked List?

1. **Bidirectional Traversal**

   * You can start at the **head** and move forward via `.next`.
   * You can start at the **tail** and move backward via `.previous`.

---

# 🛠️ **Creating a Doubly Linked List Node in Python**

To build a **doubly linked list**, each node must know:

1. **Its data**
2. **Which node comes next**
3. **Which node came before**

Below is the **Python class** for a single doubly linked-list node, followed by a **detailed breakdown**.

```python
class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data    # 📦 Holds the node’s value
        self.next = next    # ➡️ Reference to the next node (or None)
        self.prev = prev    # ⬅️ Reference to the previous node (or None)
```

---

## 🔍 Detailed Explanation

* **`data`**

  * Stores **any value** you want to keep in this node (e.g., an integer, string, object).
  * **Default**: `None` (empty) if no data is provided.

* **`next`**

  * Points to the **next node** in the list (the one to the right in diagrams).
  * When you **create** a standalone node, it has **no successor**, so `next=None`.

* **`prev`**

  * Points to the **previous node** in the list (the one to the left in diagrams).
  * A brand-new node has **no predecessor**, so `prev=None`.

---

---

# ➕ **Doubly Linked List class**

In a **doubly linked list**, each node knows both its **next** and **previous** neighbor. To append (add to the end), we update:

1. The current **tail**’s `.next` → new node
2. The new node’s `.prev` → old tail
3. The list’s **tail** pointer → new node
4. Increase the **count**

---

## 📜 Code for `DoublyLinkedList class`

```python
class DoublyLinkedList:
    def __init__(self):
        self.head = None     # First node
        self.tail = None     # Last node
        self.count = 0       # Number of nodes

```
---
