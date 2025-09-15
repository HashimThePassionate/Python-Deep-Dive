# 📊 **Graphs**

A **graph** is a set of a finite number of **vertices** (also called **nodes**) and **edges**, where the edges are the **links between vertices**.
Each edge in a graph connects two distinct nodes.

In mathematics, a graph is a formal representation of a **network**.
Formally:

<pre align="center">
G = (V, E)
</pre>

where:

* **V** = set of vertices
* **E** = set of edges

---

## 🖼️ Example of a Graph

<div align="center">
  <img src="./images/01.jpg" width="400px"/>

*Figure 9.1: An example of a graph*
</div>

The graph $G = (V, E)$ in **Figure 9.1** can be described as:

* **Vertices (V):**

<pre align="center">
V = {A, B, C, D, E}
</pre>

* **Edges (E):**

<pre align="center">
E = {{A, B}, {A, C}, {B, C}, {B, D}, {C, D}, {D, D}, {B, E}, {D, E}}
</pre>

So,

<pre align="center">
G = (V, E)
</pre>

---

## 📘 Important Definitions in Graphs

### 🔹 Node or Vertex

A **point or node** in a graph is called a **vertex**.<br/>
👉 In the diagram above, vertices are **A, B, C, D, and E** (represented as dots).

---

### 🔹 Edge

A **connection between two vertices**.<br/>
👉 Example: the line connecting **A** and **B**.

---

### 🔹 Loop

An **edge that starts and ends on the same vertex**.<br/>
👉 Example: at **D**, the edge returns to itself.

---

### 🔹 Degree of a Vertex

The **degree** of a vertex is the **total number of edges** incident on it.<br/>
👉 Example: Vertex **B** has a **degree of 4** in the figure.

---

### 🔹 Adjacency

Two vertices are **adjacent** if there is an edge between them.<br/>
👉 Example: **C** is adjacent to **A** (since there is an edge {A, C}).

---

### 🔹 Path

A **sequence of vertices and edges** connecting two nodes.<br/>
👉 Example: Path **C → A → B → E** represents a path from **C** to **E**.

---

### 🔹 Leaf Vertex (Pendant Vertex)

A **vertex with degree = 1**.<br/>
👉 Example: If a vertex has only one edge connected, it is a **leaf vertex**.

---

# 🔄 **Directed and Undirected Graphs**

Graphs are represented by the **edges** between the **nodes**.
👉 These connecting edges can be either **directed** or **undirected**.

---

## 📍 Undirected Graph

* If the connecting edges are **undirected**, then the graph is called an **undirected graph**.
* An **undirected graph** simply represents edges as **lines between the nodes**.
* There is no extra information about the relationship between nodes other than the fact that they are connected.

🖼️ Example:

<div align="center">
  <img src="./images/02.jpg" width="300px"/>

*Figure 9.2: An example of an undirected graph*
</div>

👉 In Figure 9.2, we demonstrate an undirected graph of four nodes:

```
V = {A, B, C, D}
```

These nodes are connected using undirected edges.

---

## 📍 Directed Graph

* If the connecting edges are **directed**, then the graph is called a **directed graph**.
* In a **directed graph**, edges provide information about the **direction** of connection.
* An edge **(A, B)** is **not equal** to edge **(B, A)**.
* Directed edges are drawn as **lines with arrows**, showing the direction of flow.

🖼️ Example:

<div align="center">
  <img src="./images/03.jpg" width="300px"/>

*Figure 9.3: An example of a directed graph*
</div>

👉 In Figure 9.3, many nodes are connected using **directed edges**.

* For instance, you can move from **A → B**, but not from **B → A**.

---

## 📘 Important Terms in Directed Graphs

### 🔹 Indegree

The total number of **edges that come into a vertex**.<br/>
👉 Example: Node **E** has **indegree = 1**, due to edge **C → E**.

---

### 🔹 Outdegree

The total number of **edges that go out from a vertex**.<br/>
👉 Example: Node **E** has **outdegree = 2**, because of edges **E → F** and **E → D**.

---

### 🔹 Isolated Vertex

A vertex with **degree = 0** (no incoming or outgoing edges).<br/>
👉 Example: Node **G** in Figure 9.3.

---

### 🔹 Source Vertex

