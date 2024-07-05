# Numeric Meaning of Characters

This README explains the code used to demonstrate the numerical character metadata available in the Unicode database. The script uses Python's `unicodedata` module and other string methods to analyze various Unicode characters.

## Overview

The script checks whether each character in a sample string is a digit or numeric and retrieves its numeric value and name. The output is formatted to display these properties in a readable table.

### Requirements

- Python 3.x
- `unicodedata` module (standard library)
- `re` module (standard library)

### Script Details

The script `numerics_demo.py` performs the following steps:

1. Imports the necessary modules.
2. Defines a regular expression to match digits.
3. Creates a sample string containing various Unicode characters.
4. Iterates through each character in the sample string and checks its properties.
5. Prints the results in a formatted table.

### Code Explanation

#### Import Modules

```python
import unicodedata
import re
```
- `unicodedata`: Provides access to the Unicode Character Database.
- `re`: Regular expression operations.

#### Define Regular Expression

```python
re_digit = re.compile(r'\d')
```
- `re.compile(r'\d')`: Compiles a regular expression pattern to match digits.

#### Sample String

```python
sample = '1\xbc\xb2\u0969\u136b\u216b\u2466\u2480\u3285'
```
- `sample`: This string contains various Unicode characters represented by escape sequences. Each sequence represents a specific character.

#### Iterate and Analyze Characters

```python
for char in sample:
    print(f'U+{ord(char):04x}',
          char.center(6),
          're_dig' if re_digit.match(char) else '-',
          'isdig' if char.isdigit() else '-',
          'isnum' if char.isnumeric() else '-',
          f'{unicodedata.numeric(char):5.2f}',
          unicodedata.name(char),
          sep='\t')
```

Let's break down this part of the code:

1. **Loop Through Each Character in the Sample String**

   ```python
   for char in sample:
   ```

   - This loop goes through each character in the `sample` string one by one.

2. **Getting the Unicode Code Point of the Character**

   ```python
   f'U+{ord(char):04x}'
   ```

   - `ord(char)`: Returns the Unicode code point of the character `char`.
   - `:04x`: Formats the code point as a four-digit hexadecimal number.
   - Example: For the character `'1'`, `ord('1')` returns `49`, and `f'U+{49:04x}'` results in `U+0031`.

3. **Centering the Character**

   ```python
   char.center(6)
   ```

   - `char.center(6)`: Centers the character in a string of length 6.
   - Example: `'1'.center(6)` results in `'  1   '`.

4. **Checking if the Character Matches the Digit Pattern**

   ```python
   're_dig' if re_digit.match(char) else '-'
   ```

   - `re_digit.match(char)`: Checks if the character matches the digit pattern `\d`.
   - If the character matches, it prints `'re_dig'`; otherwise, it prints `'-'`.
   - Example: For the character `'1'`, it matches the pattern, so it prints `'re_dig'`.

5. **Checking if the Character is a Digit**

   ```python
   'isdig' if char.isdigit() else '-'
   ```

   - `char.isdigit()`: Checks if the character is a digit.
   - If the character is a digit, it prints `'isdig'`; otherwise, it prints `'-'`.
   - Example: For the character `'1'`, it is a digit, so it prints `'isdig'`.

6. **Checking if the Character is Numeric**

   ```python
   'isnum' if char.isnumeric() else '-'
   ```

   - `char.isnumeric()`: Checks if the character is numeric.
   - If the character is numeric, it prints `'isnum'`; otherwise, it prints `'-'`.
   - Example: For the character `'1'`, it is numeric, so it prints `'isnum'`.

7. **Getting the Numeric Value of the Character**

   ```python
   f'{unicodedata.numeric(char):5.2f}'
   ```

   - `unicodedata.numeric(char)`: Gets the numeric value of the character.
   - `:5.2f`: Formats the number to have a width of 5 and 2 decimal places.
   - Example: For the character `'1'`, `unicodedata.numeric('1')` returns `1.0`, and `f'{1.0:5.2f}'` results in `' 1.00'`.

