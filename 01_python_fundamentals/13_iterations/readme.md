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

### 🌟 Example: Nested Loop with User Input Control

This program allows the user to print a series of multiplication tables. After each table, the user is asked if they want to continue. If they choose "yes," they can print another table; otherwise, the program will exit. Let's make it interactive and fun! 🎉

```python
print("🔢 Welcome to the Multiplication Table Generator! 🔢")

while True:
    # 🎯 Ask the user for which multiplication table they want
    try:
        number = int(input("\nEnter a number to print its multiplication table (e.g., 5): "))
    except ValueError:
        print("❌ Please enter a valid number!")
        continue

    print(f"\n📊 Multiplication Table for {number} 📊")
    
    # 🚀 Print the multiplication table for the given number
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")
    
    # 🌟 Ask if the user wants to print another table
    continue_choice = input("\n✨ Do you want to print another multiplication table? (yes/no): ").strip().lower()
    
    # 🚪 If the user types 'no', break the loop
    if continue_choice != 'yes':
        print("👋 Exiting the program. Thank you for using the Multiplication Table Generator! Goodbye! 😊")
        break
    else:
        print("👍 Let's print another table! 🎉")
```

### 💡 Explanation:

1. **Introduction Message**: A welcoming message with emojis sets a friendly tone for the user.
2. **Input Validation**: The `try-except` block ensures that the user enters a valid number. If not, it shows an error message and prompts again without crashing the program.
3. **Table Display with Emojis**: The multiplication table is presented with a heading and separators to make it more visually appealing.
4. **User Interaction**: Clear and interactive prompts (`yes/no`) allow the user to control the flow. Additional messages guide the user and provide feedback, making the program feel more conversational.
5. **Conclusion Message**: A friendly goodbye message wraps up the experience when the user chooses to exit.

### 📝 Output Example:

```plaintext
🔢 Welcome to the Multiplication Table Generator! 🔢

Enter a number to print its multiplication table (e.g., 5): 5

📊 Multiplication Table for 5 📊
5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50

✨ Do you want to print another multiplication table? (yes/no): yes
👍 Let's print another table! 🎉
```

### 🌟 Example: Pyramid Pattern with User Input Control

This program allows the user to print a pyramid pattern of a specified height. After printing, the user can choose to create another pyramid with a different height. Let's build some pyramids! 🏔️

```python
print("🏔️ Welcome to the Pyramid Pattern Generator! 🏔️")
while True:
    # \ud83c\udf1f Ask the user for the height of the pyramid
    try:
        height = int(input("\nEnter the height of the pyramid (e.g., 5): "))
    except ValueError:
        print("❌ Please enter a valid number!")
        continue

    print(f"\n🎨 Here is your pyramid of height {height} 🎨\n")

    # \ud83c\udfca Print the pyramid pattern using three loops
    for i in range(1, height + 1):
        # Loop 1: Print spaces for alignment
        for space in range(height - i):
            print(" ", end='')

        # Loop 2: Print stars to form the left half of the pyramid
        for star in range(i):
            print("⭐", end='')
        print()  # Move to the next line

    # \ud83c\udf1f Ask if the user wants to print another pyramid
    continue_choice = input(
        "\nDo you want to create another pyramid? (yes/no): ").strip().lower()

    # \ud83c\udfe2 If the user types 'no', break the loop
    if continue_choice != 'yes':
        print("👋 Exiting the program. Thank you for using the Pyramid Pattern Generator! Goodbye")
        break
    else:
        print("👍 Let's build another pyramid!")
```

### 💡 Explanation:

1. **Introduction Message**: A welcoming message with emojis introduces the Pyramid Pattern Generator.
2. **Input Validation**: The `try-except` block ensures that the user enters a valid integer for the pyramid height. If not, it shows an error message and prompts the user again.
3. **Pyramid Pattern Printing**:
   - The outer `for` loop iterates from `1` to the specified height.
   - Spaces (`' ' * (height - i)`) are printed to center-align the stars, creating a pyramid shape.
   - Stars (`'⭐' * (2 * i - 1)`) are printed to form each row of the pyramid, with the number of stars increasing in each iteration.
4. **User Interaction**: After printing the pyramid, the user is asked if they want to create another one. Depending on the user's choice, the loop continues or exits.
5. **Conclusion Message**: A friendly goodbye message wraps up the program when the user decides to exit.

### 📝 Output Example:

```plaintext
🏔️ Welcome to the Pyramid Pattern Generator! 🏔️

Enter the height of the pyramid (e.g., 5): 5

🎨 Here is your pyramid of height 5 🎨

    ⭐
   ⭐⭐
  ⭐⭐⭐
 ⭐⭐⭐⭐
⭐⭐⭐⭐⭐

Do you want to create another pyramid? (yes/no): no
👋 Exiting the program. Thank you for using the Pyramid Pattern Generator! Goodbye
```

## 📊 Conclusion

Both `for` and `while` loops are essential tools in a Python programmer's toolkit. They help automate repetitive tasks, make the code cleaner, and handle dynamic data more efficiently. Understanding these concepts will enhance your ability to write more effective and efficient Python programs!
