### Case Folding

Case folding is a way of converting all text to lowercase, with some additional changes. In Python, this is done using the `str.casefold()` method.

#### What is Case Folding?

- **Case Folding**: It is similar to converting text to lowercase, but with extra transformations.
- **str.casefold()**: A method in Python that performs case folding on strings.

#### Differences from Lowercasing

For most Latin-1 characters, `s.casefold()` gives the same result as `s.lower()`, except for two special cases:
1. **Micro Sign (µ)**:
   - The micro sign 'µ' is changed to the Greek lowercase mu 'μ'.
2. **German Eszett (ß)**:
   - The German Eszett or "sharp s" (ß) becomes "ss".

#### Examples:

1. **Micro Sign (µ)**:
   ```python
   from unicodedata import name

   micro = 'µ'
   print(name(micro))  # Output: 'MICRO SIGN'
   
   micro_cf = micro.casefold()
   print(name(micro_cf))  # Output: 'GREEK SMALL LETTER MU'
   
   print(micro, micro_cf)  # Output: ('µ', 'μ')
   ```

2. **German Eszett (ß)**:
   ```python
   from unicodedata import name

   eszett = 'ß'
   print(name(eszett))  # Output: 'LATIN SMALL LETTER SHARP S'
   
   eszett_cf = eszett.casefold()
   print(eszett, eszett_cf)  # Output: ('ß', 'ss')
   ```

There are nearly 300 characters for which `str.casefold()` and `str.lower()` return different results. 

#### Why is Case Folding Important?

- **Linguistic Special Cases**: Unicode includes many special cases due to different languages.
- **Python's Effort**: The Python core team has made significant efforts to handle these special cases effectively.

#### Conclusion

Case folding helps in normalizing text for comparisons and searching, ensuring that different representations of characters are treated uniformly.

In the next sections, we will use our normalization knowledge to develop utility functions.