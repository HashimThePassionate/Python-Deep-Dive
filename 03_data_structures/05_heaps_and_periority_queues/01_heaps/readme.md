# 🌳 Heaps

A **heap** is a specialized **tree-based data structure** where nodes are arranged following a specific rule known as the **heap property**.

👉 **Heap Property**:
There must be a certain relationship between a **parent node** and its **child nodes**.

---

## 🔼 Max Heap

* Each **parent node value** is **greater than or equal** to its children.
* The **root node** is always the **largest element**.

📌 **Example (Max Heap):**
<div align="center">
  <img src="./images/01.jpg" alt="" width="500px"/>

*Figure 7.1: An example of a max heap*
</div>

---

## 🔽 Min Heap

* Each **parent node value** is **less than or equal** to its children.
* The **root node** is always the **smallest element**.

📌 **Example (Min Heap):**
<div align="center">
  <img src="./images/02.jpg" alt="" width="500px"/>

*Figure 7.2: An example of a min heap*
</div>

---

## ⚡ Importance of Heaps

Heaps are powerful because of their applications in:

* 📊 **Heap Sort Algorithms**
* 🛠️ **Priority Queues**

The most common type is the **Binary Heap**, where:

* Each node has **at most two children**.
* If a binary heap has `n` nodes → it has a **minimum height of log₂n**.

---

## 🌲 Complete Binary Tree

A **complete binary tree** is one where **each row must be completely filled** before filling the next row.

📌 **Example:**
<div align="center">
  <img src="./images/03.jpg" alt="" width="500px"/>

*Figure 7.3: An example of a complete binary tree*
</div>

---

## 🧮 Heap Implementation using Indexing

We can represent heaps efficiently using **arrays**. The relationship between indices is:

* **Left Child of node at index `n`** → located at `2n`
* **Right Child of node at index `n`** → located at `2n + 1`
* **Parent of node at index `i`** → located at `⌊i/2⌋`

👉 **Important Rule**: Indexing starts at **1**. A dummy element is placed at **index 0** in the array.

📌 **Example:**

<div align="center">
  <img src="./images/04.jpg" alt="" width="400px"/>

*Figure 7.4: Binary tree and index positions of all the nodes*
</div>

---

# 🌳 **Insertion Operation**

## 📌 Introduction

Insertion in a **Min Heap** works in two main steps:

1. ➕ **Insert the new element** at the end of the list (bottom-most position of the tree).
2. 🔄 **Heapify (arrange)** – Compare the newly added element with its parent and swap if needed until the heap property is restored.

👉 Heap property for **Min Heap**:

* Parent value must always be **less than or equal** to its children.
* The **smallest element** is always at the **root**.

---

## 🖼️ Step-by-Step Figures

### 1️⃣ Insert new node `2` into the heap

<div align="center">
  <img src="./images/05.jpg" alt="" width="400px"/>

*Figure 7.5: Insertion of a new node `2` in the existing heap*
</div>

---

### 2️⃣ Swap nodes `2` and `6`

<div align="center">
  <img src="./images/06.jpg" alt="" width="400px"/>

*Figure 7.6: Swapping nodes `2` and `6` to maintain the heap property*
</div>

---

### 3️⃣ Swap nodes `2` and `3`

<div align="center">
  <img src="./images/07.jpg" alt="" width="400px"/>

*Figure 7.7: Swapping nodes `2` and `3` to maintain the heap property*
</div>

---

### 4️⃣ Final Heap

<div align="center">
  <img src="./images/09.jpg" alt="" width="400px"/>

*Figure 7.8: Final heap after insertion of new node `2`*
</div>

---

## 🔢 Example: Constructing a Heap from Scratch

We now insert elements `{4, 8, 7, 2, 9, 10, 5, 1, 3, 6}` step by step.

---

### 🪜 Steps 1 to 6

<div align="center">
  <img src="./images/10.jpg" alt="" width="500px"/>

*Figure 7.9: Step-by-step procedure to create a heap (Insert 4, 8, 7, 2, 9, 10)*
</div>

---

### 🪜 Steps 7 to 9

<div align="center">
  <img src="./images/11.jpg" alt="" width="500px"/>

*Figure 7.10: Steps 7 to 9 in creating the heap (Insert 5, 1, 3)*
</div>

---

### 🪜 Step 10 (Final Insertion)

<div align="center">
  <img src="./images/12.jpg" alt="" width="500px"/>