8. **Getting the Name of the Character**

   ```python
   unicodedata.name(char)
   ```

   - `unicodedata.name(char)`: Gets the name of the character.
   - Example: For the character `'1'`, `unicodedata.name('1')` returns `"DIGIT ONE"`.

9. **Using Tab as Separator**

   ```python
   sep='\t'
   ```

   - `sep='\t'`: Sets the separator between the printed values to a tab character.
   - This makes the output easier to read in a tabular format.

### Detailed Explanation for Each Character in the Sample String

#### Character `'1'`
- **Unicode Code Point**: `ord('1')` returns `49`.
- **Formatted Code Point**: `f'U+{49:04x}'` results in `U+0031`.
- **Centered Character**: `'1'.center(6)` results in `'  1   '`.
- **Regex Match**: `'re_dig' if re_digit.match('1') else '-'` results in `'re_dig'`.
- **Digit Check**: `'isdig' if '1'.isdigit() else '-'` results in `'isdig'`.
- **Numeric Check**: `'isnum' if '1'.isnumeric() else '-'` results in `'isnum'`.
- **Numeric Value**: `unicodedata.numeric('1')` returns `1.0`, formatted as `f'{1.0:5.2f}'` results in `' 1.00'`.
- **Character Name**: `unicodedata.name('1')` returns `"DIGIT ONE"`.

Output:
```plaintext
U+0031   1     re_dig  isdig   isnum  1.00  DIGIT ONE
```

#### Character `'\xbc'` (¼)
- **Unicode Code Point**: `ord('\xbc')` returns `188`.
- **Formatted Code Point**: `f'U+{188:04x}'` results in `U+00bc`.
- **Centered Character**: `'\xbc'.center(6)` results in `'  ¼   '`.
- **Regex Match**: `'re_dig' if re_digit.match('\xbc') else '-'` results in `'-'`.
- **Digit Check**: `'isdig' if '\xbc'.isdigit() else '-'` results in `'-'`.
- **Numeric Check**: `'isnum' if '\xbc'.isnumeric() else '-'` results in `'isnum'`.
- **Numeric Value**: `unicodedata.numeric('\xbc')` returns `0.25`, formatted as `f'{0.25:5.2f}'` results in `' 0.25'`.
- **Character Name**: `unicodedata.name('\xbc')` returns `"VULGAR FRACTION ONE QUARTER"`.

Output:
```plaintext
U+00bc   ¼     -       -       isnum  0.25  VULGAR FRACTION ONE QUARTER
```

#### Character `'\xb2'` (²)
- **Unicode Code Point**: `ord('\xb2')` returns `178`.
- **Formatted Code Point**: `f'U+{178:04x}'` results in `U+00b2`.
- **Centered Character**: `'\xb2'.center(6)` results in `'  ²   '`.
- **Regex Match**: `'re_dig' if re_digit.match('\xb2') else '-'` results in `'-'`.
- **Digit Check**: `'isdig' if '\xb2'.isdigit() else '-'` results in `'isdig'`.
- **Numeric Check**: `'isnum' if '\xb2'.isnumeric() else '-'` results in `'isnum'`.
- **Numeric Value**: `unicodedata.numeric('\xb2')` returns `2.0`, formatted as `f'{2.0:5.2f}'` results in `' 2.00'`.
- **Character Name**: `unicodedata.name('\xb2')` returns `"SUPERSCRIPT TWO"`.

Output:
```plaintext
U+00b2   ²     -       isdig   isnum  2.00  SUPERSCRIPT TWO
```

