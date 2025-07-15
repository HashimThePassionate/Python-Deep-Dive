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

#  **Inserting a Node at the Beginning of a Doubly Linked List** 📌

When working with doubly linked lists, adding a new node at the start requires careful handling of pointers to maintain list integrity. This topic covers both scenarios—when the list is empty and when it already contains nodes—along with detailed, step-by-step explanations, illustrative figures, and a line-by-line code walkthrough. Enjoy the deep dive! 

## 📝 1. Overview

A **doubly linked list** consists of nodes where each node has:

* `data` — holds the value.
* `next` — pointer to the next node.
* `prev` — pointer to the previous node.

When inserting at the **beginning**, we must:

1. Handle the **empty list** case (no existing nodes).
2. Handle the **non-empty list** case (updating three pointers).
3. Update the **head** reference and increment the **node count**.

## 🔹 2. Insertion into an Empty List

> **Check**: Is `head` `None`?
> If **yes**, the list is empty.

* Create the new node.
* Point **both** `head` and `tail` to this node.
* No other pointers need updating.

## 🔹 3. Insertion into a Non-Empty List

> **Else** (`head` is not `None`): list has ≥ 1 node.

We must update **three links** (shown as dotted in Figure 4.22):

1. **New node’s `next` → old head**
2. **Old head’s `prev` → new node**
3. **Update `head` → new node**


## 🖼️ Figure 4.20: Inserting into an **Empty** Doubly Linked List

<div align="center">
  <img src="./images/03.jpg" alt="" width="400px"/>
</div>

1. **Single Node Structure**

   * **Data box** holds the payload.
   * **Next pointer** is `None` (→ no successor).
   * **Prev pointer** is `None` (← no predecessor).

2. **Head & Tail Arrows**

   * **Head →** The arrow from `Head` points at the new node.
   * **Tail →** The arrow from `Tail` also points at the same node.
   * This dual pointing shows the list has **one** element; it’s both start and end.

3. **Why Both Pointers?**

   * In a doubly linked list, `head` tracks the first element; `tail` tracks the last.
   * With only one node, “first” = “last,” so both references coincide.

---

## 🖼️ Figure 4.21: Inserting into a **Non-Empty** Doubly Linked List

<div align="center">
  <img src="./images/04.jpg" alt="" width="500px"/>
</div>

1. **Pre-Insertion State**

   * Three nodes are already linked:

     * Leftmost’s `prev` = `None` (it’s head).
     * Rightmost’s `next` = `None` (it’s tail).

2. **Visual Clues**

   * **Grey shading** on each node: shows existing list.
   * **New node** (unshaded in 4.22) not yet part of the list.

3. **Conceptual Action**

   * We plan to insert a brand-new node **in front** of that leftmost head.
   * We’ll update pointers so that this new node becomes the new head.

---

## 🖼️ Figure 4.22: Step-By-Step Insertion at the Beginning


<div align="center">
  <img src="./images/05.jpg" alt="" width="500px"/>
</div>

1. **Step ① – Link New → Old**

   * **Dotted arrow** from new node’s `next` box → old head.
   * This connects the new node **forward** into the list.

2. **Step ② – Link Old ← New**

   * **Dotted arrow** from old head’s `prev` box → new node.
   * This connects the old head **backward** to the new node.

3. **Step ③ – Update Head Reference**

   * **Solid arrow** labeled “Head” moves to point at the new node.
   * This officially makes the new node the list’s starting point.

4. **Why This Order?**

   * **First**, establish internal links (① & ②) so no pointer is left dangling.
   * **Then**, move the `head` reference (③) to finalize the new structure.
   * Ensures the list is never in an inconsistent state. ✅


## 💡 4. Step-by-Step Pointer Updates

| Step | Action                                                          |
| :--: | :-------------------------------------------------------------- |
|   ①  | `new_node.next = head` — link new node forward to the old head  |
|   ②  | `head.prev = new_node` — link old head backward to the new node |
|   ③  | `head = new_node` — make the new node the new head of the list  |

---

## 📚 5. Code Implementation

```python
class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data    # Value stored in the node
        self.prev = prev    # Pointer to the previous node
        self.next = next    # Pointer to the next node

class DoublyLinkedList:
    def __init__(self):
        self.head = None    # Start of the list
        self.tail = None    # End of the list
        self.count = 0      # Number of nodes

    def append_at_start(self, data):
        """Append an item at the beginning of the list."""
        new_node = Node(data)             # 🔹 Create new node with data
        if self.head is None:             # 🔍 Case 1: Empty list?
            self.head = new_node          # 📌 Head → new node
            self.tail = new_node          # 📌 Tail → new node
        else:                             # 🔍 Case 2: Non-empty list
            new_node.next = self.head     # ① Link new_node.next → old head
            self.head.prev = new_node     # ② Link old head.prev → new_node
            self.head = new_node          # ③ Update head → new_node
        self.count += 1                   # 🧮 Increment list size
```

---

## 🔍 6. Line-by-Line Explanation

1. **`new_node = Node(data)`**

   * Instantiates a `Node` object holding `data`.
   * By default, `prev` and `next` are `None`.

2. **`if self.head is None:`**

   * **Checks** if the list is empty.

3. **`self.head = new_node`**

   * Points `head` to the newly created node.

4. **`self.tail = new_node`**

   * Since it’s the only node, `tail` must also reference it.

5. **`else:`**

   * Handles the non-empty list scenario.

6. **`new_node.next = self.head`**

   * **Step ①**: New node’s `next` pointer → old head node.

7. **`self.head.prev = new_node`**

   * **Step ②**: Old head’s `prev` pointer → new node.

8. **`self.head = new_node`**

   * **Step ③**: Update `head` to the new node.

9. **`self.count += 1`**

   * **Increments** the total node count in the list.

---

## 🎯 7. Example Usage

```python
words = DoublyLinkedList()
words.append_at_start('book')
print(words.head.data)  # Output: 'book'
print(words.tail.data)  # Output: 'book'
print(words.count)      # Output: 1
```

* **First call:** list was empty → both `head` & `tail` = `'book'`.
* **Count** correctly reflects the single-node list.

---
