# Type Hints in Functions

## Introduction

Type hints are a significant change in Python, introduced to aid in code quality without altering Python's dynamic nature. Here's a detailed look at their purpose, usage, and limitations.

### Key Points

- **Type hints remain optional.** They are not mandatory and will not become so, as emphasized by Python's key contributors.
- **Historical context:** Type hints are the biggest change since the unification of types and classes in Python 2.2 (2001).

## What are Type Hints?

Type hints, introduced in PEP 484, provide syntax for explicit type declarations in function arguments, return values, and variables. They enable static analysis tools to find bugs without running the code.

### Beneficiaries

- **Professional software engineers:** Especially those using IDEs and CI systems.
- **Static analysis:** Tools like Mypy help identify potential issues.

### Broader Python Community

- **Diverse user base:** Scientists, traders, journalists, artists, analysts, and students.
- **Learning curve:** For many, the cost of learning type hints may outweigh the benefits.
- **Dynamic typing:** Preferred for smaller codebases and teams, especially in data science and creative computing.

## Section Focus

This section focuses on type hints in function signatures. Future section will explore type hints in classes and other typing module features.

### Major Topics

1. **Gradual Typing with Mypy:**
   - A practical introduction to using Mypy for gradual typing in Python.

2. **Duck Typing vs. Nominal Typing:**
   - Duck typing: An object's suitability is determined by the presence of certain methods and properties, not by its inheritance from a specific class.
   - Nominal typing: Relies on explicit declarations and inheritance.

3. **Categories of Types in Annotations:**
   - An overview of the main types used in function annotations.

4. **Type Hinting Variadic Parameters:**
   - How to type hint functions that use `*args` and `**kwargs`.

5. **Limitations and Downsides:**
   - The constraints and potential drawbacks of using type hints and static typing in Python.

## Detailed Explanations and Examples

### Gradual Typing with Mypy

Gradual typing allows the introduction of type hints into a codebase incrementally. Mypy is a static type checker for Python that supports gradual typing.

**Example:**

```python
# A simple function without type hints
def greet(name):
    return f"Hello, {name}"

# Adding type hints
def greet(name: str) -> str:
    return f"Hello, {name}"

# Running Mypy
# mypy script.py
```

### Duck Typing vs. Nominal Typing

- **Duck Typing:** "If it looks like a duck and quacks like a duck, it must be a duck."
- **Nominal Typing:** Requires explicit type declarations.

**Example:**

```python
# Duck typing example
class Duck:
    def quack(self):
        print("Quack")

class Person:
    def quack(self):
        print("I'm a person but I can quack like a duck")

def in_the_forest(duck):
    duck.quack()

donald = Duck()
john = Person()

in_the_forest(donald)  # Quack
in_the_forest(john)    # I'm a person but I can quack like a duck
```

### Categories of Types in Annotations

- **Basic types:** `int`, `str`, `float`, `bool`
- **Collection types:** `List`, `Tuple`, `Set`, `Dict`
- **Optional types:** `Optional`
- **User-defined types:** Classes and `TypeVar`

**Example:**

```python
from typing import List, Optional

def process_data(data: List[int], threshold: Optional[int] = None) -> List[int]:
    if threshold is None:
        threshold = 0
    return [d for d in data if d > threshold]
```

### Type Hinting Variadic Parameters

**Example:**

```python
from typing import Any

def log_message(message: str, *args: Any, **kwargs: Any) -> None:
    print(message.format(*args, **kwargs))

log_message("Hello, {}!", "world")
```

### Limitations and Downsides

- **Learning curve:** Requires understanding of type systems.
- **Verbose code:** Can make the code less readable for beginners.
- **Compatibility:** Some dynamic features of Python may be harder to type hint.

## Conclusion

Type hints offer significant benefits for code quality and maintenance, especially for large projects and professional developers. However, they remain optional to accommodate Python's diverse user base.
