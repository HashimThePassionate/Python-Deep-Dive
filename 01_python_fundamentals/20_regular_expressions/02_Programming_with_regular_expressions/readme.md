# 📚 Programming with Regular Expressions

## 🌟 Introduction

Regular expressions (regex) are powerful tools used for matching patterns in text. They are used in many programming languages for tasks such as validation, searching, and text manipulation.

## 📝 Basics of Regular Expressions

### ❓ What is a Regular Expression?

A regular expression is a sequence of characters that defines a search pattern. This pattern can be used to match strings within text.

### 💡 Common Symbols and Syntax

- **Literal Characters**: Simply match themselves (e.g., `a` matches the character 'a').
- **Metacharacters**: Special characters that have a unique meaning (e.g., `.` matches any character except a newline).
- **Quantifiers**: Specify the number of occurrences (e.g., `*`, `+`, `{n}`).
- **Anchors**: Assert the position in the string (e.g., `^` for the start, `$` for the end).

### 🔤 Character Classes

Character classes allow you to define a set of characters to match. For example, `[abc]` matches any of 'a', 'b', or 'c'.

### 📚 Groups and Ranges

- **Groups**: Parentheses `( )` are used to group parts of the pattern.
- **Ranges**: Square brackets `[ ]` define a range of characters.

## 🚀 Advanced Features

### 🔍 Lookahead and Lookbehind

Lookahead and lookbehind assertions specify a pattern that must (or must not) follow or precede a certain point.

### 🚫 Non-Capturing Groups

Non-capturing groups `(?: )` group parts of the pattern without storing the matched text.

### 🏷️ Named Groups

Named groups `(?P<name> )` allow you to reference matched groups by name.

## 💡 Practical Examples

### 📧 Matching an Email Address

A common regex for matching email addresses is:

```
^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$
```

### 📞 Validating a Phone Number

A regex for validating phone numbers might look like:

```
^\+?[0-9]{1,4}?[-.\s]?(\(?\d{1,3}?\))?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}$
```

### 📅 Finding Dates in Text

To find dates in the format `DD/MM/YYYY`, you could use:

```
\b\d{2}/\d{2}/\d{4}\b
```

## 🛠️ Tools and Libraries

### 💻 Regex in Different Languages

- **Python**: `import re`
- **JavaScript**: `new RegExp()`
- **Java**: `Pattern` and `Matcher` classes

### 🌐 Online Tools

- [Regex101](https://regex101.com/)
- [RegExr](https://regexr.com/)

## 🎯 Conclusion

Regular expressions are a versatile and powerful tool for text processing. By understanding the basics and advanced features, you can leverage regex to solve complex text matching and manipulation tasks efficiently.

---