#### Character `'\u0969'` (३)
- **Unicode Code Point**: `ord('\u0969')` returns `2409`.
- **Formatted Code Point**: `f'U+{2409:04x}'` results in `U+0969`.
- **Centered Character**: `'\

u0969'.center(6)` results in `' ३   '`.
- **Regex Match**: `'re_dig' if re_digit.match('\u0969') else '-'` results in `'re_dig'`.
- **Digit Check**: `'isdig' if '\u0969'.isdigit() else '-'` results in `'isdig'`.
- **Numeric Check**: `'isnum' if '\u0969'.isnumeric() else '-'` results in `'isnum'`.
- **Numeric Value**: `unicodedata.numeric('\u0969')` returns `3.0`, formatted as `f'{3.0:5.2f}'` results in `' 3.00'`.
- **Character Name**: `unicodedata.name('\u0969')` returns `"DEVANAGARI DIGIT THREE"`.

Output:
```plaintext
U+0969   ३     re_dig  isdig   isnum  3.00  DEVANAGARI DIGIT THREE
```

#### Character `'\u136b'` (፫)
- **Unicode Code Point**: `ord('\u136b')` returns `4971`.
- **Formatted Code Point**: `f'U+{4971:04x}'` results in `U+136b`.
- **Centered Character**: `'\u136b'.center(6)` results in `' ፫   '`.
- **Regex Match**: `'re_dig' if re_digit.match('\u136b') else '-'` results in `'-'`.
- **Digit Check**: `'isdig' if '\u136b'.isdigit() else '-'` results in `'isdig'`.
- **Numeric Check**: `'isnum' if '\u136b'.isnumeric() else '-'` results in `'isnum'`.
- **Numeric Value**: `unicodedata.numeric('\u136b')` returns `3.0`, formatted as `f'{3.0:5.2f}'` results in `' 3.00'`.
- **Character Name**: `unicodedata.name('\u136b')` returns `"ETHIOPIC DIGIT THREE"`.

Output:
```plaintext
U+136b   ፫     -       isdig   isnum  3.00  ETHIOPIC DIGIT THREE
```

#### Character `'\u216b'` (Ⅻ)
- **Unicode Code Point**: `ord('\u216b')` returns `8555`.
- **Formatted Code Point**: `f'U+{8555:04x}'` results in `U+216b`.
- **Centered Character**: `'\u216b'.center(6)` results in `' Ⅻ   '`.
- **Regex Match**: `'re_dig' if re_digit.match('\u216b') else '-'` results in `'-'`.
- **Digit Check**: `'isdig' if '\u216b'.isdigit() else '-'` results in `'-'`.
- **Numeric Check**: `'isnum' if '\u216b'.isnumeric() else '-'` results in `'isnum'`.
- **Numeric Value**: `unicodedata.numeric('\u216b')` returns `12.0`, formatted as `f'{12.0:5.2f}'` results in `'12.00'`.
- **Character Name**: `unicodedata.name('\u216b')` returns `"ROMAN NUMERAL TWELVE"`.

Output:
```plaintext
U+216b   Ⅻ     -       -       isnum 12.00  ROMAN NUMERAL TWELVE
```

#### Character `'\u2466'` (⑦)
- **Unicode Code Point**: `ord('\u2466')` returns `9318`.
- **Formatted Code Point**: `f'U+{9318:04x}'` results in `U+2466`.
- **Centered Character**: `'\u2466'.center(6)` results in `' ⑦   '`.
- **Regex Match**: `'re_dig' if re_digit.match('\u2466') else '-'` results in `'-'`.
- **Digit Check**: `'isdig' if '\u2466'.isdigit() else '-'` results in `'isdig'`.
- **Numeric Check**: `'isnum' if '\u2466'.isnumeric() else '-'` results in `'isnum'`.
- **Numeric Value**: `unicodedata.numeric('\u2466')` returns `7.0`, formatted as `f'{7.0:5.2f}'` results in `' 7.00'`.
- **Character Name**: `unicodedata.name('\u2466')` returns `"CIRCLED DIGIT SEVEN"`.

Output:
```plaintext
U+2466   ⑦     -       isdig   isnum  7.00  CIRCLED DIGIT SEVEN
```

