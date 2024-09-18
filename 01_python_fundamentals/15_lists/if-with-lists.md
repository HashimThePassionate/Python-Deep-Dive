# 📘 Python: If Statements with Lists - Exercises and Solutions
In Python, combining lists and `if` statements allows for more sophisticated decision-making processes. This section explores various scenarios where lists are used with conditional statements, demonstrating how to handle special cases, check for empty lists, and manage multiple lists.
Here is the Table of Contents (TOC) for the "Python: If Statements with Lists - Exercises and Solutions" section. The TOC is formatted correctly to work in most Markdown environments, including GitHub.

## 📜 Table of Contents
### 📝 Exercises

1. [**Checking for Special Items**](#checking-for-special-items)
2. [**Checking That a List Is Not Empty**](#checking-that-a-list-is-not-empty)
3. [**Using Multiple Lists**](#using-multiple-lists)
4. [**Hello Admin**](#hello-admin)
5. [**No Users**](#no-users)
6. [**Checking Usernames**](#checking-usernames)
7. [**Ordinal Numbers**](#ordinal-numbers)
8. [**Styling Your If Statements**](#styling-your-if-statements)

### 📝 More Exercises

9. [**Styling If Statements**](#styling-if-statements)
10. [**Your Ideas**](#your-ideas)
---

## 📝 Exercises

### 1. **Checking for Special Items**

The following example demonstrates how to handle a specific item in a list that needs special attention:

#### Example Code:

```python
# List of requested toppings
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")
```

#### Output:
```
Adding mushrooms.
Sorry, we are out of green peppers right now.
Adding extra cheese.
Finished making your pizza!
```

### 2. **Checking That a List Is Not Empty**

It is essential to check if a list is empty before processing it. The following example shows how to handle an empty list:

#### Example Code:

```python
# Empty list of requested toppings
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
```

#### Output:
```
Are you sure you want a plain pizza?
```

### 3. **Using Multiple Lists**

You can use multiple lists to ensure that inputs are valid before performing operations on them. The following example checks each requested topping against a list of available toppings:

#### Example Code:

```python
# Available toppings at the pizzeria
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

# Toppings requested by the customer
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")
```

#### Output:
```
Adding mushrooms.
Sorry, we don't have french fries.
Adding extra cheese.
Finished making your pizza!
```

### 4. **Hello Admin**

Make a list of five or more usernames, including the name 'admin'. Write code that prints a greeting to each user after they log in to a website.

#### Requirements:
- If the username is 'admin', print a special greeting.
- Otherwise, print a generic greeting.

#### Example Code:

```python
# List of usernames
usernames = ['admin', 'john', 'jaden', 'lisa', 'mike']

for username in usernames:
    if username == 'admin':
        print(f"Hello {username}, would you like to see a status report?")
    else:
        print(f"Hello {username.title()}, thank you for logging in again.")
```

#### Output:
```
Hello admin, would you like to see a status report?
Hello John, thank you for logging in again.
Hello Jaden, thank you for logging in again.
Hello Lisa, thank you for logging in again.
Hello Mike, thank you for logging in again.
```

### 5. **No Users**

Add an `if` test to check if the list of users is not empty. If it is empty, print a message saying "We need to find some users!"

#### Example Code:

```python
# List of usernames
usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print(f"Hello {username}, would you like to see a status report?")
        else:
            print(f"Hello {username.title()}, thank you for logging in again.")
else:
    print("We need to find some users!")
```

#### Output:
```
We need to find some users!
```

### 6. **Checking Usernames**

Simulate how websites ensure that everyone has a unique username. Compare a list of new usernames against a list of existing usernames and print messages to indicate whether each new username is available or not.

#### Example Code:

```python
# Current usernames in use
current_users = ['john', 'jaden', 'mike', 'lisa', 'admin']

# New usernames to be checked
new_users = ['john', 'mike', 'chris', 'jane', 'ADMIN']

# Convert current_users to lowercase for case insensitive comparison
current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Username '{new_user}' is already taken, please choose a different username.")
    else:
        print(f"Username '{new_user}' is available.")
```

#### Output:
```
Username 'john' is already taken, please choose a different username.
Username 'mike' is already taken, please choose a different username.
Username 'chris' is available.
Username 'jane' is available.
Username 'ADMIN' is already taken, please choose a different username.
```

### 7. **Ordinal Numbers**

Ordinal numbers indicate their position in a list, such as 1st or 2nd. Most ordinal numbers end in "th," except for 1, 2, and 3.

#### Example Code:

```python
# List of numbers 1 through 9
numbers = list(range(1, 10))

# Loop through the list and print ordinal numbers
for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")
```

#### Output:
```
1st
2nd
3rd
4th
5th
6th
7th
8th
9th
```

### 8. **Styling Your If Statements**

PEP 8 recommends using a single space around comparison operators, such as `==`, `>=`, and `<=`, to improve readability. For example:

```python
# Good styling
if age < 4:

# Bad styling
if age<4:
```

## 📝 More Exercises

### 9. **Styling If Statements**

Review the programs you wrote and make sure you styled your conditional tests appropriately according to PEP 8 guidelines.

### 10. **Your Ideas**

Now that you have a better sense of how real-world situations are modeled in programs, consider the problems you could solve with your own programs. Think about games you might want to write, datasets you might want to explore, and web applications you’d like to create.
