# Reference to Data Classes

## Introduction

Python’s standard documentation for data class builders is comprehensive and includes several small examples. Notably, much of PEP 557—Data Classes was included in the dataclasses module documentation. However, some informative sections, such as "Why not just use namedtuple?", "Why not just use typing.NamedTuple?", and the “Rationale” section, are only found in PEP 557.

### Key Resources:
- **PEP 557 “Rationale”**:
  - **[When not to use Data Classes](https://peps.python.org/pep-0557/#id33)**: Avoid when API compatibility with tuples or dicts is needed, or when type/value validation or conversion beyond PEPs 484 and 526 is required.
- **RealPython.com**:
  - Geir Arne Hjelle's **[Ultimate guide to data classes in Python 3.7](https://realpython.com/python-data-classes/)**.
- **PyCon US 2018**:
  - Raymond Hettinger’s presentation **[Dataclasses: The code generator to end all code generators](https://www.youtube.com/watch?v=T-TwcmT6Rcw)**.
- **[attrs Project](https://glyph.twistedmatrix.com/2016/08/attrs.html)**:
  - Provides more features and validation options compared to dataclasses.
  - Authored by Hynek Schlawack.
  - Emphasizes easing the creation of classes by handling object protocols (dunder methods).
- **[cluegen](https://refactoring.guru/smells/data-class)**:
  - Another data class generator by Dave Beazley.
  - Focuses on metaprogramming Python from first principles.

## Declaring Instance Attributes in Python

Python traditionally lacked a standard way to declare instance attributes. This has been resolved with @dataclass, but it introduces its own set of challenges.

### Example:
Smalltalk:
```smalltalk
Object subclass: #Point
  instanceVariableNames: 'x y'
  classVariableNames: ''
  package: 'Kernel-BasicObjects'
```

Python:
```python
@dataclass
class Point:
  x: int
  y: int
```

## Issues with @dataclass

1. **Mandatory Type Hints**:
   - Type hints, previously optional, are now required.
   - For those opposed to static typing, attrs might be preferable.

2. **PEP 526 Syntax**:
   - Reverses the convention of class statement declarations.
   - Any top-level attribute with a type hint becomes an instance attribute.
   - Without type hints, attributes are class attributes.

### Examples:
Instance Attribute:
```python
@dataclass
class Spam:
  repeat: int  # instance attribute
```
```python
@dataclass
class Spam:
  repeat: int = 99  # instance attribute
```

Class Attribute:
```python
@dataclass
class Spam:
  repeat = 99  # class attribute
```

To annotate class attributes with a type:
```python
@dataclass
class Spam:
  repeat: ClassVar[int] = 99  # class attribute with type
```

## Proposed Alternative Syntax

An alternative syntax could involve a dot prefix for instance attributes:
```python
@dataclass
class HackerClubMember:
  .name: str
  .guests: list = field(default_factory=list)
  .handle: str = ''
  all_handles = set()  # class attribute
```
- Attributes with a dot prefix are instance attributes.
- Attributes without a dot prefix are class attributes.

This proposed syntax would require changes to the language grammar.

## Conclusion

Python's @dataclass provides a standardized way to declare instance attributes but introduces challenges related to type hints and attribute declaration syntax. Exploring alternative approaches and understanding existing tools like attrs and cluegen can provide more flexibility and features.
For more detailed explanations and further reading, refer to the resources mentioned above.
