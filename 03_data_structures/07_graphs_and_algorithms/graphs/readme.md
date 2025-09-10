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

