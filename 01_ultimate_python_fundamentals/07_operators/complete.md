# 🐍 Python Operators

### 🌟 1. Arithmetic Operators ➕➖✖️➗

Arithmetic operators perform basic mathematical operations.

- **`+` (Addition) ➕:** Adds two operands.
  - **Example:** `a = 5 + 3` results in `a = 8`.
  - **Use Case:** Calculating total scores, sums, etc.
  
- **`-` (Subtraction) ➖:** Subtracts the second operand from the first.
  - **Example:** `a = 10 - 4` results in `a = 6`.
  - **Use Case:** Calculating the difference between values, such as time intervals.

- **`*` (Multiplication) ✖️:** Multiplies two operands.
  - **Example:** `a = 7 * 6` results in `a = 42`.
  - **Use Case:** Used in area calculations, scaling values, etc.

- **`/` (Division) ➗:** Divides the first operand by the second.
  - **Example:** `a = 20 / 4` results in `a = 5.0`.
  - **Use Case:** Splitting data, average calculations, etc.

- **`%` (Modulus) ➗:** Returns the remainder after division.
  - **Example:** `a = 10 % 3` results in `a = 1`.
  - **Use Case:** Used in checks for even/odd numbers, cyclic operations.

- **`**` (Exponent) 🌟:** Raises the first operand to the power of the second.
  - **Example:** `a = 2 ** 3` results in `a = 8`.
  - **Use Case:** Calculating powers, such as in mathematical formulas.

- **`//` (Floor Division) 🏠:** Divides and returns the largest integer smaller than or equal to the result.
  - **Example:** `a = 7 // 2` results in `a = 3`.
  - **Use Case:** Used in loops, partitioning tasks, etc.

**Detailed Example:**

```python
a = 10
b = 3

addition = a + b  # ➕ 10 + 3 = 13
subtraction = a - b  # ➖ 10 - 3 = 7
multiplication = a * b  # ✖️ 10 * 3 = 30
division = a / b  # ➗ 10 / 3 = 3.33
modulus = a % b  # ➗ 10 % 3 = 1
exponent = a ** b  # 🌟 10 ** 3 = 1000
floor_division = a // b  # 🏠 10 // 3 = 3

print(addition, subtraction, multiplication, division, modulus, exponent, floor_division)
```

---

### 🧮 2. Comparison Operators 🆚

Comparison operators compare values and return a boolean (`True` or `False`).

- **`==` (Equal to) ✅:** Returns `True` if both operands are equal.
  - **Example:** `5 == 5` results in `True`.
  - **Use Case:** Checking equality in conditional statements.

- **`!=` (Not equal to) ❌:** Returns `True` if operands are not equal.
  - **Example:** `5 != 3` results in `True`.
  - **Use Case:** Validating inputs, detecting changes.

- **`<` (Less than) ⬇️:** Returns `True` if the first operand is smaller.
  - **Example:** `3 < 5` results in `True`.
  - **Use Case:** Sorting algorithms, comparing dates.

- **`>` (Greater than) ⬆️:** Returns `True` if the first operand is greater.
  - **Example:** `5 > 3` results in `True`.
  - **Use Case:** Validation of ranges, threshold checks.

- **`<=` (Less than or equal to) ⬇️✅:** Returns `True` if the first operand is smaller or equal.
  - **Example:** `5 <= 5` results in `True`.
  - **Use Case:** Boundary condition checks.

- **`>=` (Greater than or equal to) ⬆️✅:** Returns `True` if the first operand is greater or equal.
  - **Example:** `5 >= 4` results in `True`.
  - **Use Case:** Threshold validations, comparisons.

**Detailed Example:**

```python
a = 5
b = 10

equal = a == b  # ✅ False
not_equal = a != b  # ❌ True
less_than = a < b  # ⬇️ True
greater_than = a > b  # ⬆️ False
less_equal = a <= b  # ⬇️✅ True
greater_equal = a >= b  # ⬆️✅ False

print(equal, not_equal, less_than, greater_than, less_equal, greater_equal)
```

---

### 📝 3. Assignment Operators

Assignment operators assign values to variables.

