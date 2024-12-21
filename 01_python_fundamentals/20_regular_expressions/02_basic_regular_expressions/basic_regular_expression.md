### 📄 Problem 2.1 Match literel text

Create a regular expression to exactly match this gloriously contrived sentence:

The punctuation characters in the ASCII table are: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~.


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

The punctuation characters in the ASCII table are: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~.


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
### 📄 Problem 2.2 Match nonprintable charachters

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

By following these steps, we ensure that the regular expression matches strings consisting solely of the specified
ASCII control characters.
---
### 📄 Problem 2.3 Match one of many charachters

1. Create a regular expression to match all common misspellings of "calendar", allowing an "a" or "e" to be used in each of the vowel positions.
2. Create another regular expression to match a single hexadecimal character.
3. Create a third regex to match a single character that is not a hexadecimal character.

### 📝 Answer

```python
import re

# Regular expression to match all common misspellings of "calendar"
regex_calendar = r'c[ae]l[ae]nd[ae]r'

# Regular expression to match a single hexadecimal character
regex_hexadecimal = r'[0-9a-fA-F]'

# Regular expression to match a single character that is not a hexadecimal character
regex_not_hexadecimal = r'[^0-9a-fA-F]'

# Test strings
test_string_calendar = "calender, calendr, celendar, celendr"
test_string_hexadecimal = "123abcDEF"
test_string_not_hexadecimal = "123xyzXYZ!@#"

# Find all matches for common misspellings of "calendar"
matches_calendar = re.findall(regex_calendar, test_string_calendar)
print("Matches for common misspellings of 'calendar':", matches_calendar)

# Find all matches for a single hexadecimal character
matches_hexadecimal = re.findall(regex_hexadecimal, test_string_hexadecimal)
print("Matches for a single hexadecimal character:", matches_hexadecimal)

# Find all matches for a single character that is not a hexadecimal character
matches_not_hexadecimal = re.findall(regex_not_hexadecimal, test_string_not_hexadecimal)
print("Matches for a single character that is not a hexadecimal character:", matches_not_hexadecimal)
```

### 📚 Detailed Explanation

#### 🔍 Understanding the Regular Expressions:

1. **Common Misspellings of "Calendar":**
   - The word "calendar" can be misspelled by substituting "a" or "e" in each vowel position.
   - Regular expression: `c[ae]l[ae]nd[ae]r`
     - `c`: Matches the literal character "c".
     - `[ae]`: Matches either "a" or "e".
     - `l`: Matches the literal character "l".
     - `[ae]`: Matches either "a" or "e".
     - `nd`: Matches the literal characters "nd".
     - `[ae]`: Matches either "a" or "e".
     - `r`: Matches the literal character "r".

2. **Single Hexadecimal Character:**
   - A hexadecimal character can be a digit from 0 to 9 or a letter from a to f (case insensitive).
   - Regular expression: `[0-9a-fA-F]`
     - `[0-9]`: Matches any digit from 0 to 9.
     - `[a-fA-F]`: Matches any letter from a to f (case insensitive).

3. **Single Character That Is Not a Hexadecimal Character:**
   - This matches any character that is not a hexadecimal character.
   - Regular expression: `[^0-9a-fA-F]`
     - `[^0-9a-fA-F]`: Matches any character except those specified (0-9, a-f, A-F).

#### 🧪 Matching the Strings:

- The `re.findall` function is used to find all occurrences of the patterns in the given test strings.

#### 🖥️ Code Execution:

- The `test_string_calendar` contains various misspellings of "calendar".
- The `test_string_hexadecimal` contains a mix of hexadecimal characters.
- The `test_string_not_hexadecimal` includes characters that are not hexadecimal.

By following these steps, we ensure that the regular expressions match their respective patterns correctly.
---
### 📄 Problem 2.4 Match any characters
1. Create a regular expression to match a quoted character, allowing any single character, except a line break, between the quotes.
2. Create another regular expression to match a quoted character, truly allowing any character, including line breaks, between the quotes.

### 📝 Answer

```python
import re

# Regular expression to match a quoted character, allowing any single character except a line break
regex_any_single_character = r'"[^"\n]"'

# Regular expression to match a quoted character, truly allowing any character including line breaks
regex_any_character = r'"(.|\n)"'

# Test strings
test_string_any_single_character = '"a" "b" "1" "!" "\\\\"'
test_string_any_character = '"a" "b" "1" "!" "\\\\" "line\nbreak"'

# Find all matches for any single character except a line break
matches_any_single_character = re.findall(regex_any_single_character, test_string_any_single_character)
print("Matches for any single character except a line break:", matches_any_single_character)

# Find all matches for any character including line breaks
matches_any_character = re.findall(regex_any_character, test_string_any_character)
print("Matches for any character including line breaks:", matches_any_character)
```

### 📚 Detailed Explanation

#### 🔍 Understanding the Regular Expressions:

1. **Match a Quoted Character (Single Character, No Line Breaks):**
   - Regular expression: `r'"[^"\n]"'
     - `"`: Matches the literal double quote character.
     - `[^"\n]`: Matches any single character except a double quote or a line break.
     - `"`: Matches the literal double quote character again.
   - This pattern ensures that any single character enclosed in double quotes is matched, except for line breaks and double quotes.

2. **Match a Quoted Character (Any Character, Including Line Breaks):**
   - Regular expression: `r'"(.|\n)"'
     - `"`: Matches the literal double quote character.
     - `(.|\n)`: Matches any single character or a line break.
     - `"`: Matches the literal double quote character again.
   - This pattern ensures that any character, including line breaks, enclosed in double quotes is matched.

#### 🧪 Matching the Strings:

- The `re.findall` function is used to find all occurrences of the patterns in the given test strings.

#### 🖥️ Code Execution:

- The `test_string_any_single_character` contains various quoted single characters that do not include line breaks.
- The `test_string_any_character` includes examples of quoted characters and a quoted string with a line break.

By following these steps, we ensure that the regular expressions match their respective patterns correctly.
---
### 📄 Problem 2.5 Match something at start/end of line

1. Create a regular expression to match the word "alpha", but only if it occurs at the very beginning of the subject text.
2. Create a regular expression to match the word "omega", but only if it occurs at the very end of the subject text.
3. Create a regular expression to match the word "begin", but only if it occurs at the beginning of a line.
4. Create a regular expression to match the word "end", but only if it occurs at the end of a line.

### 📝 Answer

```python
import re

# Regular expression to match the word "alpha" at the very beginning of the subject text
regex_alpha_beginning = r'^alpha'

# Regular expression to match the word "omega" at the very end of the subject text
regex_omega_end = r'omega$'

# Regular expression to match the word "begin" at the beginning of a line
regex_begin_line = r'^begin'

# Regular expression to match the word "end" at the end of a line
regex_end_line = r'end$'

# Test strings
test_string_alpha_beginning = "alpha is the first letter of the Greek alphabet."
test_string_omega_end = "The last letter of the Greek alphabet is omega"
test_string_begin_line = "begin with the first step\nthen continue"
test_string_end_line = "This is the end\nof the line"

# Find matches for "alpha" at the beginning of the subject text
match_alpha_beginning = re.match(regex_alpha_beginning, test_string_alpha_beginning)
print("Match for 'alpha' at the beginning of the subject text:", bool(match_alpha_beginning))

# Find matches for "omega" at the end of the subject text
match_omega_end = re.search(regex_omega_end, test_string_omega_end)
print("Match for 'omega' at the end of the subject text:", bool(match_omega_end))

# Find matches for "begin" at the beginning of a line
matches_begin_line = re.findall(regex_begin_line, test_string_begin_line, re.MULTILINE)
print("Matches for 'begin' at the beginning of a line:", matches_begin_line)

# Find matches for "end" at the end of a line
matches_end_line = re.findall(regex_end_line, test_string_end_line, re.MULTILINE)
print("Matches for 'end' at the end of a line:", matches_end_line)
```

### 📚 Detailed Explanation

#### 🔍 Understanding the Regular Expressions:

1. **Match the Word "Alpha" at the Very Beginning of the Subject Text:**
   - Regular expression: `^alpha`
     - `^`: Asserts the position at the start of the string.
     - `alpha`: Matches the literal word "alpha".
   - This pattern ensures that "alpha" must be at the very beginning of the subject text.

2. **Match the Word "Omega" at the Very End of the Subject Text:**
   - Regular expression: `omega$`
     - `omega`: Matches the literal word "omega".
     - `$`: Asserts the position at the end of the string.
   - This pattern ensures that "omega" must be at the very end of the subject text.

3. **Match the Word "Begin" at the Beginning of a Line:**
   - Regular expression: `^begin`
     - `^`: Asserts the position at the start of a line.
     - `begin`: Matches the literal word "begin".
   - This pattern ensures that "begin" must be at the beginning of a line. The `re.MULTILINE` flag is used to match the start of each line.

4. **Match the Word "End" at the End of a Line:**
   - Regular expression: `end$`
     - `end`: Matches the literal word "end".
     - `$`: Asserts the position at the end of a line.
   - This pattern ensures that "end" must be at the end of a line. The `re.MULTILINE` flag is used to match the end of each line.

#### 🧪 Matching the Strings:

- The `re.match` function is used to check if the entire string starts with "alpha".
- The `re.search` function is used to check if "omega" occurs at the end of the string.
- The `re.findall` function is used with the `re.MULTILINE` flag to find all occurrences of "begin" at the beginning of lines and "end" at the end of lines.

#### 🖥️ Code Execution:

- The `test_string_alpha_beginning` contains the word "alpha" at the start of the text.
- The `test_string_omega_end` contains the word "omega" at the end of the text.
- The `test_string_begin_line` includes lines where "begin" appears at the start of a line.
- The `test_string_end_line` includes lines where "end" appears at the end of a line.

By following these steps, we ensure that the regular expressions match their respective patterns correctly.