A vertex with **indegree = 0**.<br/>
👉 Example: Node **A** in Figure 9.3.

---

### 🔹 Sink Vertex

A vertex with **outdegree = 0**.<br/>
👉 Example: Node **F** in Figure 9.3.

---

# 🎯 Directed Acyclic Graphs (DAGs)

A **Directed Acyclic Graph (DAG)** is a **directed graph** that contains **no cycles**.

* All edges are directed from one node to another.
* The sequence of edges never forms a **closed loop**.
* A **cycle** in a graph is formed when the starting node of the first edge is equal to the ending node of the last edge.

🖼️ Example:

<div align="center">
  <img src="./images/04.jpg" width="350px"/>

*Figure 9.4: An example of a directed acyclic graph*
</div>

👉 In this DAG:

* All edges are directed.
* There is **no cycle** (no path that starts and ends at the same node).

📌 **Key property:**
If we start on any path from a given node, we will **never end up on the same node again**.

✨ **Applications of DAGs:**

* Job scheduling 🗓️
* Citation graphs 📚
* Data compression 📦

---

# ⚖️ Weighted Graphs

A **Weighted Graph** is a graph in which each edge has a **numeric weight** associated with it.

* Can be **directed** or **undirected**.
* Weight may represent **distance**, **cost**, or **any metric** depending on the problem.

🖼️ Example:

<div align="center">
  <img src="./images/05.jpg" width="350px"/>

*Figure 9.5: An example of a weighted graph*
</div>

👉 In this weighted graph:

* **Edge weights** represent distances between nodes.
* We want to travel from **A → D**.

### 🔹 Possible Paths:

1. **Direct path:**

   * $A \to D$
   * Cost = **40**

2. **Via B and C:**

   * $A \to B \to C \to D$
   * Cost = $5 + 10 + 10 = 25$

### ✅ Best Path:

* Path **A → B → C → D** is **better**, since **25 < 40**.
* Hence, the shortest path is chosen using weights.

---

# 🔗 Bipartite Graphs

A **Bipartite Graph** (also called a **Bigraph**) is a **special type of graph** in which:

* All the nodes can be divided into **two disjoint sets**.
* Every edge **always connects a node from one set to a node in the other set**.
* No edge exists **between nodes of the same set**.

🖼️ Example:

<div align="center">
  <img src="./images/06.jpg" width="400px"/>
  
*Figure 9.6: An example of a bipartite graph*
</div>

👉 In this graph:

* The vertices are divided into **two sets**:

  * **Set U = {A, B, C, D}**
  * **Set V = {E, F, G, H}**
* Each edge has **one vertex in U** and **the other vertex in V**.

---

## 📘 Key Property of Bipartite Graphs

* **No edge** connects vertices **within the same set**.
* All edges **must connect across the two sets**.

---

## 🏗️ Applications of Bipartite Graphs

1. **Applicants and Jobs** 💼

   * One set = Applicants
   * Other set = Jobs
   * An edge shows which applicant is eligible for which job.

2. **Football Players and Clubs** ⚽

   * One set = Players
   * Other set = Clubs
   * An edge shows if a player has played for a particular club.

---

# 🗂️ **Graph Representations**

Graph representation techniques define **how we store a graph in memory**.
This includes storing:

* **Vertices (nodes)** 🟢
* **Edges (connections)** 🔗
* **Weights (if weighted graph)** ⚖️

There are **two common methods** to represent a graph:

1. **Adjacency List** 📋
2. **Adjacency Matrix** 🧮

---

## 📋 Adjacency List Representation

* Based on a **linked list**.
* For every vertex, we maintain a **list of its neighbors** (adjacent nodes).
* Efficient when the graph is **sparse** (few edges compared to vertices).

👉 Example:

* If a graph has **200 nodes** but only **100 edges**, then adjacency list is best.
* Saves space because we only store existing edges, not unnecessary zeros.

---

## 🧮 Adjacency Matrix Representation

* Based on a **matrix (2D array)**.
* Each **row and column** represent vertices.
* A cell value indicates whether an edge exists between two nodes.

👉 Example:

* For a graph with **200 nodes**, the matrix will be **200 × 200**.
* Most cells may be **0** if the graph is sparse.

