# Character Issues
## Definition
A **string** is a sequence of **characters**. Defining what a **“character”** is can be complex.

### Definition of Character
In modern programming, a character is best defined as a Unicode character. In Python 3, strings (`str`) are sequences of Unicode characters. In Python 2, strings were sequences of raw bytes.

### Unicode Standard
The Unicode standard separates the identity of characters from their byte representations.The Unicode Standard is a system for encoding, representing, and handling text from different writing systems in computers and other digital devices. **It ensures that characters from almost all languages can be used and displayed consistently across various platforms and programs.**
When we talk about encoding characters consistently across various platforms and programs, we mean different types of systems and software that can handle text. Here are some examples:

#### Types of Platforms:

<pre>
+---------------------+-----------------------+-------------------------+
| Operating Systems   | Web Browsers          | Text Editors & IDEs     |
+---------------------+-----------------------+-------------------------+
| - Windows           | - Google Chrome       | - Visual Studio Code    |
| - macOS             | - Mozilla Firefox     | - Sublime Text          |
| - Linux             | - Safari              | - Atom                  |
| - Android           | - Microsoft Edge      | - PyCharm               |
| - iOS               |                       |                         |
+---------------------+-----------------------+-------------------------+

+---------------------+-----------------------+-------------------------+
| Office Suites       | Email Clients         | Social Media Platforms  |
+---------------------+-----------------------+-------------------------+
| - Microsoft Office  | - Microsoft Outlook   | - Facebook              |
| - Google Workspace  | - Gmail               | - Twitter               |
| - LibreOffice       | - Apple Mail          | - Instagram             |
|                     | - Thunderbird         | - LinkedIn              |
+---------------------+-----------------------+-------------------------+

+---------------------+-----------------------+-------------------------+
| Messaging Apps      | Databases             | Programming Languages   |
+---------------------+-----------------------+-------------------------+
| - WhatsApp          | - MySQL               | - Python                |
| - Telegram          | - PostgreSQL          | - Java                  |
| - Slack             | - SQLite              | - JavaScript            |
| - Microsoft Teams   | - MongoDB             | - C++                   |
|                     |                       | - Ruby                  |
+---------------------+-----------------------+-------------------------+

+---------------------+-----------------------+-------------------------+
| Web Frameworks      | Multimedia Applications                         |
+---------------------+-----------------------+-------------------------+
| - Django            | - Adobe Photoshop                               |
| - Flask             | - Final Cut Pro                                 |
| - React             | - VLC Media Player                              |
| - Angular           |                                                 |
+---------------------+-----------------------+-------------------------+
</pre>

#### Importance:

By using a standardized encoding like Unicode, these platforms and programs can correctly display, process, and exchange text data, regardless of the language or symbols used. This ensures that text looks the same and functions properly no matter where it's being used or viewed.

#### Key Concepts:
- A code point is a unique number given to each character.
- The range of code points is from 0 to 1,114,111 in decimal (base 10).
- Code points are usually written in hexadecimal (base 16) and start with “U+”.

Here are a few examples of characters and their corresponding code points:
<pre>
+----------------+-------------------------+--------------------------+
| Character      | Decimal Code Point      | Hexadecimal Code Point   |
+----------------+-------------------------+--------------------------+
| A              | 65                      | U+0041                   |
| B              | 66                      | U+0042                   |
| €              | 8364                    | U+20AC                   |
+----------------+-------------------------+--------------------------+
</pre>
#### Examples:

1. **Letter A**:
   - Code Point: U+0041
   - The letter 'A' is represented by the number 0041 in hexadecimal.

2. **Euro Sign (€)**:
   - Code Point: U+20AC
   - The euro currency symbol is represented by the number 20AC in hexadecimal.

3. **Musical Symbol G Clef (𝄞)**:
   - Code Point: U+1D11E
   - The musical G clef symbol is represented by the number 1D11E in hexadecimal.

