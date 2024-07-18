# Defensive Programming with Mutable Parameters

## Introduction

When coding a function that receives a mutable parameter, you should carefully consider whether the caller expects the argument to be changed. For example, if your function receives a dictionary and needs to modify it, should this side effect be visible outside the function? It depends on the context and the expectations of both the function coder and the caller.

## Example

The following example demonstrates how a `TwilightBus` class breaks expectations by sharing its passenger list with its clients.

### Client Perspective

Consider the following interaction with the `TwilightBus` class:

```python
basketball_team = ['Sue', 'Tina', 'Maya', 'Diana', 'Pat']
bus = TwilightBus(basketball_team)
bus.drop('Tina')
bus.drop('Pat')
print(basketball_team)  # Output: ['Sue', 'Maya', 'Diana']
```

- `basketball_team` holds five student names.
- A `TwilightBus` is loaded with the team.
- The bus drops one student, then another.
- The dropped passengers vanish from the basketball team!

### Explanation

`TwilightBus` violates the "Principle of Least Astonishment," a best practice of interface design. This principle suggests that software should behave in a way that least surprises the users. In this context, it is surprising that when the bus drops a student, their name is removed from the basketball team roster. Users would typically expect the `TwilightBus` to manage its own list of passengers independently of the original list passed to it.

## Implementation and Problem

### TwilightBus Class Definition

```python
class TwilightBus:
    """A bus model that makes passengers vanish"""
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)
```

### Problem Analysis

- If `passengers` is `None`, a new empty list is created.
- If `passengers` is provided, `self.passengers` becomes an alias for it.
- Methods `.remove()` and `.append()` mutate the original list received as an argument.

The issue is that the bus is aliasing the list passed to the constructor, affecting the original list.

## Solution

To prevent this, initialize `self.passengers` with a copy of the `passengers` list:

```python
class TwilightBus:
    """A bus model that makes passengers vanish"""
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)
```

### Benefits of the Solution

- Our internal handling of the passenger list will not affect the original argument.
- This solution is more flexible: the argument can be a tuple or any other iterable (e.g., set, database results).
- By creating our own list, we ensure it supports the necessary `.remove()` and `.append()` operations.

## Best Practices

Unless a method is explicitly intended to mutate an object received as an argument, avoid aliasing the argument object by assigning it to an instance variable. If in doubt, make a copy. While copying has a CPU and memory cost, it prevents subtle bugs that can be more problematic than a slight performance hit.

## Conclusion

Defensive programming with mutable parameters ensures that your functions do not unintentionally modify the caller's data, leading to more predictable and reliable code.