#### Character `'\u2480'` (⒀)
- **Unicode Code Point**: `ord('\u2480')` returns `9344`.
- **Formatted Code Point**: `f'U+{9344:04x}'` results in `U+2480`.
- **Centered Character**: `'\u2480'.center(6)` results in `' ⒀   '`.
- **Regex Match**: `'re_dig' if re_digit.match('\u2480') else '-'` results in `'-'`.
- **Digit Check**: `'isdig' if '\u2480'.isdigit() else '-'` results in `'-'`.
- **Numeric Check**: `'isnum' if '\u2480'.isnumeric() else '-'` results in `'isnum'`.
- **Numeric Value**: `unicodedata.numeric('\u2480')` returns `13.0`, formatted as `f'{13.0:5.2f}'` results in `'13.00'`.
- **Character Name**: `unicodedata.name('\u2480')` returns `"PARENTHESIZED NUMBER THIRTEEN"`.

Output:
```plaintext
U+2480   ⒀     -       -       isnum 13.00  PARENTHESIZED NUMBER THIRTEEN
```

#### Character `'\u3285'` (㊅)
- **Unicode Code Point**: `ord('\u3285')` returns `12933`.
- **Formatted Code Point**: `f'U+{12933:04x}'` results in `U+3285`.
- **Centered Character**: `'\u3285'.center(6)` results in `' ㊅   '`.
- **Regex Match**: `'re_dig' if re_digit.match('\u3285') else '-'` results in `'-'`.
- **Digit Check**: `'isdig' if '\u3285'.isdigit() else '-'` results in `'-'`.
- **Numeric Check**: `'isnum' if '\u3285'.isnumeric() else '-'` results in `'isnum'`.
- **Numeric Value**: `unicodedata.numeric('\u3285')` returns `6.0`, formatted as `f'{6.0:5.2f}'` results in `' 6.00'`.
- **Character Name**: `unicodedata.name('\u3285')` returns `"CIRCLED IDEOGRAPH SIX"`.

Output:
```plaintext
U+3285   ㊅     -       -       isnum  6.00  CIRCLED IDEOGRAPH SIX
```

### Summary

- Each character in the sample string is processed using the `ord()` function to obtain its Unicode code point.
- The code point is then formatted as a four-digit hexadecimal number using `:04x`.
- The script centers each character in a string of length 6, checks if it matches the regex pattern for digits, if it is a digit, if it is numeric, retrieves its numeric value, and gets its Unicode name.
- The results are printed in a tabular format with columns for the code point, character, regex match status, digit status, numeric status, numeric value, and character name.

### Example Output

When you run the script, it prints a table like this:

```plaintext
U+0031   1     re_dig  isdig   isnum  1.00  DIGIT ONE
U+00bc   ¼     -       -       isnum  0.25  VULGAR FRACTION ONE QUARTER
U+00b2   ²     -       isdig   isnum  2.00  SUPERSCRIPT TWO
U+0969   ३     re_dig  isdig   isnum  3.00  DEVANAGARI DIGIT THREE
U+136b   ፫     -       isdig   isnum  3.00  ETHIOPIC DIGIT THREE
U+216b   Ⅻ     -       -       isnum 12.00  ROMAN NUMERAL TWELVE
U+2466   ⑦     -       isdig   isnum  7.00  CIRCLED DIGIT SEVEN
U+2480   ⒀     -       -       isnum 13.00  PARENTHESIZED NUMBER THIRTEEN
U+3285   ㊅     -       -       isnum  6.00  CIRCLED IDEOGRAPH SIX
```

### Conclusion
This script demonstrates how to use the Unicode database to obtain numerical and descriptive metadata for various characters. Understanding these methods and the data they provide can be very useful in applications that need to handle a wide range of Unicode characters, such as text editors, spreadsheets, and more.

**Unicode Conversion**:
[Unicode Conversion](https://r12a.github.io/app-conversion/)