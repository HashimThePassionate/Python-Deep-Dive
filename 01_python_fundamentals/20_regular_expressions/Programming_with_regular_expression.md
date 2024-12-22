# Problem 3.1 🚩 

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
# Problem 3.2 🚩 

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
# Problem 3.3 🚩

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
# Problem 3.4 🚩

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

---
# Problem 3.5  🚩

## Checking for a Partial Match with Regular Expressions ✨
You want to check whether a match can be found for a particular regular expression in a particular string. A partial match is sufficient. For instance, the regex `regex pattern` partially matches the string "The regex pattern can be found." You don’t care about any of the details of the match. You just want to know whether the regex matches the string.

This exercise helps us understand how to use regular expressions to check for partial matches within a string. Let's break it down in a detailed way! 🕵️‍♂️

## Solution 🛠️

To check for a partial match in Python, we can use the `re.search()` function. This function scans through a string, looking for any location where the regular expression pattern produces a match.

### Example in Python:

```python
import re

# String constant representing the regular expression
regex_pattern = r'regex pattern'

# The text in which we want to search for the pattern
example_text = 'The regex pattern can be found.'

# Performing the search
match = re.search(regex_pattern, example_text)

# Checking if a match was found
if match:
    print("Match found! ✅")
else:
    print("No match found. ❌")
```

🧐 Here’s what this means:

- **`re.search()`** 🛡️: Searches the string for a match to the regular expression pattern. It returns a match object if a match is found and `None` if no match is found.
- **Checking the Match**: By checking if the `match` object is not `None`, we can determine if a partial match was found.

## Explanation 🌟

### Why Use `re.search()`?

The `re.search()` function is useful for checking if a pattern exists anywhere in the string, not just at the beginning. It allows for more flexible matching compared to `re.match()`, which only checks for matches at the start of the string.

### Example:

If we want to search for the pattern `regex pattern` in the string "The regex pattern can be found.", we use `re.search()` as shown in the example.

## Tips for Beginners 🐣

- **Understand the Difference**: `re.search()` looks for the pattern anywhere in the string, while `re.match()` only looks at the start.
- **Check the Result**: Always check if the result of `re.search()` is not `None` to confirm a match was found.

## Case-Insensitive Matching 🔠

To make the search case-insensitive, use the `re.IGNORECASE` flag:

```python
import re

# Compiling the regular expression with case insensitivity
regex_pattern = re.compile(r'regex pattern', re.IGNORECASE)

# The text in which we want to search for the pattern
example_text = 'The REGEX pattern can be found.'

# Performing the search
match = re.search(regex_pattern, example_text)

# Checking if a match was found
if match:
    print("Match found! ✅")
else:
    print("No match found. ❌")
```

This will make the regex match patterns regardless of case.

### Explanation:
1. **`import re`**: This line imports the regular expression library in Python.
2. **`regex_pattern`**: The regular expression pattern provided as a raw string.
3. **`re.search()`**: Searches the string for a match to the regular expression pattern.
4. **`example_text`**: Example text to demonstrate the pattern matching.
5. **Checking the Match**: Determines if a match was found by checking if the `match` object is not `None`.
6. **`print()`**: Prints whether a match was found or not.

---
# Problem 3.6 🚩

## Checking for a Full Match with Regular Expressions ✨
You want to check whether a string fits a certain pattern in its entirety. That is, you want to check that the regular expression holding the pattern can match the string from start to end. For instance, if your regex is `regex pattern`, it will match input text consisting of `regex pattern` but not the longer string "The regex pattern can be found."

This exercise helps us understand how to use regular expressions to check for full matches within a string. Let's break it down in a detailed way! 🕵️‍♂️

## Solution 🛠️

To check for a full match in Python, we can use the `re.fullmatch()` function. This function checks if the entire string matches the regular expression pattern from start to end.

### Example in Python:

```python
import re

# String constant representing the regular expression
regex_pattern = r'regex pattern'

# The text we want to check for a full match
example_text = 'regex pattern'

# Performing the full match check
match = re.fullmatch(regex_pattern, example_text)

# Checking if a full match was found
if match:
    print("Full match found! ✅")
else:
    print("No full match found. ❌")
```

🧐 Here’s what this means:

- **`re.fullmatch()`** 🛡️: Checks if the entire string matches the regular expression pattern from start to end. It returns a match object if a full match is found and `None` if no full match is found.
- **Checking the Match**: By checking if the `match` object is not `None`, we can determine if a full match was found.

## Explanation 🌟

### Why Use `re.fullmatch()`?

The `re.fullmatch()` function is useful for validating that a string conforms exactly to a specified pattern, with no extra characters before or after the match. This is particularly useful for input validation and strict pattern matching.

### Example:

If we want to ensure that the string "regex pattern" matches the pattern `regex pattern` exactly, we use `re.fullmatch()` as shown in the example.

## Tips for Beginners 🐣

- **Use Fullmatch for Exact Matches**: When you need to ensure the entire string matches the pattern exactly, use `re.fullmatch()`.
- **Check the Result**: Always check if the result of `re.fullmatch()` is not `None` to confirm a full match was found.

## Case-Insensitive Matching 🔠

To make the full match case-insensitive, use the `re.IGNORECASE` flag:

```python
import re

# Compiling the regular expression with case insensitivity
regex_pattern = re.compile(r'regex pattern', re.IGNORECASE)

# The text we want to check for a full match
example_text = 'REGEX PATTERN'

# Performing the full match check
match = regex_pattern.fullmatch(example_text)

# Checking if a full match was found
if match:
    print("Full match found! ✅")
else:
    print("No full match found. ❌")
```

This will make the regex match patterns regardless of case.

### Explanation:
1. **`import re`**: This line imports the regular expression library in Python.
2. **`regex_pattern`**: The regular expression pattern provided as a raw string.
3. **`re.fullmatch()`**: Checks if the entire string matches the regular expression pattern from start to end.
4. **`example_text`**: Example text to demonstrate the pattern matching.
5. **Checking the Match**: Determines if a full match was found by checking if the `match` object is not `None`.
6. **`print()`**: Prints whether a full match was found or not.

---
# Problem 3.7 🚩

## Extracting the First Match with Regular Expressions ✨
You have a regular expression that matches a part of the subject text, and you want to extract the text that was matched. If the regular expression can match the string more than once, you want only the first match. For example, when applying the regex `\d+` to the string "Do you like 13 or 42?", `13` should be returned.

This exercise helps us understand how to use regular expressions to extract the first match from a string. Let's break it down in a detailed way! 🕵️‍♂️

## Solution 🛠️

To extract the first match in Python, we can use the `re.search()` function. This function searches the string for the first location where the regular expression pattern produces a match.

### Example in Python:

```python
import re

# String constant representing the regular expression
regex_pattern = r'\d+'

# The text in which we want to search for the pattern
example_text = 'Do you like 13 or 42?'

# Performing the search for the first match
match = re.search(regex_pattern, example_text)

# Extracting the matched text
if match:
    first_match = match.group()
    print("First match found:", first_match)
else:
    print("No match found.")
```

🧐 Here’s what this means:

- **`re.search()`** 🛡️: Searches the string for the first match to the regular expression pattern. It returns a match object if a match is found and `None` if no match is found.
- **Extracting the Match**: By using the `group()` method on the match object, we can extract the text that was matched.

## Explanation 🌟

### Why Use `re.search()`?

The `re.search()` function is useful for finding the first occurrence of a pattern in a string. It allows you to quickly locate and extract matched text without needing to check the entire string.

### Example:

If we want to find and extract the first number (`\d+`) in the string "Do you like 13 or 42?", we use `re.search()` as shown in the example.

## Tips for Beginners 🐣

- **Check the Result**: Always check if the result of `re.search()` is not `None` to confirm a match was found.
- **Use `group()`**: Use the `group()` method to extract the matched text from the match object.

## Case-Insensitive Matching 🔠

To make the search case-insensitive, use the `re.IGNORECASE` flag:

```python
import re

# Compiling the regular expression with case insensitivity
regex_pattern = re.compile(r'\d+', re.IGNORECASE)

# The text in which we want to search for the pattern
example_text = 'Do you like 13 or 42?'

# Performing the search for the first match
match = regex_pattern.search(example_text)

# Extracting the matched text
if match:
    first_match = match.group()
    print("First match found:", first_match)
else:
    print("No match found.")
```

This will make the regex match patterns regardless of case.

### Explanation:
1. **`import re`**: This line imports the regular expression library in Python.
2. **`regex_pattern`**: The regular expression pattern provided as a raw string.
3. **`re.search()`**: Searches the string for the first match to the regular expression pattern.
4. **`example_text`**: Example text to demonstrate the pattern matching.
5. **Extracting the Match**: Uses the `group()` method on the match object to extract the matched text.
6. **`print()`**: Prints the first match found or indicates if no match was found.

