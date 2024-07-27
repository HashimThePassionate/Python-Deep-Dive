# Special Methods for Numeric Objects

In Python, special methods enable instances of classes to support numeric operations. These methods allow objects to behave like numbers and support operations such as addition, multiplication, and division, among others. Here's a detailed explanation of these special methods along with practical examples.

### List of Special Methods

#### Unary Operators
- `__abs__(self)`: Called by the `abs()` function.
- `__invert__(self)`: Called by the `~` (bitwise NOT) operator.
- `__neg__(self)`: Called by the unary `-` (negation) operator.
- `__pos__(self)`: Called by the unary `+` (positive) operator.

#### Binary Operators
- `__add__(self, other)`: Called by the `+` operator.
- `__mod__(self, other)`: Called by the `%` operator.
- `__mul__(self, other)`: Called by the `*` operator.
- `__sub__(self, other)`: Called by the `-` operator.
- `__truediv__(self, other)`: Called by the `/` operator.
- `__floordiv__(self, other)`: Called by the `//` operator.
- `__divmod__(self, other)`: Called by the `divmod()` function.
- `__pow__(self, other, modulo=None)`: Called by the `**` operator and `pow()` function.

#### Augmented Assignment Operators
- `__iadd__(self, other)`: Called by the `+=` operator.
- `__isub__(self, other)`: Called by the `-=` operator.
- `__imul__(self, other)`: Called by the `*=` operator.
- `__itruediv__(self, other)`: Called by the `/=` operator.
- `__ifloordiv__(self, other)`: Called by the `//=` operator.
- `__imod__(self, other)`: Called by the `%=` operator.
- `__ipow__(self, other)`: Called by the `**=` operator.

#### Reflection Operators
- `__radd__(self, other)`: Called by the `+` operator when the left operand does not support the addition operation.
- `__rsub__(self, other)`: Called by the `-` operator when the left operand does not support the subtraction operation.
- `__rmul__(self, other)`: Called by the `*` operator when the left operand does not support the multiplication operation.
- `__rtruediv__(self, other)`: Called by the `/` operator when the left operand does not support the division operation.
- `__rfloordiv__(self, other)`: Called by the `//` operator when the left operand does not support the floor division operation.
- `__rmod__(self, other)`: Called by the `%` operator when the left operand does not support the modulus operation.
- `__rpow__(self, other)`: Called by the `**` operator when the left operand does not support the power operation.
- `__rdivmod__(self, other)`: Called by the `divmod()` function when the left operand does not support the divmod operation.

#### Bitwise Operators
- `__and__(self, other)`: Called by the `&` operator.
- `__or__(self, other)`: Called by the `|` operator.
- `__xor__(self, other)`: Called by the `^` operator.
- `__lshift__(self, other)`: Called by the `<<` operator.
- `__rshift__(self, other)`: Called by the `>>` operator.

#### Reflection Bitwise Operators
- `__rand__(self, other)`: Called by the `&` operator when the left operand does not support the bitwise AND operation.
- `__ror__(self, other)`: Called by the `|` operator when the left operand does not support the bitwise OR operation.
- `__rxor__(self, other)`: Called by the `^` operator when the left operand does not support the bitwise XOR operation.
- `__rlshift__(self, other)`: Called by the `<<` operator when the left operand does not support the left shift operation.
- `__rrshift__(self, other)`: Called by the `>>` operator when the left operand does not support the right shift operation.

### Implementation of Numeric Special Methods

Below is an example implementation of a custom numeric class that supports several special methods:

```python
class CustomNumber:
    def __init__(self, value):
        self.value = value
    
    # Unary operators
    def __abs__(self):
        return CustomNumber(abs(self.value))
    
    def __invert__(self):
        return CustomNumber(~self.value)
    
    def __neg__(self):
        return CustomNumber(-self.value)
    
    def __pos__(self):
        return CustomNumber(+self.value)
    
    # Binary operators
    def __add__(self, other):
        if isinstance(other, CustomNumber):
            other = other.value
        return CustomNumber(self.value + other)
    
    def __sub__(self, other):
        if isinstance(other, CustomNumber):
            other = other.value
        return CustomNumber(self.value - other)
    
    def __mul__(self, other):
        if isinstance(other, CustomNumber):
            other = other.value
        return CustomNumber(self.value * other)
    
    def __truediv__(self, other):
        if isinstance(other, CustomNumber):
            other = other.value
        return CustomNumber(self.value / other)
    
    def __floordiv__(self, other):
        if isinstance(other, CustomNumber):
            other = other.value
        return CustomNumber(self.value // other)
    
    def __mod__(self, other):
        if isinstance(other, CustomNumber):
            other = other.value
        return CustomNumber(self.value % other)
    
    def __pow__(self, other, modulo=None):
        if isinstance(other, CustomNumber):
            other = other.value
        if modulo is None:
            return CustomNumber(pow(self.value, other))
        else:
            return CustomNumber(pow(self.value, other, modulo))
    
    # Augmented assignment operators
    def __iadd__(self, other):
        if isinstance(other, CustomNumber):
            other = other.value
        self.value += other
        return self
    
    def __isub__(self, other):
        if isinstance(other, CustomNumber):
            other = other.value
        self.value -= other
        return self
    
    def __imul__(self, other):
        if isinstance(other, CustomNumber):
            other = other.value
        self.value *= other
        return self
    
    def __itruediv__(self, other):
        if isinstance(other, CustomNumber):
            other = other.value
        self.value /= other
        return self
    
    def __ifloordiv__(self, other):
        if isinstance(other, CustomNumber):
            other = other.value
        self.value //= other
        return self
    
    def __imod__(self, other):
        if isinstance(other, CustomNumber):
            other = other.value
        self.value %= other
        return self
    
    def __ipow__(self, other):
        if isinstance(other, CustomNumber):
            other = other.value
        self.value **= other
        return self
    
    # Reflection operators
    def __radd__(self, other):
        return self + other
    
    def __rsub__(self, other):
        return CustomNumber(other) - self.value
    
    def __rmul__(self, other):
        return self * other
    
    def __rtruediv__(self, other):
        return CustomNumber(other) / self.value
    
    def __rfloordiv__(self, other):
        return CustomNumber(other) // self.value
    
    def __rmod__(self, other):
        return CustomNumber(other) % self.value
    
    def __rpow__(self, other):
        return CustomNumber(other) ** self.value
    
    # String representation
    def __repr__(self):
        return f"CustomNumber({self.value})"

# Example usage
a = CustomNumber(10)
b = CustomNumber(5)

print(abs(a))        # Output: CustomNumber(10)
print(~a)            # Output: CustomNumber(-11)
print(-a)            # Output: CustomNumber(-10)
print(+a)            # Output: CustomNumber(10)

print(a + b)         # Output: CustomNumber(15)
print(a - b)         # Output: CustomNumber(5)
print(a * b)         # Output: CustomNumber(50)
print(a / b)         # Output: CustomNumber(2.0)
print(a // b)        # Output: CustomNumber(2)
print(a % b)         # Output: CustomNumber(0)
print(a ** b)        # Output: CustomNumber(100000)

a += b
print(a)             # Output: CustomNumber(15)
a -= b
print(a)             # Output: CustomNumber(10)
a *= b
print(a)             # Output: CustomNumber(50)
a /= b
print(a)             # Output: CustomNumber(10.0)
a //= b
print(a)             # Output: CustomNumber(2.0)
a %= b
print(a)             # Output: CustomNumber(2.0)
a **= b
print(a)             # Output: CustomNumber(32.0)

print(5 + a)         # Output: CustomNumber(37.0)
print(5

 - a)         # Output: CustomNumber(-27.0)
print(5 * a)         # Output: CustomNumber(160.0)
print(5 / a)         # Output: CustomNumber(0.15625)
print(5 // a)        # Output: CustomNumber(0.0)
print(5 % a)         # Output: CustomNumber(5.0)
print(5 ** a)        # Output: CustomNumber(298023223876953125)
```

