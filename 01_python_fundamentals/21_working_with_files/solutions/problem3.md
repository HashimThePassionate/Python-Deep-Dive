# 📝 **Quiz 3: Changing `print()` Separators or Line Endings**

### Problem:
You want to **customize the output** of the `print()` function by changing the **separator** between printed values or modifying the **line ending**.

### 💡 **Hint**:
The `print()` function in Python has two optional parameters:
- **`sep`**: Defines the **separator** between multiple arguments (default is a space `' '`).
- **`end`**: Specifies what will be printed at the **end of the output** (default is a newline `'\n'`).

### 🔧 **Solution: Customizing Separators and Line Endings in `print()`**

You can modify how `print()` behaves by using the `sep` and `end` parameters to control the formatting of the output.

### **1. Changing the Separator with `sep`**

By default, when you print multiple arguments, Python separates them with a **space**. You can change this to any character, such as commas, dashes, or even custom strings.

#### **Example: Using a Custom Separator**

```python
# Print multiple values separated by a comma
print("Python", "Java", "C++", sep=", ")

# Print multiple values separated by dashes
print("2024", "10", "08", sep="-")
```

#### **Output**:
```
Python, Java, C++
2024-10-08
```

- **Explanation**: The `sep` parameter is used to define what should appear **between** the printed arguments. Here, we use `", "` and `"-"` as separators instead of the default space.

### **2. Changing the Line Ending with `end`**

By default, `print()` adds a **newline** (`'\n'`) at the end of the output. You can change this to any other character or string.

#### **Example: Using a Custom Line Ending**

```python
# Print multiple values with a custom line ending
print("Hello", end="... ")
print("World!", end="!\n")
```

#### **Output**:
```
Hello... World!!
```

- **Explanation**: The `end` parameter is used to define what will be printed **after** the print statement. In this case, `"... "` is added after the first print, and `"!\n"` (new line) after the second print.

### **3. Combining `sep` and `end` Parameters**

You can use both `sep` and `end` together to fully customize the output format.

#### **Example: Custom Separator and Line Ending**

```python
# Print multiple values with both a custom separator and custom line ending
print("apple", "banana", "cherry", sep=" | ", end=".\n")
print("Done with the list!")
```

#### **Output**:
```
apple | banana | cherry.
Done with the list!
```

- **Explanation**: In this example, we use `" | "` as the **separator** and `"."\n"` as the **line ending**, giving us a nicely formatted list with a period at the end.

### 📋 **Key Points**:

- **`sep`**: Controls the separator between printed arguments (e.g., `", "`, `"-"`, `" | "`).
- **`end`**: Specifies what to append after the printed output (e.g., `"..."`, `"!\n"`, `" "`).
- By default, `sep=" "` (a space) and `end="\n"` (a newline) are used.
- Customizing these can help format your output more flexibly for various purposes, such as creating lists, logs, or formatted text.

### 📝 **Complete Example**:

```python
# Changing both separator and line ending in the same example
print("Muhammad", "Hashim", "@", sep=", ", end="!\n")
print("Welcome to the team!")
```

#### **Output**:
```
Muhammad, Hashim, @!
Welcome to the team!
```

This complete example demonstrates how to use both `sep` and `end` to control the **separator** between values and the **line ending** after printing.

By adjusting `sep` and `end`, you can format your output exactly the way you need, making it more readable and customized for various purposes! 😊