---

# Problem 3.8 🚩

## Finding the Starting Position and Length of a Regex Match ✨
Instead of extracting the substring matched by the regular expression, as shown in the previous recipe, you want to determine the starting position and length of the match. With this information, you can extract the match in your own code or apply whatever processing you fancy on the part of the original string matched by the regex.

This exercise helps us understand how to use regular expressions to find the starting position and length of a match within a string. Let's break it down in a detailed way! 🕵️‍♂️

## Solution 🛠️

To find the starting position and length of the first match in Python, we can use the `re.search()` function along with the `start()` and `end()` methods of the match object. These methods provide the start and end positions of the match, respectively.

### Example in Python:

```python
import re

# String constant representing the regular expression
regex_pattern = r'\d+'

# The text in which we want to search for the pattern
example_text = 'Do you like 13 or 42?'

# Performing the search for the first match
match = re.search(regex_pattern, example_text)

# Checking if a match was found and extracting the starting position and length
if match:
    start_position = match.start()
    end_position = match.end()
    match_length = end_position - start_position
    print(f"Match found at position {start_position} with length {match_length}.")
else:
    print("No match found.")
```

🧐 Here’s what this means:

- **`re.search()`** 🛡️: Searches the string for the first match to the regular expression pattern. It returns a match object if a match is found and `None` if no match is found.
- **`start()` Method**: Returns the starting position of the match.
- **`end()` Method**: Returns the position just after the end of the match.
- **Calculating Length**: The length of the match is calculated as `end_position - start_position`.

## Explanation 🌟

### Why Use `start()` and `end()` Methods?

The `start()` and `end()` methods of the match object provide precise positions of where the match starts and ends in the string. This information is useful when you need to process or manipulate the matched substring based on its position within the original string.

### Example:

If we want to find the starting position and length of the first number (`\d+`) in the string "Do you like 13 or 42?", we use `re.search()` and the `start()` and `end()` methods as shown in the example.

## Tips for Beginners 🐣

- **Check the Result**: Always check if the result of `re.search()` is not `None` to confirm a match was found.
- **Use `start()` and `end()`**: Use these methods to get the exact positions of the match within the string.

## Case-Insensitive Matching 🔠

To make the search case-insensitive, use the `re.IGNORECASE` flag:

```python
import re

# Compiling the regular expression with case insensitivity
regex_pattern = re.compile(r'\d+', re.IGNORECASE)

# The text in which we want to search for the pattern
example_text = 'Do you like 13 or 42?'

# Performing the search for the first match
match = regex_pattern.search(example_text)

# Checking if a match was found and extracting the starting position and length
if match:
    start_position = match.start()
    end_position = match.end()
    match_length = end_position - start_position
    print(f"Match found at position {start_position} with length {match_length}.")
else:
    print("No match found.")
```

This will make the regex match patterns regardless of case.

### Explanation:
1. **`import re`**: This line imports the regular expression library in Python.
2. **`regex_pattern`**: The regular expression pattern provided as a raw string.
3. **`re.search()`**: Searches the string for the first match to the regular expression pattern.
4. **`example_text`**: Example text to demonstrate the pattern matching.
5. **`start()` and `end()` Methods**: Used to get the starting and ending positions of the match.
6. **Calculating Length**: Determines the length of the match by subtracting the start position from the end position.
7. **`print()`**: Prints the starting position and length of the match or indicates if no match was found.

---
# Problem 3.9  🚩

## Retrieving All Matches with Regular Expressions ✨
All the preceding recipes in this chapter deal only with the first match that a regular expression can find in the subject string. But in many cases, a regular expression that partially matches a string can find another match in the remainder of the string. And there may be a third match after the second, and so on. For example, the regex `\d+` can find six matches in the subject string "The lucky numbers are 7, 13, 16, 42, 65, and 99: 7, 13, 16, 42, 65, and 99." You want to retrieve the list of all substrings that the regular expression finds when it is applied repeatedly to the remainder of the string, after each match.

This exercise helps us understand how to use regular expressions to find all matches within a string. Let's break it down in a detailed way! 🕵️‍♂️

## Solution 🛠️

To retrieve all matches in Python, we can use the `re.findall()` function. This function returns a list of all matches found in the string.

### Example in Python:

```python
import re

# String constant representing the regular expression
regex_pattern = r'\d+'

# The text in which we want to search for the pattern
example_text = 'The lucky numbers are 7, 13, 16, 42, 65, and 99: 7, 13, 16, 42, 65, and 99.'

# Finding all matches
matches = re.findall(regex_pattern, example_text)

# Printing all matches
print("Matches found:", matches)
```

🧐 Here’s what this means:

- **`re.findall()`** 🛡️: Searches the string for all matches to the regular expression pattern and returns them as a list of strings.
- **Retrieving All Matches**: By using `re.findall()`, we can easily retrieve all instances of the pattern within the string.

## Explanation 🌟

### Why Use `re.findall()`?

The `re.findall()` function is useful for retrieving all occurrences of a pattern within a string. It simplifies the process of extracting multiple matches, making it easy to work with repeating patterns.

### Example:

If we want to find all numbers (`\d+`) in the string "The lucky numbers are 7, 13, 16, 42, 65, and 99: 7, 13, 16, 42, 65, and 99.", we use `re.findall()` as shown in the example.

## Tips for Beginners 🐣

- **Use `findall()` for Multiple Matches**: When you need to find all occurrences of a pattern, `re.findall()` is the most straightforward method.
- **Check the Result**: The result is a list of strings, where each string is a match found in the text.

## Case-Insensitive Matching 🔠

To make the search case-insensitive, use the `re.IGNORECASE` flag:

```python
import re

# Compiling the regular expression with case insensitivity
regex_pattern = re.compile(r'\d+', re.IGNORECASE)

# The text in which we want to search for the pattern
example_text = 'The lucky numbers are 7, 13, 16, 42, 65, and 99: 7, 13, 16, 42, 65, and 99.'

# Finding all matches
matches = regex_pattern.findall(example_text)

# Printing all matches
print("Matches found:", matches)
```

This will make the regex match patterns regardless of case.

### Explanation:
1. **`import re`**: This line imports the regular expression library in Python.
2. **`regex_pattern`**: The regular expression pattern provided as a raw string.
3. **`re.findall()`**: Searches the string for all matches to the regular expression pattern and returns them as a list of strings.
4. **`example_text`**: Example text to demonstrate the pattern matching.
5. **Printing Matches**: Prints the list of all matches found in the text.

---
# Problem 3.10 🚩
## Iterating Over All Matches with Regular Expressions ✨
The previous recipe shows how a regex could be applied repeatedly to a string to get a list of matches. Now you want to iterate over all the matches in your own code.

This exercise helps us understand how to use regular expressions to iterate over all matches within a string and process each match individually. Let's break it down in a detailed way! 🕵️‍♂️

## Solution 🛠️

To iterate over all matches in Python, we can use the `re.finditer()` function. This function returns an iterator yielding match objects for all non-overlapping matches of the pattern in the string.

### Example in Python:

```python
import re

# String constant representing the regular expression
regex_pattern = r'\d+'

# The text in which we want to search for the pattern
example_text = 'The lucky numbers are 7, 13, 16, 42, 65, and 99: 7, 13, 16, 42, 65, and 99.'

# Using finditer to get an iterator over all matches
matches = re.finditer(regex_pattern, example_text)

# Iterating over all matches
for match in matches:
    # Extracting the matched text
    matched_text = match.group()
    # Getting the start and end positions of the match
    start_position = match.start()
    end_position = match.end()
    # Printing match details
    print(f"Match found: {matched_text} at position {start_position}-{end_position}")
```

🧐 Here’s what this means:

- **`re.finditer()`** 🛡️: Returns an iterator yielding match objects for all non-overlapping matches of the pattern in the string.
- **Iterating Over Matches**: By iterating over the matches, we can process each match individually, extracting the matched text and its position within the string.

## Explanation 🌟

### Why Use `re.finditer()`?

The `re.finditer()` function is useful for scenarios where you need to process each match individually. Unlike `re.findall()`, which returns a list of all matched strings, `re.finditer()` gives you match objects. These match objects provide detailed information about each match, such as the start and end positions, which can be useful for further processing.

### Example:

If we want to find and process all numbers (`\d+`) in the string "The lucky numbers are 7, 13, 16, 42, 65, and 99: 7, 13, 16, 42, 65, and 99.", we use `re.finditer()` as shown in the example.

## Tips for Beginners 🐣

- **Understand Match Objects**: Match objects contain useful methods like `group()`, `start()`, and `end()`. Familiarize yourself with these methods to effectively work with matches.
- **Iterate Carefully**: When iterating over matches, ensure you handle cases where no matches are found to avoid errors.

## Case-Insensitive Matching 🔠

To make the search case-insensitive, use the `re.IGNORECASE` flag:

