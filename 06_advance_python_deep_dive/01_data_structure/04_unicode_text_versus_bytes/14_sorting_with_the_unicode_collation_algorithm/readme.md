### Sorting with the Unicode Collation Algorithm

James Tauber, a prolific Django contributor, created `pyuca`, a pure-Python implementation of the Unicode Collation Algorithm (UCA). This library makes it easy to sort Unicode text correctly across different platforms.

### Using `pyuca`

#### Installation
First, install the `pyuca` library using pip:
```sh
pip install pyuca
```

#### Example: Sorting Fruits
Here's how you can use `pyuca` to sort a list of Brazilian fruits:
```python
import pyuca

coll = pyuca.Collator()
fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']
sorted_fruits = sorted(fruits, key=coll.sort_key)
print(sorted_fruits)
# Output: ['açaí', 'acerola', 'atemoia', 'cajá', 'caju']
```

### Explanation
1. **Import and Initialize**:
    ```python
    import pyuca
    coll = pyuca.Collator()
    ```
    - Import the `pyuca` library and create a `Collator` object.

2. **Sorting**:
    ```python
    sorted_fruits = sorted(fruits, key=coll.sort_key)
    print(sorted_fruits)
    ```
    - Use the `sort_key` method of the `Collator` object as the sorting key to sort the list of fruits.

### Platform Compatibility
The `pyuca` library works on GNU/Linux, macOS, and Windows, making it a versatile solution for sorting Unicode text.

### Custom Collation Table
`pyuca` does not take the locale into account by default. If you need to customize the sorting order, you can provide a custom collation table to the `Collator` constructor. By default, it uses `allkeys.txt`, a copy of the Default Unicode Collation Element Table from Unicode.org.

### PyICU: An Alternative for Unicode Sorting
**Tech reviewer Miroslav Šedivý recommends using PyICU for more advanced Unicode sorting needs.**

#### Why PyICU?
- **Locale-Specific Sorting**:
    - `pyuca` has a single sorting algorithm that does not respect the sorting order of individual languages. For instance, in German, Ä is between A and B, while in Swedish, it comes after Z.
    - `PyICU` respects these language-specific sorting rules without changing the process's locale.

- **Case-Sensitive Sorting**:
    - `PyICU` is also needed for handling special cases like changing the case of `iİ/ıI` in Turkish.

- **Installation**:
    - `PyICU` includes an extension that must be compiled, which may make it harder to install on some systems compared to `pyuca`, which is pure Python.

#### Example with PyICU
```python
import icu

collator = icu.Collator.createInstance(icu.Locale('de_DE.UTF-8'))
fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']
sorted_fruits = sorted(fruits, key=collator.getSortKey)
print(sorted_fruits)
```

### Summary
- **`pyuca`**: A pure-Python library for Unicode sorting, easy to use and install, but does not support locale-specific sorting.
- **`PyICU`**: A more advanced library for Unicode sorting that respects locale-specific rules and handles special cases but requires more complex installation.

Using `pyuca` or `PyICU` ensures that your Unicode text is sorted correctly according to the Unicode Collation Algorithm or specific language rules, providing more accurate and expected sorting results.