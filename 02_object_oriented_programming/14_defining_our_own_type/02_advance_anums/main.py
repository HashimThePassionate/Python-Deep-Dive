from enum import Enum, auto

class MotherSauce(Enum):
    BECHAMEL = auto()
    VELOUTE = auto()
    ESPAGNOLE = auto()
    TOMATO = auto()
    HOLLANDAISE = auto()
    # Intentional alias
    BECHAMEL_ALIAS = BECHAMEL

# Usage
print(list(MotherSauce))
