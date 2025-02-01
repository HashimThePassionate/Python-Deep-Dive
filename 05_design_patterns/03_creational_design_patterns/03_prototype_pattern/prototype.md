# 🔥 **Understanding the `Prototype` Class in Python** 🚀

The `Prototype` pattern is a **creational design pattern** that allows objects to be **cloned (duplicated)** while optionally modifying some of their attributes. This is useful when **creating a new object from scratch is expensive**, and instead, we reuse an existing one.

Let’s **break down** the `Prototype` class step by step! 📘✨

---

## 📌 **1. The Purpose of This Class**
This class provides:
- **A registry (`self.registry`)** to store objects with unique identifiers.
- **Methods to register/unregister objects.**
- **A `clone()` method to create copies** of stored objects with optional modifications.

---

## 🟢 **2. Breaking Down the `__init__()` Constructor**
```python
class Prototype:
    def __init__(self):
        self.registry = {}  # Stores objects
```
### **🔹 What is happening?**
- A dictionary **`self.registry`** is created.
- This dictionary will **map unique identifiers (keys)** to objects (values).
- This allows easy lookup and retrieval of stored objects.

---

## 🟡 **3. Registering an Object (`register()`)**
```python
def register(self, identifier: int, obj: object):
    self.registry[identifier] = obj  # Register object
```
### **🔹 How It Works?**
- The method takes:
  - `identifier` → A **unique ID** (integer) for an object.
  - `obj` → The object to store in the registry.
- It **stores the object** in the `registry` dictionary.

### **🔹 Example Usage**
```python
proto = Prototype()
obj1 = {"name": "Alice", "age": 30}
proto.register(1, obj1)
print(proto.registry)  
# Output: {1: {'name': 'Alice', 'age': 30}}
```
Now, object `obj1` is **stored** in the `registry` with ID `1`.

---

## 🔵 **4. Unregistering an Object (`unregister()`)**
```python
def unregister(self, identifier: int):
    del self.registry[identifier]  # Remove object
```
### **🔹 How It Works?**
- **Deletes** the object with the given `identifier` from `registry`.

### **🔹 Example Usage**
```python
proto.unregister(1)
print(proto.registry)  # Output: {}
```
Now, object `1` has been **removed** from the registry.

---

## 🔴 **5. Cloning an Object (`clone()`)**
```python
def clone(self, identifier: int, **attrs) -> object:
    found = self.registry.get(identifier)
    if not found:
        raise ValueError(f"Incorrect object identifier: {identifier}")

    obj = copy.deepcopy(found)  # Clone the object
    for key in attrs:
        setattr(obj, key, attrs[key])  # Modify attributes if provided
    
    return obj
```
### **🔹 How It Works?**
1. **Retrieve the object** from `registry` using `identifier`.
2. If not found, it **raises an error**.
3. **Clone the object** using `copy.deepcopy()`, which creates a **new independent copy**.
4. **Modify attributes if any are provided** using `setattr()`.
5. **Return the new object**.

---

## 🟣 **6. Understanding `copy.deepcopy()`**
```python
obj = copy.deepcopy(found)  # Clone the object
```
- `copy.deepcopy()` creates a **new object with a completely new memory address**.
- This ensures that modifying the clone **does not affect the original object**.

### **🔹 Example**
```python
import copy

obj1 = {"name": "Alice", "age": 30}
obj2 = copy.deepcopy(obj1)

obj2["age"] = 40  # Change only the cloned object

print(obj1)  # {'name': 'Alice', 'age': 30}  (Original remains unchanged)
print(obj2)  # {'name': 'Alice', 'age': 40}  (Clone is modified)
```

---

## 🟠 **7. Using `setattr()` for Dynamic Modifications**
```python
for key in attrs:
    setattr(obj, key, attrs[key])  # Modify attributes if provided
```
- If any additional attributes are passed, they are **dynamically updated** in the cloned object.
- `setattr(obj, key, value)` sets **new attributes** to the clone.

### **🔹 Example Usage**
```python
proto.register(1, {"name": "Alice", "age": 30})

# Clone object and modify 'age'
clone_obj = proto.clone(1, age=35)

print(clone_obj)  # {'name': 'Alice', 'age': 35} (Cloned and modified)
```
- The original object **remains unchanged**.
- The cloned object **has updated attributes**.

---

## 🎯 **8. Full Working Example**
```python
import copy

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
        for key, value in attrs.items():
            setattr(obj, key, value)  # Modify attributes if provided
        
        return obj

# ✅ Creating prototype registry
proto = Prototype()

# ✅ Registering an object
proto.register(1, {"name": "Alice", "age": 30})

# ✅ Cloning the object and modifying attributes
clone_obj = proto.clone(1, age=35, location="New York")

print(clone_obj)  
# Output: {'name': 'Alice', 'age': 35, 'location': 'New York'}

# ✅ The original object remains unchanged
print(proto.registry[1])  
# Output: {'name': 'Alice', 'age': 30}
```