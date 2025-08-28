# 📑 **Introducing Hash Tables**

As we know, **arrays** and **lists** store the data elements in **sequence**.
In an array, the data items are accessed by an **index number**.

✔️ Accessing array elements using index numbers is **fast**.
❌ However, they are **inconvenient** when we cannot remember the index number.

👉 Example:
If we wish to extract the **phone number** of a person from the address book at **index 56**, there is **nothing linking a contact to number 56**.
It becomes **difficult to retrieve** an entry from the list using only the index value.

---

## 🔑 Why Hash Tables?

Hash tables are a **data structure** better suited for this kind of problem.

* A **hash table** stores elements in **key–value pairs**.
* Unlike arrays/lists, elements are accessed by a **keyword** (not by index).
* It uses a **hash function** to compute the index position where an element should be stored or retrieved.
* This provides **fast lookups** ⚡, since the index corresponds to the **hash value** of the key.

---

## 🖼️ Visual Representation

Below is an overview of how a **hash table** stores data.

<div align="center">
  <img src="./images/01.png" alt="" width="500px"/>

**Figure 8.1:** An example of a hash table
</div>

Here:

* Keys like `Hashim`, `Muhammad`, `Ishaque`, `Sara` are passed into a **hash function**.
* Example hash function:

```python
sum(ord(c) for c in key) % 256
```

* This function computes a **hash value (index)**.
* Each **key** is then mapped to its corresponding **value** (e.g., phone numbers).

---

## 📘 Dictionaries (Real-World Example)

Dictionaries in Python are widely used and are often built using **hash tables**.

* A dictionary stores data in **(key, value)** pairs.
* Instead of accessing the contact with an **index**, we use the **key**.

### 🐍 Python Example

```python
my_dict = {
    "Hashim": "9229012345",
    "Muhammad": "9229012346",
    "Ishaque": "9229012347",
    "Sara": "9229012348"
}

print("All keys and values")
for x, y in my_dict.items():
    print(x, ":", y)  # prints keys and values

print(my_dict["Hashim"])
```

---

### 📤 Output

```
All keys and values
Hashim: 9229012345
Muhammad: 9229012346
Ishaque: 9229012347
Sara: 9229012348
9229012345
```

---

## ⚡ Efficiency of Hash Tables

* Hash tables store data in a way that makes retrieval **extremely fast**.
* They are based on the concept of **hashing**, which converts keys into index values.

👉 This makes them a fundamental structure for applications like **dictionaries, symbol tables, caching, and databases**.

---

