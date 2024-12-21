### 📄 Problem 2.1

Create a regular expression to exactly match this gloriously contrived sentence:

```
The punctuation characters in the ASCII table are: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~.
```

### 📝 Answer

```python
import re

# The given sentence
sentence = r'The punctuation characters in the ASCII table are: !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~.'

# Regular expression to exactly match the sentence
regex = r'^The punctuation characters in the ASCII table are: [!"#$%&\'()*+,-./:;<=>?@[\\\]^_`{|}~.]+$'

# Check if the sentence matches the regular expression
match = re.match(regex, sentence)

if match:
    print("The sentence matches the regular expression.")
else:
    print("The sentence does not match the regular expression.")
```

### 📚 Detailed Explanation

#### 🔍 Understanding the Sentence:

The sentence to match is:

```
The punctuation characters in the ASCII table are: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~.
```

This sentence includes a string of punctuation characters from the ASCII table.

#### 🛠️ Constructing the Regular Expression:

- `^`: Asserts the position at the start of the string.
- `The punctuation characters in the ASCII table are: `: Matches the exact literal string.
- `[!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~.]+`: Matches one or more of any of the listed punctuation characters. Note the following:
  - `\\`: Escapes the backslash character.
  - `^` and `[` are inside the character class and do not need to be escaped.
- `$`: Asserts the position at the end of the string.

Combined, this regular expression ensures that the entire string exactly matches the given sentence, including all punctuation characters and spacing.

#### 🧪 Matching the Sentence:

The `re.match` function is used to check if the entire string matches the regular expression from the start to the end. If it matches, the function returns a match object; otherwise, it returns `None`.

#### 🖥️ Code Execution:

- The given sentence is defined using a raw string (using `r'...'`) to handle the backslashes correctly.
- The regular expression is applied to the sentence.
- The result is printed based on whether the sentence matches the regular expression.

By following these steps, we ensure that the regular expression matches the exact sentence, including all punctuation characters.
---
### 📄 Problem 2.2

Match a string of the following ASCII control characters: bell, escape, form feed, line feed, carriage return, horizontal tab, vertical tab. These characters have the hexadecimal ASCII codes 07, 1B, 0C, 0A, 0D, 09, 0B.

### 📝 Answer

```python
import re

# The regular expression pattern to match the specified control characters
pattern = r'^[\x07\x1B\x0C\x0A\x0D\x09\x0B]+$'

# Examples of strings containing only the specified control characters
test_string_1 = '\x07\x1B\x0C\x0A'
test_string_2 = '\x0D\x09\x0B'

# Example of a string that should not match
test_string_invalid = 'Hello\x07World'

# Check if the strings match the pattern
match_1 = re.match(pattern, test_string_1)
match_2 = re.match(pattern, test_string_2)
match_invalid = re.match(pattern, test_string_invalid)

print("test_string_1 matches:", bool(match_1))  # Expected output: True
print("test_string_2 matches:", bool(match_2))  # Expected output: True
print("test_string_invalid matches:", bool(match_invalid))  # Expected output: False
```

### 📚 Detailed Explanation

#### 🔍 Understanding the Control Characters:

The ASCII control characters to match are:
- Bell (`\x07`)
- Escape (`\x1B`)
- Form Feed (`\x0C`)
- Line Feed (`\x0A`)
- Carriage Return (`\x0D`)
- Horizontal Tab (`\x09`)
- Vertical Tab (`\x0B`)

Each of these characters has a corresponding hexadecimal code which is used in the regular expression.

#### 🛠️ Constructing the Regular Expression:

- `^`: Asserts the position at the start of the string.
- `[\x07\x1B\x0C\x0A\x0D\x09\x0B]+`: Matches one or more of any of the specified control characters.
- `$`: Asserts the position at the end of the string.

Combined, this regular expression ensures that the entire string consists of only the specified control characters.

#### 🧪 Matching the Strings:

The `re.match` function is used to check if the entire string matches the regular expression from the start to the end. If it matches, the function returns a match object; otherwise, it returns `None`.

#### 🖥️ Code Execution:

- The `test_string_1` and `test_string_2` examples are strings containing only the specified control characters and should match the pattern.
- The `test_string_invalid` example contains additional characters and should not match the pattern.

By following these steps, we ensure that the regular expression matches strings consisting solely of the specified ASCII control characters.
