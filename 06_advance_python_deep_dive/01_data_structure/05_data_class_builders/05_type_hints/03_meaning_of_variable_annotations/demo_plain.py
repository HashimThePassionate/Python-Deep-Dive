# 03_meaning_of_variable_annotations/demo_plain.py: a plain class with type hints
import typing
from dataclasses import dataclass


class DemoPlainClass:
    a: int
    b: float = 1.1
    c = 'spam'


# 03_meaning_of_variable_annotations/demo_plain.py: a class built with typing.NamedTuple
class DemoNTClass(typing.NamedTuple):
    a: int
    b: float = 1.1
    c = 'spam'



# 03_meaning_of_variable_annotations/demo_plain.py: a class built with @dataclass
@dataclass
class DemoDataClass:
    a: int
    b: float = 1.1
    c = 'spam'