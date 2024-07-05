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