```python
import re

# Compiling the regular expression with case insensitivity
regex_pattern = re.compile(r'\d+', re.IGNORECASE)

# The text in which we want to search for the pattern
example_text = 'The lucky numbers are 7, 13, 16, 42, 65, and 99: 7, 13, 16, 42, 65, and 99.'

# Using finditer to get an iterator over all matches
matches = regex_pattern.finditer(example_text)

# Iterating over all matches
for match in matches:
    # Extracting the matched text
    matched_text = match.group()
    # Getting the start and end positions of the match
    start_position = match.start()
    end_position = match.end()
    # Printing match details
    print(f"Match found: {matched_text} at position {start_position}-{end_position}")
```

This will make the regex match patterns regardless of case.

### Explanation:
1. **`import re`**: This line imports the regular expression library in Python.
2. **`regex_pattern`**: The regular expression pattern provided as a raw string.
3. **`re.finditer()`**: Returns an iterator yielding match objects for all non-overlapping matches of the pattern in the string.
4. **`example_text`**: Example text to demonstrate the pattern matching.
5. **Iterating Over Matches**: Iterates over all matches using a for loop.
6. **Extracting the Matched Text**: Uses the `group()` method on the match object to extract the matched text.
7. **Getting Match Positions**: Uses the `start()` and `end()` methods on the match object to get the start and end positions of the match.
8. **`print()`**: Prints the matched text and its position within the string.

This code will let you know if the provided regular expression finds and iterates over all matches in the example text, providing details about each match! 🎉

## Detailed Explanation for Beginners 🐣

### Steps to Understand the Example:

1. **Importing the `re` Module**:
   - The `re` module is Python's regular expression library. Import it to use regex functions.

2. **Defining the Regular Expression Pattern**:
   - `regex_pattern = r'\d+'`
   - This pattern matches one or more digits (`\d+`).

3. **Example Text**:
   - `example_text = 'The lucky numbers are 7, 13, 16, 42, 65, and 99: 7, 13, 16, 42, 65, and 99.'`
   - This is the string where we want to find all numbers.

4. **Using `re.finditer()`**:
   - `matches = re.finditer(regex_pattern, example_text)`
   - This function returns an iterator over all matches of the pattern in the string.

5. **Iterating Over Matches**:
   - `for match in matches:`
   - A for loop is used to iterate over each match object.

6. **Extracting Matched Text**:
   - `matched_text = match.group()`
   - The `group()` method returns the matched text.

7. **Getting Match Positions**:
   - `start_position = match.start()`
   - `end_position = match.end()`
   - The `start()` method returns the start position of the match, and the `end()` method returns the position just after the end of the match.

8. **Printing Match Details**:
   - `print(f"Match found: {matched_text} at position {start_position}-{end_position}")`
   - This prints the matched text and its position within the string.

---
# Problem 3.11 🚩

## Finding Matches Only Within Certain Sections of a String ✨
You want to find all the matches of a particular regular expression, but only within certain sections of the subject string. Another regular expression matches each of the sections in the string. Suppose you have an HTML file in which various passages are marked as bold with `<b>` tags. You want to find all numbers marked as bold. If some bold text contains multiple numbers, you want to match all of them separately. For example, when processing the string `1 <b>2</b> 3 4 <b>5 6 7</b>`, you want to find four matches: `2`, `5`, `6`, and `7`.

This exercise helps us understand how to use regular expressions to find matches within specific sections of a string. Let's break it down in a detailed way! 🕵️‍♂️

## Solution 🛠️

To achieve this, we will use two regular expressions:
1. One to find the sections marked as bold (`<b>...</b>`).
2. Another to find the numbers within these sections.

We will use the `re.finditer()` function to iterate over the bold sections and then apply another regex to find the numbers within each bold section.

### Example in Python:

```python
import re

# Regular expression to find bold sections
bold_section_pattern = re.compile(r'<b>(.*?)</b>', re.IGNORECASE | re.DOTALL)

# Regular expression to find numbers
number_pattern = re.compile(r'\d+')

# The text in which we want to search for the patterns
example_text = '1 <b>2</b> 3 4 <b>5 6 7</b>'

# Using finditer to get an iterator over all bold sections
bold_sections = bold_section_pattern.finditer(example_text)

# List to store all numbers found within bold sections
numbers_in_bold = []

# Iterating over all bold sections
for section in bold_sections:
    # Extracting the content within the bold tags
    bold_content = section.group(1)
    # Finding all numbers within the bold content
    numbers = number_pattern.findall(bold_content)
    # Adding the numbers to the list
    numbers_in_bold.extend(numbers)

# Printing all numbers found within bold sections
print("Numbers found within bold sections:", numbers_in_bold)
```

🧐 Here’s what this means:

- **`bold_section_pattern`** 🛡️: This regex pattern finds content within `<b>` tags. The `.*?` is a non-greedy match for any character sequence, and `re.IGNORECASE | re.DOTALL` makes the pattern case-insensitive and allows `.` to match newline characters.
- **`number_pattern`**: This regex pattern finds sequences of digits (`\d+`).
- **Iterating Over Bold Sections**: We use `re.finditer()` to iterate over each bold section and then apply `number_pattern` to find numbers within each section.
- **Collecting Matches**: We collect all numbers found within bold sections into a list and print them.

## Explanation 🌟

### Why Use Two Regular Expressions?

Using two regular expressions allows us to first isolate the sections of interest (bold sections) and then apply a second regex to find specific patterns within those sections (numbers). This approach is modular and can be adapted to various scenarios where nested pattern matching is required.

### Example:

If we want to find all numbers within bold sections in the string `1 <b>2</b> 3 4 <b>5 6 7</b>`, we use the two regex patterns as shown in the example.

## Tips for Beginners 🐣

- **Understand Nested Matching**: Breaking down the problem into smaller regex tasks (finding sections and then finding patterns within sections) makes it easier to manage.
- **Check for Correct Flags**: Ensure you use appropriate flags (`re.IGNORECASE`, `re.DOTALL`) to match the desired patterns correctly.

## Case-Insensitive and Dotall Matching 🔠

To make the regex case-insensitive and allow `.` to match newline characters, use the `re.IGNORECASE` and `re.DOTALL` flags:

```python
bold_section_pattern = re.compile(r'<b>(.*?)</b>', re.IGNORECASE | re.DOTALL)
```

This ensures the regex correctly matches bold tags and their content regardless of case and newline characters.

### Detailed Explanation for Each Step:

1. **Importing the `re` Module**:
   - The `re` module is Python's regular expression library. Import it to use regex functions.

2. **Defining the Regular Expression Patterns**:
   - `bold_section_pattern = re.compile(r'<b>(.*?)</b>', re.IGNORECASE | re.DOTALL)`
     - This pattern matches content within `<b>` tags. The `.*?` is a non-greedy match for any character sequence.
     - `re.IGNORECASE` makes the pattern case-insensitive.
     - `re.DOTALL` allows `.` to match newline characters.
   - `number_pattern = re.compile(r'\d+')`
     - This pattern matches sequences of digits (`\d+`).

3. **Example Text**:
   - `example_text = '1 <b>2</b> 3 4 <b>5 6 7</b>'`
   - This is the string where we want to find numbers within bold sections.

4. **Using `finditer()` for Bold Sections**:
   - `bold_sections = bold_section_pattern.finditer(example_text)`
   - This function returns an iterator over all matches of bold sections in the string.

5. **Iterating Over Bold Sections**:
   - `for section in bold_sections:`
   - A for loop is used to iterate over each match object representing a bold section.

6. **Extracting Bold Content**:
   - `bold_content = section.group(1)`
   - The `group(1)` method returns the content within the bold tags.

7. **Finding Numbers in Bold Content**:
   - `numbers = number_pattern.findall(bold_content)`
   - The `findall()` function returns a list of all numbers found within the bold content.

8. **Collecting Matches**:
   - `numbers_in_bold.extend(numbers)`
   - The numbers found are added to the `numbers_in_bold` list.

9. **Printing Matches**:
   - `print("Numbers found within bold sections:", numbers_in_bold)`
   - This prints the list of all numbers found within bold sections.
---
# Problem 3.12 🚩

## Performing a Search-and-Replace with Capturing Groups ✨
You want to run a search-and-replace that reinserts parts of the regex match back into the replacement. The parts you want to reinsert have been isolated in your regular expression using capturing groups. For example, you want to match pairs of words delimited by an equals sign, and swap those words in the replacement.

This exercise helps us understand how to use regular expressions with capturing groups to perform complex replacements. Let's break it down in a detailed way! 🕵️‍♂️

## Solution 🛠️

To achieve this, we will use capturing groups in our regular expression and the `re.sub()` function with a replacement string that references these groups.

### Example in Python:

