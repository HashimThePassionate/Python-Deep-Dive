# Basic Regular Expressions — Practical Guide 🚀

> Learn regex with **use cases + explanations + Python examples**.
> Regex is not just syntax — it’s about solving real search-and-match problems.

---

## 1) Match Exact Text (and escape the tricky characters) ✍️

**Why?**
Sometimes you need to **match text exactly as written** (like config lines, passwords, punctuation strings). But some symbols have **special meanings** in regex (e.g. `*` means “repeat”, `.` means “any character”). To match them literally, you must **escape** them with `\`.

**Regex**

```regex
!"#\$%&'\(\)\*\+,-\./:;<=>\?@\[\]\\\^_`\{\|\}~\.
```

**Python Example**

```python
import re
text = 'The punctuation characters in the ASCII table are: !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~.'
pat  = r'The\s+punctuation\s+characters\s+in\s+the\s+ASCII\s+table\s+are:\s+!"#\$%&\'\(\)\*\+,-\./:;<=>\?@\[\]\\\^_`\{\|\}~\.'
print(bool(re.fullmatch(pat, text)))  # ✅ True
```

---

## 2) Match Nonprintable / Control Characters 🔔↩️

**Why?**
Text files or network data often contain **hidden characters**:

* `\n` = newline
* `\t` = tab
* `\x1B` = escape

You may need to detect or remove them.

**Regex**

```regex
\a\x1B\f\n\r\t\v
```

**Python Example**

```python
s = "\a\x1B\f\n\r\t\v"
print(bool(re.fullmatch(r"\a\x1B\f\n\r\t\v", s)))  # ✅ True
```

---

## 3) Character Classes 🔤

**Why?**
A character class `[ ]` lets you choose **one of many** characters at a position.

* `[ae]` → matches **either** `a` or `e`
* `[^0-9]` → matches **anything except digits**

### Example 3.1: catch misspellings of *calendar*

```python
pat = r'c[ae]l[ae]nd[ae]r'
print(re.findall(pat, "calender, calandar, celendar, celandar"))
# ['calender', 'calandar', 'celendar', 'celandar']
```

### Example 3.2: match one **hex digit**

```python
pat = r'[0-9A-Fa-f]'
```

### Example 3.3: match one **non-hex** character

```python
pat = r'[^0-9A-Fa-f]'
```

---

## 4) The Dot `.` 🟦

**Why?**
The `.` metacharacter matches **any single character** (except line breaks).
Useful for “match anything here” situations.

* Without newlines → `.`
* With newlines → `(?s).` or `[\s\S]`

**Example**

```python
text = "Hi\nThere"
print(re.findall(r'.', text))        # skips '\n'
print(re.findall(r'(?s).', text))    # includes '\n'
```

---

## 5) Anchors (Start / End) 📍

**Why?**
Anchors don’t match characters, they match **positions**.

* `^` = start of line
* `$` = end of line
* `\A` = start of entire text
* `\Z` = end of entire text

**Example**

```python
print(bool(re.match(r'^\balpha\b', "alpha is first")))     # ✅ True
print(bool(re.search(r'\bomega\b$', "ends with omega")))   # ✅ True
```

With `MULTILINE`, `^` and `$` work on each line:

```python
text = "line1\nbegin here"
print(re.findall(r'^begin', text, re.MULTILINE))  # ['begin']
```

---

## 6) Word Boundaries 🐱

**Why?**
Use `\b` to ensure a word is matched as a **whole word**.
Use `\B` to match **inside a word**.

**Example**

```python
print(re.findall(r'\bcat\b', "My cat, not bobcat or category")) # ['cat']
print(re.findall(r'\Bcat\B', "staccato bobcat cat"))            # ['cat'] from sta**cat**to
```

---

## 7) Alternation (OR) 🔀

**Why?**
The `|` operator works like “OR”. Great for matching **one of many keywords**.

**Example**

```python
pat = r'\b(Muhammad|Hashim|Ali)\b'
text = "Muhammad, Hashim, and Ali went to Muhammad's house."
print(re.findall(pat, text))
# ['Muhammad', 'Hashim', 'Ali', 'Muhammad']
```

---

## 8) Backreferences 🔁

**Why?**
Sometimes the same text must appear in multiple places.
Backreferences let you say “repeat what group 1 matched”.

**Example: magical dates (2008-08-08, 2011-11-11)**

```python
pat = r'\b\d{2}(\d{2})-\1-\1\b'
text = "2008-08-08 2024-09-12 2011-11-11"
print(re.findall(pat, text))  # ['08', '11']
```

---

## 9) Quantifiers 🔢

**Why?**
Quantifiers control **how many times** something repeats.

* `{n}` → exactly n
* `{n,m}` → between n and m
* `+` → 1 or more
* `*` → 0 or more
* `?` → optional

**Examples**

```python
# Exactly 100 digits
googol = r'\b\d{100}\b'

# 1 to 8 hex digits (case-insensitive)
hexnum = r'(?i)\b[0-9a-f]{1,8}\b'

# Optional 'h' suffix
hex_h  = r'(?i)\b[0-9a-f]{1,8}h?\b'

# Floating point
floatnum = r'\d*\.\d+(?:[eE][+-]?\d+)?'
```

---

## 10) Minimal vs Greedy 🔄

**Why?**
Regex is greedy by default: `.*` grabs as much as possible.
Use `*?` to make it **lazy** and stop earlier.

**Example: get `<p>...</p>` blocks**

```python
html = "<p>one <em>em</em></p><p>two</p>"
print(re.findall(r'<p>.*?</p>', html, re.DOTALL))
# ['<p>one <em>em</em></p>', '<p>two</p>']
```

---

## 11) Lookarounds 👀

**Why?**
Sometimes you need to match something **inside a context** but not include the context itself.

**Example: text inside `<b>...</b>`**

```python
text = "My <b>cat</b> is <b>fluffy</b>."
print(re.findall(r'(?<=<b>)\w+(?=</b>)', text))  # ['cat', 'fluffy']
```

---

## 12) Substitution / Replacement 🔄

**Why?**
Regex isn’t only for matching—it can also **reformat text**.

### Wrap entire match with HTML

```python
text = "Visit example.com"
print(re.sub(r'\b\w+\b', r'<a href="\g<0>">\g<0></a>', text))
```

### Format phone numbers

```python
text = "Call 1234567890"
print(re.sub(r'(\d{3})(\d{3})(\d{4})', r'(\1) \2-\3', text))
# (123) 456-7890
```

---

## 13) Named Groups 🏷️

**Why?**
Named groups make regexes self-documenting.

**Example**

```python
pat = r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})'
m = re.search(pat, "2024-09-12")
print(m.group('year'), m.group('month'), m.group('day'))  # 2024 09 12
```

---

## Cheatsheet 🧠

* Escape meta: `.^$*+?()[]{}|\`
* Dot `.` = any char (except newline)
* `\d` digit, `\w` word, `\s` space
* `^` start, `$` end, `\b` word boundary
* `(...)` capture, `(?:...)` non-capture
* Backref `\1`, whole match in replace: `\g<0>`

---

✨ with this, you now know the **core 80% of regex** used in real projects:

* parsing logs,
* cleaning data,
* validating input,
* text extraction.

---

