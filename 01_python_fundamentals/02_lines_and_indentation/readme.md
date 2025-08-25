# Lines and Indentation in Python 🐍

In this section, we will explore how Python handles lines and indentation. Python's approach to indentation is unique and critical to understand as it directly impacts the structure and readability of your code.

## Table of Contents 📚

- [Lines and Indentation in Python 🐍](#lines-and-indentation-in-python-)
  - [Table of Contents 📚](#table-of-contents-)
  - [Logical and Physical Lines 📏](#logical-and-physical-lines-)
    - [Example:](#example)
    - [Blank Lines ✏️](#blank-lines-️)
    - [Statement Termination 🚧](#statement-termination-)
    - [Example:](#example-1)
  - [Triple-Quoted Strings 📜](#triple-quoted-strings-)
    - [Example:](#example-2)
  - [Continuation Lines ➡️](#continuation-lines-️)
  - [Indentation and Block Structure 📚](#indentation-and-block-structure-)
    - [Example:](#example-3)
    - [Important Rules 📝](#important-rules-)
  - [Indentation Best Practices 🌟](#indentation-best-practices-)
    - [Pro Tip 💡](#pro-tip-)
    - [Example:](#example-4)

## Logical and Physical Lines 📏

- A **Python program** consists of **logical lines**, each made up of one or more **physical lines**.
- A **physical line** is what you see as a single line in your code editor, which may end with a **comment**. 
  - **Comments** in Python start with a hash sign `#` and continue to the end of the line.
  - Python ignores everything after the `#`, making comments useful for adding explanations or notes to your code.
  
### Example:
```python
x = 10  # This is a comment
y = 20  # Python will ignore everything after the hash sign
```

### Blank Lines ✏️

- A **blank line** in Python is a line that contains only whitespace or a comment.
- Python completely ignores blank lines, which makes them useful for improving code readability by separating logical sections.

### Statement Termination 🚧

- In Python, most statements end at the end of a physical line. 
- Unlike other programming languages, Python does not require a semicolon `;` to terminate statements.
- If a statement is too long for one physical line, you can:
  - Use a backslash `\` to join two physical lines into a single logical line.
  - Or, Python can automatically join lines if an open parenthesis `(`, bracket `[`, or brace `{` has not been closed.

### Example:
```python
# Using a backslash to continue the statement
total = 1 + 2 + 3 + \
        4 + 5 + 6

# Using parentheses to continue the statement
total = (1 + 2 + 3 +
         4 + 5 + 6)
```

## Triple-Quoted Strings 📜

- **Triple-quoted string literals** allow you to span physical lines without using backslashes.
  
### Example:
```python
text = """This is a long string
that spans multiple lines."""
```

## Continuation Lines ➡️

- Physical lines that follow the first one in a logical line are known as **continuation lines**. 
- **Indentation** rules apply only to the first physical line of each logical line.

## Indentation and Block Structure 📚

- Python uses **indentation** to define the block structure of code. 
- Unlike other languages that use braces `{}`, Python relies solely on indentation.
- **Blocks** are sequences of logical lines with the same indentation level.
- A block ends when a logical line has less indentation.

### Example:
```python
if x > 0:
    print("Positive number")
    y = x
else:
    print("Non-positive number")
    y = 0
```

### Important Rules 📝

- The first statement in a Python source file must not be indented.
- Statements typed at the interactive prompt `>>>` must also have no indentation.

## Indentation Best Practices 🌟

- **Standard Python style** recommends using **four spaces** per indentation level.
- Never mix spaces and tabs, as different tools handle them differently.
  - Use the `-t` and `-tt` options in Python to ensure consistent tab and space usage.
- **Python v3** enforces no mixing of tabs and spaces for indentation.

### Pro Tip 💡

- Configure your code editor to replace tabs with four spaces. This ensures consistent indentation across all tools and Python itself.
  
### Example:
```python
def greet(name):
    print(f"Hello, {name}!")  # Correct: 4 spaces for indentation

```

