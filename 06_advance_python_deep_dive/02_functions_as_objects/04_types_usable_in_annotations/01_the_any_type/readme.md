# The Any Type

## Introduction
The cornerstone of any gradual type system is the `Any` type, also known as the dynamic type. It plays a crucial role in type checking by allowing flexibility when the exact type is unknown or when multiple types are possible.

## Understanding `Any` Type

When a type checker sees an untyped function like this:
```python
def double(x):
    return x * 2
```
it assumes this:
```python
from typing import Any

def double(x: Any) -> Any:
    return x * 2
```
This means that the `x` argument and the return value can be of any type, including different types. `Any` is assumed to support every possible operation.

### Comparison with `object`

Contrast `Any` with `object`. Consider this function:
```python
def double(x: object) -> object:
    return x * 2
```
This function also accepts arguments of every type because every type is a subtype of `object`. However, a type checker will reject this function:
```python
def double(x: object) -> object:
    return x * 2
```
The problem is that `object` does not support the `__mul__` operation. Here is what Mypy reports:
```sh
$ mypy double_object.py
double_object.py:2: error: Unsupported operand types for * ("object" and "int")
Found 1 error in 1 file (checked 1 source file)
```

### General Types and Interfaces

More general types have narrower interfaces, meaning they support fewer operations. For example:
- The `object` class implements fewer operations than `abc.Sequence`.
- `abc.Sequence` implements fewer operations than `abc.MutableSequence`.
- `abc.MutableSequence` implements fewer operations than `list`.

But `Any` is a magic type that sits at the top and bottom of the type hierarchy. It’s simultaneously the most general type—so that an argument `n: Any` accepts values of every type—and the most specialized type, supporting every possible operation. At least, that’s how the type checker understands `Any`.

Using `Any` prevents the type checker from detecting potentially illegal operations before your program crashes with a runtime exception.

## Subtype-of vs. Consistent-with

Traditional object-oriented nominal type systems rely on the "is subtype-of" relationship. Given a class `T1` and a subclass `T2`, then `T2` is a subtype of `T1`.

### Example of Subtype-of

In simpler terms, if class `T2` inherits from class `T1`, then `T2` is considered a subtype of `T1`. This means that wherever a `T1` is expected, a `T2` can be used. Here's an example:

```python
class T1:
    def method(self):
        print("T1 method")

class T2(T1):
    def method(self):
        print("T2 method")

def f1(p: T1) -> None:
    p.method()

o2 = T2()
f1(o2)  # OK because T2 is a subtype of T1
```

Output:
```
T2 method
```

In this example:
- `T2` is a subclass of `T1`.
- The function `f1` expects a parameter of type `T1`.
- Since `T2` is a subtype of `T1`, you can pass an instance of `T2` to `f1`.

### Violation of LSP

Continuing from the previous code, this shows a violation of the Liskov Substitution Principle (LSP):
```python
def f2(p: T2) -> None:
    p.method()

o1 = T1()
f2(o1)  # Type error because T1 is not a subtype of T2
```

When you run Mypy on this code, you get the following error:
```sh
$ mypy main.py
main.py:21: error: Argument 1 to "f2" has incompatible type "T1"; expected "T2"  [arg-type]
Found 1 error in 1 file (checked 1 source file)
```

From the point of view of supported operations, this makes perfect sense: as a subclass, `T2` inherits and must support all operations that `T1` does. So an instance of `T2` can be used anywhere an instance of `T1` is expected. But the reverse is not necessarily true: `T2` may implement additional methods, so an instance of `T1` may not be used everywhere an instance of `T2` is expected. This focus on supported operations is reflected in the name "behavioral subtyping," also used to refer to the LSP.

### Consistent-with Relationship

In a gradual type system, there is another relationship: "consistent-with," which applies wherever "subtype-of" applies, with special provisions for type `Any`.

The rules for "consistent-with" are:
1. Given `T1` and a subtype `T2`, then `T2` is consistent with `T1` (Liskov substitution).
2. Every type is consistent with `Any`: you can pass objects of every type to an argument declared of type `Any`.
3. `Any` is consistent with every type: you can always pass an object of type `Any` where an argument of another type is expected.

### Example of Consistent-with

Considering the previous definitions of the objects `o1` and `o2`, here are examples of valid code, illustrating rules #2 and #3:
```python
from typing import Any

def f3(p: Any) -> None:
    print(p)

o0 = object()
o1 = T1()
o2 = T2()
f3(o0)  # OK: rule #2
f3(o1)  # OK: rule #2
f3(o2)  # OK: rule #2

def f4() -> Any:  # implicit return type: `Any`
    return "example"

o4 = f4()  # inferred type: `Any`
f3(o4)  # OK: rule #3
```

Output:
```
<object object at 0x7f96b80c0b20>
<__main__.T1 object at 0x7f96b80c0b50>
<__main__.T2 object at 0x7f96b80c0b80>
example
```

If you try to call `f1(o4)` or `f2(o4)`, they will raise errors at runtime because the inferred type `Any` does not guarantee the presence of the required methods:

```python
f1(o4)  # Raises AttributeError at runtime
f2(o4)  # Raises AttributeError at runtime
```

Error:
```sh
Traceback (most recent call last):
  File "main.py", line 39, in <module>
    f1(o4)  # Raises AttributeError at runtime
  File "main.py", line 12, in f1
    p.method()
AttributeError: 'str' object has no attribute 'method'
```

### Why Does This Happen?

When you use `Any` in your type annotations, it tells the type checker to accept any type for that variable or function argument. This provides a lot of flexibility, but it also means the type checker cannot verify if the actual object passed at runtime has the methods or properties you expect.

In the example above:
- `f1` expects an object of type `T1`, which has a `method` method.
- `f2` expects an object of type `T2`, which also has a `method` method.

However, `f4` returns a value of type `Any`, which means the type checker does not enforce what specific type `o4` will be. In this case, `f4` returns a string (`"example"`). When you try to pass this string to `f1` or `f2`, it results in a runtime error because the string type does not have a `method` method.

Every gradual type system needs a wildcard type like `Any`.

The verb "to infer" is a fancy synonym for "to guess," used in the context of type analysis. Modern type checkers in Python and other languages don’t require type annotations everywhere because they can infer the type of many expressions. For example, if I write `x = len(s) * 10`, the type checker doesn’t need an explicit local declaration to know that `x` is an `int`, as long as it can find type hints for the `len` built-in.

Now we can explore the rest of the types used in annotations.