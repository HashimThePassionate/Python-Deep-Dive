# **Introducing to Linked Lists** 🔗

A **linked list** is a fundamental and widely used data structure in computer science. It offers flexibility and efficiency in memory usage and is ideal when dealing with dynamic data.

---

## 🧠 Key Properties of Linked Lists

1. **Data Stored in Separate Memory Locations**
   Each data element (called a **node**) is stored in a separate location in memory. These nodes are connected through **pointers**.

   > 🔗 A **pointer** is a variable that stores the **memory address** of another variable.

2. **Linked via Pointers**
   Every node contains:

   * 🗃 **Data** — the actual value
   * 🧭 **Next** — a pointer that links to the next node in the list

3. **Dynamic Size**
   Unlike arrays, linked lists can **grow or shrink** during program execution. You don’t need to define the size in advance.

---

## 🔍 Breakdown of a Node

Each **node** in a linked list has the following structure:

```plaintext
┌───────────┐
│   Data    │
├───────────┤
│   Next →  │──→ Next Node or None
└───────────┘
```

* **Data** stores the actual value.
* **Next** is a pointer to the next node (or `None` if it is the last node).

---

## 🖼️ Diagram Explanation

<div align="center">
  <img src="./images/01.jpg" alt="" width="400px"/>
</div>

In the figure above:

* `A` and `B` are two nodes.
* Node `A` holds data and a pointer to node `B`.
* Node `B` holds data and a pointer to `None`, indicating it is the **last node**.

---
