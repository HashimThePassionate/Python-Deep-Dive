# Finding Characters by Name

The `unicodedata` module has functions to retrieve character metadata, including `unicodedata.name()`, which returns a character’s official name in the standard.

#### Example Usage of unicodedata.name()

```python
from unicodedata import name

print(name('A'))    # Output: 'LATIN CAPITAL LETTER A'
print(name('ä'))    # Output: 'LATIN SMALL LETTER A WITH TILDE'
print(name('♕'))    # Output: 'BLACK CHESS QUEEN'
print(name('😸'))  # Output: 'GRINNING CAT FACE WITH SMILING EYES'
```

**Explanation**: 
- `name('A')` returns the official name 'LATIN CAPITAL LETTER A' for the character 'A'.
- `name('ä')` returns the official name 'LATIN SMALL LETTER A WITH TILDE' for the character 'ä'.
- `name('♕')` returns the official name 'BLACK CHESS QUEEN' for the chess queen symbol.
- `name('😸')` returns the official name 'GRINNING CAT FACE WITH SMILING EYES' for the cat face emoji.

You can use the `name()` function to build apps that let users search for characters by name.

### Example: main.py Script

Figure 4-6 demonstrates the `main.py` command-line script that takes one or more words as arguments and lists the characters that have those words in their official Unicode names. The full source code for `main.py` is in Example 4-21.

#### Example 4-21: main.py: The Character Finder Utility

```python
#!/usr/bin/env python3
import sys
import unicodedata

# Set the start and end range for Unicode code points
START, END = ord(' '), sys.maxunicode + 1

def find(*query_words, start=START, end=END):
    # Convert query words to uppercase and store them in a set
    query = {w.upper() for w in query_words}
    for code in range(start, end):
        # Get the character for the Unicode code point
        char = chr(code)
        # Get the official Unicode name of the character, or None if it doesn't have a name
        name = unicodedata.name(char, None)
        # If the character has a name and the query is a subset of the name's words
        if name and query.issubset(name.split()):
            # Print the code point, character, and name in a formatted string
            print(f'U+{code:04X}\t{char}\t{name}')

def main(words):
    if words:
        # If words are provided, call the find function
        find(*words)
    else:
        # If no words are provided, print a prompt to the user
        print('Please provide words to find.')

if __name__ == '__main__':
    # If the script is run directly, execute the main function with command-line arguments
    main(sys.argv[1:])
```

**Explanation**: 
- `START, END = ord(' '), sys.maxunicode + 1`: This sets the range of Unicode code points to search. It starts at the space character (`' '`) and ends at the maximum Unicode code point (`sys.maxunicode + 1`).
- `def find(*query_words, start=START, end=END)`: The `find` function accepts `query_words` as arguments and optional keyword-only arguments `start` and `end` to limit the range of the search.
- `query = {w.upper() for w in query_words}`: This converts the `query_words` into a set of uppercased strings for case-insensitive matching.
- `for code in range(start, end)`: This loop iterates over the range of Unicode code points.
- `char = chr(code)`: This gets the Unicode character corresponding to the current code point.
- `name = unicodedata.name(char, None)`: This gets the official Unicode name of the character, or `None` if the character does not have a name.
- `if name and query.issubset(name.split())`: This checks if the character has a name and if all the words in the query set are present in the character's name.
- `print(f'U+{code:04X}\t{char}\t{name}')`: This prints the Unicode code point, the character, and its name in a formatted string.
- `def main(words)`: This function is the entry point of the script, which calls the `find` function with the provided words.
- `if __name__ == '__main__'`: This ensures that the `main` function is called only when the script is executed directly, not when it is imported as a module.

#### Output Example: Using main.py to Find Smiling Cats

```shell
$ ./main.py cat smiling
U+1F638 😸  GRINNING CAT FACE WITH SMILING EYES
U+1F63A 😺  SMILING CAT FACE WITH OPEN MOUTH
U+1F63B 😻  SMILING CAT FACE WITH HEART-SHAPED EYES
```

**Explanation**: 
- The script `main.py` searches for and displays characters by name, showing the Unicode code point, the character, and its official name.

### Emoji Support in Different Systems

Emoji support varies widely across operating systems and apps. In recent years, the macOS terminal offers the best support for emojis, followed by modern GNU/Linux graphic terminals. Windows `cmd.exe` and PowerShell now support Unicode output, but as of January 2020, they still don’t display emojis “out of the box.” A new open-source Windows Terminal by Microsoft might have better Unicode support than the older Microsoft consoles.

### Using the `issubset()` Method

In Example 4-21, the `if` statement in the `find` function uses the `.issubset()` method to quickly test whether all the words in the query set appear in the list of words built from the character’s name. Thanks to Python’s rich set API, we don’t need a nested `for` loop and another `if` to implement this check.

### Summary

- **Unicode Database**: Provides detailed information about each character.
- **String Methods**: Utilize this database to check character properties.
- **main.py Script**: Demonstrates how to search for characters by name using command-line arguments.
