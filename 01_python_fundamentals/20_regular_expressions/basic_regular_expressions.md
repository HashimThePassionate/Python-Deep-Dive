# Matching Literal Text with Regular Expressions ✨

## Problem 1.1 🚩

We want to create a **regular expression** that matches the following sentence **exactly**:

📝 **Sentence to Match:**
```
The punctuation characters in the ASCII table are: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~.
```
This exercise helps us understand which characters in regular expressions have special meanings 🎯 and which ones match themselves without any special rules. Let's break it down in a fun way! 🕵️‍♂️

## Solution 🛠️

To match this sentence exactly, we need a **regular expression** like this:

```regex
The\s+punctuation\s+characters\s+in\s+the\s+ASCII\s+table\s+are:\s+↵
!"#\$%&'\(\)\*\+,-\./:;<=>\?@\[\\]\^_`\{\|}~
```

🧐 Here’s what this means:

- **Special Characters Escaped** 🛡️: Some characters have special roles in regular expressions. To match them **literally** (as they appear), we need to put a backslash `\` before them. For example:
  - `*` becomes `\*`
  - `?` becomes `\?`
  - `.` becomes `\.`

- **Normal Characters Match Themselves** 🔠: Characters like letters (A-Z, a-z), numbers (0-9), and some punctuation marks (like `,` or `:`) match themselves directly without any extra rules.

## Explanation 🌟

A **regular expression** (regex) can be thought of as a "search pattern" 🔍. It helps you find specific sequences of text in a larger body of text 📖.

When we want to match text **exactly** as it is, we need to consider certain characters that have special meanings, known as **metacharacters** 🚀. Here are the most common ones:

- **Metacharacters**: `$`, `(`, `)`, `*`, `+`, `.`, `?`, `[`, `\`, `^`, `{`, `|`
  - These characters have special meanings in regex. For instance, `*` means "zero or more of the previous character."
  - To match these characters **exactly**, we use a backslash `\` to "escape" them 🏃‍♂️.

### Example:

If we want to search for the string `$()*+.?[\^{|`, we use the regex:

```regex
\$\(\)\*\+\.\?\[\\\^\{\|
```

💡 Each metacharacter has a backslash `\` before it to indicate that we want the **literal** character, not its special function. 🚀

## Tips for Beginners 🐣

- **Don’t Over-Escape!** 🚫: Avoid adding too many backslashes (`\`). Over-escaping can make your regex harder to read and understand 🕵️‍♂️. Only escape characters that need it!

- **Block Escape 🧱**: Some regex "flavors" (variations) support a cool feature called **block escape** using `\Q...\E`. Everything between `\Q` and `\E` is treated as **literal**, meaning you don’t have to escape any special characters.
  - Example:
    ```regex
    \Q!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~\E
    ```
  - This is much easier to read than escaping each character individually! 🏆

## Case-Insensitive Matching 🔠

Regular expressions are **case-sensitive** by default. This means `regex` will match `regex`, but **not** `Regex`, `REGEX`, or `ReGeX`. If you want to match all of them, you can turn on **case insensitivity** using `(?i)`:

```regex
(?i)regex
```

- `(?i)` makes everything **after** it case-insensitive. 🌀
- `(?-i)` can turn case sensitivity back **on**.

Example:

```regex
sensitive(?i)caseless(?-i)sensitive
```

This will match `sensitiveCASELESSsensitive` but **not** `SENSITIVEcaselessSENSITIVE`. Think of `(?i)` and `(?-i)` as switches to turn case sensitivity on or off. 🔄

To match the exact pattern using the provided regular expression, you can use Python's `re` module. Here's the code to achieve this:

```python
import re

# The sentence to match
text_to_match = """The punctuation characters in the ASCII table are: !"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~."""

# Regular expression to match the exact text
pattern = r"The\s+punctuation\s+characters\s+in\s+the\s+ASCII\s+table\s+are:\s+↵!"r"#\$%&'\(\)\*\+,-\./:;<=>\?@\[\\]\^_`\{\|}~"

# Performing the match
if re.fullmatch(pattern, text_to_match):
    print("The text matches the pattern exactly! ✅")
else:
    print("The text does not match the pattern. ❌")
```

### Explanation:
1. **`import re`**: Imports Python's regular expression library.
2. **`pattern`**: The regular expression pattern provided.
3. **`re.fullmatch()`**: Checks if the entire string matches the regular expression pattern.

This code will let you know if the provided text matches the exact pattern! 🎉

---

## Problem 1.2 🚩
### Matching Nonprintable Characters with Regular Expressions ✨

We want to create a **regular expression** to match a string containing these nonprintable ASCII control characters: 

1. **Bell** 🔔 (`\a`)
2. **Escape** 🏃‍♂️ (`\x1B`)
3. **Form Feed** 📄 (`\f`)
4. **Line Feed** 🆕 (`\n`)
5. **Carriage Return** ↩️ (`\r`)
6. **Horizontal Tab** ➡️ (`\t`)
7. **Vertical Tab** ↕️ (`\v`)

These characters have specific uses in programming and text processing. Each has a hexadecimal ASCII code that is used to represent it.

## Solution 🛠️

### Option 1: Common Escape Sequences and Hexadecimal Codes 🚀
```regex
\a\x1B\f\n\r\t\v
```
This uses the escape sequences and hexadecimal codes for each character:
- `\a` for Bell 🔔
- `\x1B` for Escape 🏃‍♂️
- `\f` for Form Feed 📄
- `\n` for Line Feed 🆕
- `\r` for Carriage Return ↩️
- `\t` for Horizontal Tab ➡️
- `\v` for Vertical Tab ↕️

### Option 2: All Hexadecimal Codes 💡
```regex
\x07\x1B\x0C\x0A\x0D\x09\x0B
```
This option uses the hexadecimal ASCII codes to represent each character:
- `\x07` for Bell 🔔
- `\x1B` for Escape 🏃‍♂️
- `\x0C` for Form Feed 📄
- `\x0A` for Line Feed 🆕
- `\x0D` for Carriage Return ↩️
- `\x09` for Horizontal Tab ➡️
- `\x0B` for Vertical Tab ↕️

## Python Code to Match Nonprintable Characters 🐍

Let's write a Python code to match a string containing all these control characters.

```python
import re
# String to match
nonprintable_string = "\a\x1B\f\n\r\t\v"
# Regular expression pattern to match the nonprintable characters
pattern = r"\a\x1B\f\n\r\t\v"
# Matching the pattern
if re.fullmatch(pattern, nonprintable_string):
    print("The text matches the pattern exactly! ✅")
else:
    print("The text does not match the pattern. ❌")
```

### Explanation 🌟

1. **Use `\x1B` for Escape**: Python's `re` module does not support `\e`, so we use the hexadecimal `\x1B`.
2. **Other Characters**: Escape sequences like `\a`, `\f`, `\n`, `\r`, `\t`, and `\v` are directly supported.
3. **`re.fullmatch()`**: Ensures the entire string matches the provided pattern.

## Usage of Each Nonprintable Character 📚

1. **Bell (`\a`)** 🔔: Triggers an alert sound in terminals or consoles. Used in older systems for notifications.
2. **Escape (`\x1B`)** 🏃‍♂️: Starts an escape sequence for formatting text in terminals (e.g., colors).
3. **Form Feed (`\f`)** 📄: Moves the cursor to the next page or clears the screen. Used in text processing to separate pages.
4. **Line Feed (`\n`)** 🆕: Represents a newline in UNIX-based systems. Commonly used in text files.
5. **Carriage Return (`\r`)** ↩️: Moves the cursor to the beginning of the current line. Used in Windows for newlines (`\r\n`).
6. **Horizontal Tab (`\t`)** ➡️: Adds horizontal spacing, useful for formatting text into columns.
7. **Vertical Tab (`\v`)** ↕️: Moves the cursor vertically to the next tab stop. Rarely used in modern text processing.

---

## Problem 1.3 🚩

### Match One of Many Characters 

We need to create **regular expressions** (regex) that solve the following problems:

1. **Match all common misspellings of the word "calendar."** 🗓️  
   Allow either "a" or "e" in each vowel position. This helps us catch different variations of spelling without worrying about exact correctness.
   
2. **Match a single hexadecimal character.** 🔢  
   This is a character that is part of the set 0-9 or A-F (case-insensitive).
   
3. **Match a single character that is not a hexadecimal character.** 🚫  
   This is any character that is not in the set 0-9 or A-F.

These problems introduce us to a powerful regex feature called **character classes**. Let's break it down step-by-step! 🚀

### Solution 🛠️

#### 1. Matching Common Misspellings of "Calendar" 🗓️

To match different misspellings of the word "calendar," we can use this regex pattern:

```python
import re

# Regex to match common misspellings of 'calendar'
calendar_regex = r'c[ae]l[ae]nd[ae]r'

# Example usage
text = "calender, calandar, celendar, celandar"
matches = re.findall(calendar_regex, text)
print(matches)  # Output: ['calender', 'calandar', 'celendar', 'celandar']
```

🧐 **Explanation:**

- **Pattern Breakdown**:
  - `c[ae]l[ae]nd[ae]r`:
    - `c` matches the letter "c." ✅
    - `[ae]` matches either "a" or "e." 🅰️🅴
    - `l` matches the letter "l." ✅
    - `[ae]` again matches either "a" or "e." 🅰️🅴
    - `nd` matches the sequence "nd." ✅
    - `[ae]` matches either "a" or "e." 🅰️🅴
    - `r` matches the letter "r." ✅
- **Result**: This regex will match all variations of the word "calendar" where each vowel can be either "a" or "e."

#### 2. Matching a Single Hexadecimal Character 🔢

A hexadecimal character is any digit from 0 to 9 or any letter from A to F (case-insensitive). Here’s how you can match a single hexadecimal character:

```python
# Regex to match a single hexadecimal character
hex_char_regex = r'[a-fA-F0-9]'

# Example usage
text = "1, A, g, 3F, Z"
matches = re.findall(hex_char_regex, text)
print(matches)  # Output: ['1', 'A', '3', 'F']
```

🧐 **Explanation:**

- **Pattern Breakdown**:
  - `[a-fA-F0-9]`:
    - Matches any lowercase letter from "a" to "f." 🔤
    - Matches any uppercase letter from "A" to "F." 🔠
    - Matches any digit from "0" to "9." 🔟
- **Result**: This regex will match any valid hexadecimal character (e.g., "1", "A", "3F").

#### 3. Matching a Single Non-Hexadecimal Character 🚫

To match a single character that is **not** a hexadecimal character, we use the `^` symbol to negate the class:

```python
# Regex to match a single non-hexadecimal character
non_hex_char_regex = r'[^a-fA-F0-9]'

# Example usage
text = "1, A, g, 3F, Z, !"
matches = re.findall(non_hex_char_regex, text)
print(matches)  # Output: [',', ' ', ',', ' ', 'g', ',', ' ', ',', ' ', 'Z', ',', ' ', '!']
```

🧐 **Explanation:**

- **Pattern Breakdown**:
  - `[^a-fA-F0-9]`:
    - `^` placed at the beginning **negates** the character class. 🚫
    - Matches any character that is **not** a lowercase letter from "a" to "f," an uppercase letter from "A" to "F," or a digit from "0" to "9." ❌
- **Result**: This regex will match any character that is not a hexadecimal character.

### Explanation 🌟

A **character class** is a group of characters you put inside square brackets `[]`. It matches **one single character** from the list inside the brackets. They are very useful when you want to allow multiple possible characters to match a single position.

#### Key Points on Character Classes 📚

- **Metacharacters** in character classes:
  - `\` (Escape), `^` (Negation), `-` (Range), `]` (Closing Bracket). ⚠️
- **Shorthand Classes**:
  - `\d`: Matches any digit (`[0-9]`). 🔢
  - `\D`: Matches any non-digit (`[^0-9]`). 🚫
  - `\w`: Matches any word character (`[a-zA-Z0-9_]`). 🅰️🔤
  - `\W`: Matches any non-word character (`[^a-zA-Z0-9_]`). 🚫
  - `\s`: Matches any whitespace character (spaces, tabs, newlines). 🟦
  - `\S`: Matches any non-whitespace character. 🚫🟦

#### Case Insensitivity with Character Classes 🔠

You can make a regex **case-insensitive** using the `(?i)` flag:

```python
# Case insensitive match for hexadecimal characters
case_insensitive_hex_regex = r'(?i)[a-f0-9]'

# Example usage
text = "A, b, C, d, 3, F"
matches = re.findall(case_insensitive_hex_regex, text)
print(matches)  # Output: ['A', 'b', 'C', 'd', '3', 'F']
```

- **Explanation**: `(?i)` makes the regex case-insensitive. This means it will match both lowercase and uppercase characters without needing to specify both!

---

## Problem Statement 1.4 🚩
### Match Any Character

We need to create **regular expressions** (regex) that solve the following problems:

1. **Match any single character except a line break.** 📝  
   This will match any character except for newline characters (like `\n`).

2. **Match any single character including line breaks.** 📝  
   This will match all characters, even newline characters.

The solution requires understanding the dot `.` metacharacter in regex. Let's explore how it works! 🚀

### Solution 🛠️

#### 1. Match Any Character Except Line Breaks 📝

To match **any single character** except for line breaks (like `\n`), we use the dot `.` metacharacter in regex.

```python
import re

regex_any_char_except_linebreaks = r'.'

text = "Hello! How are \nyou?"

matches = re.findall(regex_any_char_except_linebreaks, text)

print(matches)  # Output: ['H', 'e', 'l', 'l', 'o', '!', ' ', 'H', 'o', 'w', ' ', 'a', 'r', 'e', ' ', 'y', 'o', 'u', '?']
```

🧐 **Explanation:**

- **Pattern Breakdown**:
  - `.`: The dot metacharacter matches **any single character** except for line break characters (`\n`, `\r`). ✅
- **Result**: The regex matches every character in the string except line breaks.

#### 2. Match Any Character Including Line Breaks 📝

To match **any character including line breaks**, we have a few options:

1. **Enable Dot to Match Line Breaks**: Some programming languages have a special option to allow the dot to match line breaks.
2. **Use a Character Class Combination**: A character class like `[\s\S]` matches both whitespace (`\s`) and non-whitespace (`\S`) characters, effectively matching any character.

Let's see the Python implementation using the second option:

```python
# Regex to match any character, including line breaks
regex_any_char_including_linebreaks = r'[\s\S]'

# Example usage
text = "Hello!\nHow are you?"
matches = re.findall(regex_any_char_including_linebreaks, text)
print(matches)  # Output: ['H', 'e', 'l', 'l', 'o', '!', '\n', 'H', 'o', 'w', ' ', 'a', 'r', 'e', ' ', 'y', 'o', 'u', '?']
```

🧐 **Explanation:**

- **Pattern Breakdown**:
  - `[\s\S]`:
    - `\s` matches any whitespace character (like spaces, tabs, or line breaks). 🟦
    - `\S` matches any non-whitespace character. 🔤
    - Combined, `[\s\S]` matches **any character**, including line breaks. ✅
- **Result**: The regex matches every character, including line breaks.

#### Alternative Method with Mode Modifier 🛠️

We can also enable the "dot matches line breaks" mode using a **mode modifier** in regex:

```python
# Regex with mode modifier to match any character, including line breaks
regex_with_mode_modifier = r'(?s).'

# Example usage
text = "Hello!\nHow are you?"
matches = re.findall(regex_with_mode_modifier, text)
print(matches)  # Output: ['H', 'e', 'l', 'l', 'o', '!', '\n', 'H', 'o', 'w', ' ', 'a', 'r', 'e', ' ', 'y', 'o', 'u', '?']
```

- **Explanation**:
  - `(?s).` enables "dot matches line breaks" mode with `(?s)` and then matches any character with `.`.
  - This is another way to match any character, including line breaks.

### Explanation 🌟

The **dot `.` metacharacter** in regex is one of the most commonly used patterns to match **any character**, but by default, it does not match newline characters (`\n`). Here’s what you need to know:

- **Dot (`.`) Matches Any Character Except Line Breaks**: It matches letters, digits, symbols, etc., but not line breaks. 📝
- **Dot with "Dot Matches Line Breaks" Mode**: Enables the dot to match line breaks as well. 🔄
- **Combining `[\s\S]` to Match Any Character**: Combines whitespace (`\s`) and non-whitespace (`\S`) classes to match all characters. 🔄

#### Tips for Using Dot `.` Metacharacter ⚠️

- Use `.` when you want to match any character except line breaks.
- Use `[\s\S]` or `(?s).` when you want to match any character, **including** line breaks.
- Avoid "dot abuse" by using it only when you genuinely want to match any character. Use specific character classes when needed!🛡️

---

## Problem 1.5 🚩
### Match Something at the Start and/or the End of a Line

We need to create **regular expressions** (regex) to solve the following problems:

1. **Match the word "alpha" only at the start of the entire text.** 📝  
2. **Match the word "omega" only at the end of the entire text.** 📝  
3. **Match the word "begin" only at the start of a line.** 📝  
4. **Match the word "end" only at the end of a line.** 📝  

These solutions will introduce the concept of **anchors** in regex, which are used to specify positions in text rather than matching characters. Let’s break it down! 🚀

### Solution 🛠️

#### 1. Match the Word "alpha" Only at the Start of the Text 📝

To match the word **"alpha"** at the very **start of the text**, we use the `^` anchor or `\A` anchor.

```python
import re

# Regex to match "alpha" at the start of the text
regex_start_alpha = r'^\balpha\b'

# Example usage
text1 = "alpha is at the beginning. Not in between."
text2 = "Is alpha at the beginning. Not in between."
matche1 = re.findall(regex_start_alpha, text1)
matche2 = re.findall(regex_start_alpha, text2)
print(matche1)  # Output: ['alpha']
print(matche2)  # Output: No match
```

🧐 **Explanation:**

- **Pattern Breakdown**:
  - `^`: Matches the **start** of the text. 📍
  - `\balpha\b`: Matches the word "alpha" as a **whole word**. 💬
- **Result**: The regex matches "alpha" only if it appears at the start of the text.

Alternatively, you can use `\A`:

```python
regex_start_alpha = r'\Aalpha'
```

- `\A` also matches the **start** of the text but is more precise and not affected by options.

#### 2. Match the Word "omega" Only at the End of the Text 📝

To match the word **"omega"** at the very **end of the text**, we use the `$` anchor or `\Z` anchor.

```python
# Regex to match "omega" at the end of the text
regex_end_omega = r'\bomega\b$'
# Example usage
text1 = "Not in between, but omega is at the end."
text2 = "Not in between, but  is at the end omega"
matche1 = re.findall(regex_end_omega, text1)
matche2 = re.findall(regex_end_omega, text2)
print(matche1)  # Output: no  match
print(matche2)  # Output: no  ['omega']
```

🧐 **Explanation:**

- **Pattern Breakdown**:
  - `\bomega\b`: Matches the word "omega" as a **whole word**. 💬
  - `$`: Matches the **end** of the text. 📍
- **Result**: The regex matches "omega" only if it appears at the end of the text.

Alternatively, you can use `\Z`:

```python
regex_end_omega = r'omega\Z'
```

- `\Z` also matches the **end** of the text, with more specific behavior regarding trailing line breaks.

#### 3. Match the Word "begin" Only at the Start of a Line 📝

To match the word **"begin"** at the **start of a line**, we use the `^` anchor in **multiline mode**.

```python
# Regex to match "begin" at the start of a line
regex_line_start_begin = r'^begin'
# Example usage
text1 = "Not in between.\nbegin is at the start of a line."
text2 = "Not in between.\n begin is at the start of a line."
matche1 = re.findall(regex_line_start_begin, text1, re.MULTILINE)
matche2 = re.findall(regex_line_start_begin, text2, re.MULTILINE)
print(matche1)  # Output: ['begin']
print(matche2)  # Output: no match
```

🧐 **Explanation:**

- **Pattern Breakdown**:
  - `^`: Matches the **start** of each line when in **multiline mode**. 📍
  - `begin`: Matches the word "begin". 💬
- **Result**: The regex matches "begin" only if it appears at the start of a line.

#### 4. Match the Word "end" Only at the End of a Line 📝

To match the word **"end"** at the **end of a line**, we use the `$` anchor in **multiline mode**.

```python
# Regex to match "end" at the end of a line
regex_line_end_end = r'end$'

# Example usage
text1 = "Not in between.\nBut this line ends with end"
text2 = "Not in between.\nBut this line ends end with"
matche1 = re.findall(regex_line_end_end, text1, re.MULTILINE)
matche2 = re.findall(regex_line_end_end, text2, re.MULTILINE)
print(matche1)  # Output: ['end']
print(matche2)  # Output: no match
```

🧐 **Explanation:**

- **Pattern Breakdown**:
  - `end`: Matches the word "end". 💬
  - `$`: Matches the **end** of each line when in **multiline mode**. 📍
- **Result**: The regex matches "end" only if it appears at the end of a line.

### Explanation 🌟

**Anchors** are special regex tokens that match positions in the text rather than actual characters:

- `^`: Matches the **start** of the text or line. 📍
- `$`: Matches the **end** of the text or line. 📍
- `\A`: Matches the **start** of the entire text (not affected by options). 📍
- `\Z`: Matches the **end** of the entire text, including before a trailing newline (not affected by options). 📍

---

## Problem 1.6 🚩
### Match Whole Words 

We need to create **regular expressions** (regex) that solve the following problems:

1. **Match the word "cat" only if it appears as a whole word** in a sentence like "My cat is brown," but **not** in words like "category" or "bobcat."
   
2. **Match the word "cat" only if it is part of another word**, such as in "staccato," but **not** as a standalone word like in "My cat is brown."

These solutions introduce the concept of **word boundaries** in regex. Let’s break it down! 🚀

### Solution 🛠️

#### 1. Match the Word "cat" Only as a Whole Word 🐱

To match **"cat"** as a **whole word** and not as part of another word, we use the `\b` (word boundary) metacharacter in regex.

```python
import re

# Regex to match "cat" as a whole word
regex_whole_word_cat = r'\bcat\b'

# Example usage
text = "My cat is brown. A category is different from a cat."
matches = re.findall(regex_whole_word_cat, text)
print(matches)  # Output: ['cat', 'cat']
```

🧐 **Explanation:**

- **Pattern Breakdown**:
  - `\b`: Matches a **word boundary** (the position between a word character and a non-word character). 🛑
  - `cat`: Matches the literal string "cat". 🐱
  - `\b`: Matches another **word boundary**. 🛑
- **Result**: This regex will match "cat" only if it appears as a separate word.

#### 2. Match the Word "cat" Only If It Is Part of Another Word 🐱

To match **"cat"** only when it is **inside** another word (e.g., "staccato"), we use the `\B` (non-word boundary) metacharacter in regex.

```python
# Regex to match "cat" only if it is part of another word
regex_non_whole_word_cat = r'\Bcat\B'

# Example usage
text = "My cat is brown. staccato is a word, and so is bobcat."
matches = re.findall(regex_non_whole_word_cat, text)
print(matches)  # Output: ['cat', 'cat']
```

🧐 **Explanation:**

- **Pattern Breakdown**:
  - `\B`: Matches a **non-word boundary** (a position between two word characters or two non-word characters). 🛑
  - `cat`: Matches the literal string "cat". 🐱
  - `\B`: Matches another **non-word boundary**. 🛑
- **Result**: This regex will match "cat" only when it is part of another word.

### Explanation 🌟

#### Word Boundaries (`\b`) and Non-Word Boundaries (`\B`) in Regex 📚

- **`\b` (Word Boundary)**: Matches the position where a word character (`[a-zA-Z0-9_]`) is next to a non-word character (like spaces, punctuation, or start/end of the text). It helps in matching **whole words only**.
  - Example: `\bcat\b` matches "cat" in "My cat is brown," but not in "bobcat" or "category".

- **`\B` (Non-Word Boundary)**: Matches the position **not** at a word boundary, i.e., between two word characters or two non-word characters. It helps in matching **substrings within words**.
  - Example: `\Bcat\B` matches "cat" in "staccato" or "bobcat," but not in "My cat is brown."

---

## Problem 1.7 🚩

### Unicode Code Points, Categories, Blocks, and Scripts 📝

We need to use **regular expressions** (regex) to solve the following problems related to Unicode:

1. **Find the trademark sign (™) by specifying its Unicode code point** rather than copying and pasting it.  
2. **Match any character that belongs to the "Currency Symbol" Unicode category**.  
3. **Match any character in the "Greek Extended" Unicode block**.  
4. **Match any character that is part of the "Greek" script according to Unicode**.  
5. **Match a grapheme (a base character with all its combining marks)**.  

These tasks require an understanding of **Unicode properties** in regex, such as code points, categories, blocks, and scripts.

### Explanation of `\p{}` in Regex 🌍

The `\p{}` notation in regular expressions is used to match **Unicode properties**. It allows us to match characters based on their properties defined in the Unicode standard, such as **letters**, **numbers**, **symbols**, **scripts**, and **blocks**.

- **Syntax**: `\p{Property}` where `Property` can be a **Unicode Category**, **Script**, or **Block**.
- **Negated Version**: `\P{Property}` matches any character **not** in the specified property.

Common Unicode properties include:
- `\p{L}`: Matches any **letter** character.
- `\p{N}`: Matches any **numeric** character.
- `\p{Sc}`: Matches any **currency symbol**.
- `\p{Greek}`: Matches any character in the **Greek script**.

The `\p{}` syntax is supported in regex flavors that handle Unicode, such as Perl, PCRE, and Python (with the `regex` module).

### Installing the `regex` Module 📥

Python's built-in `re` module does not support the `\p{}` syntax for Unicode properties. To use Unicode properties like `\p{Sc}` (currency symbol) in Python, you need to install the `regex` module, which is an enhanced alternative to the `re` module.

1. **Install the `regex` module**:
   Use pip to install the `regex` module:
   ```bash
   pip install regex
   ```

2. **Update your code** to use `regex` instead of `re`.

### Solution Table [fun with unicode](https://checkserp.com/encode/unicode/) 🛠️

| **Category**                        | **Description**                                                        | **Regex Pattern**              | **Python Example**                                                                                                                                   |
|-------------------------------------|------------------------------------------------------------------------|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Unicode Code Point**              | Matches a specific Unicode character by its code point.                | `\u2122`                      | `r'\u2122'` for ™ (trademark)                                                                                                                       |
| **Currency Symbol Category**        | Matches any currency symbol like $, €, ¥, etc.                         | `\p{Sc}`                      | `r'\p{Sc}'` (requires `regex` module)                                                                                                               |
| **Greek Extended Block**            | Matches any character in the Greek Extended Unicode block.             | `[\u1F00-\u1FFF]`             | `r'[\u1F00-\u1FFF]'`                                                                                                                                |
| **Greek Script**                    | Matches any character in the Greek script.                             | `[\u0370-\u03FF]`             | `r'[\u0370-\u03FF]'`                                                                                                                                |
| **Grapheme (Base + Combining Marks)**| Matches a grapheme (base character and its combining marks).            | `(\P{M}\p{M}*)`               | `r'(\P{M}\p{M}*)'`                                                                                                                                  |

### Detailed Examples and Explanations 🌟

#### 1. Find the Trademark Sign (™) by Unicode Code Point ™

To match the trademark sign using its **Unicode code point**, we use `\u2122` in regex.

```python
import re

# Regex to find the trademark sign (™)
regex_trademark = r'\u2122'

text = "This is a trademark symbol ™ and here is another one: ™."
matches = re.findall(regex_trademark, text)
print(matches)  # Output: ['™', '™']
```

🧐 **Explanation:**

- **Pattern Breakdown**:
  - `\u2122`: Matches the trademark symbol using its Unicode code point `U+2122`. 🄂
- **Result**: The regex finds all occurrences of the trademark symbol.

#### 2. Match Any Character in the "Currency Symbol" Unicode Category 💲

To match **any character in the "Currency Symbol" category**, we use `\p{Sc}` in regex with the `regex` module.

```python
import regex as re  # Use 'regex' module instead of 're'

# Regex to match any currency symbol
regex_currency = r'\p{Sc}'

text = "The price is $100 or €85 or ¥1000."
matches = re.findall(regex_currency, text)
print(matches)  # Output: ['$', '€', '¥']
```

🧐 **Explanation:**

- **Pattern Breakdown**:
  - `\p{Sc}`: Matches any character in the "Currency Symbol" category. 💰
- **Result**: The regex finds all currency symbols like `$`, `€`, and `¥`.

#### 3. Match Any Character in the "Greek Extended" Unicode Block 🇬🇷

To match **any character in the "Greek Extended" Unicode block**, we use `[\u1F00-\u1FFF]`.

```python
import re

# Regex to match any character in the "Greek Extended" block
regex_greek_extended = r'[\u1F00-\u1FFF]'

text = "Greek letters: ἀ ἁ ἂ ἃ."
matches = re.findall(regex_greek_extended, text)
print(matches)  # Output: ['ἀ', 'ἁ', 'ἂ', 'ἃ']
```

🧐 **Explanation:**

- **Pattern Breakdown**:
  - `[\u1F00-\u1FFF]`: Matches any character in the "Greek Extended" block, which ranges from `U+1F00` to `U+1FFF`. 🏺
- **Result**: The regex matches all characters in the "Greek Extended" block.

#### 4. Match Any Character in the "Greek" Script 🇬🇷

To match **any character in the "Greek" script**, we use `[\u0370-\u03FF]` in regex.

```python
import re

# Regex to match any character in the "Greek" script
regex_greek_script = r'[\u0370-\u03FF]'

text = "Greek letters: Α, Β, Γ, Δ, ε, ζ."
matches = re.findall(regex_greek_script, text)
print(matches)  # Output: ['Α', 'Β', 'Γ', 'Δ', 'ε', 'ζ']
```

🧐 **Explanation:**

- **Pattern Breakdown**:
  - `[\u0370-\u03FF]`: Matches any character in the "Greek" script, covering code points from `U+0370` to `U+03FF`. 🏺
- **Result**: The regex matches all characters that are part of the "Greek" script.

#### 5. Match a Grapheme (Base Character with All Its Combining Marks) ✍️

To match a **grapheme**, which is a base character along with all its combining marks, we can use `(\P{M}\p{M}*)`. This regex will match each grapheme cluster, but it will also match standalone characters (such as letters or spaces) individually.

```python
import regex as re  # Use 'regex' module

# Regex to match a grapheme (base character + combining marks)
regex_grapheme = r'(\P{M}\p{M}*)'

text = "à is a grapheme."
matches = re.findall(regex_grapheme, text)
print(matches)  # Output: ['à', ' ', 'i', 's', ' ', 'a', ' ', 'g', 'r', 'a', 'p', 'h', 'e', 'm', 'e', '.']
```

🧐 **Explanation:**

- **Pattern Breakdown**:
  - `\P{M}`: Matches any character that is **not** a combining mark (e.g., base characters like 'a'). 🚫
  - `\p{M}*`: Matches zero or more combining marks that follow. 🌟
- **Result**: The regex matches graphemes (base character with its marks), but it also matches individual characters (spaces, punctuation, etc.) separately if they are not part of a grapheme.

---

Got it! Let's update the regex example to match the names "Muhammad," "Hashim," or "Ali."

## Problem 2.8: 🚩
### Match One of Several Alternatives

We need to create a **regular expression** (regex) that matches one of several alternatives. Specifically, we want a regex that matches any of the names "Muhammad," "Hashim," or "Ali" in the following text:

```
Muhammad, Hashim, and Ali went to Muhammad's house.
```

The regex should be applied repeatedly to find each name in the text until no more matches are found. Let’s break down the solution using Python. 🚀

### Solution 🛠️

To match any of the names "Muhammad," "Hashim," or "Ali," we can use the **pipe symbol** (`|`) to create an **alternation** in regex:

```python
import re

# Regex to match "Muhammad", "Hashim", or "Ali"
regex_names = r'Muhammad|Hashim|Ali'

# Example text
text = "Muhammad, Hashim, and Ali went to Muhammad's house."

# Find all matches
matches = re.findall(regex_names, text)
print(matches)  # Output: ['Muhammad', 'Hashim', 'Ali', 'Muhammad']
```

🧐 **Explanation:**

- **Pattern Breakdown**:
  - `Muhammad|Hashim|Ali`: This regex uses the **pipe symbol (`|`)** to specify an **alternation**. It matches **either** "Muhammad," **or** "Hashim," **or** "Ali."  
- **Result**: The regex finds all occurrences of the names "Muhammad," "Hashim," and "Ali" in the text. The `re.findall()` function returns all matches as a list.

### Explanation 🌟

#### Key Points About Alternation (`|`) 📚

- The **pipe symbol** (`|`) is used to specify **alternatives** in regex. It allows matching any one of several alternatives. For example, `cat|dog` matches either "cat" or "dog".
- The regex engine scans the text **from left to right** and tries all alternatives at each character position.
- **Order matters** only when two alternatives can match at the same position. For example, `Ali|Alias` would match "Ali" in "His name is Alias" because "Ali" comes first.
- **Tip**: To avoid this problem, put the **longer alternative first** or use **word boundaries** (`\b`). For example, `Alias|Ali` or `\bAli\b|\bAlias\b`.

### Example with Word Boundaries 📝

If you want to make sure that only **whole words** are matched, you can use **word boundaries** (`\b`):

```python
import re

# Regex to match whole words "Muhammad", "Hashim", or "Ali"
regex_names_whole = r'\bMuhammad\b|\bHashim\b|\bAli\b'

# Example text
text = "Muhammad, Hashim, and Ali went to Muhammad's house."

# Find all matches
matches = re.findall(regex_names_whole, text)
print(matches)  # Output: ['Muhammad', 'Hashim', 'Ali', 'Muhammad']
```

🧐 **Explanation**:

- **Pattern Breakdown**:
  - `\bMuhammad\b|\bHashim\b|\bAli\b`: This regex uses **word boundaries** (`\b`) to ensure that only **whole words** "Muhammad," "Hashim," or "Ali" are matched.
- **Result**: The regex works the same way but prevents partial matches in other contexts.

---

Here's the complete example with all sections combined in the README format, explaining regex grouping, capturing, non-capturing groups, and everything needed to understand the concepts:

---

## Problem 2.9 🚩
### Group and Capture Parts of the Match

We need to create **regular expressions** (regex) that solve the following problems:

1. Improve the regex for matching "Muhammad," "Hashim," or "Ali" by ensuring that the match is a **whole word**. Use grouping to apply **one pair** of word boundaries for the whole regex, instead of a pair for each alternative.
   
2. Create a regex to match any date in the format `yyyy-mm-dd` and separately capture the **year**, **month**, and **day** for easy processing.

These problems help us understand how to **group** and **capture** specific parts of the match using regex in Python. Let's explore each solution in detail with examples! 🚀

### Solution 🛠️

#### 1. Matching Whole Words with Grouping 📝

To match whole words like "Muhammad," "Hashim," or "Ali," we use **grouping** with parentheses `()` to apply a **single pair** of word boundaries around the entire group:

```python
import re

# Regex to match whole words "Muhammad", "Hashim", or "Ali" using grouping
regex_names = r'\b(Muhammad|Hashim|Ali)\b'

# Example text
text = "Muhammad, Hashim, and Ali went to Muhammad's house."

# Find all matches
matches = re.findall(regex_names, text)
print(matches)  # Output: ['Muhammad', 'Hashim', 'Ali', 'Muhammad']
```

🧐 **Explanation:**

- **Pattern Breakdown**:
  - `\b`: Word boundary to ensure the match starts at the beginning of a word.
  - `(Muhammad|Hashim|Ali)`: **Grouping** using parentheses `()` to match "Muhammad," "Hashim," or "Ali."
  - `\b`: Word boundary to ensure the match ends at the end of a word.
- **Result**: This regex finds all whole word matches of "Muhammad," "Hashim," or "Ali" in the text.

This regex solution finds matches at the word boundaries, ensuring we only capture whole words and not partial matches within other words or text.

#### 2. Capturing Groups for Dates in `yyyy-mm-dd` Format 📅

To match a date in the `yyyy-mm-dd` format and capture the **year**, **month**, and **day** separately, we use **capturing groups** with parentheses `()`:

```python
import re

# Regex to match and capture date parts in yyyy-mm-dd format
regex_date = r'\b(\d{4})-(\d{2})-(\d{2})\b'

# Example text with today's date
text = "The event is scheduled for 2024-09-12."

# Find all matches with captured groups
matches = re.findall(regex_date, text)
print(matches)  # Output: [('2024', '09', '12')]

# Extracting year, month, and day from the first match
if matches:
    year, month, day = matches[0]
    print(f"Year: {year}, Month: {month}, Day: {day}")
    # Output: Year: 2024, Month: 09, Day: 12
```

🧐 **Explanation:**

- **Pattern Breakdown**:
  - `\b`: Word boundary to ensure the match starts at the beginning of a word.
  - `(\d{4})`: **Capturing group** for **year**, matches exactly 4 digits.
  - `-`: Matches the hyphen `-` separating year, month, and day.
  - `(\d{2})`: **Capturing group** for **month**, matches exactly 2 digits.
  - `-`: Matches the hyphen `-`.
  - `(\d{2})`: **Capturing group** for **day**, matches exactly 2 digits.
  - `\b`: Word boundary to ensure the match ends at the end of a word.
- **Result**: This regex captures the **year**, **month**, and **day** separately when a date in `yyyy-mm-dd` format is found.

#### Complete Example 🧩

Combining both regex examples into a complete program:

```python
import re

# Example 1: Matching Whole Words "Muhammad", "Hashim", or "Ali"
regex_names = r'\b(Muhammad|Hashim|Ali)\b'
text_names = "Muhammad, Hashim, and Ali went to Muhammad's house."

# Find all matches
matches_names = re.findall(regex_names, text_names)
print("Matching Names:", matches_names)  # Output: ['Muhammad', 'Hashim', 'Ali', 'Muhammad']

# Example 2: Matching and Capturing Dates in yyyy-mm-dd Format
regex_date = r'\b(\d{4})-(\d{2})-(\d{2})\b'
text_date = "The event is scheduled for 2024-09-12."

# Find all matches with captured groups
matches_date = re.findall(regex_date, text_date)
print("Matching Dates:", matches_date)  # Output: [('2024', '09', '12')]

# Extracting year, month, and day from the first match
if matches_date:
    year, month, day = matches_date[0]
    print(f"Year: {year}, Month: {month}, Day: {day}")
    # Output: Year: 2024, Month: 09, Day: 12
```

### Explanation 🌟

#### Key Points About Grouping and Capturing 📚

- **Grouping** `()`:
  - Parentheses `()` are used for **grouping** in regex. They allow you to apply an operator to the group or capture matched text.
  - Grouping can also **reduce redundancy** by applying a common condition to multiple options (e.g., word boundaries around multiple names).
  
- **Capturing Groups**:
  - When you use parentheses `()` in regex, they also **capture** the matched text. This is helpful for extracting specific parts of a match, such as dates in different formats.
  - Capturing groups are **numbered** from left to right based on the order of the opening parentheses.

#### Non-Capturing Groups `(?:...)` 🔍

- **Non-Capturing Groups**:
  - If you only want to **group** but not **capture**, you can use `(?:...)`. This prevents unnecessary captures and helps maintain the correct numbering of capturing groups.

```python
# Example of non-capturing group for matching "Muhammad", "Hashim", or "Ali"
regex_names_non_capture = r'\b(?:Muhammad|Hashim|Ali)\b'
regex_date = r'\b(\d{4})-(\d{2})-(\d{2})\b'
regex_date_without_capture = r'\b(?:\d{4})-(?:\d{2})-(?:\d{2})\b'
# Example text with today's date
text = "The event is scheduled for 2024-09-12."

# Find all matches with captured groups
matches = re.findall(regex_date, text)
print(matches)  # Output: [('2024', '09', '12')]
matches = re.findall(regex_date_without_capture, text)
print(matches)  # Output: ['2024-09-12']
```

- The use of `?:` inside the parentheses creates a **non-capturing group**, which groups the alternatives without capturing them.

This way, we can use powerful grouping and capturing techniques to enhance our regex patterns for more flexible and precise text matching in Python.

--- 

## Problem 2.0 🚩
### Match Previously Matched Text Again

We want to create a regular expression that matches **"magical" dates** in the format `yyyy-mm-dd`. A date is considered **magical** if the last two digits of the year (the year minus the century), the month, and the day are all the same numbers. For example, **2008-08-08** is a magical date because **08** is the same for the year, month, and day. Assume all dates are valid; we only need to identify these magical dates.

### Solution 🛠️

To solve this problem, we use the concept of **capturing groups** and **backreferences** in regular expressions.

```python
import re

# Regex to match "magical" dates in yyyy-mm-dd format
regex_magical_date = r'\b\d\d(\d\d)-\1-\1\b'

# Example text containing dates
text_dates = "Here are some dates: 2008-08-08, 1999-12-12, 2024-09-12, and 2011-11-11."

# Find all magical dates
matches_magical_dates = re.findall(regex_magical_date, text_dates)
print("Magical Dates:", matches_magical_dates)
```

### Explanation 🌟

- **Regex Pattern**: `\b\d\d(\d\d)-\1-\1\b`
  - `\b` matches a **word boundary** to ensure the date stands alone.
  - `\d\d` matches any two digits. This represents the first two digits of the year (e.g., **20** in **2008**).
  - `(\d\d)` is a **capturing group** that matches the last two digits of the year (e.g., **08** in **2008**). The `()` makes it a capturing group.
  - `\1` is a **backreference** that matches the same text as previously matched by the **first capturing group** `(\d\d)`. This ensures the **month** matches the last two digits of the year.
  - Another `\1` ensures that the **day** also matches the last two digits of the year.
  - `\b` again matches a **word boundary**.

### Output 📤

When you run the code, it will output:

```plaintext
Magical Dates: ['08', '11']
```

### How It Works 🧙‍♂️

1. **2008-08-08**:
   - **Year**: `2008` ➔ Capturing group captures `08`.
   - **Month**: `08` ➔ Matches backreference `\1` (`08`).
   - **Day**: `08` ➔ Matches backreference `\1` (`08`).
   - **Result**: This is a magical date! ✅

2. **1999-12-12**:
   - **Year**: `1999` ➔ Capturing group captures `99`.
   - **Month**: `12` ➔ Does not match `99`.
   - **Result**: Not a magical date. ❌

3. **2024-09-12**:
   - **Year**: `2024` ➔ Capturing group captures `24`.
   - **Month**: `09` ➔ Does not match `24`.
   - **Result**: Not a magical date. ❌

4. **2011-11-11**:
   - **Year**: `2011` ➔ Capturing group captures `11`.
   - **Month**: `11` ➔ Matches backreference `\1` (`11`).
   - **Day**: `11` ➔ Matches backreference `\1` (`11`).
   - **Result**: This is a magical date! ✅

---

## Problem 2.1 🚩
### Capture and Name Parts of the Match

1. **Match any date** in the `yyyy-mm-dd` format and capture the year, month, and day with **descriptive names**. This helps us easily work with these separate values in code.

2. **Match "magical" dates** in the `yyyy-mm-dd` format. A date is "magical" if the year minus the century, the month, and the day of the month are all the same numbers. For example, `2008-08-08` is a magical date. Capture the magical number (e.g., `08`) and label it as `"magic"`.

#### Explanation of `(?P<name>...)` and `(?P=name)` in Regular Expressions 🌟

The `(?P<name>...)` syntax in Python regular expressions allows you to create **named capturing groups**. Named capturing groups are similar to regular capturing groups, but they are easier to reference and make the code more readable and maintainable.

#### Syntax Details:

1. **Named Capturing Group: `(?P<name>...)`**  
   - This syntax creates a **named group** and captures the text matched by the regex inside the parentheses `(...)`.
   - `?P<name>` specifies the **name** of the group.
   - `name` must be a valid Python identifier (letters, digits, and underscores but no spaces).
   - The `...` part is the regex pattern that the group will match.
   - **Example**: `(?P<year>\d{4})` captures a four-digit number as a "year."

2. **Named Backreference: `(?P=name)`**  
   - This syntax allows you to **reference a previously captured named group** within the same regex.
   - It ensures that the text matches exactly what was previously captured by the named group `name`.
   - **Example**: `(?P=magic)` references the previously captured text named `"magic"` to ensure it matches again later in the pattern.

### Solution 🛠️

We can use **named capturing groups** in Python to make our regular expressions more readable and easier to maintain.

### 1. Named Capture for Dates 📅

```python
import re

# Regex to match dates and capture year, month, and day
regex_named_date = r'\b(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})\b'

# Example text containing dates
text_dates = "Here are some dates: 2024-09-12, 1999-12-25, 2008-08-08."

# Find all matches and extract named groups
matches_dates = re.finditer(regex_named_date, text_dates)
for match in matches_dates:
    print(f"Year: {match.group('year')}, Month: {match.group('month')}, Day: {match.group('day')}")
```
### Output 📤
Running the code will output:
```plaintext
Year: 2024, Month: 09, Day: 12
Year: 1999, Month: 12, Day: 25
Year: 2008, Month: 08, Day: 08
```

### 2. Named Capture for Magical Dates ✨

```python
# Regex to match "magical" dates and capture the magical number
regex_magical_named = r'\b\d{2}(?P<magic>\d{2})-(?P=magic)-(?P=magic)\b'

# Example text containing dates
text_magical_dates = "Some magical dates are: 2008-08-08, 2024-09-12, and 2011-11-11."

# Find all matches and extract the "magic" number
matches_magical = re.finditer(regex_magical_named, text_magical_dates)
for match in matches_magical:
    print(f"Magical Number: {match.group('magic')}")
```
### Output 📤
Running the code will output:
```plaintext
Magical Number: 08
Magical Number: 11
```
### Explanation 🌟

1. **Named Capture for Dates**:
   - **Pattern**: `r'\b(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})\b'`
     - `(?P<year>\d{4})` captures the **year** with the name `"year"`.
     - `(?P<month>\d{2})` captures the **month** with the name `"month"`.
     - `(?P<day>\d{2})` captures the **day** with the name `"day"`.
   - **Usage**: Named groups make it easy to access parts of the match using descriptive names (`match.group('year')`, `match.group('month')`, etc.).

2. **Named Capture for Magical Dates**:
   - **Pattern**: `r'\b\d{2}(?P<magic>\d{2})-(?P=magic)-(?P=magic)\b'`
     - `(?P<magic>\d{2})` captures the **magical number** with the name `"magic"`.
     - `(?P=magic)` is a **named backreference** that ensures the **month** and **day** match the `"magic"` number.

--- 


## Problem 2.2 🚩
### Repeating Parts of a Regex a Certain Number of Times 🔄

Create regular expressions in Python to match these types of numbers:

1. **Googol**: A number with exactly 100 digits.
2. **32-bit Hexadecimal Number**: A number with 1 to 8 hexadecimal digits.
3. **32-bit Hexadecimal Number with Optional 'h' Suffix**: Same as above, but may end with an 'h'.
4. **Floating-Point Number**: A number that has a decimal point, with optional integer and exponent parts.

### Explanation 🌟

To match these patterns, we need to understand how to repeat parts of a regex pattern using **quantifiers**. Here’s a quick rundown:

- **`{n}`**: Matches the preceding token exactly `n` times.
- **`{n,m}`**: Matches the preceding token at least `n` times and at most `m` times.
- **`?`**: Matches the preceding token zero or one time (makes it optional).
- **`*`**: Matches the preceding token zero or more times.

Now, let's apply these concepts to each problem:

### Solution 🛠️

#### 1. Match a Googol (100-digit Number) 📏

A **googol** is a number with exactly 100 digits. In regex, `\d` represents a digit (0-9). To repeat this 100 times, we use `\d{100}`.

**Regex Pattern**: `\b\d{100}\b`

- **`\b`**: Word boundary, ensures the number is isolated (not part of another number).
- **`\d{100}`**: Matches exactly 100 digits.

**Python Code Example**:

```python
import re

# Match a googol (100-digit number)
regex_googol = r'\b\d{100}\b'

text = "Number: 12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890."

matches = re.findall(regex_googol, text)
print("Googol Matches:", matches)
```

**Output**:

```plaintext
Googol Matches: ['12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890']
```

#### Explanation 🌟

- **`\d{100}`**: This is the core part of the regex. It says, "find exactly 100 digits." 
- **`\b`**: The `\b` at the beginning and end ensures the number stands alone and isn’t part of a larger string of digits.

#### 2. Match a 32-bit Hexadecimal Number 🔢

A **32-bit hexadecimal number** contains digits from `0-9` and letters from `a-f`, and it can have 1 to 8 characters. 

**Regex Pattern**: `\b[a-f0-9]{1,8}\b` (Case insensitive)

- **`[a-f0-9]`**: Matches any digit from `0-9` or any letter from `a-f`.
- **`{1,8}`**: Matches between 1 and 8 of the previous character class.
- **`re.IGNORECASE`**: Makes the regex case insensitive, so it matches both uppercase and lowercase letters.

**Python Code Example**:

```python
# Match a 32-bit hexadecimal number
regex_hex = r'\b[a-f0-9]{1,8}\b'

text = "Hex numbers: 1a2b, deadbeef, 01234567."

matches = re.findall(regex_hex, text, re.IGNORECASE)
print("Hexadecimal Matches:", matches)
```

**Output**:

```plaintext
Hexadecimal Matches: ['1a2b', 'deadbeef', '01234567']
```

#### Explanation 🌟

- **`[a-f0-9]`**: This part defines the range of characters that can appear in a hexadecimal number.
- **`{1,8}`**: Limits the number of allowed characters to between 1 and 8.

#### 3. Match a 32-bit Hexadecimal Number with Optional 'h' Suffix 🆎

This is similar to the previous regex but allows an optional `'h'` at the end using `h?`.

**Regex Pattern**: `\b[a-f0-9]{1,8}h?\b` (Case insensitive)

- **`h?`**: Matches an `'h'` zero or one time (optional).

**Python Code Example**:

```python
# Match a 32-bit hexadecimal number with optional 'h'
regex_hex_suffix = r'\b[a-f0-9]{1,8}h?\b'

text = "Hex numbers: 1a2bh, deadbeef, 01234567h."

matches = re.findall(regex_hex_suffix, text, re.IGNORECASE)
print("Hexadecimal Matches with 'h' suffix:", matches)
```

**Output**:

```plaintext
Hexadecimal Matches with 'h' suffix: ['1a2bh', 'deadbeef', '01234567h']
```

#### Explanation 🌟

- **`h?`**: Makes the 'h' suffix optional. If 'h' is present, it matches; if not, it still matches.

#### 4. Match a Floating-Point Number 🌊

A **floating-point number** has a mandatory decimal part and an optional exponent.

**Regex Pattern**: `\d*\.\d+(e\d+)?`

- **`\d*`**: Matches zero or more digits (optional integer part).
- **`\.\d+`**: Matches a mandatory decimal point followed by one or more digits (fractional part).
- **`(e\d+)?`**: Matches an optional exponent part (like `e10`).

**Python Code Example**:

```python
# Match a floating-point number
regex_float = r'\d*\.\d+(?:e\d+)?'

text = "Floating-point numbers: 0.5, 1.23e10, .75."

matches = re.findall(regex_float, text)
```

**Output**:

```plaintext
Floating-Point Matches: ['0.5', '1.23e10', '.75']
```

#### Explanation 🌟

- **`\d*\.\d+`**: Ensures the number has a decimal point and some digits after it.
- **`(?:e\d+)?`**: The exponent part (like `e10`) is optional. If it’s there, it matches; if not, it still matches.

### Summary 🌟

1. **Googol**: Matches exactly 100 digits.
2. **Hexadecimal Number**: Matches 1 to 8 digits in hexadecimal format.
3. **Hexadecimal Number with 'h' Suffix**: Same as above but may end with 'h'.
4. **Floating-Point Number**: Matches numbers with decimals and optional exponents.

---

## Problem 2.3 🚩
### Choose Minimal or Maximal Repetition 🔄

Match a pair of `<p>` and `</p>` XHTML tags and the text between them. The text between the tags may contain other XHTML tags.

### Explanation 🌟

Regular expressions can be **greedy** or **lazy** when matching patterns. 

- **Greedy Quantifiers** (like `*`, `+`, `{n,m}`) try to match as much as possible.
- **Lazy Quantifiers** (like `*?`, `+?`, `{n,m}?`) match as little as possible.

To correctly match a pair of `<p>` and `</p>` tags with everything between them (including other tags), we need a **lazy** quantifier to ensure it stops at the first `</p>` after `<p>`.

### Solution 🛠️

#### Correct Regex to Match Text Between `<p>` and `</p>` Tags 📝

**Regex Pattern**: `<p>.*?</p>`

- **`<p>`**: Matches the opening `<p>` tag.
- **`.*?`**: Matches any character (including newlines) **as few times as possible**.
- **`</p>`**: Matches the closing `</p>` tag.

The `.*?` is a **lazy quantifier**; it matches the least amount of text needed to satisfy the pattern. This prevents it from matching everything from the first `<p>` to the last `</p>`.

#### Python Code Example

```python
import re

# Correct regex to match text between <p> and </p> tags
regex_lazy = r'<p>.*?</p>'

text = """
<p>
The very <em>first</em> task is to find the beginning of a paragraph.
</p>
<p>
Then you have to find the end of the paragraph
</p>
"""

# Find all matches for text between <p> and </p> tags
matches = re.findall(regex_lazy, text, re.DOTALL)
print("Matched Paragraphs:", matches)
```

**Output 📤**

```plaintext
Matched Paragraphs: ['<p>\nThe very <em>first</em> task is to find the beginning of a paragraph.\n</p>', '<p>\nThen you have to find the end of the paragraph\n</p>']
```

### Explanation 🌟

- **`.*?`**: This lazy quantifier makes sure we match **only up to the nearest `</p>`**, rather than greedily matching everything up to the last `</p>`.

### Summary 🌟

- **Lazy Quantifiers (`*?`, `+?`)** are used when you want to match **as little as possible**.
- **Greedy Quantifiers (`*`, `+`)** match **as much as possible**.
- Use **`.*?`** to match text between tags like `<p>` and `</p>` without over-matching.


---

## Problem 2.4 🚩
### Eliminate Needless Backtracking 

When writing regular expressions (regex), the pattern sometimes performs **unnecessary backtracking**, which can slow down matching. We want to make a regex more efficient by eliminating this backtracking.

For example, consider these two regex patterns:

1. **Greedy Quantifier:** `\b\d+\b`
2. **Lazy Quantifier:** `\b\d+?\b`

Both patterns are used to match integers (whole numbers). Given the same text, they both find the exact same matches, but both can backtrack unnecessarily, making the matching process slower.

### Explanation 🌟

#### What is Backtracking?

When a regex engine tries to match a pattern, it sometimes tries many possibilities to find a match. If it doesn't find a match, it "backtracks" (goes back) to try different possibilities. This process is called **backtracking**.

Backtracking can make a regex slow, especially if the pattern is complex or has overlapping options. We want to avoid unnecessary backtracking to make our regex faster and more efficient.

#### Types of Quantifiers in Regex

1. **Greedy Quantifiers (`+`, `*`, `{n,m}`):** Try to match as much text as possible.
2. **Lazy Quantifiers (`+?`, `*?`, `{n,m}?`):** Try to match as little text as possible.
3. **Possessive Quantifiers (`++`, `*+`, `{n,m}+`):** Match as much as possible **without** backtracking. These are not supported in Python.

### How to Optimize Regex in Python

Python does not support **possessive quantifiers** (which prevent backtracking completely). However, we can still optimize regex by:

1. **Using Simple and Specific Patterns:** Make your regex as straightforward as possible.
2. **Avoiding Overlapping Patterns:** Overlapping patterns force the regex engine to try many combinations, leading to more backtracking.

### Example: Matching Integers Efficiently 📝

Let’s look at matching integers (whole numbers) surrounded by word boundaries using different quantifiers:

1. **Greedy Pattern (`\b\d+\b`):** Matches as many digits as possible.
2. **Lazy Pattern (`\b\d+?\b`):** Matches as few digits as possible, then expands if needed.

Both patterns work, but both can still backtrack in Python.

#### Python Code Example

```python
import re

# Example text with numbers and letters
text = "123abc 456"

# Greedy quantifier example
regex_greedy = r'\b\d+\b'
matches_greedy = re.findall(regex_greedy, text)
print("Greedy Matches:", matches_greedy)

# Lazy quantifier example
regex_lazy = r'\b\d+?\b'
matches_lazy = re.findall(regex_lazy, text)
print("Lazy Matches:", matches_lazy)
```

**Expected Output 📤**

```plaintext
Greedy Matches: ['123', '456']
Lazy Matches: ['123', '456']
```

#### Explanation of Output

- **Greedy Pattern (`\b\d+\b`):** Matches '123' and '456' by trying to match as many digits as possible and stops at word boundaries (`\b`).
- **Lazy Pattern (`\b\d+?\b`):** Also matches '123' and '456', but it starts by matching the smallest possible number of digits and expands as needed.

### Key Takeaways

- **Greedy Quantifiers** match as much as possible.
- **Lazy Quantifiers** match as little as possible.
- **Possessive Quantifiers** (which avoid all backtracking) are not supported in Python.

---

## Problem 2.5 🚩
### Prevent Runaway Repetition 🚫
Sometimes, when using regex patterns that repeat (like `.*?`), the regex engine might take a very long time to match, or even crash, if the pattern can't be fully matched. This happens when it tries **all possible ways** to match the pattern, a situation known as **catastrophic backtracking**.

### Example of the Problem:

Imagine we have this regex to match HTML content:

```regex
<.*?></html>
```

- This pattern matches anything until it finds `</html>`.
- If the `</html>` tag is **missing** in the text, the `.*?` part keeps expanding, trying every possible match, which can cause serious performance problems.

### Solution: Use Atomic Grouping to Prevent Backtracking 🛠️

To avoid this problem, we can use **atomic grouping** to "lock" matches so that the regex engine doesn’t go back to try other possibilities if it fails later.

#### What is Atomic Grouping?

An **atomic group** `(? >...)` is like a “don’t look back” rule. Once the regex engine matches something inside an atomic group, it won't reconsider it even if it fails to match later parts.

### How to Apply Atomic Grouping

Instead of this problematic regex:

```regex
<.*?></html>
```

We use:

```regex
(?>.*?</body>)</html>
```

- Here, `(?>.*?</body>)` is an **atomic group**. It matches everything up to `</body>` and **won't backtrack** if the `</html>` is missing.

### Python Code Example 🐍

Let’s see how this works in Python:

```python
import re

# Sample HTML text where the </html> tag is missing
text = """
<html>
  <body>
    Some content here.
  </body>
  <div>
    More content without closing the HTML tag.
"""

# Regex with atomic grouping to prevent runaway repetition
regex_atomic = r'(?>.*?</body>)</html>'

# Try to find matches
matches_atomic = re.findall(regex_atomic, text, re.DOTALL)
print("Matches with Atomic Grouping:", matches_atomic)
```

**Expected Output 📤**

```plaintext
Matches with Atomic Grouping: []
```

### Explanation 🌟

- **`(?>.*?</body>)`**: Matches everything up to `</body>`. If `</html>` isn’t found, it **doesn’t** go back to retry matching `.*?`. This prevents unnecessary backtracking.
- **`</html>`**: This part tries to match `</html>` after `</body>`. If it isn’t there, the regex fails right away, avoiding performance issues.

### Why Use Atomic Grouping?

1. **Prevents Catastrophic Backtracking**: Stops the regex engine from wasting time trying all possible matches.
2. **Improves Performance**: Makes the regex run faster and more efficiently.

### Key Takeaway 🌟

When you have repeating patterns that can cause excessive backtracking, use **atomic grouping** `(?>...)` to make your regex more efficient and safe from performance issues.

---

## Problem 2.6 🚩
### Test for a Match Without Including It in the Overall Match 🎯


We want to find any word that appears between a pair of HTML bold tags (`<b>` and `</b>`) **without including the tags** in the match result. For example, in the string `"My <b>cat</b> is furry"`, the match should only be `"cat"`.

### Solution 🛠️

We can use **lookaround assertions** (specifically, lookbehind and lookahead) to solve this problem. Lookaround assertions allow us to check for text **before** or **after** our match without including it in the result.

#### Regex Pattern:

```regex
(?<=<b>)\w+(?=</b>)
```

- **`(?<=<b>)`**: Positive **lookbehind**. This checks that `<b>` appears **before** the word we want to match.
- **`\w+`**: Matches **one or more word characters** (letters, digits, and underscores).
- **`(?=</b>)`**: Positive **lookahead**. This checks that `</b>` appears **after** the word we want to match.

### Python Code Example 🐍

Let's implement this in Python:

```python
import re

# Sample text with bold tags
text = "My <b>cat</b> is furry"

# Regex pattern with lookbehind and lookahead
regex_pattern = r"(?<=<b>)\w+(?=</b>)"

# Find matches
matches = re.findall(regex_pattern, text)
print("Matches:", matches)
```

**Expected Output 📤**

```plaintext
Matches: ['cat']
```

### Explanation 🌟

1. **`(?<=<b>)`**: This part checks that `<b>` is immediately before the word but doesn't include it in the match.
2. **`\w+`**: Matches the word itself (like "cat").
3. **`(?=</b>)`**: This part checks that `</b>` is immediately after the word but doesn't include it in the match.

### Additional Information: Lookaround Assertions

- **Lookbehind (`(?<=...)`)**: Checks if a certain pattern is **behind** the current position.
- **Lookahead (`(?=...)`)**: Checks if a certain pattern is **ahead** of the current position.
- Both lookahead and lookbehind **do not consume characters** in the match; they just "assert" conditions.

### Alternative Solution Without Lookbehind 🔄

If you're using a regex flavor that doesn't support lookbehind (like JavaScript), you can use **capturing groups**:

#### Regex Pattern:

```regex
<b>(\w+)(?=</b>)
```

- **`<b>`**: Matches the opening tag.
- **`(\w+)`**: Captures the word in a group.
- **`(?=</b>)`**: Lookahead to ensure `</b>` follows.

#### Python Code Example:

```python
import re

# Sample text with bold tags
text = "My <b>cat</b> is furry"

# Regex pattern with capturing group
regex_pattern = r"<b>(\w+)(?=</b>)"

# Find matches
matches = re.findall(regex_pattern, text)
print("Matches without lookbehind:", matches)
```

**Expected Output 📤**

```plaintext
Matches without lookbehind: ['cat']
```

### Explanation 🌟

- **`<b>(\w+)`**: Captures the word after `<b>`.
- **`(?=</b>)`**: Ensures `</b>` is present after the word, but doesn't include it in the match.

---

## Problem 2.7 🚩
### Match One of Two Alternatives Based on a Condition 🛠️

Create a regular expression to match a **comma-delimited list** containing the words `one`, `two`, and `three`. Each word can appear any number of times and in any order, but **each word must appear at least once**.

### Solution 🛠️

To solve this, we use a combination of **capturing groups** and **conditional statements** in regex. This allows us to check if each word appears at least once.

### Regex Pattern

```regex
\b(?:(?:(one)|(two)|(three))(?:,|\b)){3,}(?(1)|(?!))(?(2)|(?!))(?(3)|(?!))
```

#### Explanation:

1. **`\b`**: Word boundary to ensure we match whole words.
   
2. **`(?:(one)|(two)|(three))`**: Matches **one**, **two**, or **three** and captures them in separate capturing groups:
   - **`(one)`**: Capturing group 1.
   - **`(two)`**: Capturing group 2.
   - **`(three)`**: Capturing group 3.

3. **`(?:,|\b)`**: Matches either a comma `,` or a word boundary `\b` to separate the words.

4. **`{3,}`**: Ensures the group matches **at least 3 times** because there are three words that must each appear at least once.

5. **`(?(1)|(?!))`**: Conditional statement to check if **capturing group 1** (i.e., `one`) has matched. If not, the regex fails with `(?!)` (a negative lookahead that always fails).

6. **`(?(2)|(?!))`** and **`(?(3)|(?!))`**: Similar checks for **capturing group 2** (`two`) and **capturing group 3** (`three`), respectively.

### Python Code Example 🐍

Here’s how to implement it in Python:

```python
import re

# Sample list of comma-separated words
text = "one,two,three,one,two"

# Regex pattern with conditionals to ensure each word appears at least once
regex_pattern = r'\b(?:(?:(one)|(two)|(three))(?:,|\b)){3,}(?(1)|(?!))(?(2)|(?!))(?(3)|(?!))'

# Test for matches
match = re.match(regex_pattern, text)

# Check if the pattern matched the text
if match:
    print("Valid match: All three words are present at least once.")
else:
    print("Invalid match: Not all three words are present.")
```

**Expected Output 📤**

```plaintext
Valid match: All three words are present at least once.
```

### Explanation 🌟

1. **Word Matching with Alternation:** The regex uses `one|two|three` inside a non-capturing group `(?:...)` to match any of the three words.
2. **Counting Matches with `{3,}`:** We use `{3,}` to ensure that the three words appear at least three times combined, but in any order.
3. **Conditionals to Check Each Word Appears:** The conditionals `(?(1)|(?!))`, `(?(2)|(?!))`, and `(?(3)|(?!))` ensure each capturing group (corresponding to `one`, `two`, and `three`) has matched at least once.

### Simpler Alternative for Languages Without Conditional Support 🔄

If you're using a language like JavaScript or Ruby that doesn’t support conditionals in regex, you can use a simpler regex and write some extra code to check if all words are present:

```regex
\b(?:(one|two|three)(?:,|\b)){3,}
```

#### Python Code Example:

```python
import re

# Sample list of comma-separated words
text = "one,two,three,one,two"

# Regex pattern without conditionals
regex_pattern_simple = r'\b(?:(one|two|three)(?:,|\b)){3,}'

# Test for matches
matches = re.findall(regex_pattern_simple, text)

# Check if all three words are present
if set(matches) == {'one', 'two', 'three'}:
    print("Valid match: All three words are present at least once.")
else:
    print("Invalid match: Not all three words are present.")
```

**Expected Output 📤**

```plaintext
Valid match: All three words are present at least once.
```
---


## Problem 2.8 🚩
### Add Comments to a Regular Expression 📝

We have a regular expression `\d{4}-\d{2}-\d{2}` that matches a date in `yyyy-mm-dd` format. We want to add comments to this regex to explain what each part does.

### Solution 🛠️

To make the regex more understandable, we can add comments directly inside the regex using **free-spacing mode**. This mode allows us to ignore whitespace and add comments for better readability.

### Free-Spacing Mode in Python

In Python, you can enable **free-spacing mode** using `re.VERBOSE`. This allows you to add whitespace and comments inside the regex for clarity.

### Commented Regular Expression

Here’s the regular expression with comments:

```python
import re

# Regular expression with comments using free-spacing mode
regex_pattern = r'''
    \d{4}  # Year (four digits)
    -      # Separator (hyphen)
    \d{2}  # Month (two digits)
    -      # Separator (hyphen)
    \d{2}  # Day (two digits)
'''

# Sample text
text = "The date is 2024-08-19."

# Finding matches with re.VERBOSE to allow comments and spaces
matches = re.findall(regex_pattern, text, re.VERBOSE)
print("Matches:", matches)
```

### Explanation 🌟

1. **`\d{4}`**: Matches **four digits** representing the year.
2. **`-`**: Matches the **hyphen** separator.
3. **`\d{2}`**: Matches **two digits** representing the month.
4. **`-`**: Matches another **hyphen** separator.
5. **`\d{2}`**: Matches **two digits** representing the day.

### Expected Output 📤

```plaintext
Matches: ['2024-08-19']
```

### Discussion on Free-Spacing Mode

- **Free-spacing mode** allows you to use spaces and comments for better readability.
- **Comments** start with a `#` and run to the end of the line.
- **Whitespace** (spaces, tabs, and line breaks) outside character classes is ignored.

### Alternative: Using Inline Comments `(?#...)`

If you cannot or prefer not to use free-spacing mode, you can use **inline comments** with the syntax `(?#...)`:

#### Example with Inline Comments

```python
import re

# Regular expression with inline comments
regex_pattern = r'(?#Year)\d{4}-(?#Separator)\d{2}-(?#Day)\d{2}'

# Sample text
text = "The date is 2024-08-19."

# Finding matches without re.VERBOSE
matches = re.findall(regex_pattern, text)
print("Matches with inline comments:", matches)
```

### Expected Output 📤

```plaintext
Matches with inline comments: ['2024-08-19']
```
---

## Problem 2.9 🚩

### Insert Literal Text into the Replacement Text ✍️

Perform a search-and-replace where any regex match is replaced **literally** with the text `$%\*$1\1`.

### Solution 🛠️

To achieve this in Python, we need to understand how **special characters** work in replacement text. In Python, special characters like `$` and `\` are used for backreferences and need to be **escaped** properly to treat them as **literal characters**.

### Correct Replacement Text for Python

In Python, to replace a regex match with the literal text `$%\*$1\1`, the replacement string should be:

```python
replacement_text = r"$%\*$1\\1"
```

Here's the breakdown:
- **`$%`**: `$` and `%` are literal characters.
- **`\*`**: The backslash `\` is used to escape the `*`, making it literal.
- **`$1`**: A **backreference** to the first captured group in regex.
- **`\\1`**: The backslash `\` needs to be escaped to remain literal, and `\1` is another backreference to the first captured group.

### Python Code Example 🐍

Below is the Python code to perform the search-and-replace:

```python
import re

# Sample text to perform search-and-replace
text = "This is a test: 123-456."

# Regex pattern to match any three-digit number
regex_pattern = r"\d{3}"

# Replacement text: insert literal text including backreferences
replacement_text = r"$%\*$1\\1"

# Perform search-and-replace
# `re.sub` is used to substitute matches with replacement text
result = re.sub(regex_pattern, replacement_text, text)

print("Result after replacement:", result)
```

### Expected Output 📤

```plaintext
Result after replacement: This is a test: $%*$1\1123-$%*$1\1456.
```

### Explanation 🌟

1. **Regex Pattern (`\d{3}`):** Matches any three-digit number.
2. **Replacement Text (`$%\*$1\\1`):** Replaces the matched text with the literal characters:
   - **`$%`**: Just as they are.
   - **`\*`**: An asterisk `*` after escaping the backslash.
   - **`$1`**: Inserts the matched text (first capturing group) back into the result.
   - **`\\1`**: Adds a literal backslash followed by the matched text (first capturing group).

### Key Points

- **Backslashes (`\`) need to be escaped** with another backslash in the replacement string if they are meant to be literal.
- **Dollar signs (`$`) have no special meaning in Python replacement strings** but need escaping in other languages (e.g., Java).

---


## Problem 3.0 🚩
### Insert the Whole Regex Match into Replacement Text ✍️

Insert the entire match of a regex back into the replacement text to modify or wrap it with additional text. For example, if a regex matches some text, you might want to wrap it with an HTML `<a>` tag.

### Solution for Python 🛠️

In Python, to insert the **entire regex match** back into the replacement text, you use the **zeroth capturing group**: `\g<0>`. This group represents the entire match.

### Python Replacement Example

Suppose you want to wrap any matched text with an `<a>` HTML tag. Here is how you can achieve it:

#### Regex Replacement Syntax for Python

```python
import re

# Sample text where we want to wrap matches in <a> tags
text = "Visit example.com for more info."

# Regex pattern to match words (simple example)
regex_pattern = r"\b\w+\b"

# Replacement text: wrap the entire match (group 0) with an <a> tag
replacement_text = r'<a href="\g<0>">\g<0></a>'

# Perform search-and-replace
result = re.sub(regex_pattern, replacement_text, text)

print("Result after replacement:", result)
```

### Explanation 🌟

1. **Regex Pattern (`\b\w+\b`)**:
   - Matches any word (sequence of word characters) in the text.

2. **Replacement Text (`<a href="\g<0>">\g<0></a>`)**:
   - **`\g<0>`**: Inserts the entire matched text. Python uses the syntax `\g<0>` to refer to the entire match.
   - The replacement text wraps the matched text in an `<a>` tag with the match as both the `href` attribute and the link text.

### Expected Output 📤

```plaintext
Result after replacement: <a href="Visit">Visit</a> <a href="example">example</a>.<a href="com">com</a> <a href="for">for</a> <a href="more">more</a> <a href="info">info</a>.
```

### Discussion

- **Python Replacement Syntax (`\g<0>`)**: Python uses named capturing syntax `\g<0>` to reference the entire match because it doesn’t support `\0` directly.
- **Other Languages**:
  - In **PHP** and **Ruby**, different escape rules apply, like `\0` or `\&` for the entire match.
  - In **Perl**, `$&` is used, but it has performance penalties.

### Key Takeaway 🌟

- Using `\g<0>` in Python replacement text allows you to insert the entire regex match, making it easy to wrap or modify matches without additional capturing groups.

---

## Problem 3.1 🚩
### Insert Part of the Regex Match into the Replacement Text 🔄

Match any contiguous sequence of 10 digits (like `1234567890`) and convert it into a nicely formatted phone number like `(123) 456-7890`.

### Solution 🛠️

To achieve this, we can use **capturing groups** in our regular expression to match specific parts of the 10-digit number. Then, we use those groups in the replacement text to format the number.

### Regular Expression and Replacement Text for Python

#### Regular Expression:

```regex
\b(\d{3})(\d{3})(\d{4})\b
```

- **`\b`**: Word boundary to ensure whole words are matched.
- **`(\d{3})`**: Matches the **first three digits** and captures them in **Group 1**.
- **`(\d{3})`**: Matches the **next three digits** and captures them in **Group 2**.
- **`(\d{4})`**: Matches the **last four digits** and captures them in **Group 3**.
- **`\b`**: Word boundary to end the match.

#### Replacement Text for Python:

```text
(\1) \2-\3
```

- **`\1`**: Refers to the **first capturing group** (the area code).
- **`\2`**: Refers to the **second capturing group** (the first part of the number).
- **`\3`**: Refers to the **third capturing group** (the last part of the number).

### Python Code Example 🐍

```python
import re

# Sample text containing a 10-digit number
text = "My number is 1234567890, please call me!"

# Regex pattern to match a 10-digit phone number
regex_pattern = r"\b(\d{3})(\d{3})(\d{4})\b"

# Replacement pattern to format the matched phone number
replacement_text = r"(\1) \2-\3"

# Perform search-and-replace using re.sub()
formatted_text = re.sub(regex_pattern, replacement_text, text)

print("Formatted text:", formatted_text)
```

### Expected Output 📤

```plaintext
Formatted text: My number is (123) 456-7890, please call me!
```

### Explanation 🌟

1. **Regex Pattern (`\b(\d{3})(\d{3})(\d{4})\b`)**:
   - Matches any 10-digit number by breaking it down into three groups of three, three, and four digits.

2. **Replacement Text (`(\1) \2-\3`)**:
   - Uses backreferences (`\1`, `\2`, `\3`) to refer to the matched groups and formats them as `(123) 456-7890`.

### Named Capturing Groups in Python 🐍

Python also supports **named capturing groups** in regex. This allows you to reference the matched text by name instead of a number.

#### Regex with Named Groups:

```regex
\b(?P<area>\d{3})(?P<exchange>\d{3})(?P<number>\d{4})\b
```

- **`(?P<area>\d{3})`**: Captures the first three digits as the **area**.
- **`(?P<exchange>\d{3})`**: Captures the next three digits as the **exchange**.
- **`(?P<number>\d{4})`**: Captures the last four digits as the **number**.

#### Replacement Text with Named Groups:

```text
(\g<area>) \g<exchange>-\g<number>
```

- **`\g<area>`**: References the **named capturing group** `area`.
- **`\g<exchange>`**: References the **named capturing group** `exchange`.
- **`\g<number>`**: References the **named capturing group** `number`.

### Python Code Example with Named Groups 🐍

```python
import re

# Sample text containing a 10-digit number
text = "My number is 1234567890, please call me!"

# Regex pattern with named capturing groups
regex_pattern = r"\b(?P<area>\d{3})(?P<exchange>\d{3})(?P<number>\d{4})\b"

# Replacement pattern using named groups
replacement_text = r"(\g<area>) \g<exchange>-\g<number>"

# Perform search-and-replace using re.sub()
formatted_text = re.sub(regex_pattern, replacement_text, text)

print("Formatted text with named groups:", formatted_text)
```

### Expected Output 📤

```plaintext
Formatted text with named groups: My number is (123) 456-7890, please call me!
```

---

## Problem 3.2 🚩
### Insert Match Context into the Replacement Text 🔄

Create replacement text that replaces a regex match with the text **before** the match, followed by the **whole subject text**, and then the text **after** the match.

For example, if the word "Match" is found in the string "BeforeMatchAfter," the replacement should result in "BeforeBeforeMatchAfterAfter," producing "BeforeBeforeBeforeMatchAfterAfterAfter."

### Solution for Python 🛠️

Unlike .NET or Perl, Python does not have built-in tokens like `$`, `$'`, and `$_` to directly insert the left context, right context, or whole subject text into the replacement text. However, we can achieve this by using Python’s powerful **regular expression** and **string manipulation** capabilities.

### Approach

1. **Use capturing groups** in the regex to capture the **left context**, **matched text**, and **right context**.
2. **Recompose** the desired replacement using the captured groups.

### Python Code Example 🐍

Below is the Python code to accomplish the task:

```python
import re

# Sample text where "Match" is the regex match
text = "BeforeMatchAfter"

# Regex pattern to capture the left context, the match, and the right context
regex_pattern = r"(.*?)(Match)(.*)"

# Replacement function to construct the desired replacement text
def replacement_function(match):
    # Group 1: Left context (text before the match)
    left_context = match.group(1)
    # Group 2: The regex match (the word "Match")
    matched_text = match.group(2)
    # Group 3: Right context (text after the match)
    right_context = match.group(3)
    
    # Construct the replacement text: Left + Whole + Right
    return f"{left_context}{left_context}{matched_text}{right_context}{right_context}"

# Perform the search-and-replace using re.sub()
result = re.sub(regex_pattern, replacement_function, text)

print("Result after replacement:", result)
```

### Expected Output 📤

```plaintext
Result after replacement: BeforeBeforeBeforeMatchAfterAfterAfter
```

### Explanation 🌟

1. **Regex Pattern (`(.*?)(Match)(.*)`)**:
   - **`(.*?)`**: Captures any text before the match (`Match`). This is the **left context**.
   - **`(Match)`**: Captures the exact word "Match." This is the **matched text**.
   - **`(.*)`**: Captures any text after the match (`Match`). This is the **right context**.

2. **Replacement Function (`replacement_function`)**:
   - Takes the match object and extracts **left context**, **matched text**, and **right context**.
   - Reconstructs the desired text by concatenating the left context twice, the whole subject, and the right context twice.

3. **`re.sub()` with a Function**:
   - The `re.sub()` function in Python allows us to use a function to generate the replacement text dynamically.

---