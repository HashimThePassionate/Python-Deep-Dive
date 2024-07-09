## Explanation of Note on Mutable Default Values in `@dataclass`

### The Note
**Note**: While `@dataclass` rejects class definitions with a list default value in a field, it only applies to `list`, `dict`, and `set`. Other mutable values used as defaults will not be flagged by `@dataclass`. It's up to you to understand the problem and remember to use a default factory to set mutable default values.

### What It Means
This note highlights a specific behavior and limitation of the `@dataclass` decorator regarding mutable default values.

### Key Points

1. **Rejection of Certain Mutable Defaults**:
   - The `@dataclass` decorator is designed to reject class definitions where fields have mutable default values for `list`, `dict`, and `set`.
   - This rejection helps prevent the common issue of sharing mutable defaults between instances, which can lead to unexpected behavior.

2. **Limited Scope of Rejection**:
   - The rejection only applies to `list`, `dict`, and `set`.
   - If you use other types of mutable default values (e.g., custom mutable objects or other container types), `@dataclass` will not automatically flag these as problematic.

3. **Responsibility on the Developer**:
   - It's the developer's responsibility to understand the issue of shared mutable defaults.
   - For mutable default values not covered by `@dataclass`'s automatic rejection, the developer should manually ensure that a default factory is used to prevent shared defaults.

### Example to Illustrate the Note

#### Automatically Rejected Mutable Defaults
The following example correctly raises a `ValueError` because `@dataclass` automatically rejects the mutable default value of `list`:

```python
from dataclasses import dataclass

@dataclass
class ClubMember:
    name: str
    guests: list = []
```

#### Not Automatically Rejected Mutable Defaults
Consider a custom mutable object as a default value. `@dataclass` does not automatically reject this:

```python
class CustomMutable:
    def __init__(self, value):
        self.value = value

@dataclass
class ClubMember:
    name: str
    custom: CustomMutable = CustomMutable(0)
```

In this example, `custom` is a field with a mutable default value (`CustomMutable(0)`), but `@dataclass` does not flag this as problematic. Each instance of `ClubMember` would share the same `CustomMutable` instance, leading to potential issues.

#### Correcting with `default_factory`
To avoid sharing the mutable default value, use `default_factory`:

```python
from dataclasses import dataclass, field

@dataclass
class ClubMember:
    name: str
    custom: CustomMutable = field(default_factory=lambda: CustomMutable(0))
```

Now, each instance of `ClubMember` will get its own `CustomMutable` instance, avoiding shared mutable defaults.

### Summary
- `@dataclass` helps prevent shared mutable defaults for `list`, `dict`, and `set` by rejecting such definitions.
- The rejection does not cover all mutable types, so developers must be aware and use `default_factory` for other mutable defaults.
- Understanding this behavior helps prevent bugs and ensures that each instance of a data class behaves as expected with its own independent default values.