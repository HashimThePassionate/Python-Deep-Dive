
# **🚀 The Prototype Pattern**  

## **📚 Table of Contents**  

- [**🚀 The Prototype Pattern**](#-the-prototype-pattern)
  - [**📚 Table of Contents**](#-table-of-contents)
  - [**📌 Introduction**](#-introduction)
  - [**🎯 Real-World Analogy**](#-real-world-analogy)
  - [**📌 When to Use the Prototype Pattern?**](#-when-to-use-the-prototype-pattern)
  - [**🔧 Implementing the Prototype Pattern in Python**](#-implementing-the-prototype-pattern-in-python)
    - [**🚀 Step 1: Import Required Modules**](#-step-1-import-required-modules)
    - [**📝 Code Explanation:**](#-code-explanation)
    - [**🏗️ Step 2: Creating the `Website` Class**](#️-step-2-creating-the-website-class)
      - [**📝 Code Implementation:** ➡️ Learn Set Attr Method and kwargs](#-code-implementation-️-learn-set-attr-method-and-kwargs)
    - [**📌 Code Breakdown:**](#-code-breakdown)
    - [**📄 Step 3: Adding a `__str__()` Method**](#-step-3-adding-a-__str__-method)
      - [**📝 Code Implementation:**  ➡️ Learn str method implementation](#-code-implementation--️-learn-str-method-implementation)
    - [**📌 Code Breakdown:**](#-code-breakdown-1)
  - [**🔁 Step 4: Implementing the `Prototype` Class**](#-step-4-implementing-the-prototype-class)
      - [**📝 Code Implementation:**  ➡️ Learn Prototype Class](#-code-implementation--️-learn-prototype-class)
  - [**🎯 Step 5: Using the Prototype Pattern in `main()`**](#-step-5-using-the-prototype-pattern-in-main)
      - [**📝 Code Implementation:**  ➡️ Learn main() implementation](#-code-implementation--️-learn-main-implementation)
  - [**🎬 Step 6: Running the Program**](#-step-6-running-the-program)
  - [**📌 Summary**](#-summary)

---

## **📌 Introduction**  
The **Prototype Pattern** is a **creational design pattern** that allows us to create new objects **by cloning existing ones** rather than building them from scratch. This is particularly useful when:  

- **Object initialization is expensive or complex** 🏗️  
- **We need multiple copies of an object with slight modifications** 🔁  
- **We want to avoid the overhead of re-initialization** 💡  

Instead of constructing an object from scratch every time, we **duplicate an existing one**, reducing processing time and complexity.  

---

## **🎯 Real-World Analogy**  
Imagine you want to **grow a plant**. You have **two options**:  

🌱 **Option 1: Start from a Seed** (Slow, Time-Consuming 🌍)  
🌿 **Option 2: Take a Cutting and Grow It** (Fast, Efficient 🚀)  

The **Prototype Pattern** follows the **second approach**: Instead of creating an object from **scratch**, we **clone** an existing one.  

Similarly, in **Python**, we use `copy.deepcopy()` to duplicate objects without modifying the original.  

---

## **📌 When to Use the Prototype Pattern?**  

✅ **When object creation is expensive** (e.g., database queries)  
✅ **When object initialization is complex** (e.g., requires many dependencies)  
✅ **When we need multiple similar objects**  
✅ **When we need to keep the original object unchanged**  

---

## **🔧 Implementing the Prototype Pattern in Python**  

### **🚀 Step 1: Import Required Modules**  
Python provides the **`copy` module**, which helps us perform deep copies of objects.  

```python
import copy
```

### **📝 Code Explanation:**  
- **`copy.deepcopy(obj)`** allows us to create **a full clone** of an object, ensuring that changes to the new copy do not affect the original.  

---

### **🏗️ Step 2: Creating the `Website` Class**  

The **`Website`** class will:  
- Store **website-related information**  
- Allow **dynamic attributes** using `kwargs`  
- Use **`setattr()`** for flexible object properties  

#### **📝 Code Implementation:** ➡️ [Learn Set Attr Method and kwargs](./setattr.md)

```python
class Website:
    def __init__(self, name: str, domain: str, description: str, **kwargs):
        self.name = name
        self.domain = domain
        self.description = description
        # Dynamically assign additional attributes
        for key in kwargs:
            setattr(self, key, kwargs[key])
```

### **📌 Code Breakdown:**  
1️⃣ **`__init__()` method** initializes attributes `name`, `domain`, and `description`.  
2️⃣ **`kwargs` (keyword arguments)** allow flexible additional attributes.  
3️⃣ **`setattr(self, key, kwargs[key])`** dynamically assigns any extra attributes to the object.  

📌 **Why use `kwargs`?**  
Instead of defining a fixed number of attributes, `kwargs` allows **flexibility**, so we can pass any number of optional attributes.  

---

### **📄 Step 3: Adding a `__str__()` Method**  

This method **formats object details** in a human-readable way.  

#### **📝 Code Implementation:**  ➡️ [Learn str method implementation](./str_method.md)

```python
def __str__(self) -> str:
    summary = [f"- {self.name} (ID: {id(self)})\n"]
    infos = vars(self).items()
    ordered_infos = sorted(infos)
    
    for attr, val in ordered_infos:
        if attr == "name":
            continue
        summary.append(f"{attr}: {val}\n")
    
    return "".join(summary)
```

### **📌 Code Breakdown:**  
✅ **`vars(self).items()`** retrieves all attributes dynamically.  
✅ **`sorted(infos)`** sorts attributes alphabetically for consistency.  
✅ **`id(self)`** prints the memory address to differentiate cloned objects.  

📌 **Why use `vars()`?**  
- `vars()` returns an object's attributes as a dictionary.  
- Helps **inspect** and **debug** attributes easily.  

---

## **🔁 Step 4: Implementing the `Prototype` Class**  

This class **manages object cloning and tracking**.  

#### **📝 Code Implementation:**  ➡️ [Learn Prototype Class](./prototype.md)

```python
class Prototype:
    def __init__(self):
        self.registry = {}  # Stores objects

    def register(self, identifier: int, obj: object):
        self.registry[identifier] = obj  # Register object

    def unregister(self, identifier: int):
        del self.registry[identifier]  # Remove object

    def clone(self, identifier: int, **attrs) -> object:
        found = self.registry.get(identifier)
        if not found:
            raise ValueError(f"Incorrect object identifier: {identifier}")

        obj = copy.deepcopy(found)  # Clone the object
        for key in attrs:
            setattr(obj, key, attrs[key])  # Modify attributes if provided
        
        return obj
```

---

## **🎯 Step 5: Using the Prototype Pattern in `main()`**  

Now, let's **test** the prototype pattern by cloning a `Website` object.  

#### **📝 Code Implementation:**  ➡️ [Learn main() implementation](./main.md)

```python
def main():
    keywords = ("python", "programming", "scripting", "data", "automation")

    site1 = Website(
        "Python",
        domain="python.org",
        description="Programming language and ecosystem",
        category="Open Source Software",
        keywords=keywords,
    )

    proto = Prototype()
    proto.register("python-001", site1)  # Register site1

    # Clone site1 and modify some attributes
    site2 = proto.clone(
        "python-001",
        name="Python Package Index",
        domain="pypi.org",
        description="Repository for published packages",
    )

    # Print both original and cloned sites
    for site in (site1, site2):
        print(site)
```

---

## **🎬 Step 6: Running the Program**  

Run the script using:  

```bash
python prototype.py
```

---

## **📌 Summary**  

✔ **Prototype Pattern** allows object duplication instead of creating from scratch.  
✔ **Efficient for costly or complex object creation.**  
✔ **Useful in scenarios where database queries are expensive.**  
✔ **Python’s `copy.deepcopy()` is used for deep cloning.**  