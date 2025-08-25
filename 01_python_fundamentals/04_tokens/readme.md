# Tokens in Python 🔠🔍

## Table of Contents 📋

- [Tokens in Python 🔠🔍](#tokens-in-python-)
  - [Table of Contents 📋](#table-of-contents-)
  - [What Are Tokens? 🧩](#what-are-tokens-)
    - [Types of Tokens 🏷️](#types-of-tokens-️)
  - [The Role of Whitespace 🧩](#the-role-of-whitespace-)
    - [Example:](#example)

---

In this section, we'll delve into how Python processes each line of code by breaking it down into basic components known as **tokens**. Understanding tokens is essential for grasping how Python interprets your code.

## What Are Tokens? 🧩

- Python breaks each **logical line** into a sequence of elementary lexical components called **tokens**.
- Each token corresponds to a specific substring of the logical line.

### Types of Tokens 🏷️

The main types of tokens in Python include:

1. **Identifiers**: Names used for variables, functions, classes, etc.
2. **Keywords**: Reserved words that have special meanings in Python (e.g., `if`, `else`, `while`).
3. **Operators**: Symbols that perform operations on variables and values (e.g., `+`, `-`, `*`, `/`).
4. **Delimiters**: Characters used to separate tokens (e.g., `()`, `[]`, `{}`, `,`).
5. **Literals**: Fixed values like numbers, strings, and booleans.

## The Role of Whitespace 🧩

- **Whitespace** (spaces, tabs, and newlines) can be freely used between tokens to separate them.
- Some whitespace is **necessary** to separate logically adjacent identifiers or keywords.

### Example:
```python
# Incorrect: Python would parse 'ifx' as a single identifier
ifx = 10

# Correct: Adding whitespace to separate 'if' and 'x'
if x == 10:
    print("x is 10")
```

- In the above example, without the space between `if` and `x`, Python would mistakenly interpret `ifx` as a single identifier rather than the keyword `if` followed by the identifier `x`.

---

This section covered the basic building blocks of Python code—**tokens**. Understanding how Python breaks down lines into tokens is crucial for writing clear and error-free code. 💡
