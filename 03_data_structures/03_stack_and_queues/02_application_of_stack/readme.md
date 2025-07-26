#  **Applications of Stacks** 

## 📚 Why Are Stacks Important?

Even though **arrays** and **linked lists** can do what stacks do,
**stacks** (and queues) are crucial because they provide special ways to add or delete elements in a specific order.

* **Benefit:**
  Stacks prevent bugs by restricting access/deletion to only the top element,
  avoiding accidental changes from the middle of the list.

## 🧩 Example: Bracket-Matching Using a Stack

One common and practical application of stacks is **bracket-matching**:

* **Goal:** Check if every opening bracket has a matching closing bracket in an expression.
* **Types:** `()`, `[]`, `{}`

### 💡 Why Use a Stack?

* **Reverse order processing:** Since stacks are LIFO, they help keep track of the most recent opening bracket and match it with closing brackets in order.



## 🐍 Python Code: Bracket-Matching Function

> The following code is for a separate check_brackets method defined outside the Stack class.This method will use the Stack class that we discussed in the previous section

```python
def check_brackets(expression):
    brackets_stack = Stack()  # The Stack class from earlier
    last = ' '
    for ch in expression:
        if ch in ('{', '[', '('):
            brackets_stack.push(ch)
        if ch in ('}', ']', ')'):
            last = brackets_stack.pop()
            if last == '{' and ch == '}':
                continue
            elif last == '[' and ch == ']':
                continue
            elif last == '(' and ch == ')':
                continue
            else:
                return False
    if brackets_stack.size > 0:
        return False
    else:
        return True
```

### 📝 How This Function Works:

1. **Traverse each character:**

   * If it’s an **opening bracket** (`{`, `[`, `(`), push onto the stack.
   * If it’s a **closing bracket** (`}`, `]`, `)`), pop from the stack and check if the brackets match.
2. **Mismatch:**
   If a closing bracket doesn’t match the most recent opening bracket, return `False`.
3. **End of Expression:**
   * If the stack is **empty**, all brackets matched → `True`
   * If the stack still has items, some opening brackets were not closed → `False`

## 🧑‍💻 Example: Testing the Bracket-Matcher

```python
sl = (
    "{(foo)(bar)}[hello](((this)is)a)test",
    "{(foo)(bar)}[hello](((this)is)atest",
    "{(foo)(bar)}[hello](((this)is)a)test))"
)
for s in sl:
    m = check_brackets(s)
    print("{}: {}".format(s, m))
```

### 🖨️ Output

```
{(foo)(bar)}[hello](((this)is)a)test: True
{(foo)(bar)}[hello](((this)is)atest: False
{(foo)(bar)}[hello](((this)is)a)test)): False
```

* ✅ The **first expression** is balanced: returns **True**
* ❌ The **other two** are unbalanced: return **False**

## ⏱️ Stack Operations Are Fast!

* `push`, `pop`, and `peek` operations all run in **O(1) time** (constant time)
  because they always work at the **top** of the stack.

## 🌎 Real-World Uses of Stacks

* 🔙 **Back and Forward buttons** in web browsers
  (navigation history)
* ↩️ **Undo and Redo** in word processors and text editors
  (restore previous states)
* 🧮 **Bracket matching** in compilers, interpreters, and text editors