- **`=` (Assign) 📝:** Assigns the value of the right operand to the left.
  - **Example:** `a = 5` results in `a` being `5`.
  - **Use Case:** Variable initialization, updates.

- **`+=` (Add and assign) ➕📝:** Adds the right operand to the left operand and assigns the result to the left.
  - **Example:** `a += 5` results in `a` being `10` if `a` was `5`.
  - **Use Case:** Accumulating values in loops.

- **`-=` (Subtract and assign) ➖📝:** Subtracts the right operand from the left operand and assigns the result to the left.
  - **Example:** `a -= 3` results in `a` being `2` if `a` was `5`.
  - **Use Case:** Reducing counters.

- **`*=` (Multiply and assign) ✖️📝:** Multiplies the left operand by the right operand and assigns the result to the left.
  - **Example:** `a *= 2` results in `a` being `10` if `a` was `5`.
  - **Use Case:** Scaling values.

- **`/=` (Divide and assign) ➗📝:** Divides the left operand by the right operand and assigns the result to the left.
  - **Example:** `a /= 2` results in `a` being `2.5` if `a` was `5`.
  - **Use Case:** Averaging values.

- **`%=` (Modulus and assign) ➗📝:** Takes the modulus of the left operand by the right operand and assigns the result to the left.
  - **Example:** `a %= 3` results in `a` being `2` if `a` was `5`.
  - **Use Case:** Keeping track of cycles.

- **`**=` (Exponent and assign) 🌟📝:** Raises the left operand to the power of the right operand and assigns the result to the left.
  - **Example:** `a **= 2` results in `a` being `25` if `a` was `5`.
  - **Use Case:** Repeated exponentiation.

- **`//=` (Floor division and assign) 🏠📝:** Takes the floor division of the left operand by the right operand and assigns the result to the left.
  - **Example:** `a //= 2` results in `a` being `2` if `a` was `5`.
  - **Use Case:** Dividing tasks into chunks.

**Detailed Example:**

```python
a = 5

a += 5  # ➕📝 a = a + 5 -> 10
a -= 3  # ➖📝 a = a - 3 -> 7
a *= 2  # ✖️📝 a = a * 2 -> 14
a /= 2  # ➗📝 a = a / 2 -> 7.0
a %= 4  # ➗📝 a = a % 4 -> 3.0
a **= 2  # 🌟📝 a = a ** 2 -> 9.0
a //= 2  # 🏠📝 a = a // 2 -> 4.0

print(a)
```

---

### 🤔 4. Logical Operators

Logical operators are used to combine conditional statements.

- **`and` (Logical AND) 🤝:** Returns `True` if both operands are `True`.
  - **Example:** `True and False` results in `False`.
  - **Use Case:** Checking multiple conditions simultaneously.

- **`or` (Logical OR) 🚪:** Returns `True` if at least one of the operands is `True`.
  - **Example:** `True or False` results in `True`.
  - **Use Case:** Validating multiple possible conditions.

- **`not` (Logical NOT) 🚫:** Returns `True` if the operand is `False`.
  - **Example:** `not True` results in `False`.
  - **Use Case:** Reversing the result of a condition.

**

Detailed Example:**

```python
a = True
b = False

result_and = a and b  # 🤝 False
result_or = a or b  # 🚪 True
result_not = not a  # 🚫 False

print(result_and, result_or, result_not)
```

---

### 🔢 5. Bitwise Operators

Bitwise operators perform bit-level operations on operands.

- **`&` (AND) 🔗:** Performs bitwise AND operation.
  - **Example:** `5 & 3` results in `1`.
  - **Use Case:** Masking bits.

- **`|` (OR) 🚪:** Performs bitwise OR operation.
  - **Example:** `5 | 3` results in `7`.
  - **Use Case:** Setting specific bits.

- **`^` (XOR) ⚡:** Performs bitwise XOR operation.
  - **Example:** `5 ^ 3` results in `6`.
  - **Use Case:** Toggling bits.

- **`~` (NOT) 🚫:** Performs bitwise NOT operation.
  - **Example:** `~5` results in `-6`.
  - **Use Case:** Flipping bits.

