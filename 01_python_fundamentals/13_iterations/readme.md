# 📘 Control Flows - Loops

## 🌟 What are Iterations or Loops?

**Iterations** or **loops** are fundamental concepts in programming that allow you to execute a block of code multiple times. The use of loops makes it possible to perform repetitive tasks efficiently. Instead of writing the same code multiple times, loops allow you to write it once and execute it as many times as needed.

### 🔍 Why Do We Need Iterations with Loops?

- **Reduce Repetition**: Loops help avoid repetitive code, making programs shorter and easier to read.
- **Dynamic Behavior**: Allows programs to handle variable-sized data or input.
- **Automation**: Loops automate repetitive tasks, making code more efficient and reducing human error.
- **Efficiency**: Code with loops is easier to maintain and modify.

### 📝 Use Case and Benefits

Imagine you need to print the numbers from 1 to 100. Without loops, you would write 100 `print` statements. With a loop, you write the code once and let the loop handle the repetition. Loops are particularly useful for:

- Processing items in a list
- Automating repetitive tasks
- Reading lines from a file
- Iterating over a range of numbers

## 🔄 Types of Loops in Python

Python provides several types of loops to manage iteration:

| Sr.No. | Name of the Loop  | Loop Type & Description |
|--------|-------------------|-------------------------|
| 1      | **While Loop**    | Repeats a statement or group of statements while a given condition is `True`. It tests the condition before executing the loop body. |
| 2      | **For Loop**      | Executes a code block multiple times and manages the loop variable. It is often used to iterate over sequences like lists, strings, or ranges. |
| 3      | **Nested Loops**  | A loop inside another loop. Useful for working with multi-dimensional data or performing complex iterations. |

## 🔧 Loop Control Statements

Loop control statements are used to change the course of iteration or exit a loop early. These are essential for managing loops effectively:

| Sr.No. | Name of the Control Statement | Description |
|--------|-------------------------------|-------------|
| 1      | **Break Statement**           | Terminates the loop's execution and transfers control to the statement following the loop. |
| 2      | **Continue Statement**        | Skips the current iteration of the loop. The remaining code in the loop body is not executed for that iteration. |
| 3      | **Pass Statement**            | Used when a statement is syntactically required but no code needs to be executed. Useful as a placeholder. |

## 🔢 The `range()` Function

The built-in `range()` function is commonly used with loops to generate a sequence of numbers:

- **Syntax**: `range(start, stop, step)`
  - **start**: The starting value (default is `0`).
  - **stop**: The stopping value (not included in the sequence).
  - **step**: The difference between each number in the sequence (default is `1`).

### Example:

```python
print(list(range(10)))        # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(4, 9)))      # Output: [4, 5, 6, 7, 8]
print(list(range(5, 25, 4)))  # Output: [5, 9, 13, 17, 21]
```

## 🌀 For Loops

The `for` loop in Python is used to iterate over a sequence (like a list, tuple, dictionary, set, or string). It is the most commonly used loop and is especially useful when the number of iterations is known beforehand.

### Example: Printing a Multiplication Table

You can use a `for` loop with the `range()` function to print a multiplication table:

```python
# Multiplication table for 5
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")
```

### Example: Iterating Over a List

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}!")
```

### Example: Using `range()` to Loop Over Indices

```python
# Print even numbers from 2 to 20
for number in range(2, 21, 2):
    print(number)
```

## 🔁 Introducing While Loops

While loops run as long as a certain condition is `True`. They are useful for continuously asking for user input or running until a specific condition is met.

### Example: Printing a Multiplication Table Using `while` Loop

```python
number = 1
while number <= 10:
    print(f"5 x {number} = {5 * number}")
    number += 1
```

### Example: User Input with While Loop

You can use a `while` loop to keep a program running until the user decides to quit:

```python
prompt = "\nEnter a number to get its square (or 'quit' to stop): "

while True:
    user_input = input(prompt)
    if user_input.lower() == 'quit':
        break
    else:
        number = int(user_input)
        print(f"The square of {number} is {number ** 2}")
```

### Example: Using `continue` in a `while` Loop

```python
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue  # Skip the rest of the code inside the loop for even numbers
    print(current_number)
```

### ⚠️ Avoiding Infinite Loops

Every `while` loop needs a condition that becomes `False` to prevent infinite loops:

```python
x = 1
while x <= 5:
    print(x)
    x += 1  # This line ensures the loop will eventually stop
```

If you forget to increment `x`, the loop will run forever:

```python
# Infinite loop example (Do NOT run this)
x = 1
while x <= 5:
    print(x)  # No increment, so this loop runs forever
```

## 📊 Conclusion

Both `for` and `while` loops are essential tools in a Python programmer's toolkit. They help automate repetitive tasks, make the code cleaner, and handle dynamic data more efficiently. Understanding these concepts will enhance your ability to write more effective and efficient Python programs!
