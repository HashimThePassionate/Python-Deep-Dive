from dataclasses import dataclass, field
from typing import Any, Dict

@dataclass
class ClubMember:
    name: str
    guests: list = field(default_factory=list)

@dataclass
class ExampleDataClass:
    # Non-default argument
    unique_id: int

    # default: Provide a default value for the field
    name: str = "Unknown"

    # default_factory: Provide a function to generate a default value for the field
    ids: Dict[int, str] = field(default_factory=dict)

    # init: Exclude this field from the __init__ method parameters
    computed_value: int = field(init=False, default=42)

    # repr: Exclude this field from the __repr__ method
    password: str = field(repr=False, default="1234")

    # compare: Exclude this field from comparison methods (__eq__, __lt__, etc.)
    secret_code: str = field(compare=False, default="SECRET")

    # hash: Include this field in the __hash__ method calculation
    unique_id: int = field(hash=True)

    # metadata: Attach additional information to the field (ignored by the dataclass itself)
    description: str = field(default="No description", metadata={"info": "This is a description field"})

    def __post_init__(self):
        # computed_value is not included in __init__, so we can compute it after initialization
        self.computed_value = len(self.name) * 10

# Example usage
example = ExampleDataClass(unique_id=123)
print(example)  # __repr__ method output
print(example.name)  # Output: Unknown
print(example.ids)  # Output: {}
print(example.computed_value)  # Output: 70 (computed in __post_init__)
print(example.password)  # Not displayed in __repr__
print(example.secret_code)  # Output: SECRET
print(example.unique_id)  # Output: 123
print(example.description)  # Output: No description
print(example.__dataclass_fields__["description"].metadata)  # Output: {'info': 'This is a description field'}

# Comparison example
example2 = ExampleDataClass(unique_id=123, name="Different")
print(example == example2)  # Output: True (secret_code is excluded from comparison)
print(hash(example))  # Hash value includes unique_id
