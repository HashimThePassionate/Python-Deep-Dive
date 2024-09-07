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

## 🧑‍💻 User Input and While Loops

Most programs need to interact with users to gather input and provide output. The `input()` function allows for user input, while loops can help keep the program running until the user decides to exit.

### 🛠 Example: `input()` Function

The `input()` function pauses your program and waits for the user to enter some text. Once Python receives the input, it assigns that input to a variable.

```python
message = input("Tell me something, and I will repeat it back to you: ")
print(message)
```

### 🌟 Writing Clear Prompts

Provide clear instructions to users on what to enter:

```python
name = input("Please enter your name: ")
print(f"\nHello, {name}!")
```

### 🧮 Using `int()` to Accept Numerical Input

When using `input()`, Python interprets everything as a string. To work with numbers, use the `int()` function to convert the input:

```python
age = input("How old are you? ")
age = int(age)  # Convert input to an integer

if age >= 18:
    print("You are eligible to vote!")
else:
    print("You are not eligible to vote.")
```

## 🔁 Introducing While Loops

While loops run as long as a certain condition is `True`. They are useful for continuously asking for user input or running until a specific condition is met.

### Example: Basic While Loop

```python
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
```

### 💡 Letting the User Choose When to Quit

You can use a `while` loop to keep a program running until the user decides to quit:

```python
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
```

### 🚩 Using a Flag

Flags are variables used to control the flow of a loop. They allow more complex logic for exiting loops:

```python
active = True

while active:
    message = input("Enter 'quit' to end the program: ")
    if message == 'quit':
        active = False
    else:
        print(message)
```

### 🔚 Using `break` to Exit a Loop

The `break` statement can be used to exit a loop immediately:

```python
while True:
    city = input("Enter the name of a city you have visited (or 'quit' to stop): ")
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")
```

### 🔄 Using `continue` in a Loop

The `continue` statement skips the rest of the loop and returns to the beginning:

```python
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
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
