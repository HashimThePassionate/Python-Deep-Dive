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
