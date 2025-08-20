# 🌳 **Binary Search Trees (BST)**

A **Binary Search Tree (BST)** is a special type of binary tree that stores data in a structured way for **fast searching, insertion, and deletion**.

---

## 🧠 Definition

A **Binary Tree** is called a **Binary Search Tree** if:

* The value at any node is **greater** than (or equal to) all values in its **left subtree**.
* The value at any node is **less** than all values in its **right subtree**.

This property holds **recursively** for **every node** in the tree.

---

## 📍 Example 1 — Basic BST Condition

<div align="center">
  <img src="./images/01.jpg" alt="" width="350px"/>

**Figure 6.22:** An example of a **binary search tree** with three nodes.
</div>



* Root = `K1`
* Left child = `K2` → satisfies `K2 <= K1`
* Right child = `K3` → satisfies `K3 > K1`

✅ This satisfies the BST property.

---

## 📍 Example 2 — Valid BST with Six Nodes

<div align="center">
  <img src="./images/02.jpg" alt="" width="350px"/>

**Figure 6.23:** A **Binary Search Tree of six nodes**.
</div>

Structure:

```
        5
      /   \
     3     7
    / \      \
   1   4      9
```

* All nodes in the **left subtree** of `5` are `< 5`.
* All nodes in the **right subtree** of `5` are `> 5`.
* Node `3` → left = `1 (<3)`, right = `4 (>3)` ✅
* Node `7` → right = `9 (>7)` ✅

➡️ Every node satisfies BST rules → This is a **valid BST**.

---

## 📍 Example 3 — Not a BST ❌

<div align="center">
  <img src="./images/03.jpg" alt="" width="350px"/>

**Figure 6.24:** This is a **binary tree** but **not** a BST.
</div>



Structure:

```
        5
      /   \
     7     3
    / \      \
   1   4      9
```

Problems:

* Node `7` is in the **left subtree** of `5`, but `7 > 5` ❌
* Node `4` is in the **right subtree** of `7`, but `4 < 7` ❌

➡️ Both conditions **violate** BST rules → Not a BST.

---
