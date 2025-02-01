# 🔥 **Understanding the `main()` Function and Prototype Design Pattern in Python** 🚀

This `main()` function demonstrates how to use the **Prototype Design Pattern** to clone an object and modify its attributes dynamically. Let's break it down **step by step** with detailed explanations. 📘✨

---

## 🟢 **1. Function Definition: `main()`**
```python
def main():
```
- This is the **entry point** of the program.
- It **creates, registers, clones, and prints objects** using the `Prototype` pattern.

---

## 🟡 **2. Defining Keywords for the Website**
```python
keywords = ("python", "programming", "scripting", "data", "automation")
```
- This **tuple** contains keywords related to Python.
- It will be passed as an attribute to a `Website` object.

---

## 🔵 **3. Creating the First Website Object (`site1`)**
```python
site1 = Website(
    "Python",
    domain="python.org",
    description="Programming language and ecosystem",
    category="Open Source Software",
    keywords=keywords,
)
```
### **🔹 What Happens Here?**
- A `Website` object (`site1`) is created with the following attributes:
  - `name = "Python"`
  - `domain = "python.org"`
  - `description = "Programming language and ecosystem"`
  - `category = "Open Source Software"`
  - `keywords = ("python", "programming", "scripting", "data", "automation")`
- The `Website` constructor likely **stores these values** and **dynamically adds any extra attributes** (if `kwargs` is used inside `Website`).

---

## 🔴 **4. Creating a Prototype Registry**
```python
proto = Prototype()
proto.register("python-001", site1)  # Register site1
```
### **🔹 What Happens Here?**
1. A `Prototype` object (`proto`) is created.
2. `site1` is **registered** in the `proto.registry` with the **unique identifier** `"python-001"`.

### **🔹 Expected Registry After Registration**
```python
proto.registry = {
    "python-001": site1
}
```
Now, `site1` can be **cloned anytime** using its identifier.

---

## 🟣 **5. Cloning `site1` to Create `site2`**
```python
site2 = proto.clone(
    "python-001",
    name="Python Package Index",
    domain="pypi.org",
    description="Repository for published packages",
)
```
### **🔹 What Happens Here?**
1. The `clone()` method is called on `proto` with the identifier `"python-001"`.
2. `proto.clone()`:
   - **Finds `site1`** in `registry`.
   - **Creates a deep copy** of `site1` using `copy.deepcopy()`.
   - **Modifies the attributes**:
     - `name` → `"Python Package Index"`
     - `domain` → `"pypi.org"`
     - `description` → `"Repository for published packages"`
   - Returns the modified **clone** (`site2`).

### **🔹 How `site2` Differs from `site1`?**
| Attribute    | `site1` (Original)                        | `site2` (Clone) |
|-------------|--------------------------------|--------------------------------|
| `name`      | Python                        | Python Package Index |
| `domain`    | python.org                     | pypi.org |
| `description` | Programming language and ecosystem | Repository for published packages |
| `category`  | Open Source Software           | Open Source Software (unchanged) |
| `keywords`  | ("python", "programming", "scripting", "data", "automation") | ("python", "programming", "scripting", "data", "automation") |

- Only the **specified attributes** are changed.
- **All other attributes remain the same** as `site1`.

---

## 🟠 **6. Printing Both Objects**
```python
for site in (site1, site2):
    print(site)
```
### **🔹 What Happens Here?**
- Iterates through both **`site1` and `site2`**.
- Calls the `__str__()` method of each `Website` object, which **formats and prints** its attributes.

### **🔹 Example Expected Output**
```
- Python (ID: 140512799879232)
category: Open Source Software
description: Programming language and ecosystem
domain: python.org
keywords: ('python', 'programming', 'scripting', 'data', 'automation')

- Python Package Index (ID: 140512799879768)
category: Open Source Software
description: Repository for published packages
domain: pypi.org
keywords: ('python', 'programming', 'scripting', 'data', 'automation')
```
- **Each object is displayed separately.**
- `ID:` is different because `site2` is a **new cloned object**.

---

## 🎯 **Key Takeaways**
✅ **Prototype Pattern:** Efficiently clones objects and modifies them.  
✅ **Registry System:** Stores and retrieves objects using unique identifiers.  
✅ **Deep Copy (`copy.deepcopy`)** ensures independent clones.  
✅ **Flexible Modifications:** Attributes can be changed during cloning using `kwargs`.  
✅ **`__str__()`** provides **clear, formatted output** for each object.

This approach is **very useful** for:
- **Configurable applications**
- **Cloning templates or prototypes** dynamically
- **Reducing object creation overhead**
