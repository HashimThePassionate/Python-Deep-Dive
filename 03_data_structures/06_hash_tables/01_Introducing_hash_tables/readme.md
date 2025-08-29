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

# 🔑 **Hashing Functions**

Hashing is a technique in which, when we provide **data of arbitrary size** to a function, we get a **small, simplified value**.

This function is called a **hash function**.

👉 Hashing uses a hash function to **map the keys** to another range of data in a way that the new range of keys can be used as an index in the hash table.

In other words:
**Hashing = Convert the key values into integer values (indices) for the hash table**.

---

## 📝 Example: Hashing Strings

We are using **hashing to convert strings into integers**.

➡️ Example: Hash the string `"hello world"` so that we get a numeric value corresponding to this string which can be used as an index in the hash table.

---

### 📌 `ord()` Function in Python

In Python, the **`ord()` function** returns a unique integer value (ordinal value) mapped to a character in the **Unicode encoding system**.

✔️ Unicode is a **superset of ASCII**. <br/>
✔️ Example:

```python
ord('f')
```

Output:

```
102
```

---

### 🧮 Simple Hash with `sum(map(ord, s))`

We can sum the ordinal numbers of each character in a string to get a hash:

```python
sum(map(ord, "hello world"))
```

✅ Output:

```
1116
```

---

### 📊 Visual Representation

#### Figure 8.2

Ordinal values of each character for the `"hello world"` string:

<div align="center">
  <img src="./images/02.jpg" alt="" width="500px"/>
</div>

---

## ⚠️ Problem: Collisions

The approach above is not perfect — **different strings can yield the same hash**.

Example:

```python
sum(map(ord, "world hello"))
```

✅ Output:

```
1116
```

And even:

```python
sum(map(ord, "gello xorld"))
```

✅ Output:

```
1116
```

#### Figure 8.3

Ordinal values of each character for `"gello xorld"`:

<div align="center">
  <img src="./images/03.jpg" alt="" width="500px"/>
</div>

---

## 🎯 Perfect Hashing Functions

A **perfect hash function** gives a **unique hash value** for each input string.

👉 But designing one that is **fast, efficient, and collision-free** is very difficult.
👉 Usually, we prefer **fast hash functions** and then handle collisions separately.

---

## 🚀 Improved Hashing Strategy

To reduce collisions:
✔️ Multiply each character’s ordinal value by a continuously increasing multiplier. <br/>
✔️ Add all results to get the final hash.

---

### 📊 Visual Representation

#### Figure 8.4

Ordinal values multiplied by numeric values for each character of `"hello world"`:

<div align="center">
  <img src="./images/03.jpg" alt="" width="500px"/>
</div>

Final value = **6736**

---

## 🐍 Python Implementation

```python
def myhash(s):
    mult = 1
    hv = 0
    for ch in s:
        hv += mult * ord(ch)
        mult += 1
    return hv
```

---

### 🔎 Testing the Function

```python
for item in ("hello world", "world hello", "gello xorld"):
    print("{}: {}".format(item, myhash(item)))
```

✅ Output:

```
hello world: 6736
world hello: 6616
gello xorld: 6742
```

---

### ⚠️ Still Not Perfect

Trying with `"ad"` and `"ga"`:

```python
for item in ("ad", "ga"):
    print("{}: {}".format(item, myhash(item)))
```

✅ Output:

```
ad: 297
ga: 297
```

⚡ Even here we see **collisions still exist** → which means we must use **collision resolution techniques** in practice.

---

