# ✂️ **Splitting Strings on Multiple Delimiters** ✂️

### **🌟 Problem**
You need to split a string into fields, but the delimiters (and spacing around them) aren’t consistent throughout the string.

### **🔧 Solution**
The `split()` method of string objects is simple and does not allow for multiple delimiters or account for possible whitespace around the delimiters. For more flexibility, use the `re.split()` method.

```python
import re
line = 'asdf fjdk; afed, fjek,asdf, foo'
re.split(r'[;,\s]\s*', line)
# Output: ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
```

##### **💡 Explanation:**

1. **📥 Import the `re` module**: 
   - The `re` module in Python provides support for regular expressions, which are a powerful tool for matching patterns in strings.

2. **📝 Define a string `line`**:
   - `line = 'asdf fjdk; afed, fjek,asdf, foo'`: This string contains several words separated by different delimiters: spaces, semicolons, and commas.

3. **🔍 Use `re.split()`**:
   - `re.split(r'[;,\s]\s*', line)`: This line uses the `re.split()` method to split the string based on multiple delimiters.
   - `r'[;,\s]\s*'` is a regular expression pattern:
     - `;` matches a semicolon.
     - `,` matches a comma.
     - `\s` matches any whitespace character (spaces, tabs, newlines).
     - `\s*` matches zero or more whitespace characters following the delimiter.
   - The `re.split()` function splits the string wherever it matches any of these patterns.
   
4. **📜 Output**:
   - The string is split into a list of words: `['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']`.

---

### 🎯 **Matching Text at the Start or End of a String** 🎯

### **🌟 Problem**
You need to check the start or end of a string for specific text patterns, such as filename extensions or URL schemes.

### **🔧 Solution**
A simple way to check the beginning or end of a string is to use the `str.startswith()` or `str.endswith()` methods.

```python
filename = 'spam.txt'
filename.endswith('.txt')  # Output: True
filename.startswith('file:')  # Output: False
url = 'http://www.python.org'
url.startswith('http:')  # Output: True
```

##### **💡 Explanation:**

1. **🔚 Check if a string ends with a specific pattern**:
   - `filename.endswith('.txt')`: This method checks if the string `filename` ends with the substring `.txt`.
   - **Output**: Returns `True` because `'spam.txt'` indeed ends with `.txt`.

2. **🔜 Check if a string starts with a specific pattern**:
   - `filename.startswith('file:')`: This method checks if the string `filename` starts with the substring `'file:'`.
   - **Output**: Returns `False` because `'spam.txt'` does not start with `'file:'`.

3. **🌐 Check if a URL starts with a specific scheme**:
   - `url.startswith('http:')`: This method checks if the string `url` starts with `'http:'`.
   - **Output**: Returns `True` because the URL `'http://www.python.org'` starts with `'http:'`.

---

### 🧩 **Matching Strings Using Shell Wildcard Patterns** 🧩

### **🌟 Problem**
You want to match text using the same wildcard patterns commonly used in Unix shells (e.g., `*.py`, `Dat[0-9]*.csv`, etc.).

### **🔧 Solution**
The `fnmatch` module provides functions `fnmatch()` and `fnmatchcase()` for such matching.

```python
from fnmatch import fnmatch, fnmatchcase
fnmatch('foo.txt', '*.txt')  # Output: True
fnmatch('foo.txt', '?oo.txt')  # Output: True
fnmatch('Dat45.csv', 'Dat[0-9]*')  # Output: True
```

##### **💡 Explanation:**

1. **📥 Import `fnmatch` module**:
   - `from fnmatch import fnmatch, fnmatchcase`: The `fnmatch` module provides functions for matching filenames and other strings using Unix shell-style wildcards.

2. **📄 Match a file against a wildcard pattern**:
   - `fnmatch('foo.txt', '*.txt')`: This checks if the filename `'foo.txt'` matches the wildcard pattern `'*.txt'`.
   - `*` matches any sequence of characters, so this returns `True` because `'foo.txt'` ends with `.txt`.

3. **❓ Match with a single character wildcard**:
   - `fnmatch('foo.txt', '?oo.txt')`: Here, `?` matches any single character.
   - This returns `True` because `'foo.txt'` has a single character `'f'` followed by `'oo.txt'`.

4. **🔢 Match a filename with a range of numbers**:
   - `fnmatch('Dat45.csv', 'Dat[0-9]*')`: This matches filenames starting with `'Dat'` followed by one or more digits.
   - `[0-9]` matches any digit from `0` to `9`, and `*` matches any sequence of characters.
   - **Output**: Returns `True` because `'Dat45.csv'` matches the pattern.

---

### 🔍 **Matching and Searching for Text Patterns** 🔍

### **🌟 Problem**
You want to match or search text for a specific pattern.

### **🔧 Solution**
For simple literals, use string methods like `str.find()`, `str.endswith()`, or `str.startswith()`.

```python
text = 'yeah, but no, but yeah, but no, but yeah'
text.find('no')  # Output: 10
```

##### **💡 Explanation:**

1. **🔎 Find the position of a substring**:
   - `text.find('no')`: This method searches for the first occurrence of the substring `'no'` in the string `text`.
   - **Output**: Returns `10` because the first `'no'` appears at the 10th position (indexing starts from `0`).

#### **🔧 Solution for more complex patterns**:
For more complicated matching, use regular expressions with the `re` module.

```python
import re
text1 = '11/27/2012'
if re.match(r'\d+/\d+/\d+', text1):
    print('yes')  # Output: yes
```

