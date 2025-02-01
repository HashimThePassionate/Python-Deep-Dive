# 🔍 **Understanding `__str__()` in Python** 🚀

In Python, the `__str__()` method is a **special method** that defines how an object is **converted into a string** when using `print(obj)` or `str(obj)`. It helps in providing a **human-readable representation** of the object.

Now, let’s **break down** the given `__str__()` method **step by step** to understand its functionality in detail! 📘✨

---

## 🟢 **1. The Function Signature**
```python
def __str__(self) -> str:
```
- This is a **special (magic) method** in Python.
- It **returns a string representation** of the object.
- The `-> str` in the function signature is a **type hint** that indicates this method should return a **string**.

---

## 🟡 **2. Creating a Summary List**
```python
summary = [f"- {self.name} (ID: {id(self)})\n"]
```
- **Creates a list** called `summary`, which will store formatted details of the object.
- The first entry in this list is:
  - `self.name`: The object's `name` attribute.
  - `id(self)`: The **memory address (unique ID)** of the object.
- `f"- {self.name} (ID: {id(self)})\n"` formats the string to show the object's name and ID.

### 🔹 **Example Output for an Object `obj` with `name="Website"`**
```
- Website (ID: 140562799879232)
```
This acts as a **header** for the object’s string representation.

---

## 🔵 **3. Getting Object Attributes**
```python
infos = vars(self).items()
```
- `vars(self)` **returns a dictionary** of all attributes of the object.
- `.items()` converts it into a **list of key-value pairs**.

### 🔹 **Example `vars(self)` Output for an Object**
```python
{
    "name": "Website",
    "domain": "google.com",
    "description": "Search Engine",
    "year": 1998
}
```
So, `infos.items()` would return:
```python
[("name", "Website"), ("domain", "google.com"), ("description", "Search Engine"), ("year", 1998)]
```

---

## 🟣 **4. Sorting the Attributes**
```python
ordered_infos = sorted(infos)
```
- **Sorts** the attributes alphabetically by their names (`key`).
- Sorting ensures that when we print the attributes, they appear in **a consistent order**.

### 🔹 **Sorted Example Output**
```python
[("description", "Search Engine"), ("domain", "google.com"), ("name", "Website"), ("year", 1998)]
```
Now, the attributes appear in **alphabetical order**.

---

## 🔴 **5. Looping Through Attributes**
```python
for attr, val in ordered_infos:
    if attr == "name":
        continue  # Skip 'name' since it was already used in the header
    summary.append(f"{attr}: {val}\n")
```
- **Loops through each attribute** (`attr`) and its value (`val`).
- If the attribute is `"name"`, it is **skipped** because we already used it in the header.
- **Each attribute-value pair is added to `summary`** in the format:
  ```
  attribute: value
  ```

### 🔹 **Example Iteration**
For an object with:
```python
{
    "name": "Website",
    "domain": "google.com",
    "description": "Search Engine",
    "year": 1998
}
```
After **skipping `"name"`**, it adds:
```
description: Search Engine
domain: google.com
year: 1998
```

---

## 🟢 **6. Returning the Final String**
```python
return "".join(summary)
```
- Joins all elements in the `summary` list into a **single formatted string**.
- Ensures **proper newlines** (`\n`) for readability.

---

## 🎯 **Final Example: Putting Everything Together**
### **Python Code**
```python
class Website:
    def __init__(self, name: str, domain: str, description: str, **kwargs):
        self.name = name
        self.domain = domain
        self.description = description
        
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self) -> str:
        summary = [f"- {self.name} (ID: {id(self)})\n"]
        infos = vars(self).items()
        ordered_infos = sorted(infos)
        
        for attr, val in ordered_infos:
            if attr == "name":
                continue
            summary.append(f"{attr}: {val}\n")
        
        return "".join(summary)

# Creating an object
site = Website(name="Google", domain="google.com", description="Search Engine", year=1998, founder="Larry Page")

# Printing the object
print(site)
```

---

## **📝 Expected Output**
```
- Google (ID: 140562799879232)
description: Search Engine
domain: google.com
founder: Larry Page
year: 1998
```
