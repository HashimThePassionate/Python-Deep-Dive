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

We begin the implementation by creating a `Tree` class that maintains the **root node** of the tree:

```python
class Tree:
    def __init__(self):
        self.root_node = None
```

That’s all it takes to maintain the **state of a tree**.
Now, let’s examine the **main operations** used within the binary search tree.

---

## 🔑 **Binary Search Tree Operations**

The operations that can be performed on a BST are:

* ➕ Insert
* ❌ Delete
* 🔎 Search
* 🔽 Find Minimum
* 🔼 Find Maximum

We will start with the **Insert Operation**.

---

## 🌱 Inserting Nodes

To insert a new element, we must ensure that the **properties of a BST are not violated**:

* If the new value is **less than the root**, it goes into the **left subtree**.
* If the new value is **greater**, it goes into the **right subtree**.

We keep comparing until we reach a `None` position, where the node is inserted.

---

## 🛠 Example: Insert `5, 3, 7, 1`

### Step 1: Insert `5`

* Create a node with value `5`.
* Since it’s the **first node**, it becomes the **root**.

---

### Step 2: Insert `3`

* Compare `3` with root `5`.
* `3 < 5`, so it goes to the **left** of `5`.

<div align="center">
  <img src="./images/04.jpg" alt="" width="150px"/>

📷 *Figure 6.25*
</div>

👉 The BST property is satisfied.

---

### Step 3: Insert `7`

* Compare `7` with root `5`.
* `7 > 5`, so it goes to the **right** of `5`.

<div align="center">
  <img src="./images/05.jpg" alt="" width="250px"/>

📷 *Figure 6.26*
</div>

---

### Step 4: Insert `1` (First Comparison)

* Compare `1` with root `5`.
* `1 < 5`, so we go left to node `3`.

<div align="center">
  <img src="./images/06.jpg" alt="" width="250px"/>

📷 *Figure 6.27*
</div>

---

### Step 5: Insert `1` (Second Comparison)

* Compare `1` with node `3`.
* `1 < 3`, so it goes to the **left of node 3**.

<div align="center">
  <img src="./images/06.jpg" alt="" width="250px"/>

📷 *Figure 6.28*
</div>

---

### ✅ Final Tree

Now we have the complete BST:

<div align="center">
  <img src="./images/07.jpg" alt="" width="450px"/>

📷 *Figure 6.29*
</div>

---

## 💻 Python Implementation

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None


class Tree:
    def __init__(self):
        self.root_node = None

    def insert(self, data):
        node = Node(data)
        if self.root_node is None:
            self.root_node = node
            return self.root_node
        else:
            current = self.root_node
            parent = None
            while True:
                parent = current
                if node.data < parent.data:
                    current = current.left_child
                    if current is None:
                        parent.left_child = node
                        return self.root_node
                else:
                    current = current.right_child
                    if current is None:
                        parent.right_child = node
                        return self.root_node
```

---

## 🔄 In-Order Traversal (to view inserted elements)

```python
def inorder(self, root_node):
    current = root_node
    if current is None:
        return
    self.inorder(current.left_child)
    print(current.data)
    self.inorder(current.right_child)
```

---

## 🧪 Example Usage

```python
tree = Tree()
r = tree.insert(5)
r = tree.insert(2)
r = tree.insert(7)
r = tree.insert(9)
r = tree.insert(1)

tree.inorder(r)
```

📌 **Output:**

```
1
2
5
7
9
```

---

## ⏱ Time Complexity

* Insertion of a node in a BST takes **O(h)**,
  where **h** is the height of the tree.

---

# 🌳 **BST Searching the Tree**

## 📌 Introduction

A **Binary Search Tree (BST)** is a tree data structure in which:

* All the nodes in the **left subtree** of a node have **lower key values**.
* All the nodes in the **right subtree** have **greater key values**.

This property makes **searching for an element very efficient** ⚡.

---

## 📖 Example BST

Below is an example binary search tree containing **seven nodes**:

<div align="center">
  <img src="./images/09.jpg" alt="" width="400px"/>

**Figure 6.30:** An example binary search tree with nodes **1, 2, 3, 4, 5, 8, 10**.
</div>


---

## 🔍 Searching in BST

➡️ Suppose we want to search for a node with the value **5**:

1. Start from the **root node** → `4`.
2. Compare `5` with `4`: since **5 > 4**, move to the **right subtree**.
3. In the right subtree, root is `8`. Compare `5` with `8`: since **5 < 8**, move to the **left subtree**.
4. The left child of `8` is `5`. Compare with required value `5`: ✅ **match found**.

📢 Output: `"Item found"` 🎉

---

## 💻 Implementation in Python

Here’s how searching can be implemented in the **Tree class**:

```python
def search(self, data):
    current = self.root_node
    while True:
        if current is None:
            print("Item not found")
            return None
        elif current.data is data:
            print("Item found", data)
            return data
        elif current.data > data:
            current = current.left_child
        else:
            current = current.right_child
```

### ⚙️ Working of the Algorithm:

* Start searching from the **root node**.
* If the data item **doesn’t exist**, return `None`.
* If found, return the **data value**.
* If `data < current node`, move **left**.
* If `data > current node`, move **right**.

---

## 🌱 Example Code — Insert & Search

```python
tree = Tree()
tree.insert(5)
tree.insert(2)
tree.insert(7)
tree.insert(9)
tree.insert(1)

tree.search(9)
```

---

## 🖥️ Output

```
Item found 9
```

✅ The program successfully finds items present in the tree.
❌ Values not present in the BST (within range `1–10`) return `"Item not found"`.

---