```python
import re

# Regular expression pattern to match word pairs delimited by an equals sign
pattern = r'(\w+)=\w+'

# Replacement pattern to swap the words
replacement = r'\2=\1'

# The text in which we want to swap the word pairs
example_text = 'foo=bar fizz=buzz'

# Using re.sub() to replace all matches with the swapped words
result_text = re.sub(pattern, replacement, example_text)

# Printing the result
print("Original text:", example_text)
print("Modified text:", result_text)
```

🧐 Here’s what this means:

- **Capturing Groups**: `(\w+)=\w+` uses `(\w+)` to capture the first word and `(\w+)` to capture the second word.
- **Replacement Pattern**: `r'\2=\1'` swaps the positions of the captured groups.
- **`re.sub()`**: This function takes the pattern, replacement string, and original text, and returns a new string with all replacements made.

## Explanation 🌟

### Why Use Capturing Groups?

Capturing groups allow us to isolate specific parts of the matched text and reference them in the replacement string. This makes it possible to perform complex replacements where parts of the matched text are rearranged or modified.

### Example:

If we want to swap pairs of words delimited by an equals sign (e.g., `foo=bar` to `bar=foo`), we use capturing groups to isolate each word and then reference these groups in the replacement string.

## Tips for Beginners 🐣

- **Understand Capturing Groups**: Capturing groups are defined by parentheses `()` in the regex pattern. Each group can be referenced in the replacement string using `\1`, `\2`, etc.
- **Test Your Patterns**: Use tools like regex101.com to test and visualize your regex patterns and replacements.

## Case-Insensitive Matching 🔠

To make the replacement case-insensitive, use the `re.IGNORECASE` flag:

```python
import re

# Regular expression pattern to match word pairs delimited by an equals sign
pattern = re.compile(r'(\w+)=(\w+)', re.IGNORECASE)

# Replacement pattern to swap the words
replacement = r'\2=\1'

# The text in which we want to swap the word pairs
example_text = 'Foo=Bar Fizz=Buzz'

# Using re.sub() to replace all matches with the swapped words
result_text = pattern.sub(replacement, example_text)

# Printing the result
print("Original text:", example_text)
print("Modified text:", result_text)
```

This will make the regex match patterns regardless of case.

### Detailed Explanation for Each Step:

1. **Importing the `re` Module**:
   - The `re` module is Python's regular expression library. Import it to use regex functions.

2. **Defining the Regular Expression Pattern**:
   - `pattern = r'(\w+)=\w+'`
     - This pattern matches pairs of words delimited by an equals sign. The `\w+` matches one or more word characters.
     - The parentheses `()` create capturing groups for each word.

3. **Defining the Replacement Pattern**:
   - `replacement = r'\2=\1'`
     - This pattern references the captured groups and swaps their positions. `\1` refers to the first captured group, and `\2` refers to the second captured group.

4. **Example Text**:
   - `example_text = 'foo=bar fizz=buzz'`
   - This is the string where we want to swap the word pairs.

5. **Using `re.sub()` for Replacement**:
   - `result_text = re.sub(pattern, replacement, example_text)`
   - This function searches for the pattern in the string and replaces each occurrence with the replacement string.

6. **Printing the Result**:
   - `print("Original text:", example_text)`
   - `print("Modified text:", result_text)`
   - These lines print the original and modified strings to show the effect of the replacement.
---
# Problem 3.13 🚩

## Replacing Matches with Procedural Code ✨
You want to replace all matches of a regular expression with a new string that you build up in procedural code. You want to be able to replace each match with a different string, based on the text that was actually matched. For example, suppose you want to replace all numbers in a string with the number multiplied by two.

This exercise helps us understand how to use regular expressions with a custom replacement function to perform complex replacements. Let's break it down in a detailed way! 🕵️‍♂️

## Solution 🛠️

To achieve this, we will use the `re.sub()` function with a custom replacement function. The replacement function will be called for each match, allowing us to replace each match with a different string based on the matched text.

### Example in Python:

```python
import re

# Custom replacement function
def multiply_by_two(match):
    # Extract the matched text (a number)
    number = int(match.group())
    # Multiply the number by two
    return str(number * 2)

# Regular expression pattern to find numbers
pattern = r'\d+'

# The text in which we want to replace the numbers
example_text = 'The numbers are 1, 2, 3, 4, and 5.'

# Using re.sub() with the custom replacement function
result_text = re.sub(pattern, multiply_by_two, example_text)

# Printing the result
print("Original text:", example_text)
print("Modified text:", result_text)
```

🧐 Here’s what this means:

- **Custom Replacement Function**: `multiply_by_two` takes a match object, extracts the matched text (a number), multiplies it by two, and returns the result as a string.
- **`re.sub()` with Custom Function**: The `re.sub()` function is called with the pattern, the custom replacement function, and the original text. For each match, the replacement function is called to determine the replacement string.

## Explanation 🌟

### Why Use a Custom Replacement Function?

A custom replacement function allows us to perform complex replacements based on the matched text. This is useful when the replacement logic depends on the content of the match, such as modifying numbers, formatting text, or applying transformations.

### Example:

If we want to replace all numbers in the string "The numbers are 1, 2, 3, 4, and 5." with the number multiplied by two, we use a custom replacement function `multiply_by_two` to achieve this.

## Tips for Beginners 🐣

- **Understand Match Objects**: The match object passed to the replacement function contains useful methods like `group()`, `start()`, and `end()`. Familiarize yourself with these methods to effectively work with matches.
- **Test Your Functions**: Test your replacement function separately to ensure it works correctly before integrating it with `re.sub()`.

## Case-Insensitive Matching 🔠

To make the replacement case-insensitive, use the `re.IGNORECASE` flag:

```python
import re

# Custom replacement function
def multiply_by_two(match):
    # Extract the matched text (a number)
    number = int(match.group())
    # Multiply the number by two
    return str(number * 2)

# Compiling the regular expression with case insensitivity
pattern = re.compile(r'\d+', re.IGNORECASE)

# The text in which we want to replace the numbers
example_text = 'The numbers are 1, 2, 3, 4, and 5.'

# Using re.sub() with the custom replacement function
result_text = pattern.sub(multiply_by_two, example_text)

# Printing the result
print("Original text:", example_text)
print("Modified text:", result_text)
```

This will make the regex match patterns regardless of case.

### Detailed Explanation for Each Step:

1. **Importing the `re` Module**:
   - The `re` module is Python's regular expression library. Import it to use regex functions.

2. **Defining the Custom Replacement Function**:
   - `def multiply_by_two(match):`
     - A function that takes a match object as an argument.
     - `number = int(match.group())`: Extracts the matched text and converts it to an integer.
     - `return str(number * 2)`: Multiplies the number by two and returns the result as a string.

3. **Defining the Regular Expression Pattern**:
   - `pattern = r'\d+'`
     - This pattern matches sequences of digits (`\d+`).

4. **Example Text**:
   - `example_text = 'The numbers are 1, 2, 3, 4, and 5.'`
   - This is the string where we want to replace the numbers.

5. **Using `re.sub()` with Custom Function**:
   - `result_text = re.sub(pattern, multiply_by_two, example_text)`
   - This function searches for the pattern in the string and replaces each occurrence with the result of the custom replacement function.

6. **Printing the Result**:
   - `print("Original text:", example_text)`
   - `print("Modified text:", result_text)`
   - These lines print the original and modified strings to show the effect of the replacement.
---
# Problem 3.14 🚩

## Search-and-Replace within Certain Sections of a String ✨
You want to replace all matches of a particular regular expression, but only within certain sections of the subject string. Another regular expression matches each of the sections in the string. Say you have an HTML file in which various passages are marked as bold with `<b>` tags. Between each pair of bold tags, you want to replace all matches of the regular expression `before` with the replacement text `after`. For example, when processing the string `before <b>first before</b> before <b>before before</b>`, you want to end up with: `before <b>first after</b> before <b>after after</b>`.

This exercise helps us understand how to apply regular expressions to specific sections of a string. Let's break it down in a detailed way! 🕵️‍♂️

## Solution 🛠️

To achieve this, we will use two regular expressions:
1. One to find the sections marked as bold (`<b>...</b>`).
2. Another to find and replace the target pattern (`before`) within these sections.

We'll use the `re.sub()` function to perform the replacements within the bold sections.

### Example in Python:

```python
import re

# Regular expression to find bold sections
bold_section_pattern = re.compile(r'(<b>.*?</b>)', re.IGNORECASE | re.DOTALL)

# Regular expression to find the target pattern within bold sections
target_pattern = re.compile(r'before')

# Replacement text
replacement_text = 'after'

# The text in which we want to search for the patterns
example_text = 'before <b>first before</b> before <b>before before</b>'

# Function to replace the target pattern within bold sections
def replace_within_bold(match):
    # Extract the content within the bold tags
    bold_content = match.group(0)
    # Replace the target pattern within the bold content
    modified_content = target_pattern.sub(replacement_text, bold_content)
    return modified_content

# Using re.sub() to replace the target pattern within all bold sections
result_text = bold_section_pattern.sub(replace_within_bold, example_text)

# Printing the result
print("Original text:", example_text)
print("Modified text:", result_text)
```