*Figure 7.11: Last step and construction of the final heap (Insert 6)*
</div>

---

## 🧑‍💻 Implementation in Python

We use two methods:

### ⚙️ `arrange()` (Heapify Up)

```python
def arrange(self, k):
    while k // 2 > 0:   # loop until root
        if self.heap[k] < self.heap[k // 2]:  # if child < parent
            self.heap[k], self.heap[k // 2] = self.heap[k // 2], self.heap[k]  # swap
        k //= 2  # move up to parent
```

🔎 Explanation:

* `while k // 2 > 0:` → Continue until reaching the root.
* `if self.heap[k] < self.heap[k // 2]:` → If child is smaller, swap with parent.
* `k //= 2` → Move up one level.

---

### ⚙️ `insert()` Method

```python
def insert(self, item):
    self.heap.append(item)   # add item at the end
    self.size += 1           # increase heap size
    self.arrange(self.size)  # heapify (restore property)
```

---

## 🏗️ Building the Heap

```python
h = MinHeap()
for i in (4, 8, 7, 2, 9, 10, 5, 1, 3, 6):
    h.insert(i)

print(h.heap)
```

---

## 🖨️ Output

```text
[0, 1, 2, 5, 3, 6, 10, 7, 8, 4, 9]
```

---

## ✅ Final Observation

* The output matches the structure shown in **Figure 7.11** 🎯
* The **root element is the smallest (1)**, and all parents are smaller than their children, maintaining **Min Heap property**.

---

# 🗑️ **Delete Operation** (Percolate-Down)

## 🔍 What is the **Delete** operation?

The delete operation removes an element from the heap. Most commonly we **delete the root** because:

* In a **min-heap**, the root is the **minimum** element.
* In a **max-heap**, the root is the **maximum** element.

**Important:** After removing the root, we **move the last element** of the heap to the root position. This **violates** the heap property, so we must **reorganize** the nodes so that *every parent ≤ its children* (min-heap).
This reorganization from **top to bottom** is called **heapify** or **percolate down** (also “sink”).

---

## 🪜 Algorithm (Min-Heap) — Step-by-Step

1. ✅ **Delete the root** (which holds the minimum value).
2. ⬆️ **Move the last element** to the **root** position.
3. 🔄 **Heapify (percolate down / sink)** from the root:

   * Compare the current node with **both children**.
   * **Pick the smaller child** (for min-heap).
   * If `current > smaller_child`, **swap** and continue **downwards**.
   * Stop when the heap property is satisfied or you reach a leaf.

---

## 🖼️ Figures (Full sequence)

### 1) Delete the current root (= 2)

<div align="center">
  <img src="./images/13.jpg" alt="" width="400px"/>

*Figure 7.12: Deletion of a node with value `2` at the root in the existing heap.*
</div>

---

### 2) Move the **last element** (here `6`) to the **root**

<div align="center">
  <img src="./images/14.jpg" alt="" width="400px"/>

*Figure 7.13: Moving the last element (node `6`) to the root position.*
</div>

---

### 3) Compare root (`6`) with its children (`5` and `3`) → **swap with smaller child `3`**

<div align="center">
  <img src="./images/15.jpg" alt="" width="400px"/>

*Figure 7.14: Swapping root `6` with node `3`.*
</div>

---

### 4) Continue percolating `6` down — here **no swap** with `10`

<div align="center">
  <img src="./images/16.jpg" alt="" width="400px"/>

*Figure 7.15: Comparing `6` with child `10` → already satisfies min-heap (no swap).*
</div>

> ✅ After this last comparison, the heap again satisfies the **min-heap** property.

---

## 🧑‍💻 Helper & Core Methods (Python)

> Below methods are defined inside a `MinHeap` class that uses **1-based indexing** with a **sentinel** at index `0` (that is why you’ll see arrays start with `0`).

### 🔎 `minchild(k)` — pick the **smaller** child’s index

```python
def minchild(self, k):
    if k * 2 + 1 > self.size:
        return k * 2
    elif self.heap[k * 2] < self.heap[k * 2 + 1]:
        return k * 2
    else:
        return k * 2 + 1
```

* 👇 **Explanation**

  * `if k * 2 + 1 > self.size:` → There is **no right child**, so return **left** child index.
  * Else, return the index of the **smaller** of the two children.

> ℹ️ In one narrative line you may see “`minindex()`” mentioned—this is just a naming slip. The actual helper is **`minchild()`**.