✅ **Best used when graph is dense** (many edges).
✅ **Faster lookups** – checking if an edge exists between two vertices is **O(1)**.

---

## ⚖️ Choosing Between Them

| Representation       | Best For 🏆               | Space Usage 📦                         | Lookup Speed ⏱️ |
| -------------------- | ------------------------- | -------------------------------------- | --------------- |
| **Adjacency List**   | Sparse graphs (few edges) | Less space (only store existing edges) | Slower lookup   |
| **Adjacency Matrix** | Dense graphs (many edges) | More space (matrix always stored)      | Fast lookup     |

---

# 📋 **Adjacency Lists**

In an **Adjacency List representation**:

* All the nodes **directly connected** to a node $x$ are listed in its adjacency list.
* The graph is represented by showing the **adjacent list of every vertex**.

👉 Example Graph:

<div align="center">
  <img src="./images/07.jpg" alt="" width="350px"/>

*Figure 9.7: A sample graph of five nodes*
</div>

Here:

* **A** is adjacent to **B** and **C**.
* **B** is adjacent to **E, C, A**, etc.

---

## 🔗 Adjacency List Representation

A **linked list** can be used to implement adjacency lists.

* We need as many **linked lists** as there are **nodes**.
* At each index, we store the **adjacent vertices** of that node.

👉 Example Adjacency List for Figure 9.7:

<div align="center">
  <img src="./images/08.jpg" alt="" width="350px"/>

*Figure 9.8 : Adjacency list for the graph shown in Figure 9.7*
</div>

---

### 🖥️ Python Dictionary Implementation

In Python, instead of linked lists, we often use **dictionaries** to represent adjacency lists (since they allow easy key–value storage).

```python
# Graph represented as adjacency list using dictionary
graph = dict()

graph['A'] = ['B', 'C']
graph['B'] = ['E', 'C', 'A']
graph['C'] = ['A', 'B', 'E', 'F']
graph['E'] = ['B', 'C']
graph['F'] = ['C']
```

---

### 🔎 Explanation (Line by Line)

1. `graph = dict()`

   * Creates an empty dictionary called **graph**.
   * Each key will represent a **vertex**.
   * Each value will be a **list of adjacent vertices**.

2. `graph['A'] = ['B', 'C']`

   * Vertex **A** has neighbors **B** and **C**.

3. `graph['B'] = ['E', 'C', 'A']`

   * Vertex **B** has neighbors **E, C, and A**.

4. `graph['C'] = ['A', 'B', 'E', 'F']`

   * Vertex **C** has neighbors **A, B, E, and F**.

5. `graph['E'] = ['B', 'C']`

   * Vertex **E** has neighbors **B and C**.

6. `graph['F'] = ['C']`

   * Vertex **F** has only one neighbor: **C**.

---

## ✅ Advantages of Adjacency List

* Saves space when the graph is **sparse**.
* Easy to **add or delete nodes/edges**.

## ⚠️ Disadvantage

* Checking if a particular edge exists can be **slow** compared to adjacency matrix.

---

# 🧮 **Adjacency Matrix**

Another approach to represent a graph is by using an **Adjacency Matrix**.

* The graph is represented using a **matrix (V × V)**, where **V = number of vertices**.
* Each cell in the matrix shows whether there is an **edge** between two vertices:

  * `1` → edge exists
  * `0` → edge does not exist
* The adjacency matrix is essentially a **2D array**.

---

## 📍 Example
<div align="center">
  <img src="./images/09.jpg" alt="" width="400px"/>

*Figure 9.9: A sample graph and its adjacency matrix*
</div>

👉 The graph has **vertices**: A, B, C, E, F

👉 The corresponding adjacency matrix is:

|       | A | B | C | E | F |
| ----- | - | - | - | - | - |
| **A** | 0 | 1 | 1 | 0 | 0 |
| **B** | 1 | 0 | 0 | 1 | 0 |
| **C** | 1 | 1 | 0 | 1 | 1 |
| **E** | 0 | 1 | 1 | 0 | 0 |
| **F** | 0 | 0 | 1 | 0 | 0 |

---

## 🖥️ Python Implementation

We will now implement the adjacency matrix step by step using Python.

### 1️⃣ Step 1: Graph Representation (Adjacency List in Dictionary Form)

