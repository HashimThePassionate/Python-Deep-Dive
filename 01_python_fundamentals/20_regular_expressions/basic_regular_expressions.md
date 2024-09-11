# Matching Literal Text with Regular Expressions ✨

## Problem 2.1 🚩

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

## Problem 2.2 🚩
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

## Problem 2.3 🚩

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

## Problem Statement 2.4 🚩
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