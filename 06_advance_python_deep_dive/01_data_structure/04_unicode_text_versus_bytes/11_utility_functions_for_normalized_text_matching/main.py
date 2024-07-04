from unicodedata import normalize, name

def nfc_equal(str1, str2):
    """
    Compare two strings using Normal Form C (NFC).
    This ensures that equivalent characters are treated as equal.
    """
    return normalize('NFC', str1) == normalize('NFC', str2)

def fold_equal(str1, str2):
    """
    Compare two strings using Normal Form C (NFC) with case folding.
    This ensures that equivalent characters are treated as equal,
    ignoring case differences.
    """
    return (normalize('NFC', str1).casefold() == normalize('NFC', str2).casefold())

def print_unicode_names(s):
    """
    Print the Unicode names of each character in the string.
    """
    for char in s:
        print(f"{char}: {name(char)}")

s1 = 'café'
s2 = 'cafe\u0301'

print("Unicode names for s1:")
print_unicode_names(s1)
print("\nUnicode names for s2:")
print_unicode_names(s2)

print(f"\ns1: {s1}")
print(f"s2: {s2}")
print(s1 == s2)  # Output: False
print(nfc_equal(s1, s2))  # Output: True

print("\nUnicode names for 'A':")
print(name('A'))  # Output: 'LATIN CAPITAL LETTER A'
print("\nUnicode names for 'a':")
print(name('a'))  # Output: 'LATIN SMALL LETTER A'
print(nfc_equal('A', 'a'))  # Output: False