---

### ⬇️ `sink(k)` — **percolate down** from index `k`

```python
def sink(self, k):
    while k * 2 <= self.size:
        mc = self.minchild(k)
        if self.heap[k] > self.heap[mc]:
            self.heap[k], self.heap[mc] = self.heap[mc], self.heap[k]
        k = mc
```

* 🔁 Loop while `k` has at least a **left child**.
* 🎯 Find the **smaller child** `mc = minchild(k)`.
* 🔄 If `parent > child`, **swap** and continue sinking.

---

### 🗑️ `delete_at_root()` — remove and return the **min (root)**

```python
def delete_at_root(self):
    item = self.heap[1]                 # save root (min)
    self.heap[1] = self.heap[self.size] # move last -> root
    self.size -= 1                      # shrink size
    self.heap.pop()                     # drop last slot
    self.sink(1)                        # restore heap property
    return item
```

* 🧠 Copy the **root value** to return later.
* ⬆️ Move the **last element** to the root position.
* ➖ Decrease **size** and remove the old last element.
* ⛏️ **Sink** from the root to restore heap order.

---

## 🧪 Full Example (Insert → Delete Root)

We will first insert the items `{2, 3, 5, 7, 9, 10, 6}` into a min-heap and then delete the root.

```python
h = MinHeap()
for i in (2, 3, 5, 7, 9, 10, 6):
    h.insert(i)
print(h.heap)

n = h.delete_at_root()
print(n)
print(h.heap)
```

### 🖨️ Output

```text
[0, 2, 3, 5, 7, 9, 10, 6]
2
[0, 3, 6, 5, 7, 9, 10]
```

* The first line is the internal **array** for the heap, using 1-based indexing with a leading `0`.
* The second line shows the **deleted root** (`2`), which is the **minimum** in a min-heap.
* The third line is the **reorganized heap** after percolating down: `[0, 3, 6, 5, 7, 9, 10]`.

> 🔎 **Note about figures vs array layout:**
> The figures (7.12–7.15) illustrate one valid min-heap configuration of these keys. Your array trace also shows a valid min-heap but with the left/right subtrees swapped compared to the figure. Both obey the min-heap rule; heap **shape** depends on the exact insertion sequence and how ties/positions are handled during insert.

---

## 🧩 Dry-Run of the **Percolate-Down** (matches the printed arrays)

Initial array (before delete):
`[0, 2, 3, 5, 7, 9, 10, 6]`

1. **Delete root `2`** and move last element `6` to root:
   `[0, 6, 3, 5, 7, 9, 10]`  ← (size reduced by 1)

2. At index `1` (value `6`), children are `3` (idx 2) and `5` (idx 3).
   **Smaller child = 3** → `6 > 3` ⇒ **swap**
   `[0, 3, 6, 5, 7, 9, 10]`

3. Now at index `2` (value `6`), children are `7` (idx 4) and `9` (idx 5).
   **Smaller child = 7** and `6 ≤ 7` ⇒ **stop**.

✅ Final heap matches the output:
`[0, 3, 6, 5, 7, 9, 10]`

> The text mentions *“indexes of the nodes can \[be] checked as shown in **Figure 7.16**”*. That statement simply refers to validating the final **level-order** array ↔ **tree** mapping.

---

## ⏱️ Time Complexity

* **Delete root** (with percolate-down): **O(log n)**
  (Height of a complete binary tree is `⌊log₂ n⌋`, and we swap down at most that many levels.)

* **Space**: **O(1)** extra (in-place within the heap array).

---

# 📚 **Deletion of an Element at a Specific Location**

Generally, we delete an element at the **root** of a heap. However, an element can also be deleted at a **specific location** from the heap.

Let’s understand this step by step with an example.

---

## 🖼 Step 1: Deleting Node 3

We want to delete **node 3** (at index `2`).
👉 After deleting node `3`, the **last node** (value `15`) is moved to the deleted node's position.

<div align="center">
  <img src="./images/17.jpg"/>

*Figure 7.16: The deletion of node 3 from the heap*
</div>

---

## 🖼 Step 2: Comparing and Swapping

* The moved node `15` is compared with its parent and children.
* Since `15` is already greater than the root `1`, no swap is needed there.
* Next, compare with children → the left child `5` is **smaller**, so **swap `15` with `5`**.

<div align="center">
  <img src="./images/18.jpg"/>