```python
# Graph represented as adjacency list
graph = dict()
graph['A'] = ['B', 'C']
graph['B'] = ['E', 'C', 'A']
graph['C'] = ['A', 'B', 'E', 'F']
graph['E'] = ['B', 'C']
graph['F'] = ['C']
```

✔️ Here, the **keys** represent vertices (A, B, C, E, F).<br/>
✔️ The **values** are lists of adjacent vertices.

---

### 2️⃣ Step 2: Extract Vertices

```python
# Extract vertices and sort them
matrix_elements = sorted(graph.keys())
cols = rows = len(matrix_elements)
```

✔️ `matrix_elements` = `['A', 'B', 'C', 'E', 'F']`<br/>
✔️ Number of rows = columns = `5` (since 5 vertices).

---

### 3️⃣ Step 3: Initialize Empty Matrix

```python
# Create empty adjacency matrix (filled with 0s)
adjacency_matrix = [[0 for x in range(rows)] for y in range(cols)]
edges_list = []
```

✔️ `adjacency_matrix` will be a 5×5 matrix filled with zeros initially.<br/>
✔️ Example:

```
[0, 0, 0, 0, 0]
[0, 0, 0, 0, 0]
[0, 0, 0, 0, 0]
[0, 0, 0, 0, 0]
[0, 0, 0, 0, 0]
```

✔️ `edges_list` will store edges like `('A', 'B')`.

---

### 4️⃣ Step 4: Build Edge List

```python
for key in matrix_elements:
    for neighbor in graph[key]:
        edges_list.append((key, neighbor))
print(edges_list)
```

✔️ This creates a list of all edges.<br/>
✔️ Output:

```
[('A', 'B'), ('A', 'C'), 
 ('B', 'E'), ('B', 'C'), ('B', 'A'), 
 ('C', 'A'), ('C', 'B'), ('C', 'E'), ('C', 'F'), 
 ('E', 'B'), ('E', 'C'), 
 ('F', 'C')]
```

---

### 5️⃣ Step 5: Fill the Adjacency Matrix

```python
for edge in edges_list:
    index_of_first_vertex = matrix_elements.index(edge[0])
    index_of_second_vertex = matrix_elements.index(edge[1])
    adjacency_matrix[index_of_first_vertex][index_of_second_vertex] = 1
```

✔️ For each edge `(u, v)`, we find their **indices** in `matrix_elements` and set the matrix cell to `1`.

---

### 6️⃣ Final Output Matrix

```python
print(adjacency_matrix)
```

✔️ Output:

```
[0, 1, 1, 0, 0]
[1, 0, 0, 1, 0]
[1, 1, 0, 1, 1]
[0, 1, 1, 0, 0]
[0, 0, 1, 0, 0]
```

This corresponds exactly to the adjacency matrix shown in Figure 9.9 ✅

---

## ✅ Advantages of Adjacency Matrix

* Very **fast lookup** for checking if an edge exists (`O(1)` time).
* Useful in **dense graphs** (many edges).
* Widely used in **routing tables, navigation systems, transport networks**.

## ⚠️ Disadvantages

* **Consumes more space** (O(V²)), even if graph is sparse.
* **Adding/deleting vertices** is difficult compared to adjacency list.

---

# 📊 **Graph Traversals**

## 🔎 What is Graph Traversal?

A **graph traversal** means to **visit all the vertices (nodes)** of the graph while keeping track of:

* ✅ Which vertices have already been **visited**
* ❌ Which vertices have **not been visited yet**

👉 A graph traversal algorithm is considered **efficient** if it can traverse all the nodes of the graph in the **minimum possible time**.

---

## 🌳 Graph Traversal vs Tree Traversal

Graph traversal is also called a **graph search algorithm**. It is quite similar to **tree traversal algorithms** such as:

* Preorder traversal
* Inorder traversal
* Postorder traversal
* Level order traversal

📌 Just like tree traversal, in a graph traversal we:

1. Start from a **specific node**
2. Traverse through **edges** to reach all other nodes

---

## 🛤️ Common Strategy of Graph Traversal

The main strategy is:

1. **Follow a path** until a **dead end** is reached
2. **Backtrack** (move back) until we find an **alternative path**
3. Continue the process until all nodes are visited

