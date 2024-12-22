# Problem 3.1 🚩  Literal Regular Expressions in Source Code 
 
## Hardcoding Regular Expression into Source Code ✨
You have been given the regular expression `[$"'\n\d/\\]` as the solution to a problem. This regular expression consists of a single character class that matches a dollar sign, a double quote, a single quote, a line feed, any digit between 0 and 9, a forward slash, or a backslash. You want to hardcode this regular expression into your source code as a string constant or regular expression operator.

This exercise helps us understand how to embed regular expressions into our code properly, ensuring that special characters are correctly escaped. Let's break it down in a detailed way! 🕵️‍♂️

## Solution 🛠️

To match this regular expression exactly, we need a **string constant** or **regular expression operator** like this:

```python
import re

# String constant representing the regular expression
regex_pattern = r'[$"\'\n\d/\\]'

# Compiling the regular expression
compiled_regex = re.compile(regex_pattern)

# Example text to search within
example_text = 'Here is a test string: $ " \' \n 5 / \\'

# Performing the match
matches = compiled_regex.findall(example_text)

# Printing the matches
print("Matches found:", matches)
```

🧐 Here’s what this means:

- **Special Characters Escaped** 🛡️: Some characters have special roles in regular expressions. To match them **literally** (as they appear), we need to put a backslash `\` before them. For example:
  - `$` becomes `\$`
  - `"` becomes `\"`
  - `'` becomes `\'`
  - `\` becomes `\\`

- **Normal Characters Match Themselves** 🔠: Characters like digits (`0-9`) and some punctuation marks (like `/`) match themselves directly without any extra rules.

## Explanation 🌟

A **regular expression** (regex) can be thought of as a "search pattern" 🔍. It helps you find specific sequences of text in a larger body of text 📖.

When we want to match text **exactly** as it is in a regular expression, we need to consider certain characters that have special meanings, known as **metacharacters** 🚀. Here are the most common ones:

- **Metacharacters**: `$`, `(`, `)`, `*`, `+`, `.`, `?`, `[`, `\`, `^`, `{`, `|`
  - These characters have special meanings in regex. For instance, `*` means "zero or more of the previous character."
  - To match these characters **exactly**, we use a backslash `\` to "escape" them 🏃‍♂️.

### Example:

If we want to search for the string `[$"'\n\d/\\]`, we use the regex:

```regex
\[\$\"\''\\n\\d\/\\\\\]
```

💡 Each metacharacter has a backslash `\` before it to indicate that we want the **literal** character, not its special function. 🚀

## Tips for Beginners 🐣

- **Don’t Over-Escape!** 🚫: Avoid adding too many backslashes (`\`). Over-escaping can make your regex harder to read and understand 🕵️‍♂️. Only escape characters that need it!

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

To match the exact pattern using the provided regular expression and embed it into source code, you can use Python's `re` module. Here's the code to achieve this:

```python
import re

# The regular expression pattern as a string constant
regex_pattern = r'[$"\'\n\d/\\]'

# Compiling the regular expression
compiled_regex = re.compile(regex_pattern)

# Example text to search within
example_text = 'Here is a test string: $ " \' \n 5 / \\'

# Performing the match
matches = compiled_regex.findall(example_text)

# Printing the matches
print("Matches found:", matches)
```

### Explanation:
1. **`import re`**: Imports Python's regular expression library.
2. **`regex_pattern`**: The regular expression pattern provided as a raw string.
3. **`re.compile()`**: Compiles the regular expression pattern into a regex object.
4. **`example_text`**: Example text to demonstrate the pattern matching.
5. **`compiled_regex.findall()`**: Finds all matches in the example text.
6. **`print()`**: Prints the matches found in the text.

---
# Problem 3.2 🚩   Import the Regular Expression Library 

## Importing the Regular Expression Library ✨
To be able to use regular expressions in your application, you want to import the regular expression library or namespace into your source code.

This exercise helps us understand how to prepare our code for using regular expressions by importing the necessary libraries. Let's break it down in a detailed way! 🕵️‍♂️

## Solution 🛠️

To use regular expressions in Python, we can import the `re` module, which provides support for working with regular expressions.

### Example in Python:

```python
# Importing the regular expression library
import re

# String constant representing the regular expression
regex_pattern = r'[$"\'\n\d/\\]'

# Compiling the regular expression
compiled_regex = re.compile(regex_pattern)

# Example text to search within
example_text = 'Here is a test string: $ " \' \n 5 / \\'

# Performing the match
matches = compiled_regex.findall(example_text)

# Printing the matches
print("Matches found:", matches)
```

🧐 Here’s what this means:

- **Importing the Library** 🛡️: We import the `re` module using `import re`. This makes the functions and classes in the `re` module available for use in our code.
- **Using Regular Expressions**: Once the library is imported, we can use functions like `re.compile()` to create regex objects and methods like `findall()` to search for matches in text.

## Explanation 🌟

### Why Import Libraries?

Libraries provide pre-written code that helps you accomplish common tasks without having to write everything from scratch. In the case of regular expressions, the `re` module in Python provides functions to create, compile, and work with regular expressions efficiently.

### Example:

If we want to search for the string `[$"'\n\d/\\]`, we use the regex as shown in the example.

## Tips for Beginners 🐣

- **Start Simple**: Begin with simple regular expressions and gradually move to more complex ones.
- **Practice**: Regular expressions can be tricky. Practice by writing and testing different patterns.

## Case-Insensitive Matching 🔠

Regular expressions are **case-sensitive** by default. To make them case-insensitive, you can use the `re.IGNORECASE` flag:

```python
import re

# Compiling the regular expression with case insensitivity
compiled_regex = re.compile(r'pattern', re.IGNORECASE)
```

This will make the regex match patterns regardless of case.

### Explanation:
1. **`import re`**: This line imports the regular expression library in Python.
2. **`regex_pattern`**: The regular expression pattern provided as a raw string.
3. **`re.compile()`**: Compiles the regular expression pattern into a regex object.
4. **`example_text`**: Example text to demonstrate the pattern matching.
5. **`compiled_regex.findall()`**: Finds all matches in the example text.
6. **`print()`**: Prints the matches found in the text.

---
# Problem 3.3  Create Regular Expression Objects  🚩
## Compiling Regular Expressions for Efficient Use ✨
You want to instantiate a regular expression object or otherwise compile a regular expression so you can use it efficiently throughout your application.

This exercise helps us understand how to compile regular expressions for repeated use, which improves performance and readability. Let's break it down in a detailed way! 🕵️‍♂️

## Solution 🛠️

To compile a regular expression in Python, we use the `re.compile()` function. This allows us to create a regex object that can be used multiple times without recompiling the pattern each time.

### Example in Python:

```python
import re

# String constant representing the regular expression
regex_pattern = r'[$"\'\n\d/\\]'

# Compiling the regular expression
compiled_regex = re.compile(regex_pattern)

# Example text to search within
example_text = 'Here is a test string: $ " \' \n 5 / \\'

# Performing the match
matches = compiled_regex.findall(example_text)

# Printing the matches
print("Matches found:", matches)
```

🧐 Here’s what this means:

- **Compiling the Regular Expression** 🛡️: We use `re.compile()` to compile the regular expression pattern into a regex object. This compiled object can be used for matching operations, which is more efficient than re-compiling the pattern each time.
- **Using the Compiled Regex**: We can use methods like `findall()` on the compiled regex object to find matches in a given text.

## Explanation 🌟

### Why Compile Regular Expressions?

Compiling regular expressions is beneficial when you need to use the same pattern multiple times. It improves performance because the pattern is parsed and transformed into an internal format once, rather than each time the pattern is used.

### Example:

If we want to search for the string `[$"'\n\d/\\]`, we compile the regex pattern and use it as shown in the example.

## Tips for Beginners 🐣

- **Compile Once, Use Often**: Compile your regular expressions once and use the compiled object multiple times to improve performance.
- **Maintain Readability**: Compiling regular expressions makes your code cleaner and easier to read, especially when dealing with complex patterns.

## Case-Insensitive Matching 🔠

To make a compiled regex case-insensitive, use the `re.IGNORECASE` flag:

```python
import re

# Compiling the regular expression with case insensitivity
compiled_regex = re.compile(r'[$"\'\n\d/\\]', re.IGNORECASE)
```

This will make the regex match patterns regardless of case.

### Explanation:
1. **`import re`**: This line imports the regular expression library in Python.
2. **`regex_pattern`**: The regular expression pattern provided as a raw string.
3. **`re.compile()`**: Compiles the regular expression pattern into a regex object.
4. **`example_text`**: Example text to demonstrate the pattern matching.
5. **`compiled_regex.findall()`**: Finds all matches in the example text.
6. **`print()`**: Prints the matches found in the text.

---
# Problem 3.4  Set Regular Expression Options  🚩
## Compiling a Regular Expression with All Matching Modes ✨
You want to compile a regular expression with all of the available matching modes: free-spacing, case insensitive, dot matches line breaks, and “^ and $ match at line breaks.”

This exercise helps us understand how to set various matching modes when compiling regular expressions, enhancing their flexibility and power. Let's break it down in a detailed way! 🕵️‍♂️

## Solution 🛠️

To compile a regular expression with all the available matching modes in Python, we use the `re.compile()` function along with several flags: `re.VERBOSE`, `re.IGNORECASE`, `re.DOTALL`, and `re.MULTILINE`.

### Example in Python:

```python
import re

# String constant representing the regular expression
regex_pattern = r'''
    [$"'\n\d/\\]  # Matches a dollar sign, double quote, single quote, newline, digit, forward slash, or backslash
'''

# Compiling the regular expression with all matching modes
compiled_regex = re.compile(
    regex_pattern, 
    re.VERBOSE | re.IGNORECASE | re.DOTALL | re.MULTILINE
)

# Example text to search within
example_text = '''Here is a test string:
$ " ' 
5 / \\'''

# Performing the match
matches = compiled_regex.findall(example_text)

# Printing the matches
print("Matches found:", matches)
```

🧐 Here’s what this means:

- **`re.VERBOSE` (free-spacing mode)** 🛡️: Allows the regex pattern to be spread across multiple lines with comments and whitespace for better readability.
- **`re.IGNORECASE` (case insensitive)**: Makes the pattern matching case insensitive.
- **`re.DOTALL` (dot matches line breaks)**: Allows the dot `.` character to match any character, including newline characters.
- **`re.MULTILINE` (“^ and $ match at line breaks”)**: Makes the `^` and `$` anchors match at the start and end of each line, not just the start and end of the entire string.

## Explanation 🌟

### Why Use Matching Modes?

Matching modes enhance the flexibility and readability of regular expressions. They allow you to write more understandable patterns and handle various text scenarios effectively.

### Example:

If we want to search for the string `[$"'\n\d/\\]` with all matching modes, we compile the regex pattern using the appropriate flags as shown in the example.

## Tips for Beginners 🐣

- **Use Comments and Whitespace**: When using `re.VERBOSE`, take advantage of comments and whitespace to make your regular expressions more readable.
- **Combine Flags**: You can combine multiple flags using the bitwise OR operator (`|`).

## Case-Insensitive Matching 🔠

To make a compiled regex case-insensitive, use the `re.IGNORECASE` flag:

```python
import re

# Compiling the regular expression with case insensitivity
compiled_regex = re.compile(r'[$"\'\n\d/\\]', re.IGNORECASE)
```

This will make the regex match patterns regardless of case.

### Explanation:
1. **`import re`**: This line imports the regular expression library in Python.
2. **`regex_pattern`**: The regular expression pattern provided as a raw string, spread across multiple lines with comments.
3. **`re.compile()`**: Compiles the regular expression pattern into a regex object with all the matching modes enabled.
4. **`example_text`**: Example text to demonstrate the pattern matching.
5. **`compiled_regex.findall()`**: Finds all matches in the example text.
6. **`print()`**: Prints the matches found in the text.