- **`<<` (Left Shift) ⬅️:** Shifts bits to the left by a specified number.
  - **Example:** `5 << 1` results in `10`.
  - **Use Case:** Multiplying by powers of two.

- **`>>` (Right Shift) ➡️:** Shifts bits to the right by a specified number.
  - **Example:** `5 >> 1` results in `2`.
  - **Use Case:** Dividing by powers of two.

**Detailed Example:**

```python
a = 5  # Binary: 0101
b = 3  # Binary: 0011

bitwise_and = a & b  # 🔗 0101 & 0011 -> 0001 (1)
bitwise_or = a | b  # 🚪 0101 | 0011 -> 0111 (7)
bitwise_xor = a ^ b  # ⚡ 0101 ^ 0011 -> 0110 (6)
bitwise_not = ~a  # 🚫 ~0101 -> 1010 (-6 in signed binary)
left_shift = a << 1  # ⬅️ 0101 << 1 -> 1010 (10)
right_shift = a >> 1  # ➡️ 0101 >> 1 -> 0010 (2)

print(bitwise_and, bitwise_or, bitwise_xor, bitwise_not, left_shift, right_shift)
```

---

### 🔍 6. Membership Operators

Membership operators test if a value is in a sequence or not.

- **`in` 👀:** Returns `True` if the value is found in the sequence.
  - **Example:** `3 in [1, 2, 3]` results in `True`.
  - **Use Case:** Checking if an item exists in a list or string.

- **`not in` 🚫👀:** Returns `True` if the value is not found in the sequence.
  - **Example:** `4 not in [1, 2, 3]` results in `True`.
  - **Use Case:** Validating absence of an item in a collection.

**Detailed Example:**

```python
lst = [1, 2, 3, 4, 5]

check_in = 3 in lst  # 👀 True
check_not_in = 6 not in lst  # 🚫👀 True

print(check_in, check_not_in)
```

---

### 🆔 7. Identity Operators

Identity operators compare memory locations of two objects.

- **`is` 👯:** Returns `True` if two variables point to the same object.
  - **Example:** `a is b` results in `True` if `a` and `b` reference the same object.
  - **Use Case:** Checking for singleton objects like `None`.

- **`is not` 🚫👯:** Returns `True` if two variables point to different objects.
  - **Example:** `a is not b` results in `True` if `a` and `b` reference different objects.
  - **Use Case:** Ensuring two objects are distinct.

**Detailed Example:**

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

identity_check = a is b  # 👯 False (Different objects)
identity_check_same = a is c  # 👯 True (Same object)
identity_check_not = a is not b  # 🚫👯 True (Different objects)

print(identity_check, identity_check_same, identity_check_not)
```

---

### 🎯 8. Operator Precedence

Operator precedence determines the order in which operations are evaluated.

**Order of Precedence (Highest to Lowest):**
1. **`**`** 🌟 (Exponent)
2. **`~ + -`** ➕➖ (Unary operators)
3. **`* / % //`** ✖️➗ (Multiplication, Division, Modulus, Floor Division)
4. **`+ -`** ➕➖ (Addition, Subtraction)
5. **`>> <<`** ➡️⬅️ (Right and Left Shifts)
6. **`&`** 🔗 (Bitwise AND)
7. **`^ |`** ⚡🚪 (Bitwise XOR, OR)
8. **`<= < > >=`** 📏 (Comparisons)
9. **`== !=`** ✅❌ (Equality)
10. **`= += -= *= /= %= **= //=`** 📝 (Assignments)
11. **`is is not`** 🆔 (Identity)
12. **`in not in`** 🔍 (Membership)
13. **`not or and`** 🚫🚪🤝 (Logical operations)

**Detailed Example:**

```python
# Example of precedence
result = 2 + 3 * 5 ** 2  # 🌟 Exponent first, then ✖️ Multiplication, then ➕ Addition
print(result)  # 2 + 3 * 25 -> 2 + 75 -> 77

# Example with logical and comparison operators
check = (5 > 3) and (10 != 2)
print(check)  # ✅ True and ✅ True -> True
```