Alternatively, we can **iteratively move** from one node to another until the **whole graph (or part of it)** is traversed.

---

## 🎯 Importance of Graph Traversal Algorithms

Graph traversal algorithms are very important for solving **fundamental problems** such as:

* 🚶 Determining how to get from **one vertex to another**
* 📍 Comparing **different paths** from **Node A to Node B**
* 🛣️ Finding the **shortest route** from one city to another in a **network of cities**

---

## 🧮 Types of Graph Traversal Algorithms

There are **two important graph traversal algorithms**:

1. **Breadth-First Search (BFS)** 🔄

   * Traverses the graph **level by level**
   * Uses a **queue** data structure

2. **Depth-First Search (DFS)** 🔂

   * Traverses the graph by going **deep into one path first**
   * Uses a **stack** (or recursion)

---

# 🌐 **Breadth-First Traversal (BFS)**

## 📌 Introduction

Breadth-First Search (BFS) works very similarly to a **level-order traversal algorithm** in a tree data structure.

* 🔹 It visits **level by level**
* 🔹 Starts at the **root node** (level 0)
* 🔹 Then visits all nodes at **level 1** (directly connected to root)
* 🔹 Moves to **level 2** and so on

👉 This ensures traversal of the graph **breadthwise**.

📌 To manage the traversal order, BFS uses a **Queue (FIFO structure)**.

---

## 🏗️ How BFS Works

1. Begin with the **starting node**
2. Visit the node and mark it as **visited**
3. Look at all its **neighbors** (adjacent vertices)
4. Add these neighbors into the **queue**
5. Repeatedly visit the **next node from the queue**
6. Add its unvisited neighbors into the queue
7. Continue until all nodes are visited

✅ Each node is visited **only once**.

---

## 🖼️ Example Graph

<div align="center">
  <img src="./images/10.jpg" width="500"/>

**Figure 9.10: A sample graph with Queue & Visited array**
</div>

* Graph has **5 nodes**: `A, B, C, D, E`
* On the right side, we have:

  * **Visited Array** → keeps track of visited nodes
  * **Queue** → helps manage BFS order

---

## 🔵 Step 1: Start with Node A

<div align="center">
  <img src="./images/11.jpg" width="500px"/>

**Figure 9.11: Node A is visited in BFS**
</div>

* Start at **A**
* Mark **A** as visited → `Visited = [A]`
* Add all adjacent nodes of A → `B, C, E` into the **Queue**

👉 Queue = `[B, C, E]`

---

## 🔵 Step 2: Visit Node B

<div align="center">
  <img src="./images/12.jpg" width="500px"/>

**Figure 9.12: Node B is visited in BFS**
</div>

* Dequeue first element → **B**
* Mark **B** as visited → `Visited = [A, B]`
* Add B’s unvisited neighbor → **D**

👉 Queue = `[C, E, D]`

---

## 🔵 Step 3: Visit Node C

<div align="center">
  <img src="./images/13.jpg" width="500px"/>

**Figure 9.13: Node C is visited in BFS**
</div>

* Dequeue → **C**
* Mark **C** as visited → `Visited = [A, B, C]`
* Neighbors of C are already visited or in queue → nothing new added

👉 Queue = `[E, D]`

---

## 🔵 Step 4: Visit Node E

<div align="center">
  <img src="./images/14.jpg" width="500px"/>

**Figure 9.14: Node E is visited in BFS**
</div>

* Dequeue → **E**
* Mark **E** as visited → `Visited = [A, B, C, E]`
* Neighbors of E are already in visited list → nothing added

👉 Queue = `[D]`

---

## 🔵 Step 5: Visit Node D

<div align="center">
  <img src="./images/15.jpg" width="500px"/>
  
**Figure 9.15: Node D is visited in BFS**
</div>

* Dequeue → **D**
* Mark **D** as visited → `Visited = [A, B, C, E, D]`
* No new neighbors left

👉 Queue = `[]` (empty → traversal complete ✅)

---

## 📍 Final BFS Traversal Order

👉 The BFS visits nodes in the order:

```
A → B → C → E → D
```

⚠️ Note: The order can vary depending on **how neighbors are enqueued**.
For example: BCE, CEB, CBE, BEC, or ECB are all valid.
In this example, we used **alphabetical order**.

---

