# 🔑 **Hash Tables**

A **Hash Table** is a powerful data structure that implements an **associative array** where data is stored in the form of **key–value pairs**.

It allows operations like **insert**, **search**, and **delete** to be performed very efficiently — making it an essential structure for many real-world applications.

---

## 📘 Real-Life Example

🔹 A **compiler** uses a **symbol table** (based on hash tables) to manage identifiers.

* Here, **keys** are character strings (identifiers).
* These keys are mapped to values using a **hash function**.
* Instead of using the key directly as an array index, the **hash function** computes the index for storing or retrieving data.

👉 This makes hash tables **extremely fast** when accessing elements.

---

## ⚙️ How Hash Tables Work

1. **Hash Function** ➝ Converts the key into an index.
2. **Index** ➝ Determines where the key–value pair should be stored in the table.
3. **Direct Access** ➝ Allows very fast retrieval of data.

---

## 🚨 Hash Collisions

Ideally, every key should map to a **unique index**.
However, in practice, multiple keys may generate the **same index** — this is called a **collision**.

✅ Different techniques exist to handle these collisions efficiently.

---

## 📚 Topics Covered in This section

* 🔹 **Hashing methods** and **hash table techniques**
* 🔹 **Collision resolution techniques** in hash tables

---

✨ Hash tables are one of the **most important data structures** in computer science — combining the power of arrays and functions to provide blazing-fast lookups and insertions.

