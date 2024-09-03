# 📝 Solutions

## 1. **Rental Car Availability**

**Objective**: Write a program that repeatedly asks the user what kind of rental car they would like. If the user types "exit," the program should end. Otherwise, it should print a message such as "Let me see if I can find you a [car]." The program should keep running until the user decides to exit.

```python
while True:
    car = input("What kind of rental car would you like? (Type 'exit' to quit): ")
    
    if car.lower() == "exit":
        print("Exiting the program. Goodbye! 👋")
        break
    else:
        print(f"Let me see if I can find you a {car}. 🚗")
```

## 2. **Restaurant Seating Check**

**Objective**: Write a program that repeatedly asks the user how many people are in their dinner group. If the answer is more than eight, print a message saying they’ll have to wait for a table. Otherwise, report that their table is ready. The program should continue asking until the user types "done."

```python
while True:
    group_size = input("How many people are in your dinner group? (Type 'done' to finish): ")
    
    if group_size.lower() == "done":
        print("Thank you for using our restaurant service. Goodbye! 👋")
        break
    else:
        group_size = int(group_size)
        if group_size > 8:
            print("Sorry, you'll have to wait for a table. 🍽️")
        else:
            print("Your table is ready! 🍽️")
```

## 3. **Check Multiples of Ten Continuously**

**Objective**: Write a program that continuously asks the user for a number and then reports whether the number is a multiple of 10 or not. The program should stop if the user types "stop."

```python
while True:
    number = input("Enter a number (Type 'stop' to end): ")
    
    if number.lower() == "stop":
        print("Program stopped. Goodbye! 👋")
        break
    else:
        number = int(number)
        if number % 10 == 0:
            print(f"The number {number} is a multiple of 10. ✅")
        else:
            print(f"The number {number} is not a multiple of 10. ❌")
```

## 4. **Password Validation Loop**

**Objective**: Write a program that prompts the user to enter a password and checks if it meets a specific condition (e.g., length of at least 8 characters). If it doesn’t, the program should ask the user to input the password again. This should continue until the user enters a valid password.

```python
while True:
    password = input("Enter a password (at least 8 characters): ")
    
    if len(password) >= 8:
        print("Password is valid. 👍")
        break
    else:
        print("Password is too short! Please try again. 🔁")
```

## 5. **Number Pyramid Pattern**

**Objective**: Write a program that generates a number pyramid pattern based on the number of levels specified by the user. The program should use nested loops to generate the pattern.

```python
levels = int(input("Enter the number of levels for the pyramid: "))

for i in range(1, levels + 1):
    # Print leading spaces
    print(' ' * (levels - i), end='')
    # Print numbers
    for j in range(1, i + 1):
        print(j, end=' ')
    print()  # Move to the next line
```

## 6. **Guess the Number Game**

**Objective**: Write a loop-based program that generates a random number between 1 and 10. The user has to guess the number, and the program should provide feedback ("too high" or "too low") until the user guesses the correct number. The game should continue asking until the correct number is guessed.

```python
import random

correct_number = random.randint(1, 10)

while True:
    guess = int(input("Guess a number between 1 and 10: "))
    
    if guess == correct_number:
        print("Correct! You guessed it! 🎉")
        break
    elif guess < correct_number:
        print("Too low! Try again. 🔽")
    else:
        print("Too high! Try again. 🔼")
```

## 7. **Factorial Calculator Using a Loop**

**Objective**: Write a program that repeatedly asks the user to input a number and then calculates the factorial of that number using a loop. The program should continue asking until the user types "exit."

```python
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

while True:
    number = input("Enter a number to calculate its factorial (Type 'exit' to quit): ")
    
    if number.lower() == "exit":
        print("Exiting the program. Goodbye! 👋")
        break
    else:
        number = int(number)
        print(f"The factorial of {number} is {factorial(number)}.")
```

## 8. **Fibonacci Sequence Generator**

**Objective**: Write a program that generates the Fibonacci sequence up to a certain number entered by the user. Use a loop to generate the sequence until the user decides to stop.

```python
while True:
    n = input("Enter the number of terms for the Fibonacci sequence (Type 'stop' to end): ")
    
    if n.lower() == "stop":
        print("Program stopped. Goodbye! 👋")
        break
    else:
        n = int(n)
        a, b = 0, 1
        print("Fibonacci sequence:")
        for _ in range(n):
            print(a, end=' ')
            a, b = b, a + b
        print()
```
