# Solutions: Python Operators Practice Tasks 🎯✨

## Task 1: Simple Calculator 🧮🔢

**Solution:**
```python
# Simple Calculator

# Prompt the user to enter two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Perform arithmetic operations
addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
modulus = a % b

# Print the results using f-strings
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")
print(f"Modulus: {modulus}")
```

---

## Task 2: Compare Ages 🎂👶👵

**Solution:**
```python
# Compare Ages

# Prompt the user to enter the ages of two people
age1 = int(input("Enter age of person 1: "))
age2 = int(input("Enter age of person 2: "))

# Perform age comparisons
result_greater = age1 > age2
result_lesser = age1 < age2
result_equal = age1 == age2

# Print the comparison results using f-strings
print(f"Is person 1 older than person 2? {result_greater}")
print(f"Is person 1 younger than person 2? {result_lesser}")
print(f"Are both persons the same age? {result_equal}")
```

---

## Task 3: Even or Odd Checker 🔢🤔

**Solution:**
```python
# Even or Odd Checker

# Prompt the user to enter a number
number = int(input("Enter a number: "))

# Calculate modulus to check even or odd
remainder = number % 2

# Print the remainder using f-strings (0 indicates even, 1 indicates odd)
print(f"Remainder when divided by 2: {remainder}")
```

---

## Task 4: Power Calculation 💪⚡

**Solution:**
```python
# Power Calculation

# Prompt the user to enter a base number and an exponent
base = int(input("Enter base number: "))
exponent = int(input("Enter exponent: "))

# Calculate the power
result = base ** exponent

# Print the result using f-strings
print(f"{base} raised to the power of {exponent} is {result}")
```

---

## Task 5: Temperature Converter 🌡️🔥❄️

**Solution:**
```python
# Temperature Converter

# Prompt the user to enter a temperature in Celsius
celsius = float(input("Enter temperature in Celsius: "))

# Convert Celsius to Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Print the result using f-strings
print(f"{celsius}°C is {fahrenheit}°F")
```