*Figure 7.17: A comparison of node 15 with 5 and 11, and swapping node 15 with node 5*
</div>

---

## 🖼 Step 3: Final Heap Adjustment

* Now `15` is compared again with its new child, node `8`.
* Since `8` is smaller, **swap `15` with `8`**.
* The final heap now satisfies the **min-heap property**. ✅

<div align="center">
  <img src="./images/19.jpg"/>

*Figure 7.18: The final heap after swapping node 8 and node 15*
</div>

---

## ⚙️ Implementation in Python

The deletion operation for removing a data item at any **given index location** can be implemented as follows inside the `MinHeap` class:

```python
def delete_at_location(self, location):
    item = self.heap[location]
    self.heap[location] = self.heap[self.size]
    self.size -= 1
    self.heap.pop()
    self.sink(location)
    return item
```

👉 This implementation is very similar to deleting the **root element**, except here we specify the **index location** that has to be deleted.

---

## 📝 Example Code

```python
h = MinHeap()
for i in (4, 8, 7, 2, 9, 10, 5, 1, 3, 6):
    h.insert(i)

print(h.heap)                # Before deletion
n = h.delete_at_location(2)  # Delete element at index 2
print(n)                     # Print deleted element
print(h.heap)                # After deletion
```

---

## 💻 Output

```text
[0, 1, 2, 5, 3, 6, 10, 7, 8, 4, 9]
2
[0, 1, 3, 5, 4, 6, 10, 7, 8, 9]
```

✅ Before and after deletion, heap nodes remain arranged according to their **index positions**.

---

# 📚 **Heap Sort Algorithm**

Heap is an important **data structure** for sorting a list of elements since it is very suitable for handling **large datasets**.

If we want to sort a list of elements in **ascending order**, we can use a **Min-Heap** for this purpose.

✨ **Key idea:**

* A Min-Heap always stores the **smallest element at the root**.
* By repeatedly removing the root and reorganizing the heap, we can easily sort the entire list.

---

## ⚡ Process of Heap Sort

1️⃣ **Create a Min-Heap** using all the given data elements.
2️⃣ **Read & Delete the root element** (minimum value).

* Copy the last element of the tree to the new root.
* Reorganize the tree to maintain the heap property.
  3️⃣ **Repeat Step 2** until all elements are deleted.
  4️⃣ **Final Result →** A sorted list of elements in ascending order.

---

## 🛠️ Maintaining Heap Property

* When a new element is **added**, the heap property is maintained using the **`arrange()`** method.
* When an element is **deleted**, the heap property is restored using the **`sink()`** method.

---

## 💻 Implementation Example

Suppose we have the following data items:

```python
h = MinHeap()
unsorted_list = [4, 8, 7, 2, 9, 10, 5, 1, 3, 6]

for i in unsorted_list:
    h.insert(i)

print("Unsorted list: {}".format(unsorted_list))
```

✅ Here:

* A **Min-Heap `h`** is created.
* Each element from `unsorted_list` is inserted into the heap.
* After every `insert()`, the **heap order property** is restored by the **sink method**.

---

## 🧹 Sorting Phase

We now delete elements from the heap one by one to get the **sorted list**.

### 🔹 Heap Sort Method

```python
def heap_sort(self):
    sorted_list = []
    for node in range(self.size):
        n = self.delete_at_root()
        sorted_list.append(n)
    return sorted_list
```

📌 Explanation:

* **`sorted_list`** → An empty list to store elements in sorted order.
* Loop runs for the **number of items** in the heap.
* In each iteration:

  * **`delete_at_root()`** → Removes the minimum value (root).
  * Append it to **`sorted_list`**.
* Return the **sorted list** at the end.

---

## 🚀 Running Heap Sort

```python
print("Unsorted list: {}".format(unsorted_list))
print("Sorted list: {}".format(h.heap_sort()))
```

### ✅ Output

```
Unsorted list: [4, 8, 7, 2, 9, 10, 5, 1, 3, 6]
Sorted list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

---

## 📊 Time Complexity Analysis

* **Heap creation (Insert method):** `O(n)`
* **Reorganizing after deletion (Sink operation):** `O(log n)`
* **Total complexity:** `O(n log n)`

⏱️ Complexity in all cases:

* **Worst-case:** `O(n log n)`
* **Average-case:** `O(n log n)`
* **Best-case:** `O(n log n)`

✨ Hence, **Heap Sort** is a very **efficient and reliable sorting algorithm**.

---