##### **💡 Explanation:**

1. **📥 Import `re` module**:
   - `import re`: The `re` module provides support for working with regular expressions in Python.

2. **📅 Match a date pattern**:
   - `re.match(r'\d+/\d+/\d+', text1)`:
     - `r'\d+/\d+/\d+'` is a regular expression that matches a date in the format `MM/DD/YYYY`.
     - `\d+` matches one or more digits, and `/` matches the literal slash character.
   - `re.match()` checks if the pattern matches the start of the string `text1`.
   - **Output**: If the string matches the pattern, it returns a match object; otherwise, it returns `None`.
   - **🖨️ If statement**: If there is a match, it prints `'yes'`.

---

### 🔄 **Searching and Replacing Text** 🔄

### **🌟 Problem**
You want to search for and replace a text pattern in a string.

### **🔧 Solution**
For simple literal patterns, use `str.replace()`:

```python
text = 'yeah, but no, but yeah, but no, but yeah'
text.replace('yeah', 'yep')  # Output: 'yep, but no, but yep, but no, but yep'
```

##### **💡 Explanation:**

1. **🔄 Replace occurrences of a substring**:
   - `text.replace('yeah', 'yep')`: This method replaces all occurrences of `'yeah'` in the string `text` with `'yep'`.
   - **Output**: Returns `'yep, but no, but yep, but no, but yep'`.

#### **🔧 Solution for more complex patterns**:
For more complex patterns, use the `re.sub()` function:

```python
import re
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
# Output: 'Today is 2012-11-27. PyCon starts 2013-3-13.'
```

##### **💡 Explanation:**

1. **🔄 Substitute using a regular expression**:
   - `re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)`:
     - `r'(\d+)/(\d+)/(\d+)'` is a regular expression pattern that

 matches a date in `MM/DD/YYYY` format.
     - `r'\3-\1-\2'` specifies the replacement format: `YYYY-MM-DD`.
     - The `re.sub()` function searches for all matches of the pattern and replaces them with the specified format.
   - **Output**: Returns `'Today is 2012-11-27. PyCon starts 2013-3-13.'`.

---

### 🔠 **Handling Case-Insensitive Text Search and Replacement** 🔠

### **🌟 Problem**
You need to search for and possibly replace text in a case-insensitive manner.

### **🔧 Solution**
Use the `re.IGNORECASE` flag:

```python
text = 'UPPER PYTHON, lower python, Mixed Python'
re.findall('python', text, flags=re.IGNORECASE)
# Output: ['PYTHON', 'python', 'Python']
```

##### **💡 Explanation:**

1. **🔍 Find all case-insensitive matches**:
   - `re.findall('python', text, flags=re.IGNORECASE)`:
     - `'python'` is the pattern we want to match.
     - `re.IGNORECASE` is a flag that makes the matching case-insensitive.
     - `re.findall()` returns a list of all matches found in the string `text`.
   - **Output**: The result is `['PYTHON', 'python', 'Python']`, showing all variations of `'python'` regardless of case.

#### **🔧 Solution for case-matching replacements**:
If you need to replace text while matching the case of the original text:

```python
def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace

re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE)
# Output: 'UPPER SNAKE, lower snake, Mixed Snake'
```

##### **💡 Explanation:**

1. **🔄 Define the `matchcase` function**:
   - `matchcase(word)`:
     - This function returns a nested `replace()` function.
     - The `replace()` function takes a match object `m` and checks the case of the matched text:
       - `text.isupper()`: If the text is all uppercase, it returns the replacement word in uppercase.
       - `text.islower()`: If the text is all lowercase, it returns the replacement word in lowercase.
       - `text[0].isupper()`: If the first letter is uppercase, it returns the replacement word capitalized.
       - If none of these conditions are met, it returns the word unchanged.
   
2. **🔄 Use `re.sub()` with the case-matching function**:
   - `re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE)`:
     - This substitutes all occurrences of `'python'` in the string `text` with the word `'snake'`, preserving the original case of each match.
   - **Output**: Returns `'UPPER SNAKE, lower snake, Mixed Snake'`.

---

### 🔍 **Specifying a Regular Expression for the Shortest Match** 🔍

### **🌟 Problem**
You’re trying to match a text pattern using regular expressions but want the shortest possible match instead of the longest.

### **🔧 Solution**
Use the `?` modifier after the `*` operator to make the match nongreedy:

```python
import re
text = 'Computer says "no." Phone says "yes."'
str_pat = re.compile(r'\"(.*?)\"')
str_pat.findall(text)
# Output: ['no.', 'yes.']
```

##### **💡 Explanation:**

1. **📥 Import the `re` module**:
   - `import re`: The `re` module is used for working with regular expressions in Python.

2. **🔍 Compile a regular expression pattern**:
   - `str_pat = re.compile(r'\"(.*?)\"')`:
     - `r'\"(.*?)\"'` is a regular expression pattern designed to match text enclosed in double quotes.
     - `\"` matches the double-quote character.
     - `.*?` matches any character (.) zero or more times (*), but as few times as possible (?), making it nongreedy.
     - The entire pattern matches the shortest possible string within quotes.
   
3. **🔍 Find all matches in the text**:
   - `str_pat.findall(text)`:
     - This method searches the string `text` and returns all substrings that match the pattern.
   - **Output**: The result is `['no.', 'yes.']`, showing the shortest matches inside quotes.

