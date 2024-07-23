from collections.abc import Iterable
from decimal import Decimal
from fractions import Fraction
from typing import TypeVar

NumberT = TypeVar('NumberT', float, Decimal, Fraction)

def mode(data: Iterable[NumberT]) -> NumberT:
    from collections import Counter
    pairs = Counter(data).most_common(1)
    if len(pairs) == 0:
        raise ValueError('no mode for empty data')
    return pairs[0][0]


print(mode([1, 1, 2, 3, 3, 3, 4]))
print(mode([1.1, 1.1, 2.2, 3.3, 3.3, 3.3, 4.4]))
print(mode([Decimal('1.1'), Decimal('1.1'), Decimal('2.2'), Decimal('3.3'), Decimal('3.3'), Decimal('3.3'), Decimal('4.4')]))
print(mode([Fraction(1, 1), Fraction(1, 1), Fraction(2, 1), Fraction(3, 1), Fraction(3, 1), Fraction(3, 1), Fraction(4, 1)]))
print(mode([1, 2, 3]))  # Example: pass a valid iterable of numbers
  # 3p