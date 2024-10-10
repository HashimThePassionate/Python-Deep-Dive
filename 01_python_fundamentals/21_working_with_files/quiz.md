# Quiz Time 🌟📚

### ❓ **Quiz 1: Handling Text Encodings**
**Problem:**  
You need to read or write text data in various **text encodings** such as ASCII, UTF-8, or UTF-16.  
💡 **Hint:** Look into Python’s built-in functions for reading and writing files with different encodings.

### ❓ **Quiz 2: Redirecting `print()` Output**
**Problem:**  
You want to redirect the output of the **`print()` function** to a file instead of the console.  
💡 **Hint:** You can pass a file object to the `file` argument in `print()`.

### ❓ **Quiz 3: Changing `print()` Separators or Line Endings**
**Problem:**  
You want to output data using **`print()`**, but you also want to change the **separator** or **line ending**.  
💡 **Hint:** The `sep` and `end` parameters in `print()` allow you to control the output format.

### ❓ **Quiz 4: Reading/Writing Binary Data**
**Problem:**  
You need to read or write **binary data**, like in images, sound files, etc.  
💡 **Hint:** Use Python’s binary file mode `'rb'` and `'wb'`.

### ❓ **Quiz 5: Writing to a File (Only if it Doesn’t Exist)**
**Problem:**  
You want to write data to a file, but **only if** it doesn’t already exist on the filesystem.  
💡 **Hint:** Look into the `'x'` mode for opening files.

### ❓ **Quiz 6: Feeding a String to File-like Code**
**Problem:**  
You need to pass a text or binary string to code designed for **file-like objects**.  
💡 **Hint:** Python’s `io.StringIO` and `io.BytesIO` provide file-like objects for strings.

### ❓ **Quiz 7: Working with Compressed Files (gzip or bz2)**
**Problem:**  
You need to read or write data from a file with **gzip** or **bz2** compression.  
💡 **Hint:** The `gzip` and `bz2` libraries will help with compressed file handling.

### ❓ **Quiz 8: Reading Fixed-size Chunks from a File**
**Problem:**  
Instead of reading a file **line by line**, you want to read **fixed-sized chunks** or records.  
💡 **Hint:** The `read()` function allows reading specific byte sizes from a file.

### ❓ **Quiz 9: Reading Binary Data into a Mutable Buffer**
**Problem:**  
You want to read binary data into a **mutable buffer** without making intermediate copies and mutate the data in-place before writing it back.  
💡 **Hint:** Using `bytearray` or memoryviews might help with in-place modifications.

### ❓ **Quiz 10: Memory Mapping a File**
**Problem:**  
You want to **memory map** a binary file into a mutable byte array for **random access** and in-place modifications.  
💡 **Hint:** Use the `mmap` module to memory map files.

### ❓ **Quiz 11: Manipulating Pathnames**
**Problem:**  
You need to manipulate **pathnames** to find the base filename, directory name, or absolute path.  
💡 **Hint:** The `os.path` and `pathlib` modules are your friends here.

### ❓ **Quiz 12: Testing File/Directory Existence**
**Problem:**  
You need to check whether a **file or directory exists**.  
💡 **Hint:** Use `os.path.exists()` or `pathlib.Path.exists()` for this.

### ❓ **Quiz 13: Listing Files in a Directory**
**Problem:**  
You want to get a **list of files** contained in a directory.  
💡 **Hint:** The `os.listdir()` or `pathlib.Path().iterdir()` methods work for this.

### ❓ **Quiz 14: Handling Raw Filenames**
**Problem:**  
You need to perform file I/O using **raw filenames** that haven’t been decoded or encoded according to the default filename encoding.  
💡 **Hint:** Look into the `os` and `open()` functions that support raw filenames.

### ❓ **Quiz 15: Handling UnicodeEncodeError (Surrogates Not Allowed)**
**Problem:**  
Your program crashed with a **UnicodeEncodeError** when printing filenames due to surrogates.  
💡 **Hint:** You may need to handle invalid characters with error handling options in Python’s encoding system.

### ❓ **Quiz 16: Changing Unicode Encoding of an Open File**
**Problem:**  
You want to change the **Unicode encoding** of an already open file without closing it.  
💡 **Hint:** Use the `io.TextIOWrapper()` method to change encoding on the fly.

### ❓ **Quiz 17: Writing Raw Bytes in Text Mode**
**Problem:**  
You want to write **raw bytes** to a file opened in **text mode**.  
💡 **Hint:** Open the file in binary mode for raw byte writing.

### ❓ **Quiz 18: Creating a Temporary File/Directory**
**Problem:**  
You need to create a **temporary file or directory** that will be destroyed after use.  
💡 **Hint:** The `tempfile` module in Python is designed for this purpose.

### ❓ **Quiz 19: Serializing a Python Object**
**Problem:**  
You need to **serialize a Python object** into a byte stream for saving to a file, database, or network transmission.  
💡 **Hint:** Python’s `pickle` module is ideal for object serialization.
