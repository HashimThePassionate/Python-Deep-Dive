# From Positional to Keyword-Only Parameters

## Introduction
Python functions offer an extremely flexible parameter handling mechanism. This flexibility is enhanced by the use of `*` and `**` to unpack iterables and mappings into separate arguments when calling a function. This section will explore these features with examples.

## Example 7-9: `tag` Function

The `tag` function generates HTML elements. It uses a keyword-only argument `class_` to pass "class" attributes, as `class` is a reserved keyword in Python.

### Implementation of `tag` Function

```python
def tag(name, *content, class_=None, **attrs):
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

### Explanation of `tag` Function

1. **Parameters:**
   - `name`: The name of the HTML tag.
   - `*content`: Captures any number of additional arguments as a tuple.
   - `class_`: A keyword-only argument for the "class" attribute.
   - `**attrs`: Captures additional keyword arguments as a dictionary.

2. **Handling the `class_` Argument:**
   - If `class_` is provided, it is added to the `attrs` dictionary with the key `'class'`.

3. **Building the Attribute String:**
   - `attr_pairs` generates the attribute key-value pairs.
   - `attr_str` joins these pairs into a single string.

4. **Generating HTML Elements:**
   - If `content` is provided, the function generates and returns multiple HTML elements.
   - If `content` is empty, the function returns a self-closing tag.

## Example 7-10: Using the `tag` Function

The `tag` function can be invoked in various ways, as shown below.

### Examples of Calling the `tag` Function

```python
>>> tag('br')
'<br />'

>>> tag('p', 'hello')
'<p>hello</p>'

>>> print(tag('p', 'hello', 'world'))
<p>hello</p>
<p>world</p>

>>> tag('p', 'hello', id=33)
'<p id="33">hello</p>'

>>> print(tag('p', 'hello', 'world', class_='sidebar'))
<p class="sidebar">hello</p>
<p class="sidebar">world</p>

>>> tag(content='testing', name="img")
'<img content="testing" />'

>>> my_tag = {'name': 'img', 'title': 'Sunset Boulevard', 'src': 'sunset.jpg', 'class': 'framed'}
>>> tag(**my_tag)
'<img class="framed" src="sunset.jpg" title="Sunset Boulevard" />'
```

### Explanation of the Examples

1. **Single Positional Argument:**
   - `tag('br')` generates a self-closing `<br />` tag.

2. **Positional Content Arguments:**
   - `tag('p', 'hello')` generates a `<p>hello</p>` tag.
   - `tag('p', 'hello', 'world')` generates two `<p>` tags:
     ```html
     <p>hello</p>
     <p>world</p>
     ```

3. **Keyword Arguments:**
   - `tag('p', 'hello', id=33)` generates a `<p id="33">hello</p>` tag.
   - `tag('p', 'hello', 'world', class_='sidebar')` generates two `<p>` tags with a class attribute:
     ```html
     <p class="sidebar">hello</p>
     <p class="sidebar">world</p>
     ```

4. **Keyword Argument as Positional:**
   - `tag(content='testing', name="img")` generates a self-closing `<img content="testing" />` tag.

5. **Unpacking a Dictionary:**
   - `tag(**my_tag)` unpacks the `my_tag` dictionary and generates a `<img>` tag with multiple attributes:
     ```html
     <img class="framed" src="sunset.jpg" title="Sunset Boulevard" />
     ```

## Keyword-Only Arguments

Keyword-only arguments are a feature of Python 3. In the `tag` function, the `class_` parameter is a keyword-only argument.

### Defining Keyword-Only Arguments

To specify keyword-only arguments, name them after the `*` argument. If you don't want to support variable positional arguments but still want keyword-only arguments, use `*` by itself in the signature.

### Example

```python
def f(a, *, b):
    return a, b

>>> f(1, b=2)
(1, 2)

>>> f(1, 2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: f() takes 1 positional argument but 2 were given
```

### Explanation of the Example

1. **Defining the Function:**
   - The function `f` is defined with one positional argument `a` and one keyword-only argument `b`.

2. **Calling with Keyword Argument:**
   - `f(1, b=2)` successfully calls the function and returns `(1, 2)`.

3. **Calling without Keyword Argument:**
   - `f(1, 2)` raises a `TypeError` because `b` must be provided as a keyword argument.

### Mandatory Keyword-Only Arguments
Keyword-only arguments do not need to have a default value; they can be mandatory, as shown in the example where `b` is required.

## Conclusion
Python's flexible parameter handling allows for versatile function definitions using positional, keyword, and keyword-only arguments. Understanding and utilizing these features can enhance the readability and functionality of your code.