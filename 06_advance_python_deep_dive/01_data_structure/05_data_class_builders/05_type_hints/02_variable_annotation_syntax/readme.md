# Variable Annotation Syntax

## Introduction
Both `typing.NamedTuple` and `@dataclass` use the variable annotation syntax defined in PEP 526. This guide provides a quick introduction to that syntax, particularly for defining attributes in class statements.

### Basic Syntax:
- The basic format for variable annotation is:
  ```python
  var_name: some_type
  ```

## Acceptable Type Hints
The "Acceptable type hints" section in PEP 484 outlines what types are acceptable. In the context of defining a data class, the following types are particularly useful:
- **Concrete Class**: Examples include `str` or custom classes like `FrenchDeck`.
- **Parameterized Collection Types**: Examples include `list[int]`, `tuple[str, float]`, etc.
- **Optional Types**: Using `typing.Optional`, for example, `Optional[str]` to declare a field that can be a `str` or `None`.

## Examples

### Example of Concrete Class:
```python
from typing import NamedTuple

class FrenchDeck:
    def __init__(self):
        self.cards = ["Ace of Spades", "2 of Hearts", "3 of Clubs", "4 of Diamonds"]
    
    def __repr__(self):
        return f"FrenchDeck(cards={self.cards})"

class Card(NamedTuple):
    name: str
    deck: FrenchDeck

# Creating an instance
deck = FrenchDeck()
card = Card(name="Ace of Spades", deck=deck)
print(card)
```

**Explanation:**
- **FrenchDeck Class**: This class initializes with a list of card names and has a `__repr__` method to return a string representation of the deck.
- **Card NamedTuple**: This named tuple has two fields: `name` of type `str` and `deck` of type `FrenchDeck`.
- **Creating Instances**: An instance of `FrenchDeck` is created, followed by an instance of `Card` using the deck instance. Printing the card shows both the card name and the full deck contents.

### Example of Parameterized Collection Types:
```python
from typing import NamedTuple, List, Tuple

class Point(NamedTuple):
    coordinates: Tuple[str, float]
    values: List[int]

# Creating an instance
point = Point(coordinates=("latitude", 42.0), values=[1, 2, 3, 4])
print(point)
```

**Explanation:**
- **Point NamedTuple**: This named tuple has two fields: `coordinates` of type `Tuple[str, float]` and `values` of type `List[int]`.
- **Creating Instances**: An instance of `Point` is created with a tuple for coordinates and a list of integers for values. Printing the point shows the coordinates and values.

### Example of Optional Types:
```python
from typing import NamedTuple, Optional

class User(NamedTuple):
    nickname: Optional[str]

# Creating instances
user_with_nickname = User(nickname="Hash")
user_without_nickname = User(nickname=None)
print(user_with_nickname)
print(user_without_nickname)
```

**Explanation:**
- **User NamedTuple**: This named tuple has one field: `nickname` of type `Optional[str]`, which means it can be a string or `None`.
- **Creating Instances**: Two instances of `User` are created—one with a nickname and one without (using `None`). Printing the users shows their nicknames (or lack thereof).

### Initializing Variables with Values
You can also initialize the variable with a value. In a `typing.NamedTuple` or `@dataclass` declaration, that value becomes the default for the attribute if the corresponding argument is omitted in the constructor call.

```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str = "Unknown"
    age: int = 0

# Creating instances
person1 = Person()
person2 = Person(name="Hashim", age=25)
print(person1)
print(person2)
```

**Explanation:**
- **Person Data Class**: This data class has two fields: `name` of type `str` with a default value of `"Unknown"` and `age` of type `int` with a default value of `0`.
- **Creating Instances**: Two instances of `Person` are created—one without specifying name and age, using default values, and one with specified name and age. Printing the persons shows their names and ages.

