**1. Memory Allocation and Deallocation**

```
+--------------------+
|      Python       | (Manages Memory)
+--------------------+
          |
          v
+---------+---------+  +---------+---------+
| Stack   |         |  | Heap     |         |
+---------+---------+  +---------+---------+
| var1    | Ref1 (->) |  | Object1 | Data     |  (Unreferenced - Garbage Collected)
+---------+---------+  +---------+---------+
| var2    | Ref2 (->) |  | Object2 | Data     |
+---------+---------+  +---------+---------+
| ...     | ... (->) |  | ...     | ...     |
+---------+---------+  +---------+---------+
```

- Python manages a private heap for object allocation.
- When you create an object (Object1, Object2), memory is allocated on the heap.
- Variables (var1, var2) on the stack hold references (Ref1, Ref2) pointing to these objects.
- The `id()` function can be used to get the memory address of an object on the heap.
- Unreferenced objects (like Object1) are eventually garbage collected.

**2. Stack and Heap**

```
+--------------------+
|      Python       | (Manages Memory)
+--------------------+
          |
          v
+---------+---------+  +---------+---------+
| Stack   |         |  | Heap     |         |
+---------+---------+  +---------+---------+
| var1    | Ref1 (->) |  | Object1 | Data     |
+---------+---------+  +---------+---------+
| var2    | Ref2 (->) |  | Object2 | Data     |
+---------+---------+  +---------+---------+
| ...     | ... (->) |  | ...     | ...     |
+---------+---------+  +---------+---------+
| Local   |  Function |  |         |         |
| Variables| Call Frame|  |         |         |
+---------+---------+  +---------+---------+
```

- The stack stores variable references and function call information.
- The heap stores the actual objects.
- Variables act like labels pointing to objects on the heap, not the objects themselves.

**3. Referencing an Object**

```
+--------------------+
|      Python       | (Manages Memory)
+--------------------+
          |
          v
+---------+---------+  +---------+---------+
| Stack   |         |  | Heap     |         |
+---------+---------+  +---------+---------+
| var1    | Ref1 (->) |  | Object1 | Data     |
+---------+---------+  +---------+---------+
|         |         |  | Object2 | Data     |
+---------+---------+  +---------+---------+
| ...     | ... (->) |  | ...     | ...     |
+---------+---------+  +---------+---------+
```

- Creating an object allocates memory on the heap (Object1).
- A variable on the stack (var1) stores a reference (Ref1) pointing to the object.
- This reference acts like a pointer to the object's location in memory.

**4. Garbage Collection**

```
+--------------------+
|      Python       | (Manages Memory)
+--------------------+
          |
          v
+---------+---------+  +---------+---------+
| Stack   |         |  | Heap     |         |
+---------+---------+  +---------+---------+
| var2    | Ref2 (->) |  | Object2 | Data     |
+---------+---------+  +---------+---------+
| ...     | ... (->) |  | ...     | ...     |
+---------+---------+  +---------+---------+
```

- Python's garbage collector tracks object references.
- When a variable reference is removed (var1 is no longer assigned), the reference count drops to zero (Ref1 is gone).
- The garbage collector identifies unreferenced objects (Object1) for deallocation.
- The memory occupied by the unreferenced object is freed up. 
