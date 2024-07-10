# No Runtime Effect

## Introduction
Python type hints act as "documentation that can be verified by IDEs and type checkers." They do not impact the runtime behavior of Python programs.

### Key Points:
1. **Type Hints as Documentation**:
   - Type hints provide information about the expected types of variables and function signatures.
   - They can be checked by development tools but are not enforced during runtime.

2. **No Runtime Enforcement**:
   - Python does not enforce type hints at runtime.
   - Example 5-9 demonstrates this behavior.

## Example: No Runtime Enforcement

### Code Example:
```python
import typing

class Coordinate(typing.NamedTuple):
    lat: float
    lon: float

trash = Coordinate('Ni!', None)
print(trash)
```

### Output:
```plaintext
Coordinate(lat='Ni!', lon=None)
```
Even though the type hints suggest `lat` and `lon` should be `float`, the code runs without errors, creating a `Coordinate` with a string and `None`.

### Explanation:
- **None in Type Hints**:
  - In the context of type hints, `None` is not the `NoneType` singleton but an alias for `NoneType` itself.
  - This makes function return annotations easier to read for functions that return `None`.

### Demonstration:
- Typing the code into a Python module and running it produces:
  ```plaintext
  python main.py
  Coordinate(lat='Ni!', lon=None)
  ```

## Static Analysis Tools
- Type hints are mainly for third-party type checkers like Mypy or the PyCharm IDE built-in type checker.
- These tools perform static analysis, checking the source code without executing it.

### Example with Mypy:
```plaintext
$ mypy nocheck_demo.py
nocheck_demo.py:8: error: Argument 1 to "Coordinate" has incompatible type "str"; expected "float"
nocheck_demo.py:8: error: Argument 2 to "Coordinate" has incompatible type "None"; expected "float"
```
- Mypy identifies that both arguments for `Coordinate` should be `float`.
- The code assigns a `str` and `None`, leading to type errors detected by Mypy.

## Conclusion
Type hints improve code clarity and assist static analysis tools but have no runtime effect. For checking type hints, use tools like Mypy.