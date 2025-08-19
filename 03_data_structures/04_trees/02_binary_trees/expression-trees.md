# 📘 **Expression Trees: Postfix , **Prefix**, and **Infix****

## 📋 Table of Contents
- [📘 **Expression Trees: Postfix , **Prefix**, and **Infix****](#-expression-trees-postfix--prefix-and-infix)
  - [📋 Table of Contents](#-table-of-contents)
  - [🧱 Common Building Blocks](#-common-building-blocks)
    - [Evaluate an Expression Tree (recursive)](#evaluate-an-expression-tree-recursive)
    - [Traversals (useful to verify)](#traversals-useful-to-verify)
  - [✅ Part A — Build from **Postfix** (Recap)](#-part-a--build-from-postfix-recap)
  - [🥇 Part B — Build from **Prefix**](#-part-b--build-from-prefix)
  - [🧭 Part C — Build from **Infix**](#-part-c--build-from-infix)
  - [🧪 Quick End‑to‑End Demo (all three)](#-quick-endtoend-demo-all-three)
  - [📌 Notes \& Extensions](#-notes--extensions)

---Trees: Postfix ✅, **Prefix**, and **Infix** — Full Implementations & Explanations

This README expands your postfix (Reverse Polish) solution to also handle **prefix** and **infix** forms.
You’ll get:

* Clear algorithms (how they work and *why*),
* Python implementations for each form,
* A shared `TreeNode` + evaluation,
* Traversals to print expressions back as **prefix/infix/postfix**,
* Worked example on:

  * Postfix: `4 5 + 5 3 - *`
  * Prefix: `* + 4 5 - 5 3`
  * Infix: `(4 + 5) * (5 - 3)`

---

## 🧱 Common Building Blocks

```python
class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

def is_op(x: str) -> bool:
    return x in "+-*/"

def precedence(op: str) -> int:
    # higher number => higher precedence
    return {"+": 1, "-": 1, "*": 2, "/": 2}.get(op, 0)

def is_left_assoc(op: str) -> bool:
    # All four are left-associative here
    return True
```

### Evaluate an Expression Tree (recursive)

```python
def calc(node: TreeNode):
    if node is None:
        return 0
    if not is_op(str(node.data)):
        return node.data
    a = calc(node.left)
    b = calc(node.right)
    if node.data == "+": return a + b
    if node.data == "-": return a - b
    if node.data == "*": return a * b
    if node.data == "/": return a / b
```

### Traversals (useful to verify)

```python
def to_postfix(node: TreeNode) -> str:
    if not node: return ""
    if not is_op(str(node.data)): return str(node.data)
    return f"{to_postfix(node.left)} {to_postfix(node.right)} {node.data}".strip()

def to_prefix(node: TreeNode) -> str:
    if not node: return ""
    if not is_op(str(node.data)): return str(node.data)
    return f"{node.data} {to_prefix(node.left)} {to_prefix(node.right)}".strip()

def to_infix(node: TreeNode) -> str:
    if not node: return ""
    if not is_op(str(node.data)): return str(node.data)
    # Parenthesize to preserve structure
    return f"({to_infix(node.left)} {node.data} {to_infix(node.right)})"
```

---

## ✅ Part A — Build from **Postfix** (Recap)

**Algorithm (left → right):**

1. If token is **operand** → push node.
2. If token is **operator** → pop **right**, pop **left**, make subtree, push subtree.
3. End → single node on stack is the root.

```python
def build_from_postfix(postfix: str) -> TreeNode:
    stack = []
    for tok in postfix.split():
        if is_op(tok):
            right = stack.pop()
            left  = stack.pop()
            node = TreeNode(tok)
            node.left, node.right = left, right
            stack.append(node)
        else:
            stack.append(TreeNode(int(tok)))
    return stack.pop()
```

**Test (postfix):**
`"4 5 + 5 3 - *"` → tree prints

* Prefix: `* + 4 5 - 5 3`
* Infix: `((4 + 5) * (5 - 3))`
* Value: `18`

---

## 🥇 Part B — Build from **Prefix**

**Key idea:** Scan **right → left**.

* If token is **operand** → push node.
* If token is **operator** → pop two nodes; **first pop = left**, **second pop = right** (because we are reading from right to left); make subtree; push subtree.

Why this order?

* In prefix, an operator immediately precedes its two operands. Scanning from the end ensures that when we see an operator, its two children are already on the stack in **right-to-left** order—so the **first** popped is the **left** child.

```python
def build_from_prefix(prefix: str) -> TreeNode:
    stack = []
    tokens = prefix.split()[::-1]  # scan right → left
    for tok in tokens:
        if is_op(tok):
            left  = stack.pop()   # first pop = left
            right = stack.pop()   # second pop = right
            node = TreeNode(tok)
            node.left, node.right = left, right
            stack.append(node)
        else:
            stack.append(TreeNode(int(tok)))
    return stack.pop()
```

**Test (prefix):**
`"* + 4 5 - 5 3"` → tree prints

* Postfix: `4 5 + 5 3 - *`
* Infix: `((4 + 5) * (5 - 3))`
* Value: `18`

---

## 🧭 Part C — Build from **Infix**

We’ll use the classic **two-stack** algorithm (Dijkstra-style), which directly builds the tree **without** converting to postfix first.

**Stacks:**

* `nodes`: stack of `TreeNode` (operands/subtrees)
* `ops`: stack of operator tokens and parentheses

**Algorithm (left → right):**

1. If token is **whitespace** → skip.
2. If **number** → parse full number, push a node to `nodes`.
3. If token is `'('` → push to `ops`.
4. If token is `')'` → **reduce** until `'('` is at top of `ops`.

   * For each reduction: pop operator `op`, pop `right`, pop `left`, make node, push to `nodes`. Finally pop `'('`.
5. If token is **operator** `o1` →

   * While top of `ops` is an operator `o2` **and**

     * `precedence(o2) > precedence(o1)` **or**
     * `precedence(o2) == precedence(o1)` **and** `o1` is **left-associative**,
       reduce once (same reduction step as above).
   * Push `o1` to `ops`.
6. After all tokens, **reduce** remaining operators.

This respects **precedence** (`*`/`/` before `+`/`-`) and **associativity** (left for all here).

```python
def build_from_infix(infix: str) -> TreeNode:
    nodes, ops = [], []

    i, n = 0, len(infix)
    def reduce_once():
        op = ops.pop()
        right = nodes.pop()
        left  = nodes.pop()
        node = TreeNode(op)
        node.left, node.right = left, right
        nodes.append(node)

    while i < n:
        ch = infix[i]

        # Skip spaces
        if ch.isspace():
            i += 1
            continue

        # Number (supports multi-digit)
        if ch.isdigit():
            j = i
            while j < n and (infix[j].isdigit()):
                j += 1
            nodes.append(TreeNode(int(infix[i:j])))
            i = j
            continue

        # Parentheses
        if ch == '(':
            ops.append(ch)
            i += 1
            continue

        if ch == ')':
            while ops and ops[-1] != '(':
                reduce_once()
            ops.pop()  # pop '('
            i += 1
            continue

        # Operator
        if is_op(ch):
            while (ops and is_op(ops[-1]) and
                   (precedence(ops[-1]) > precedence(ch) or
                    (precedence(ops[-1]) == precedence(ch) and is_left_assoc(ch)))):
                reduce_once()
            ops.append(ch)
            i += 1
            continue

        raise ValueError(f"Unexpected token: {ch!r}")

    # Final reductions
    while ops:
        reduce_once()

    return nodes.pop()
```

**Test (infix):**
`"(4 + 5) * (5 - 3)"` → tree prints

* Prefix: `* + 4 5 - 5 3`
* Postfix: `4 5 + 5 3 - *`
* Value: `18`

---

## 🧪 Quick End‑to‑End Demo (all three)

```python
# Postfix
root_post = build_from_postfix("4 5 + 5 3 - *")
print(to_prefix(root_post))  # * + 4 5 - 5 3
print(to_infix(root_post))   # ((4 + 5) * (5 - 3))
print(calc(root_post))       # 18

# Prefix
root_pre = build_from_prefix("* + 4 5 - 5 3")
print(to_postfix(root_pre))  # 4 5 + 5 3 - *
print(to_infix(root_pre))    # ((4 + 5) * (5 - 3))
print(calc(root_pre))        # 18

# Infix
root_in = build_from_infix("(4 + 5) * (5 - 3)")
print(to_prefix(root_in))    # * + 4 5 - 5 3
print(to_postfix(root_in))   # 4 5 + 5 3 - *
print(calc(root_in))         # 18
```

---

## 📌 Notes & Extensions

* To support **floats**, parse numbers with a decimal point and store `float(...)` in nodes.
* Add **unary minus** by distinguishing it from binary `-` (e.g., when it appears at start or after `(` or another operator).
* For pretty infix without full parentheses, you can omit parentheses where child precedence is higher than parent—here we used full parentheses for clarity and correctness.