#### Explanation:

- **Separation of Identity and Representation:**
  - The Unicode standard separates the identity of a character (like 'A') from how it is stored in a computer (its byte representation). This helps in consistently displaying characters across different systems.

- **Assignment of Code Points:**
  - Out of the total possible code points, only about 13% are assigned to actual characters in the current version of Unicode (13.0.0). The rest are reserved for future use.

## Encoding

**Encoding** is like translating the unique numbers (code points) assigned to each character into a format that computers can store and understand, called bytes.

#### Key Points:

1. **Conversion Process:**
   - Encoding changes code points (unique numbers for characters) into bytes (the basic units of data storage).

2. **Different Encodings:**
   - There are various methods to encode characters, such as UTF-8 and UTF-16, which use different amounts of bytes to represent characters.

#### Examples:

1. **Letter A (U+0041):**
   - **UTF-8 Encoding:**
     - Uses one byte: `\x41`
     - In hexadecimal: 41
   - **UTF-16LE Encoding:**
     - Uses two bytes: `\x41\x00`
     - In hexadecimal: 41 00

2. **Euro Sign (€) (U+20AC):**
   - **UTF-8 Encoding:**
     - Uses three bytes: `\xe2\x82\xac`
     - In hexadecimal: E2 82 AC
   - **UTF-16LE Encoding:**
     - Uses two bytes: `\xac\x20`
     - In hexadecimal: AC 20

#### Why Encoding Matters:

Encoding ensures that characters are stored and transmitted correctly between different systems and devices. By converting characters into bytes, encoding enables computers to process and display text from various languages and symbols consistently. Different encodings balance between the number of bytes used and the range of characters they can represent, optimizing for different needs and systems.

## Encoding and Decoding
Encoding converts code points to bytes, while decoding converts bytes to code points.

##### Example: Encoding and Decoding
```python
s = 'café'
print(len(s))  # Output: 4

b = s.encode('utf8')
print(b)  # Output: b'caf\xc3\xa9'
print(len(b))  # Output: 5

decoded_s = b.decode('utf8')
print(decoded_s)  # Output: 'café'
```

**Explanation**:
- The string `s` ('café') has four Unicode characters.
- Encoding the string `s` to bytes using UTF-8 results in `b`, which has five bytes. The character “é” is encoded as two bytes (`\xc3\xa9`) in UTF-8.
- Bytes literals have a `b` prefix.
- Decoding the bytes `b` back to a string using UTF-8 restores the original string 'café'.

#### Memory Aid
To help distinguish `.decode()` from `.encode()`, remember:
- Byte sequences can be cryptic machine data.
- Unicode strings (`str`) are human-readable text.
- Therefore, decode bytes to strings to get human-readable text, and encode strings to bytes for storage or transmission.

#### Python 3 `str` and `bytes`
- The Python 3 `str` type is similar to the Python 2 `unicode` type.
- The Python 3 `bytes` type is not just a renamed version of the old Python 2 `str`.
- There is also the closely related `bytearray` type.

#### Conclusion
Understanding the differences between strings, bytes, and encodings is crucial for handling text effectively in Python.

---

**Simple Explanation**:

1. **Character**: A character is a symbol like 'A', '€', or 'é'.
2. **Unicode**: A standard that assigns a unique number (code point) to each character, e.g., 'A' is U+0041.
3. **Encoding**: Converting characters to bytes. Different encodings (like UTF-8, UTF-16) use different numbers of bytes to represent characters.
4. **Decoding**: Converting bytes back to characters.
5. **Example**:
   - `'café'` has 4 characters.
   - Encoding `'café'` to UTF-8 gives `b'caf\xc3\xa9'` (5 bytes).
   - Decoding `b'caf\xc3\xa9'` back to characters gives `'café'`.

Use `.encode()` to convert a string to bytes, and `.decode()` to convert bytes to a string. This helps in storing or transmitting text data.