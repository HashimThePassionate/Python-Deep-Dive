### Normalizing Unicode for Reliable Comparisons

String comparisons can be tricky because Unicode has combining characters like accent marks that attach to the preceding character, making them look the same when printed.

#### Example:
The word "café" can be written in two ways using four or five characters, but they look identical:
```python
s1 = 'café'
s2 = 'cafe\N{COMBINING ACUTE ACCENT}'
print(s1, s2)  # Output: ('café', 'café')
print(len(s1), len(s2))  # Output: (4, 5)
print(s1 == s2)  # Output: False
```
**Accent marks**, also known as diacritical marks, are symbols added to letters to alter their pronunciation or to distinguish between words. They are used in many languages to indicate various phonetic values or to show which syllable in a word is stressed.
<pre>
| Accent Mark | Name               | Example | Language   | Description                                                     |
|-------------|--------------------|---------|------------|-----------------------------------------------------------------|
| ´           | Acute Accent       | é       | French     | Indicates a stressed vowel or a change in pronunciation.        |
| `           | Grave Accent       | è       | Italian    | Often indicates a stressed syllable or a change in vowel sound. |
| ^           | Circumflex Accent  | â       | French     | Indicates a long vowel sound or a missing letter.               |
| ¨           | Diaeresis (Umlaut) | ü       | German     | Indicates a separate vowel sound or a change in pronunciation.  |
| ~           | Tilde              | ñ       | Spanish    | Indicates a nasalized sound.                                    |
| ˇ           | Caron (Háček)      | č       | Czech      | Indicates a "soft" or palatalized sound.                        |
| ˘           | Breve              | ŭ       | Romanian   | Indicates a short vowel sound.                                  |
| ˛           | Ogonek             | ą       | Polish     | Indicates nasalization or a different vowel quality.            |
| ˙           | Dot Above          | ė       | Lithuanian | Indicates a different vowel quality or a specific pronunciation.|
| ̵           | Macron             | ā       | Latvian    | Indicates a long vowel sound.                                   |
| ̧           | Cedilla            | ç       | French     | Indicates a soft 'c' sound (like 's').                          |
| ′           | Prime              | ʹ       | Phonetic   | Used in phonetic transcription to indicate primary stress.      |

</pre>
These accent marks serve various purposes in different languages, such as indicating stress, tone, vowel length, or nasalization.

In Unicode, sequences like 'é' and 'e\u0301' are called "canonical equivalents" and should be treated as the same. However, Python sees them as different sequences and considers them not equal.

#### Solution: `unicodedata.normalize()`
The `normalize()` function makes these sequences comparable by converting them into a standard form. It takes one of four strings: 'NFC', 'NFD', 'NFKC', and 'NFKD'. Let's start with the first two:

- **NFC (Normalization Form C)**: Combines characters to produce the shortest equivalent string.
- **NFD (Normalization Form D)**: Splits combined characters into base characters and separate combining characters.

Both normalizations make comparisons work as expected:
```python
from unicodedata import normalize

s1 = 'café'
s2 = 'cafe\N{COMBINING ACUTE ACCENT}'

print(len(s1), len(s2))  # Output: (4, 5)
print(len(normalize('NFC', s1)), len(normalize('NFC', s2)))  # Output: (4, 4)
print(len(normalize('NFD', s1)), len(normalize('NFD', s2)))  # Output: (5, 5)
print(normalize('NFC', s1) == normalize('NFC', s2))  # Output: True
print(normalize('NFD', s1) == normalize('NFD', s2))  # Output: True
```

Keyboard drivers usually generate composed characters, so text typed by users will be in NFC by default. It's a good practice to normalize strings with `normalize('NFC', user_text)` before saving.

#### Special Characters: Ohm and Micro Sign
Some single characters are normalized into another single character. For example, the ohm sign (Ω) is normalized to the Greek uppercase omega. They look identical but compare as unequal unless normalized.

```python
from unicodedata import normalize, name

ohm = '\u2126'
print(name(ohm))  # Output: 'OHM SIGN'

ohm_c = normalize('NFC', ohm)
print(name(ohm_c))  # Output: 'GREEK CAPITAL LETTER OMEGA'

print(ohm == ohm_c)  # Output: False
print(normalize('NFC', ohm) == normalize('NFC', ohm_c))  # Output: True
```

#### Compatibility Normalizations: NFKC and NFKD
The letter K stands for "compatibility." These forms affect "compatibility characters," which have multiple representations for compatibility with older standards.

Examples:
- The MICRO SIGN (µ) is a compatibility character.
- The compatibility decomposition of the fraction '½' (U+00BD) is '1/2'.

```python
from unicodedata import normalize, name

half = '\N{VULGAR FRACTION ONE HALF}'
print(half)  # Output: ½
print(normalize('NFKC', half))  # Output: 1⁄2

for char in normalize('NFKC', half):
    print(char, name(char), sep='\t')
# Output:
# 1   DIGIT ONE
# ⁄   FRACTION SLASH
# 2   DIGIT TWO

four_squared = '4²'
print(normalize('NFKC', four_squared))  # Output: 42

micro = 'µ'
micro_kc = normalize('NFKC', micro)
print(micro, micro_kc)  # Output: ('µ', 'μ')
print(ord(micro), ord(micro_kc))  # Output: (181, 956)
print(name(micro), name(micro_kc))  # Output: ('MICRO SIGN', 'GREEK SMALL LETTER MU')
```

NFKC and NFKD can lose or distort information, so they should be used for search and indexing, not for permanent storage.

### Important Note
#### NFKC and NFKD Normalization

- **NFKC (Normalization Form KC) and NFKD (Normalization Form KD)**:
  - These normalization forms change some characters to make them simpler or more compatible with older systems.
  - This can cause data loss, meaning some details or formatting might be lost or changed.

#### When to Use

- **Special Cases**:
  - Use NFKC and NFKD when you need to search through text or organize (index) it. This helps in finding and sorting text more reliably.

- **Not for Permanent Storage**:
  - Do not use NFKC and NFKD for saving text permanently because they might change or lose some information.

#### Case Folding

- **Case Folding**:
  - This is another technique used to make text comparisons easier by converting all characters to the same case (usually lowercase).
  - It is useful for searching and indexing text to ensure that case differences (e.g., 'A' vs 'a') do not affect the comparison.

#### Example:

Imagine you have a text document with the word "Résumé" written in different ways:
- "Résumé"
- "Resume"
- "RESUMÉ"

Using NFKC/NFKD and case folding helps in treating all these variations as the same word for searching and indexing, but not for permanently saving the document because the original formatting (like accents) might be lost.