🧐 Here’s what this means:

- **`bold_section_pattern`** 🛡️: This regex pattern finds content within `<b>` tags. The `.*?` is a non-greedy match for any character sequence, and `re.IGNORECASE | re.DOTALL` makes the pattern case-insensitive and allows `.` to match newline characters.
- **`target_pattern`**: This regex pattern finds instances of the word `before`.
- **`replace_within_bold()` Function**: This function takes a match object, extracts the content within the bold tags, replaces the target pattern within this content, and returns the modified content.
- **`re.sub()` with Custom Function**: The `re.sub()` function is called with the bold section pattern, the custom replacement function, and the original text. For each match, the replacement function is called to perform the replacement within the bold section.

## Explanation 🌟

### Why Use Two Regular Expressions?

Using two regular expressions allows us to first isolate the sections of interest (bold sections) and then apply a second regex to find and replace specific patterns within those sections. This approach is modular and can be adapted to various scenarios where nested pattern matching and replacement are required.

### Example:

If we want to replace all instances of the word "before" with "after" within bold sections in the string `before <b>first before</b> before <b>before before</b>`, we use the two regex patterns and a custom replacement function to achieve this.

## Tips for Beginners 🐣

- **Understand Nested Matching**: Breaking down the problem into smaller regex tasks (finding sections and then finding patterns within sections) makes it easier to manage.
- **Test Your Patterns**: Use tools like regex101.com to test and visualize your regex patterns and replacements.

## Case-Insensitive and Dotall Matching 🔠

To make the regex case-insensitive and allow `.` to match newline characters, use the `re.IGNORECASE` and `re.DOTALL` flags:

```python
bold_section_pattern = re.compile(r'(<b>.*?</b>)', re.IGNORECASE | re.DOTALL)
```

This ensures the regex correctly matches bold tags and their content regardless of case and newline characters.

### Detailed Explanation for Each Step:

1. **Importing the `re` Module**:
   - The `re` module is Python's regular expression library. Import it to use regex functions.

2. **Defining the Regular Expression Patterns**:
   - `bold_section_pattern = re.compile(r'(<b>.*?</b>)', re.IGNORECASE | re.DOTALL)`
     - This pattern matches content within `<b>` tags. The `.*?` is a non-greedy match for any character sequence.
     - `re.IGNORECASE` makes the pattern case-insensitive.
     - `re.DOTALL` allows `.` to match newline characters.
   - `target_pattern = re.compile(r'before')`
     - This pattern matches the word "before".

3. **Defining the Replacement Text**:
   - `replacement_text = 'after'`
     - This is the text that will replace each match of the target pattern.

4. **Example Text**:
   - `example_text = 'before <b>first before</b> before <b>before before</b>'`
   - This is the string where we want to replace the target pattern within bold sections.

5. **Defining the Custom Replacement Function**:
   - `def replace_within_bold(match):`
     - A function that takes a match object as an argument.
     - `bold_content = match.group(0)`: Extracts the content within the bold tags.
     - `modified_content = target_pattern.sub(replacement_text, bold_content)`: Replaces the target pattern within the bold content.
     - `return modified_content`: Returns the modified content.

6. **Using `re.sub()` with the Custom Function**:
   - `result_text = bold_section_pattern.sub(replace_within_bold, example_text)`
   - This function searches for the bold section pattern in the string and replaces each occurrence with the result of the custom replacement function.

7. **Printing the Result**:
   - `print("Original text:", example_text)`
   - `print("Modified text:", result_text)`
   - These lines print the original and modified strings to show the effect of the replacement.
---
# Problem 3.15 🚩

##  Replace All Matches Between the Matches of Another Regex ✨

You want to replace all matches of a particular regular expression, but only within certain sections of the subject string. Another regular expression matches the text between the sections. In other words, you want to search and replace through all parts of the subject string not matched by the other regular expression. Say you have an HTML file in which you want to replace straight double quotes with smart (curly) double quotes, but you only want to replace the quotes outside of HTML tags. Quotes within HTML tags must remain plain ASCII straight quotes, or your web browser won’t be able to parse the HTML anymore. For example, you want to turn `"text" <span class="middle">"text"</span> "text"` into `“text” <span class="middle">"text"</span> “text”`.

This exercise helps us understand how to apply regular expressions to specific sections of a string. Let's break it down in a detailed way! 🕵️‍♂️

## Solution 🛠️

To achieve this, we will use two regular expressions:
1. One to find the sections matched by HTML tags (`<[^>]+>`).
2. Another to find and replace the target pattern (straight quotes) outside these sections.

We'll use the `re.sub()` function to perform the replacements outside the HTML tags.

### Example in Python:

```python
import re

# Regular expression to find HTML tags
html_tag_pattern = re.compile(r'<[^>]+>')

# Regular expression to find straight double quotes
quote_pattern = re.compile(r'"')

# Replacement text for smart quotes
left_smart_quote = '“'
right_smart_quote = '”'

# The text in which we want to replace the quotes
example_text = '"text" <span class="middle">"text"</span> "text"'

# Function to replace quotes outside of HTML tags
def replace_quotes_outside_html(text):
    segments = []
    last_end = 0
    
    # Iterate over all HTML tags
    for match in html_tag_pattern.finditer(text):
        start, end = match.span()
        
        # Process the text segment before the HTML tag
        segment_before_tag = text[last_end:start]
        segment_before_tag = quote_pattern.sub(left_smart_quote, segment_before_tag, 1)
        segment_before_tag = quote_pattern.sub(right_smart_quote, segment_before_tag)
        segments.append(segment_before_tag)
        
        # Add the HTML tag itself unchanged
        segments.append(text[start:end])
        
        # Update the position for the next iteration
        last_end = end
    
    # Process the remaining text segment after the last HTML tag
    remaining_segment = text[last_end:]
    remaining_segment = quote_pattern.sub(left_smart_quote, remaining_segment, 1)
    remaining_segment = quote_pattern.sub(right_smart_quote, remaining_segment)
    segments.append(remaining_segment)
    
    # Join all segments back into a single string
    return ''.join(segments)

# Using the custom function to replace quotes
result_text = replace_quotes_outside_html(example_text)

# Printing the result
print("Original text:", example_text)
print("Modified text:", result_text)
```

🧐 Here’s what this means:

- **`html_tag_pattern`** 🛡️: This regex pattern finds HTML tags. The `[^>]+` matches any sequence of characters that are not `>`, ensuring we match an entire HTML tag.
- **`quote_pattern`**: This regex pattern finds instances of straight double quotes (`"`).
- **`replace_quotes_outside_html()` Function**: This function takes the entire text, processes it to replace quotes outside of HTML tags, and returns the modified text.
- **`re.sub()` with Custom Function**: The `re.sub()` function is called with the quote pattern and replacement text to replace quotes outside of HTML tags.

## Explanation 🌟

### Why Use Two Regular Expressions?

Using two regular expressions allows us to first isolate the sections of interest (HTML tags) and then apply a second regex to find and replace specific patterns outside those sections. This approach is modular and can be adapted to various scenarios where nested pattern matching and replacement are required.

### Example:

If we want to replace all instances of straight double quotes with smart quotes outside of HTML tags in the string `"text" <span class="middle">"text"</span> "text"`, we use the two regex patterns and a custom replacement function to achieve this.

## Tips for Beginners 🐣

- **Understand Nested Matching**: Breaking down the problem into smaller regex tasks (finding sections and then finding patterns within sections) makes it easier to manage.
- **Test Your Patterns**: Use tools like regex101.com to test and visualize your regex patterns and replacements.

## Case-Insensitive and Dotall Matching 🔠

To make the regex case-insensitive and allow `.` to match newline characters, use the `re.IGNORECASE` and `re.DOTALL` flags:

```python
html_tag_pattern = re.compile(r'<[^>]+>', re.IGNORECASE | re.DOTALL)
```

This ensures the regex correctly matches HTML tags and their content regardless of case and newline characters.

### Detailed Explanation for Each Step:

1. **Importing the `re` Module**:
   - The `re` module is Python's regular expression library. Import it to use regex functions.

2. **Defining the Regular Expression Patterns**:
   - `html_tag_pattern = re.compile(r'<[^>]+>')`
     - This pattern matches HTML tags. The `[^>]+` matches any sequence of characters that are not `>`.
   - `quote_pattern = re.compile(r'"')`
     - This pattern matches straight double quotes (`"`).

3. **Defining the Replacement Text**:
   - `left_smart_quote = '“'`: This is the left smart (curly) quote.
   - `right_smart_quote = '”'`: This is the right smart (curly) quote.

