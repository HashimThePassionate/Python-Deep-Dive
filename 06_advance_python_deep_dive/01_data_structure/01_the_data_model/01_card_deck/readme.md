# Before we move to Card Deck 
lets understand basic knowledge about deck game

### 1. The Suits

A standard deck of cards has four suits:

####  Hearts (♥)  Diamonds (♦)  Clubs (♣)   Spades (♠)
<pre>
                    Symbol: ♥        Symbol: ♦      Symbol: ♣        Symbol: ♠
                    Color: Red       Color: Red     Color: Black     Color: Black
</pre>

### 2. The Ranks

Each suit has 13 ranks:
<pre>
- Ace (A)
- 2 - 3 - 4 
- 5 - 6 - 7 
- 8 - 9 - 10 
- Jack (J) - Queen (Q) - King (K)
</pre>
### 3. Layout of Each Suit

Let's visually represent each suit with its ranks:

#### Hearts (♥)
```
+-----+ +-----+ +-----+ +-----+ +-----+
|  A  | |  2  | |  3  | |  4  | |  5  |
|  ♥  | |  ♥  | |  ♥  | |  ♥  | |  ♥  |
+-----+ +-----+ +-----+ +-----+ +-----+
+-----+ +-----+ +-----+ +-----+ +-----+
|  6  | |  7  | |  8  | |  9  | | 10  |
|  ♥  | |  ♥  | |  ♥  | |  ♥  | |  ♥  |
+-----+ +-----+ +-----+ +-----+ +-----+
+-----+ +-----+ +-----+
|  J  | |  Q  | |  K  |
|  ♥  | |  ♥  | |  ♥  |
+-----+ +-----+ +-----+
```

#### Diamonds (♦)
```
+-----+ +-----+ +-----+ +-----+ +-----+
|  A  | |  2  | |  3  | |  4  | |  5  |
|  ♦  | |  ♦  | |  ♦  | |  ♦  | |  ♦  |
+-----+ +-----+ +-----+ +-----+ +-----+
+-----+ +-----+ +-----+ +-----+ +-----+
|  6  | |  7  | |  8  | |  9  | | 10  |
|  ♦  | |  ♦  | |  ♦  | |  ♦  | |  ♦  |
+-----+ +-----+ +-----+ +-----+ +-----+
+-----+ +-----+ +-----+
|  J  | |  Q  | |  K  |
|  ♦  | |  ♦  | |  ♦  |
+-----+ +-----+ +-----+
```

#### Clubs (♣)
```
+-----+ +-----+ +-----+ +-----+ +-----+
|  A  | |  2  | |  3  | |  4  | |  5  |
|  ♣  | |  ♣  | |  ♣  | |  ♣  | |  ♣  |
+-----+ +-----+ +-----+ +-----+ +-----+
+-----+ +-----+ +-----+ +-----+ +-----+
|  6  | |  7  | |  8  | |  9  | | 10  |
|  ♣  | |  ♣  | |  ♣  | |  ♣  | |  ♣  |
+-----+ +-----+ +-----+ +-----+ +-----+
+-----+ +-----+ +-----+
|  J  | |  Q  | |  K  |
|  ♣  | |  ♣  | |  ♣  |
+-----+ +-----+ +-----+
```

#### Spades (♠)
```
+-----+ +-----+ +-----+ +-----+ +-----+
|  A  | |  2  | |  3  | |  4  | |  5  |
|  ♠  | |  ♠  | |  ♠  | |  ♠  | |  ♠  |
+-----+ +-----+ +-----+ +-----+ +-----+
+-----+ +-----+ +-----+ +-----+ +-----+
|  6  | |  7  | |  8  | |  9  | | 10  |
|  ♠  | |  ♠  | |  ♠  | |  ♠  | |  ♠  |
+-----+ +-----+ +-----+ +-----+ +-----+
+-----+ +-----+ +-----+
|  J  | |  Q  | |  K  |
|  ♠  | |  ♠  | |  ♠  |
+-----+ +-----+ +-----+
```

### 4. Full Deck Overview

When you put all the suits together, the full deck looks like this:

```
Hearts (♥):  A  2  3  4  5  6  7  8  9  10  J  Q  K
Diamonds (♦):  A  2  3  4  5  6  7  8  9  10  J  Q  K
Clubs (♣):  A  2  3  4  5  6  7  8  9  10  J  Q  K
Spades (♠):  A  2  3  4  5  6  7  8  9  10  J  Q  K
```

### 5. Graphical Example of Cards

Here are graphical examples of individual cards:

- **Ace of Hearts (♥)**
  ```
  +---------+
  |A        |
  |    ♥    |
  |        A|
  +---------+
  ```

- **10 of Diamonds (♦)**
  ```
  +---------+
  |10       |
  |    ♦    |
  |       10|
  +---------+
  ```

- **Queen of Clubs (♣)**
  ```
  +---------+
  |Q        |
  |    ♣    |
  |        Q|
  +---------+
  ```

