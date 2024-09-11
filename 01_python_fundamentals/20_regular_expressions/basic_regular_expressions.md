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