4. **Example Text**:
   - `example_text = '"text" <span class="middle">"text"</span> "text"'`
   - This is the string where we want to replace the straight double quotes with smart quotes, but only outside of HTML tags.

5. **Custom Replacement Function**:
   - `replace_quotes_outside_html(text)`: This function takes the entire text as an argument and processes it to replace quotes outside of HTML tags.
   - `segments = []`: An empty list to store the segments of the text.
   - `last_end = 0`: A variable to keep track of the end position of the last processed segment.
   - `for match in html_tag_pattern.finditer(text)`: This loop iterates over all HTML tags found in the text.
   - `start, end = match.span()`: These variables store the start and end positions of the current HTML tag.
   - `segment_before_tag = text[last_end:start]`: This extracts the text segment before the current HTML tag.
   - `segment_before_tag = quote_pattern.sub(left_smart_quote, segment_before_tag, 1)`: Replaces the first straight quote with the left smart quote.
   - `segment_before_tag = quote_pattern.sub(right_smart_quote, segment_before_tag)`: Replaces the remaining straight quotes with the right smart quote.
   - `segments.append(segment_before_tag)`: Adds the processed segment before the tag to the list.
   - `segments.append(text[start:end])`: Adds the HTML tag itself unchanged to the list.
   - `last_end = end`: Updates the end position for the next iteration.
   - `remaining_segment = text[last_end:]`: Processes the remaining text segment after the last HTML tag.
   - `remaining_segment = quote_pattern.sub(left_smart_quote, remaining_segment, 1)`: Replaces the first straight quote with the left smart quote.
   - `remaining_segment = quote_pattern.sub(right_smart_quote, remaining_segment)`: Replaces the remaining straight quotes with the right smart quote.
   - `segments.append(remaining_segment)`: Adds the processed remaining segment to the list.
   - `return ''.join(segments)`: Joins all segments back into a single string and returns the result.

6. **Using the Custom Function to Replace Quotes**:
   - `result_text = replace_quotes_outside_html(example_text)`: Calls the custom function with the example text to get the modified text.

7. **Printing the Result**:
   - `print("Original text:", example_text)`
   - `print("Modified text:", result_text)`
   - These lines print the original and modified strings to show the effect of the replacement.
---
# Problem 3.16 🚩

## Splitting a String with Regular Expressions ✨
You want to split a string using a regular expression. After the split, you will have an array or list of strings with the text between the regular expression matches. For example, you want to split a string with HTML tags in it along the HTML tags. Splitting `I●like●<b>bold</b>●and●<i>italic</i>●fonts` should result in an array of five strings: `I●like●`, `bold`, `●and●`, `italic`, and `●fonts`.

This exercise helps us understand how to use regular expressions to split a string into parts based on a pattern. Let's break it down in a detailed way! 🕵️‍♂️

## Solution 🛠️

To achieve this, we will use the `re.split()` function from Python's `re` module. This function splits the string by the occurrences of the pattern and includes the matches in the resulting list.

### Example in Python:

```python
import re

# Regular expression pattern to match HTML tags
html_tag_pattern = re.compile(r'<[^>]+>')

# The text we want to split
example_text = 'I●like●<b>bold</b>●and●<i>italic</i>●fonts'

# Using re.split() to split the text along HTML tags
result_list = html_tag_pattern.split(example_text)

# Printing the result
print("Original text:", example_text)
print("Split list:", result_list)
```

🧐 Here’s what this means:

- **`html_tag_pattern`** 🛡️: This regex pattern matches HTML tags. The `[^>]+` matches any sequence of characters that are not `>`, ensuring we match an entire HTML tag.
- **`re.split()`**: This function splits the string by the occurrences of the pattern and includes the matches in the resulting list.

## Explanation 🌟

### Why Use `re.split()`?

The `re.split()` function is useful for splitting a string into parts based on a pattern. It returns a list of the substrings between the matches, and if the pattern contains capturing groups, the matches themselves are included in the list.

### Example:

If we want to split the string `I●like●<b>bold</b>●and●<i>italic</i>●fonts` along the HTML tags, we use the regex pattern to match the HTML tags and the `re.split()` function to perform the split.

## Tips for Beginners 🐣

- **Understand the Pattern**: Make sure you understand the regex pattern you are using. Test it separately to ensure it matches the parts you want to split by.
- **Visualize the Result**: Use tools like regex101.com to visualize how your pattern works and what it matches.

## Case-Insensitive Matching 🔠

To make the pattern case-insensitive, use the `re.IGNORECASE` flag:

```python
html_tag_pattern = re.compile(r'<[^>]+>', re.IGNORECASE)
```

This ensures the regex correctly matches HTML tags regardless of case.

### Detailed Explanation for Each Step:

1. **Importing the `re` Module**:
   - The `re` module is Python's regular expression library. Import it to use regex functions.

2. **Defining the Regular Expression Pattern**:
   - `html_tag_pattern = re.compile(r'<[^>]+>')`
     - This pattern matches HTML tags. The `[^>]+` matches any sequence of characters that are not `>`, ensuring we match an entire HTML tag.

3. **Example Text**:
   - `example_text = 'I●like●<b>bold</b>●and●<i>italic</i>●fonts'`
   - This is the string we want to split along the HTML tags.

4. **Using `re.split()` to Split the Text**:
   - `result_list = html_tag_pattern.split(example_text)`
   - This function splits the string by the occurrences of the pattern and includes the matches in the resulting list.

5. **Printing the Result**:
   - `print("Original text:", example_text)`
   - `print("Split list:", result_list)`
   - These lines print the original text and the resulting list of substrings to show the effect of the split.
---
# Problem 3.17 🚩

## Retrieving and Filtering Matches Based on Additional Criteria ✨

You want to retrieve a list of all matches a regular expression can find in a string when it is applied repeatedly to the remainder of the string after each match. Now, you want to get a list of matches that meet certain extra criteria that you cannot (easily) express in a regular expression. For example, when retrieving a list of lucky numbers, you only want to retain those that are an integer multiple of 13.

This exercise helps us understand how to use regular expressions to find matches and then apply additional criteria to filter those matches. Let's break it down in a detailed way! 🕵️‍♂️

## Solution 🛠️

To achieve this, we will:
1. Use `re.findall()` to retrieve all matches of the regular expression in the string.
2. Apply additional criteria to filter the list of matches.

### Example in Python:

```python
import re

# Regular expression pattern to find numbers
number_pattern = re.compile(r'\d+')

# The text in which we want to search for the numbers
example_text = 'The lucky numbers are 7, 13, 26, 39, 52, 65, and 99.'

# Using re.findall() to retrieve all matches
all_matches = number_pattern.findall(example_text)

# Function to filter matches based on additional criteria
def filter_lucky_numbers(matches):
    # Convert matched strings to integers and filter those that are multiples of 13
    lucky_numbers = [int(num) for num in matches if int(num) % 13 == 0]
    return lucky_numbers

# Applying the filter function
lucky_numbers = filter_lucky_numbers(all_matches)

# Printing the result
print("All matches:", all_matches)
print("Lucky numbers:", lucky_numbers)
```

🧐 Here’s what this means:

- **`number_pattern`** 🛡️: This regex pattern finds sequences of digits (`\d+`).
- **`re.findall()`**: This function retrieves all matches of the pattern in the string and returns them as a list.
- **`filter_lucky_numbers()` Function**: This function takes the list of matches, converts them to integers, and retains only those that are multiples of 13.
- **Filtering Matches**: By using a custom function, we can apply complex criteria to filter the list of matches.

## Explanation 🌟

### Why Use `re.findall()`?

The `re.findall()` function is useful for retrieving all matches of a pattern in a string. It returns a list of matched strings, making it easy to process and filter these matches further.

### Example:

If we want to retrieve all numbers in the string `The lucky numbers are 7, 13, 26, 39, 52, 65, and 99.` and retain only those that are multiples of 13, we use the regex pattern to find all numbers and a custom function to filter the list.

## Tips for Beginners 🐣

- **Understand the Pattern**: Make sure you understand the regex pattern you are using. Test it separately to ensure it matches the parts you want to find.
- **Visualize the Result**: Use tools like regex101.com to visualize how your pattern works and what it matches.

### Detailed Explanation for Each Step:

1. **Importing the `re` Module**:
   - The `re` module is Python's regular expression library. Import it to use regex functions.

2. **Defining the Regular Expression Pattern**:
   - `number_pattern = re.compile(r'\d+')`
     - This pattern matches sequences of digits (`\d+`).

3. **Example Text**:
   - `example_text = 'The lucky numbers are 7, 13, 26, 39, 52, 65, and 99.'`
   - This is the string where we want to find numbers.

4. **Using `re.findall()` to Retrieve All Matches**:
   - `all_matches = number_pattern.findall(example_text)`
   - This function retrieves all matches of the pattern in the string and returns them as a list.

