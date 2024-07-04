### Extreme "Normalization": Taking Out Diacritics

Removing diacritics (accents, cedillas, etc.) from text can help in certain contexts, such as making text more readable or easier to search. However, it is not a proper form of normalization because it can change the meaning of words and produce false positives in searches. Despite this, it can be useful in some cases where users may not always use diacritics correctly or where spelling rules change over time.

#### Example: Wikipedia URL
Removing diacritics can make URLs more readable, especially in Latin-based languages. For example, the URL for the Wikipedia article about São Paulo:
- With diacritics: `https://en.wikipedia.org/wiki/S%C3%A3o_Paulo`
- Without diacritics: `https://en.wikipedia.org/wiki/Sao_Paulo`

### Function to Remove Diacritics

To remove all diacritics from a string, you can use the `shave_marks` function.

#### Code: shave_marks.py
```python
import unicodedata

def shave_marks(txt):
    """Remove all diacritic marks"""
    norm_txt = unicodedata.normalize('NFD', txt)
    shaved = ''.join(c for c in norm_txt if not unicodedata.combining(c))
    return unicodedata.normalize('NFC', shaved)
```

### Explanation:

1. **Decompose Characters**: Break down characters into base characters and combining marks using `NFD` normalization.
2. **Filter Combining Marks**: Remove all combining marks (diacritics).
3. **Recompose Characters**: Recompose the characters into their shortest form using `NFC` normalization.

### Usage Examples:

1. **Removing Diacritics from a Sentence**:
    ```python
    order = '“Herr Voß: • ½ cup of Œtker™ caffè latte • bowl of açaí.”'
    print(shave_marks(order))  # Output: '“Herr Voss: • ½ cup of OEtker™ caffe latte • bowl of acai.”'
    ```

2. **Removing Diacritics from Greek Text**:
    ```python
    Greek = 'Ζέφυρος, Zéfiro'
    print(shave_marks(Greek))  # Output: 'Ζεφυρος, Zefiro'
    ```

### Function for Latin Characters Only

The `shave_marks` function also removes diacritics from non-Latin characters. If you only want to remove diacritics from Latin characters, use the `shave_marks_latin` function.

#### Code: shave_marks_latin.py
```python
import unicodedata
import string

def shave_marks_latin(txt):
    """Remove all diacritic marks from Latin base characters"""
    norm_txt = unicodedata.normalize('NFD', txt)
    latin_base = False
    preserve = []
    for c in norm_txt:
        if unicodedata.combining(c) and latin_base:
            continue  # ignore diacritic on Latin base char
        preserve.append(c)
        if not unicodedata.combining(c):
            latin_base = c in string.ascii_letters
    shaved = ''.join(preserve)
    return unicodedata.normalize('NFC', shaved)
```

### Explanation:

1. **Decompose Characters**: Break down characters into base characters and combining marks using `NFD` normalization.
2. **Filter Combining Marks for Latin Characters**: Remove combining marks only if the base character is a Latin letter.
3. **Recompose Characters**: Recompose the characters into their shortest form using `NFC` normalization.

### Function to Replace Symbols with ASCII

To replace common symbols in Western texts (e.g., curly quotes, em dashes, bullets) with ASCII equivalents, use the `asciize` function.

#### Code: asciize.py
```python
single_map = str.maketrans("""‚ƒ„ˆ‹‘’“”•–—˜›""",
                          """'f"^<''""---~>""")
multi_map = str.maketrans({
    '€': 'EUR',
    '…': '...',
    'Æ': 'AE',
    'æ': 'ae',
    'Œ': 'OE',
    'œ': 'oe',
    '™': '(TM)',
    '‰': '<per mille>',
    '†': '**',
    '‡': '***',
})
multi_map.update(single_map)

def dewinize(txt):
    """Replace Win1252 symbols with ASCII chars or sequences"""
    return txt.translate(multi_map)

def asciize(txt):
    no_marks = shave_marks_latin(dewinize(txt))
    no_marks = no_marks.replace('ß', 'ss')
    return unicodedata.normalize('NFKC', no_marks)
```

### Explanation:

1. **dewinize Function**:
    - Replace Windows-1252 symbols with ASCII characters or sequences.
    - Example: Curly quotes are replaced with straight quotes.

2. **asciize Function**:
    - Apply `dewinize` to replace symbols.
    - Remove diacritical marks from Latin characters.
    - Replace the German Eszett 'ß' with 'ss'.
    - Apply `NFKC` normalization to further simplify characters.

### Usage Examples:

1. **Replacing Symbols and Removing Diacritics**:
    ```python
    order = '“Herr Voß: • ½ cup of Œtker™ caffè latte • bowl of açaí.”'
    print(dewinize(order))  # Output: '"Herr Voß: - ½ cup of OEtker(TM) caffè latte - bowl of açaí."'
    print(asciize(order))  # Output: '"Herr Voss: - 1⁄2 cup of OEtker(TM) caffe latte - bowl of acai."'
    ```

### Summary

The functions in `simplify.py` go beyond standard normalization and perform deep transformations on the text. This can significantly change its meaning, so use these functions with caution, considering the target language, your users, and how the transformed text will be used. 

This concludes our discussion on normalizing Unicode text. Next, we will explore Unicode sorting.