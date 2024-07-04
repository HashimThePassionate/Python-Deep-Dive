### Portuguese Sorting Rules for Unicode Text

In Portuguese and many other languages that use the Latin alphabet, sorting rules are slightly different from simple alphabetical order. These rules account for diacritics (accents, cedillas, etc.), which typically do not affect the primary sorting order.

#### Key Points in Portuguese Sorting:

1. **Diacritics and Accents**:
    - Diacritics such as accents (e.g., acute, grave) and cedillas (ç) are generally ignored in the primary sorting order.
    - For example, "cajá" is sorted as "caja," and should come before "caju."

2. **Case Insensitivity**:
    - Sorting is usually case-insensitive, meaning 'A' and 'a' are treated the same.

3. **Character Order**:
    - The primary sorting order follows the basic Latin alphabet: A, B, C, ..., Z.
    - Characters with diacritics follow their base character: a, à, á, â, ã, ä.

### Example of Portuguese Sorting

Consider a list of Brazilian fruits:
```python
fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']
```

### Default Sorting in Python
By default, Python sorts these strings based on Unicode code points, which does not align with Portuguese sorting rules:
```python
sorted(fruits)
# Output: ['acerola', 'atemoia', 'açaí', 'caju', 'cajá']
```

### Desired Sorting According to Portuguese Rules
In Portuguese, the desired sorted order should be:
```python
['açaí', 'acerola', 'atemoia', 'cajá', 'caju']
```

Here’s how to achieve this:

1. **Set the Locale**:
    - Use `locale` module to set the Portuguese locale for sorting.

2. **Locale-aware Sorting**:
    - Use `locale.strxfrm` to transform strings for locale-aware comparisons.

### Code Example

#### Setting Up the Locale and Sorting:
```python
import locale

# Set locale to Brazilian Portuguese
my_locale = locale.setlocale(locale.LC_COLLATE, 'pt_BR.UTF-8')
print(my_locale)  # Output: 'pt_BR.UTF-8'

fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']
sorted_fruits = sorted(fruits, key=locale.strxfrm)
print(sorted_fruits)
# Output: ['açaí', 'acerola', 'atemoia', 'cajá', 'caju']
```

### Explanation

1. **Set Locale**:
    ```python
    my_locale = locale.setlocale(locale.LC_COLLATE, 'pt_BR.UTF-8')
    ```
    - This sets the locale to Brazilian Portuguese (`pt_BR.UTF-8`), ensuring that sorting follows Portuguese rules.

2. **Sort with `locale.strxfrm`**:
    ```python
    sorted_fruits = sorted(fruits, key=locale.strxfrm)
    ```
    - `locale.strxfrm` transforms each string into a format that respects the locale's sorting rules.

### Important Considerations

- **Global Locale Setting**:
    - `setlocale` affects the global state and should be set at the beginning of your program.

- **Locale Availability**:
    - Ensure the locale is installed on your operating system. Otherwise, `setlocale` will raise an error.

- **OS Support**:
    - Locale handling may vary across different operating systems. It works well on GNU/Linux but may have issues on macOS and Windows.

### Conclusion
Portuguese sorting rules ignore diacritics in primary sorting order and treat characters case-insensitively. Using the `locale` module in Python, you can achieve locale-aware sorting that aligns with these rules. This ensures that text is sorted correctly for Portuguese and other Latin-alphabet-based languages.