5. **Defining the Custom Filter Function**:
   - `def filter_lucky_numbers(matches):`
     - A function that takes a list of matched strings.
     - `lucky_numbers = [int(num) for num in matches if int(num) % 13 == 0]`: Converts matched strings to integers and retains only those that are multiples of 13.
     - `return lucky_numbers`: Returns the filtered list.

6. **Applying the Filter Function**:
   - `lucky_numbers = filter_lucky_numbers(all_matches)`
   - Calls the custom function with the list of matches to get the filtered list.

7. **Printing the Result**:
   - `print("All matches:", all_matches)`
   - `print("Lucky numbers:", lucky_numbers)`
   - These lines print the original list of matches and the filtered list to show the effect of the filtering.
---
# Problem 3.18 🚩

## Splitting a String with Regular Expressions and Keeping the Matches ✨

You want to split a string using a regular expression. After the split, you will have an array or list of strings with the text between the regular expression matches, as well as the regex matches themselves. Suppose you want to split a string with HTML tags in it along the HTML tags, and also keep the HTML tags. Splitting `I●like●<b>bold</b>●and●<i>italic</i>●fonts` should result in an array of nine strings: `I●like●`, `<b>`, `bold`, `</b>`, `●and●`, `<i>`, `italic`, `</i>`, and `●fonts`.

This exercise helps us understand how to use regular expressions to split a string and retain the matches. Let's break it down in a detailed way! 🕵️‍♂️

## Solution 🛠️

To achieve this, we will use the `re.split()` function from Python's `re` module with a capturing group in the regular expression. The capturing group ensures that the matches are included in the resulting list.

### Example in Python:

```python
import re

# Regular expression pattern to match HTML tags and keep them in the result
html_tag_pattern = re.compile(r'(<[^>]+>)')

# The text we want to split
example_text = 'I●like●<b>bold</b>●and●<i>italic</i>●fonts'

# Using re.split() to split the text along HTML tags and keep the tags
result_list = html_tag_pattern.split(example_text)

# Printing the result
print("Original text:", example_text)
print("Split list:", result_list)
```

🧐 Here’s what this means:

- **`html_tag_pattern`** 🛡️: This regex pattern matches HTML tags. The `[^>]+` matches any sequence of characters that are not `>`, ensuring we match an entire HTML tag. The parentheses `()` create a capturing group to keep the matches in the result.
- **`re.split()`**: This function splits the string by the occurrences of the pattern and includes the matches in the resulting list.

## Explanation 🌟

### Why Use Capturing Groups?

Capturing groups allow us to include the parts of the string that match the pattern in the resulting list when using `re.split()`. This is useful when we want to retain the matches along with the text between them.

### Example:

If we want to split the string `I●like●<b>bold</b>●and●<i>italic</i>●fonts` along the HTML tags and keep the tags, we use the regex pattern with a capturing group and the `re.split()` function to perform the split.

## Tips for Beginners 🐣

- **Understand the Pattern**: Make sure you understand the regex pattern you are using. Test it separately to ensure it matches the parts you want to split by.
- **Visualize the Result**: Use tools like regex101.com to visualize how your pattern works and what it matches.

## Case-Insensitive Matching 🔠

To make the pattern case-insensitive, use the `re.IGNORECASE` flag:

```python
html_tag_pattern = re.compile(r'(<[^>]+>)', re.IGNORECASE)
```

This ensures the regex correctly matches HTML tags regardless of case.

### Detailed Explanation for Each Step:

1. **Importing the `re` Module**:
   - The `re` module is Python's regular expression library. Import it to use regex functions.

2. **Defining the Regular Expression Pattern**:
   - `html_tag_pattern = re.compile(r'(<[^>]+>)')`
     - This pattern matches HTML tags. The `[^>]+` matches any sequence of characters that are not `>`, ensuring we match an entire HTML tag. The parentheses `()` create a capturing group to keep the matches in the result.

3. **Example Text**:
   - `example_text = 'I●like●<b>bold</b>●and●<i>italic</i>●fonts'`
   - This is the string we want to split along the HTML tags and keep the tags in the resulting list.

4. **Using `re.split()` to Split the Text**:
   - `result_list = html_tag_pattern.split(example_text)`
   - This function splits the string by the occurrences of the pattern and includes the matches in the resulting list.

5. **Printing the Result**:
   - `print("Original text:", example_text)`
   - `print("Split list:", result_list)`
   - These lines print the original text and the resulting list of substrings to show the effect of the split.
---
# Problem 3.19 🚩

## Applying Regular Expressions to Each Line of a Multiline String ✨

Traditional grep tools apply your regular expression to one line of text at a time and display the lines matched (or not matched) by the regular expression. You have an array of strings, or a multiline string, that you want to process in this way.

This exercise helps us understand how to use regular expressions to process each line of a multiline string or an array of strings, similar to how traditional grep tools work. Let's break it down in a detailed way! 🕵️‍♂️

## Solution 🛠️

To achieve this, we will:
1. Split the multiline string into individual lines.
2. Apply the regular expression to each line.
3. Collect and display the lines that match (or do not match) the regular expression.

### Example in Python:

```python
import re

# Regular expression pattern to match
pattern = re.compile(r'\bbold\b', re.IGNORECASE)

# Multiline string to process
multiline_text = """I like bold statements.
This is a bold move.
Do you prefer bold or italic?
No boldness here."""

# Split the multiline string into individual lines
lines = multiline_text.split('\n')

# Function to process each line and match the pattern
def grep_lines(pattern, lines, invert_match=False):
    matched_lines = []
    for line in lines:
        if pattern.search(line):
            if not invert_match:
                matched_lines.append(line)
        else:
            if invert_match:
                matched_lines.append(line)
    return matched_lines

# Using the function to get matching lines
matching_lines = grep_lines(pattern, lines)

# Printing the result
print("Original text:\n", multiline_text)
print("\nMatching lines:")
for line in matching_lines:
    print(line)
```

🧐 Here’s what this means:

- **`pattern`** 🛡️: This regex pattern matches the word "bold" (case-insensitive) using the `\b` word boundary anchors.
- **`multiline_text`**: This is the multiline string we want to process.
- **`split('\n')`**: This splits the multiline string into individual lines.
- **`grep_lines()` Function**: This function processes each line, checks if the pattern matches, and collects the matching lines.
- **`pattern.search(line)`**: This checks if the pattern matches the current line.

## Explanation 🌟

### Why Use a Function?

Using a function allows us to encapsulate the logic for processing each line, making it reusable and easier to manage. It also allows us to add additional features, such as inverting the match (to collect lines that do not match).

### Example:

If we want to find all lines containing the word "bold" in the string:
```
I like bold statements.
This is a bold move.
Do you prefer bold or italic?
No boldness here.
```
We use the regex pattern to match "bold" and the function to process each line and collect the matching lines.

## Tips for Beginners 🐣

- **Understand the Pattern**: Make sure you understand the regex pattern you are using. Test it separately to ensure it matches the parts you want to find.
- **Visualize the Result**: Use tools like regex101.com to visualize how your pattern works and what it matches.

## Inverting the Match 🔄

To collect lines that do not match the pattern, use the `invert_match` parameter:

```python
# Using the function to get non-matching lines
non_matching_lines = grep_lines(pattern, lines, invert_match=True)

# Printing the non-matching result
print("\nNon-matching lines:")
for line in non_matching_lines:
    print(line)
```

### Detailed Explanation for Each Step:

1. **Importing the `re` Module**:
   - The `re` module is Python's regular expression library. Import it to use regex functions.

2. **Defining the Regular Expression Pattern**:
   - `pattern = re.compile(r'\bbold\b', re.IGNORECASE)`
     - This pattern matches the word "bold" (case-insensitive) using word boundary anchors (`\b`).

3. **Multiline String**:
   - `multiline_text = """I like bold statements. ... """`
   - This is the multiline string we want to process.

4. **Splitting the Multiline String into Lines**:
   - `lines = multiline_text.split('\n')`
   - This splits the multiline string into individual lines.

5. **Defining the `grep_lines()` Function**:
   - `def grep_lines(pattern, lines, invert_match=False):`
     - A function to process each line and match the pattern.
     - `matched_lines = []`: An empty list to collect matched lines.
     - `for line in lines:`: Iterates over each line.
     - `if pattern.search(line):`: Checks if the pattern matches the current line.
     - `if not invert_match:`: Adds the line to the result if it matches and `invert_match` is `False`.
     - `else:`: Adds the line to the result if it does not match and `invert_match` is `True`.
     - `return matched_lines`: Returns the list of matched lines.

6. **Using the Function to Get Matching Lines**:
   - `matching_lines = grep_lines(pattern, lines)`
   - Calls the function with the pattern and lines to get the matching lines.