- **King of Spades (♠)**
  ```
  +---------+
  |K        |
  |    ♠    |
  |        K|
  +---------+
  ```

### Summary

- **52 cards** in total
- **4 suits**: Hearts, Diamonds, Clubs, Spades
- **13 ranks** per suit: Ace, 2 through 10, Jack, Queen, King

# Now lets look a python code of this game
```python
import collections
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

beer_card = Card('7', 'diamonds')
print(beer_card)  # Output: Card(rank='7', suit='diamonds')
deck = FrenchDeck()
print(len(deck))  # Output: 52
```
# FrenchDeck: A Pythonic Card Deck

This simple yet powerful implementation of a card deck demonstrates the use of Python's special methods `__getitem__` and `__len__`. By leveraging these methods, the `FrenchDeck` class behaves like a standard Python sequence.

## Table of Contents
1. [Introduction](#introduction)
2. [Card Class](#card-class)
3. [FrenchDeck Class](#frenchdeck-class)
4. [Usage Examples](#usage-examples)
5. [Detailed Code Explanation](#detailed-code-explanation)
6. [Summary](#summary)

## Introduction

This implementation demonstrates the power of Python's data model by implementing just two special methods: `__getitem__` and `__len__`. It allows the `FrenchDeck` class to behave like a standard Python sequence, providing functionalities such as indexing, slicing, and iteration.

## Card Class

The `Card` class represents individual cards in the deck. It is created using `collections.namedtuple`, which allows us to define simple classes with attributes but no methods.

```python
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])
```

### What is `collections.namedtuple`?

`collections.namedtuple` is a factory function for creating tuple subclasses with named fields. It allows you to create simple classes with attributes but without having to write an explicit class definition. The result is an immutable sequence type that behaves like a tuple but is more readable because you can access the elements by name instead of position.

#### Syntax

```python
collections.namedtuple(typename, field_names)
```

- **typename**: The name of the new class (e.g., `Card`).
- **field_names**: A list of field names for the class (e.g., `['rank', 'suit']`).

#### Example in Your Code

```python
Card = collections.namedtuple('Card', ['rank', 'suit'])
```

This creates a new class `Card` with two attributes: `rank` and `suit`.

#### Benefits of Using `collections.namedtuple`

- **Readability**: Accessing elements by name instead of position makes the code more readable and self-documenting.
- **Immutability**: Ensures that the values of the attributes cannot be changed, which can prevent bugs.
- **Tuple-like Behavior**: Named tuples inherit the behavior of tuples, so they can be used in any context where a tuple is expected.
- **Lightweight**: Named tuples are lightweight and do not have the overhead of regular classes.

## FrenchDeck Class

The `FrenchDeck` class represents the entire deck of cards. It includes methods to initialize the deck, get its length, and access individual cards.

```python
class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]
```

### Explanation of `ranks` and `suits`

#### `ranks`

```python
ranks = [str(n) for n in range(2, 11)] + list('JQKA')
```

- **List Comprehension**: `[str(n) for n in range(2, 11)]`
  - Generates a sequence of numbers from 2 to 10 (inclusive) and converts each number to a string.
  - Result: `['2', '3', '4', '5', '6', '7', '8', '9', '10']`

- **List Concatenation**: `+ list('JQKA')`
  - Converts the string `'JQKA'` into a list of its characters: `['J', 'Q', 'K', 'A']`
  - Final `ranks`: `['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']`

#### `suits`

```python
suits = 'spades diamonds clubs hearts'.split()
```
Let's break down these lines of code in detail:

### 1. `ranks = [str(n) for n in range(2, 11)] + list('JQKA')`

This line of code creates a list of card ranks. Here's how it works step by step:

1. **List Comprehension**: `[str(n) for n in range(2, 11)]`
   - `range(2, 11)` generates a sequence of numbers from 2 to 10 (inclusive).
   - `str(n)` converts each number in this range to a string.
   - The list comprehension collects these string representations into a list.

   The result of this part is `['2', '3', '4', '5', '6', '7', '8', '9', '10']`.

2. **List Concatenation**: `+ list('JQKA')`
   - `list('JQKA')` converts the string `'JQKA'` into a list of its characters: `['J', 'Q', 'K', 'A']`.
   - The `+` operator concatenates the two lists.

   So, the final value of `ranks` is:
   ```python
   ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
   ```

### 2. `suits = 'spades diamonds clubs hearts'.split()`

This line of code creates a list of card suits. Here's how it works:

1. **String**: `'spades diamonds clubs hearts'`
   - This is a single string containing the names of the four suits, separated by spaces.

2. **String Split Method**: `.split()`
   - The `split()` method, when called without arguments, splits the string at each space.
   - This method returns a list of substrings.

   So, the final value of `suits` is:
   ```python
   ['spades', 'diamonds', 'clubs', 'hearts']
   ```
### Creating the Deck
```python
self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
```

This line of code is inside the `__init__` method of the `FrenchDeck` class. It creates a list of `Card` objects, representing a full deck of cards. Here's how it works step by step:

### List Comprehension

The line uses a list comprehension to create a list of `Card` objects. A list comprehension is a concise way to create lists in Python. The general syntax is:

```python
[expression for item in iterable]
```

In this case, the list comprehension creates `Card` objects for every combination of ranks and suits.

### Nested Loops in List Comprehension

The list comprehension includes two `for` clauses, which means it effectively performs nested loops. Here’s the breakdown:

1. **Outer Loop**: `for suit in self.suits`
   - Iterates over each suit in `self.suits` (which contains `['spades', 'diamonds', 'clubs', 'hearts']`).

2. **Inner Loop**: `for rank in self.ranks`
   - For each suit, iterates over each rank in `self.ranks` (which contains `['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']`).

### Creating `Card` Objects

The expression `Card(rank, suit)` creates a new `Card` object for each combination of `rank` and `suit`. The `Card` named tuple is defined as:

```python
Card = collections.namedtuple('Card', ['rank', 'suit'])
```

### Full Breakdown of the List Comprehension

Here’s what happens when the list comprehension runs:

1. **First Iteration of Outer Loop**: `suit = 'spades'`
   - **Inner Loop Iterations**:
     - `rank = '2'`: Creates `Card('2', 'spades')`
     - `rank = '3'`: Creates `Card('3', 'spades')`
     - ...
     - `rank = 'A'`: Creates `Card('A', 'spades')`

2. **Second Iteration of Outer Loop**: `suit = 'diamonds'`
   - **Inner Loop Iterations**:
     - `rank = '2'`: Creates `Card('2', 'diamonds')`
     - `rank = '3'`: Creates `Card('3', 'diamonds')`
     - ...
     - `rank = 'A'`: Creates `Card('A', 'diamonds')`

3. **Third Iteration of Outer Loop**: `suit = 'clubs'`
   - **Inner Loop Iterations**:
     - `rank = '2'`: Creates `Card('2', 'clubs')`
     - `rank = '3'`: Creates `Card('3', 'clubs')`
     - ...
     - `rank = 'A'`: Creates `Card('A', 'clubs')`

4. **Fourth Iteration of Outer Loop**: `suit = 'hearts'`
   - **Inner Loop Iterations**:
     - `rank = '2'`: Creates `Card('2', 'hearts')`
     - `rank = '3'`: Creates `Card('3', 'hearts')`
     - ...
     - `rank = 'A'`: Creates `Card('A', 'hearts')`

### Result

The list comprehension produces a list containing 52 `Card` objects, one for each combination of the 13 ranks and 4 suits.

```python
self._cards = [
    Card('2', 'spades'), Card('3', 'spades'), Card('4', 'spades'), ..., Card('A', 'spades'),
    Card('2', 'diamonds'), Card('3', 'diamonds'), Card('4', 'diamonds'), ..., Card('A', 'diamonds'),
    Card('2', 'clubs'), Card('3', 'clubs'), Card('4', 'clubs'), ..., Card('A', 'clubs'),
    Card('2', 'hearts'), Card('3', 'hearts'), Card('4', 'hearts'), ..., Card('A', 'hearts')
]
```

### Storing the List

The list of `Card` objects is then assigned to `self._cards`. This attribute (`self._cards`) will store the full deck of cards, which can be used by other methods in the `FrenchDeck` class to perform operations like getting the number of cards, accessing specific cards, and so on.This line of code initializes the `self._cards` attribute with a list of 52 `Card` objects, representing a standard deck of playing cards. Each `Card` object is created using a combination of ranks and suits, resulting in a complete deck.

### Special Methods

#### `__len__`

Returns the number of cards in the deck.

```python
def __len__(self):
    return len(self._cards)
```

#### `__getitem__`

Allows access to cards by index.

```python
def __getitem__(self, position):
    return self._cards[position]
```

## Usage Examples

### Creating a Deck

```python
deck = FrenchDeck()
```

### Checking the Deck Length

```python
print(len(deck))  # Output: 52
```

### Accessing Cards

```python
print(deck[0])   # Output: Card(rank='2', suit='spades')
print(deck[-1])  # Output: Card(rank='A', suit='hearts')
```

### Selecting a Random Card

```python
from random import choice

print(choice(deck))  # Example output: Card(rank='3', suit='hearts')
```

### Slicing the Deck

```python
print(deck[:3])       # Output: [Card(rank='2', suit='spades'), Card(rank='3', suit='spades'), Card(rank='4', suit='spades')]
print(deck[12::13])   # Output: [Card(rank='A', suit='spades'), Card(rank='A', suit='diamonds'), Card(rank='A', suit='clubs'), Card(rank='A', suit='hearts')]
```

### Iterating Over the Deck

```python
for card in deck:
    print(card)
```

### Checking Membership

```python
print(Card('Q', 'hearts') in deck)  # Output: True
```