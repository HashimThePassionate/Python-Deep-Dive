# Positional-Only Parameters

## Introduction
Since Python 3.8, user-defined function signatures may specify positional-only parameters. This feature has always existed for built-in functions, such as `divmod(a, b)`, which can only be called with positional parameters and not as `divmod(a=10, b=4)`.

## Defining Positional-Only Parameters

To define a function requiring positional-only parameters, use `/` in the parameter list. All arguments to the left of the `/` are positional-only. After the `/`, you may specify other arguments, which work as usual.

### Example: Emulating `divmod` Function

The following example demonstrates how to define a function that mimics the behavior of the built-in `divmod` function:

```python
def divmod(a, b, /):
    return (a // b, a % b)

# Calling the divmod function with positional arguments
result = divmod(10, 3)
print(result)  # Output: (3, 1)
```

#### Explanation:

- **Positional-Only Parameters:**
  - In the function `divmod(a, b, /)`, both `a` and `b` are positional-only parameters.
  - This means the function can be called with positional arguments only, like `divmod(10, 3)`, but not with keyword arguments like `divmod(a=10, b=3)`.

- **Function Call:**
  - `divmod(10, 3)` calls the function with `a` as 10 and `b` as 3.

- **Calculations:**
  - `10 // 3` performs integer division, resulting in 3.
  - `10 % 3` performs the modulo operation, resulting in 1.

- **Return Value:**
  - The function returns a tuple `(3, 1)`, representing the quotient and the remainder.

### Example: Modifying the `tag` Function

Consider the `tag` function from a previous example. If we want the `name` parameter to be positional-only, we can add `/` after it in the function signature:

```python
def tag(name, /, *content, class_=None, **attrs):
    """Generate one or more HTML tags"""
    if class_ is not None:
        attrs['class'] = class_
    attr_pairs = (f' {attr}="{value}"' for attr, value in sorted(attrs.items()))
    attr_str = ''.join(attr_pairs)
    if content:
        elements = (f'<{name}{attr_str}>{c}</{name}>' for c in content)
        return '\n'.join(elements)
    else:
        return f'<{name}{attr_str} />'
```

#### Explanation:

- **Function Signature:**
  - `name` is a positional-only parameter, ensuring it can only be provided as a positional argument when calling the function.
  - Other parameters (`*content`, `class_=None`, and `**attrs`) work as usual.

### Example: Using the Modified `tag` Function

```python
>>> tag('br')
'<br />'

>>> tag('p', 'hello')
'<p>hello</p>'

>>> tag(name='p', content='hello')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: tag() got some positional-only arguments passed as keyword arguments: 'name'
```

#### Explanation:

1. **Positional Argument:**
   - `tag('br')` and `tag('p', 'hello')` are valid calls because `name` is provided as a positional argument.

2. **Keyword Argument:**
   - `tag(name='p', content='hello')` raises a `TypeError` because `name` is positional-only and cannot be provided as a keyword argument.

## Additional Resources

For more examples and detailed explanations of positional-only parameters, refer to:
- [What’s New In Python 3.8](https://docs.python.org/3/whatsnew/3.8.html)
- [PEP 570](https://www.python.org/dev/peps/pep-0570/)

## Conclusion

Positional-only parameters provide additional control over function signatures, ensuring certain arguments must be passed positionally. This feature enhances the flexibility and robustness of function definitions in Python.

Next, we will cover the most useful packages in the standard library for programming in a functional style.