7. **Printing the Result**:
   - `print("Original text:\n", multiline_text)`
   - `print("\nMatching lines:")`
   - Prints the original text and the matching lines to show the effect of the pattern matching.

---

# Custom File Format Parser

# Problem 3.20 🚩

## Parsing a Custom File Format and Storing Data in Existing Data Structures ✨

You need to add a new feature to your application to import data from a file format that your application does not yet support. The file format rules are as follows:

1. The keyword `table` begins a new table. A file can have an unlimited number of tables and must have at least one.

2. Any strings following the `table` keyword form the table’s caption. A table does not need to have a caption.

3. The keyword `row` begins a new row. A row cannot exist outside of a table. A table can have an unlimited number of rows and must have at least one.

4. The `row` keyword cannot be followed by a string.

5. The keyword `cell` begins a new cell. A cell cannot exist outside of a row. A row can have an unlimited number of cells but does not need any.

6. Any strings following the `cell` keyword form the content of the cell. A cell does not need to have any content.

7. A string is a sequence of zero or more characters enclosed by percentage signs. A string with nothing between the percentage signs is an empty string. Two sequential percentage signs in a character string denote a single character, a percentage sign. No characters other than the percentage sign have a special meaning in strings. Line breaks and other control characters that appear between the percentage signs are all part of the string.

8. If two or more strings follow the same `table` or `cell` keyword, those strings form separate lines in the table’s caption or the cell’s content, regardless of whether there is a line break between the strings in the file.

9. Keywords are case insensitive. `Cell`, `cell`, `CELL`, and `CeLl` are all the same.

10. Any whitespace between keywords and/or strings must be ignored. Whitespace is required to delimit adjacent keywords. Whitespace is also required to delimit adjacent strings. Whitespace is not required to delimit keywords from strings.

11. Any characters in the file that do not form a keyword or string are an error.

### Example File:

```
table %First table%
row
cell %A1%
cell %B1%
cell%C1%
cell%D1%
ROW
row
CELL %The previous row was blank%
cell %B3%
row
cell %A4% %second line%
cEll %B4% %second line%
cell %C4 second line%
row
cell %%%string%%%
cell %%
cell %%%%
cell %%%%%%
```

### Formatted Table:

```
Table 3-1. Table to be parsed from the sample file
A1 B1 C1 D1
(omitted) (omitted) (omitted) (omitted)
The previous row was blank B3
(omitted) (omitted)
A4 second line B4 second line C4 second line
(omitted)
%string% (blank) % %%
```

## Solution 🛠️

To achieve this, we will:
1. Define the existing data structures (`RECTable`, `RECRow`, `RECCell`).
2. Create a parsing function `parse_file_content` to read and parse the file content.

### Step-by-Step Solution

#### 1. Define the Data Structures

First, let's define the existing data structures which are assumed to be provided by the application. These will be used to store the parsed data.

```python
class RECCell:
    def __init__(self, content):
        self.content = content  # Initialize the cell content
        
    def __repr__(self):
        return f"RECCell(content={self.content})"  # Representation of the cell for debugging

class RECRow:
    def __init__(self):
        self.cells = []  # Initialize an empty list of cells
        
    def add_cell(self, cell):
        self.cells.append(cell)  # Add a cell to the row
        
    def __repr__(self):
        return f"RECRow(cells={self.cells})"  # Representation of the row for debugging

class RECTable:
    def __init__(self, caption=None):
        self.caption = caption if caption else []  # Initialize the caption, default to an empty list if None
        self.rows = []  # Initialize an empty list of rows
        
    def add_row(self, row):
        self.rows.append(row)  # Add a row to the table
        
    def __repr__(self):
        return f"RECTable(caption={self.caption}, rows={self.rows})"  # Representation of the table for debugging
```

#### 2. Define the Parsing Function

Now, let's define the parsing function `parse_file_content`. This function will take in a string containing the entire contents of the file and return a list of `RECTable` objects.

```python
import re

def parse_file_content(file_content):
    # Regular expression patterns for keywords and strings
    table_pattern = re.compile(r'\btable\b', re.IGNORECASE)  # Match the keyword 'table' case insensitively
    row_pattern = re.compile(r'\brow\b', re.IGNORECASE)  # Match the keyword 'row' case insensitively
    cell_pattern = re.compile(r'\bcell\b', re.IGNORECASE)  # Match the keyword 'cell' case insensitively
    string_pattern = re.compile(r'%([^%]*)%')  # Match strings enclosed by percentage signs

    tables = []  # List to store all tables
    current_table = None  # Variable to store the current table being processed
    current_row = None  # Variable to store the current row being processed

    # Tokenize the file content
    tokens = re.findall(r'\btable\b|\brow\b|\bcell\b|%[^%]*%|\s+', file_content, re.IGNORECASE)  # Find all keywords, strings, and whitespace

    for token in tokens:
        token = token.strip()  # Remove leading and trailing whitespace
        if not token:
            continue  # Skip empty tokens

        if table_pattern.fullmatch(token):  # Check if the token is a 'table' keyword
            if current_table:
                tables.append(current_table)  # Append the current table to the list of tables
            current_table = RECTable()  # Create a new RECTable instance
            current_row = None  # Reset the current row
        elif row_pattern.fullmatch(token):  # Check if the token is a 'row' keyword
            if not current_table:
                raise ValueError("Row found outside of a table.")  # Error if a row is found outside a table
            current_row = RECRow()  # Create a new RECRow instance
            current_table.add_row(current_row)  # Add the new row to the current table
        elif cell_pattern.fullmatch(token):  # Check if the token is a 'cell' keyword
            if not current_row:
                raise ValueError("Cell found outside of a row.")  # Error if a cell is found outside a row
            current_row.add_cell(RECCell(""))  # Add a new empty cell to the current row
        else:
            match = string_pattern.fullmatch(token)  # Check if the token is a string
            if match:
                content = match.group(1).replace("%%", "%")  # Replace '%%' with '%' in the string content
                if current_table and not current_row:
                    current_table.caption.append(content)  # Add the string to the table's caption if in a table but not in a row
                elif current_row:
                    if current_row.cells:
                        current_row.cells[-1].content += content  # Append the string content to the last cell in the current row
                    else:
                        current_row.add_cell(RECCell(content))  # Add a new cell with the string content if no cells exist
            else:
                raise ValueError(f"Unexpected token: {token}")  # Error for unexpected tokens

    if current_table:
        tables.append(current_table)  # Append the last table to the list of tables

    return tables  # Return the list of tables

# Example usage
file_content = """
table %First table%
row
cell %A1%
cell %B1%
cell%C1%
cell%D1%
ROW
row
CELL %The previous row was blank%
cell %B3%
row
cell %A4% %second line%
cEll %B4% %second line%
cell %C4 second line%
row
cell %%%string%%%
cell %%
cell %%%%
cell %%%%%%
"""

tables = parse_file_content(file_content)
for table in tables:
    print(table)
```

### Detailed Explanation

1. **Importing the `re` Module**:
   - The `re` module is imported to use regular expressions for matching patterns in the file content.

2. **Defining Regular Expression Patterns**:
   - `table_pattern`, `row_pattern`, and `cell_pattern` match the keywords 'table', 'row', and 'cell' case insensitively.
   - `string_pattern` matches strings enclosed by percentage signs and captures their content.

3. **Initialization**:
   - `tables` is a list to store all parsed tables.
   - `current_table` and `current_row` are variables to keep track of the current table and row being processed.

4. **Tokenization**:
   - `tokens` is a list of all keywords, strings, and whitespace in the file content, found using `re.findall`.

5. **Iterating Through Tokens**:
   - Each token is processed in a loop.
   - Leading and trailing whitespace is removed from each token. Empty tokens are skipped.

6. **Processing Keywords and Strings**:
   - **Table Keyword**: If a 'table' keyword is found, the current table is appended to `tables` (if it exists), and a new `RECTable` instance is created.
   - **Row Keyword**: If a 'row' keyword is found, an error is raised if it is outside a table. A new `RECRow` instance is created and added to the current table.
   - **Cell Keyword**: If a 'cell' keyword is found, an error is raised if it is outside a row. A new `RECCell` instance with empty content is created and added to the current row.
   - **String**: If a string is found, its content is processed to replace '%%' with '%'. Depending on the context, the string is added to the table's caption or the last cell's content in the current row.

7. **Handling Errors**:
   - Errors are raised for unexpected tokens, rows outside tables, and cells outside rows.

8. **Appending the Last Table**:
   - After the loop, the last table is appended to `tables`.

9. **Returning the Result**:
   - The function returns the list of parsed tables.

### Example Usage

The provided `file_content` string is parsed, and the resulting tables are printed. This demonstrates how the function processes the file content and stores the data in the predefined data structures.

Understand how the file is parsed according to the specified rules and how the data is stored in the appropriate structures. This solution ensures that the parsing logic is clear and handles the complexity of the custom file format effectively

---
