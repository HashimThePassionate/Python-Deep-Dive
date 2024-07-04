### Utility Functions for Normalized Text Matching

As we’ve seen, NFC and NFD are safe to use and allow sensible comparisons between Unicode strings. NFC is the best normalized form for most applications. `str.casefold()` is the way to go for case-insensitive comparisons.

If you work with text in many languages, a pair of functions like `nfc_equal` and `fold_equal` are useful additions to your toolbox.

### Example: normeq.py - Normalized Unicode String Comparison

#### Utility Functions for Normalized Unicode String Comparison
Using Normal Form C, case sensitive:
```python
s1 = 'café'
s2 = 'cafe\u0301'
print(s1 == s2)  # Output: False
print(nfc_equal(s1, s2))  # Output: True

print(nfc_equal('A', 'a'))  # Output: False
```

Using Normal Form C with case folding:
```python
s3 = 'Straße'
s4 = 'strasse'
print(s3 == s4)  # Output: False
print(nfc_equal(s3, s4))  # Output: False
print(fold_equal(s3, s4))  # Output: True

print(fold_equal(s1, s2))  # Output: True
print(fold_equal('A', 'a'))  # Output: True
```

#### Code Explanation
```python
from unicodedata import normalize

def nfc_equal(str1, str2):
    """
    Compare two strings using Normal Form C (NFC).
    This ensures that equivalent characters are treated as equal.
    """
    return normalize('NFC', str1) == normalize('NFC', str2)

def fold_equal(str1, str2):
    """
    Compare two strings using Normal Form C (NFC) with case folding.
    This ensures that equivalent characters are treated as equal,
    ignoring case differences.
    """
    return (normalize('NFC', str1).casefold() == normalize('NFC', str2).casefold())
```

### Why Use These Functions?

- **NFC (Normalization Form C)**: Combines characters to produce the shortest equivalent string. It is best for most applications.
- **Case Folding**: Makes case-insensitive comparisons easier by converting all text to a uniform case (usually lowercase).

### Practical Use Cases

1. **Case-Sensitive Comparison with NFC**:
    - Use `nfc_equal` to compare strings where case sensitivity is important but you want to treat composed characters the same as decomposed ones.

2. **Case-Insensitive Comparison with NFC**:
    - Use `fold_equal` to compare strings where case differences should be ignored.

#### Example Scenarios:
- Comparing user input to stored data in a case-insensitive manner.
- Ensuring consistent comparisons in multi-language applications.

### Conclusion

These utility functions enhance your ability to handle Unicode text comparisons effectively, ensuring that your applications can handle text from various languages and character encodings reliably.

In the next sections, we will explore when and how to apply deeper transformations, like changing 'café' into 'cafe'.