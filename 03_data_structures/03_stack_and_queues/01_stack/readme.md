#  **Stacks** 🥞

## 📚 Introduction

A **stack** is a data structure that stores data, just like a stack of plates in a kitchen.
You can put a plate **on the top** of the stack, and when you need a plate, you always **take it from the top**.

## 🖼️ Figure 5.1: Example of a Stack

<div align="center">
  <img src="./images/01.jpg" alt="" width="400px"/>
</div>

<div align="center">

  **Figure 5.1: Example of a stack**

</div>

**Explanation:**

* Imagine a stack of plates 🍽️.
* You always add a new plate on the top.
* When you need a plate, you pick the one from the top.
* **The last plate added will always be the first to be removed.**

## 🔍 How Stack Works

* The above diagram shows a stack of plates.
* **Adding a plate:** You can only add a plate by placing it **on top** of the pile.
* **Removing a plate:** You can only remove the plate that's **on top**.

## 🚦 Stack Constraints

A **stack** stores data in a specific order (like arrays and linked lists), **but** with special rules:

* **Push:** Data can **only be inserted at the end (top)**.
* **Pop:** Data can **only be deleted from the end (top)**.
* **Peek:** You can **only read the last (top) data element**.

So, stacks are **Last In, First Out (LIFO)** structures.
That means **the last item added is always the first to be removed**.

## 🛠️ Stack Operations

There are **two main operations** on stacks:

1. **Push:** Add an element to the top of the stack.
2. **Pop:** Remove (and return) the top element of the stack.
3. **Peek:** See (but not remove) the top element.

All these operations use a pointer called **`top`**.

## 🖼️ Figure 5.2: Demonstration of Push and Pop Operations

<div align="center">
  <img src="./images/02.jpg" alt="" width="300px"/>
</div>

<div align="center">

*Figure 5.2: Demonstration of push and pop operations in a stack*

</div>


**Explanation of Figure 5.2:**

* **Push in data elements:** Adds new elements to the top.
* **Pop out data elements:** Removes elements from the top.
* **Peek:** Allows you to see the current top element without removing it.
* The stack grows and shrinks only at the **top**.

## 📝 Table 5.1: Stack Operations Example

| Stack Operation | Size | Contents         | Operation Results                                                                                  |
| --------------- | ---- | ---------------- | -------------------------------------------------------------------------------------------------- |
| `stack()`       | 0    | `[]`             | Stack object created, which is empty.                                                              |
| `push "egg"`    | 1    | `['egg']`        | One item "egg" is added to the stack.                                                              |
| `push "ham"`    | 2    | `['egg', 'ham']` | One more item, "ham", is added to the stack.                                                       |
| `peek()`        | 2    | `['egg', 'ham']` | The top element, "ham", is returned.                                                               |
| `pop()`         | 1    | `['egg']`        | The "ham" item is popped off and returned. (This item was added last, so it is removed first.)     |
| `pop()`         | 0    | `[]`             | The "egg" item is popped off and returned. (This is the first item added, so it is returned last.) |

---

## 🎯 Where Are Stacks Used?

Stacks are used in many places.
One of the most common uses is to **keep track of the return address during function calls**.

## 🧑‍💻 Function Call Example

Let's look at this simple program:

```python
def b():
    print('b')
def a():
    b()
a()
print("done")
```

### 👣 What Happens When We Run This?

When the program executes `a()`, a specific sequence of events happens.
Let’s visualize these steps!

## 🖼️ Figure 5.3: Steps for a Sequence of Events During Function Calls

<div align="center">
  <img src="./images/03.jpg" alt="" width="600px"/>
</div>

<div align="center">

*Figure 5.3: Steps for a sequence of events during function calls in our sample program*

</div>


### Step-by-Step Explanation:

1. **Push Current Instruction Address:**

   * The address of the current instruction is **pushed onto the stack**.
   * Execution jumps to the definition of `a()`.

2. **Call Function b():**

   * Inside function `a()`, function `b()` is called.

3. **Push Return Address of b():**

   * The return address of `b()` is **pushed onto the stack**.
   * Once everything in `b()` is done, the return address is **popped off the stack**, taking us back to `a()`.

4. **Complete Function a():**

   * After all instructions in `a()` are complete, the return address is **popped off the stack** again, bringing us back to the main program.

### 🖨️ Program Output

```
b
done
```

#  **Stack Implementation Using Arrays** 📦

A **stack** stores data in sequential order (like arrays and linked lists) with a key rule:
**Data can only be added or removed from one end** of the stack, always following the **Last In, First Out (LIFO)** principle.

### 📋 Two Main Stack Implementations:

* **Arrays:** Fixed length stack
* **Linked Lists:** Stack of variable length

**Array-based stacks** need careful checks:

* If you try to add to a full stack ➡️ **Overflow error**
* If you try to remove from an empty stack ➡️ **Underflow error**

## 🖼️ Figure 5.4: Push Operations in an Array-Based Stack

<div align="center">
  <img src="./images/04.jpg" alt="" width="600px"/>
</div>

<div align="center">

*Figure 5.4: Sequence of push operations in a stack implementation using an array*

</div>


### Step-by-Step Push Operation:

1. **Initial Stack:**

   * All positions are empty.
   * `top = -1` (Stack is empty)

2. **Push "egg":**

   * `top` is incremented to `0`
   * `"egg"` is placed at position 0

3. **Push "ham":**

   * `top` is incremented to `1`
   * `"ham"` is placed at position 1

4. **Push "spam":**

   * `top` is incremented to `2`
   * `"spam"` is placed at position 2

5. **Push (Stack Overflow):**

   * Attempt to push another element.
   * **Error:** Stack is full, cannot add more elements!
   * **Stack Overflow** occurs.

## 🐍 Python Code for Stack Push Operation

```python
size = 3
data = [0] * size   # Initialize the stack

top = -1
def push(x):
    global top
    if top >= size - 1:
        print("Stack Overflow")
    else:
        top = top + 1
        data[top] = x
```

* **Initialize:** `top = -1` means the stack is empty.
* **Check overflow:** If `top` is at the last index, cannot add new elements.
* **Push:** Increment `top` and add new value.

### 🧑‍💻 Example Usage

```python
push('egg')
push('ham')
push('spam')
print(data[0:top+1])   # Output: ['egg', 'ham', 'spam']
push('new')            # Stack Overflow
push('new2')           # Stack Overflow
```

**Output:**

```
['egg', 'ham', 'spam']
Stack Overflow
Stack Overflow
```

## 🖼️ Figure 5.5: Pop Operations in an Array-Based Stack

<div align="center">
  <img src="./images/05.jpg" alt="" width="600px"/>
</div>

<div align="center">

*Figure 5.5: Sequence of the pop operation in a stack implementation using an array*

</div>

### Step-by-Step Pop Operation:

1. **Initial Stack:**

   * Stack contains `["egg", "ham", "spam"]`
   * `top = 2`

2. **Pop "spam":**

   * Remove `"spam"` from position 2
   * `top` is decremented to `1`

3. **Pop "ham":**

   * Remove `"ham"` from position 1
   * `top` is decremented to `0`

4. **Pop "egg":**

   * Remove `"egg"` from position 0
   * `top` is decremented to `-1`
   * Stack is now empty

5. **Pop (Stack Underflow):**

   * Attempt to pop from empty stack
   * **Error:** Stack is empty, cannot remove elements!
   * **Stack Underflow** occurs

---

## 🐍 Python Code for Stack Pop Operation

```python
def pop():
    global top
    if top == -1:
        print("Stack Underflow")
        return None
    else:
        value = data[top]
        data[top] = None
        top -= 1
        return value
```

* **Check underflow:** If `top == -1`, stack is empty.
* **Pop:** Return the value at `top` and decrement `top`.

### 🧑‍💻 Example Usage

```python
print(pop())          # 'spam'
print(data[0:top+1])  # ['egg', 'ham']

print(pop())          # 'ham'
print(data[0:top+1])  # ['egg']

print(pop())          # 'egg'
print(data[0:top+1])  # []

print(pop())          # Stack Underflow
print(data[0:top+1])  # []
```

**Output:**

```
spam
['egg', 'ham']
ham
['egg']
egg
[]
Stack Underflow
[]
```

## 👀 Python Code for Stack Peek Operation

```python
def peek():
    global top
    if top == -1:
        print("Stack is empty")
    else:
        print(data[top])
```

* **Check if empty:** If `top == -1`, stack is empty.
* **Peek:** Print the value at the `top` position.


#  **Stack Implementation Using Linked Lists** 🔗

## 📚 Introduction

A **stack** can also be implemented using a **linked list**.
This approach is flexible and can grow or shrink as needed (unlike fixed-size array stacks).

## 🖼️ Figure 5.6: Stack Representation Using a Linked List

<div align="center">
  <img src="./images/06.jpg" alt="" width="600px"/>
</div>

<div align="center">

*Figure 5.6: Representation of the stack using a linked list*

</div>


### Figure Explanation:

* Each **node** contains two parts:

  1. **Data:** The value stored in the node
  2. **Next:** A reference to the next node
* The **top** points to the first node (the top of the stack)
* **Push:** Insert a new node at the top
* **Pop:** Remove the node from the top
* The stack ends when the `next` pointer of a node is `None`

## 🏗️ Node Class Implementation

To build a stack using a linked list, first define a **Node** class:

```python
class Node:
    def __init__(self, data=None):
        self.data = data      # Holds the value
        self.next = None      # Reference to the next node
```

* Each node holds data and a reference to the next node.

## 🏢 Stack Class Implementation

Next, define a **Stack** class.
This is similar to a singly linked list but with stack-specific constraints:

```python
class Stack:
    def __init__(self):
        self.top = None      # Pointer to the top node
        self.size = 0        # Number of elements in the stack
```

* **`top`:** Points to the node at the top of the stack (where push and pop happen)
* **`size`:** Tracks the current number of elements

## 💡 Key Points for Stack Using Linked List

1. **Track the Top Node:**
   To push or pop, always use the node pointed to by `top`.

2. **Maintain Stack Size:**
   Keep a variable (`size`) to quickly know how many elements are in the stack.

3. **Dynamic Size:**
   Unlike array-based stacks, linked list stacks can grow or shrink without a fixed limit.

