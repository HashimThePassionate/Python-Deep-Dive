# 🔧 Solutions

## 1. **Login System Verification**

```python
# Predefined username and password
correct_username = "admin"
correct_password = "password123"

# User input
username = input("Enter your username: ")
password = input("Enter your password: ")

# Check if the input matches the predefined values
if username == correct_username and password == correct_password:
    print("✨ Login successful! Welcome back! ✨")
    print("You have access to all the features.")
    print(f'Welcome, {username}!')
else:
    print("❌ Invalid credentials. Please try again.")
```

## 2. **Temperature Advisor**

```python
# User input for temperature
temperature = int(input("Enter the current temperature in °C: "))

# Temperature check and suggestions
if temperature > 30:
    print("It's quite hot! Make sure to stay hydrated. 💧")
elif 20 <= temperature <= 30:
    print("It's a pleasant day! How about a walk in the park? 🚶‍♂️")
else:
    print("It's a bit chilly. Don't forget your jacket! 🧥")
```

## 3. **Simple Tax Calculator**

```python
# User input for income
income = float(input("Enter your annual income: "))

# Tax calculation based on income
if income < 50000:
    tax = income * 0.10
    print(f"Your tax is 10%, which amounts to ${tax:.2f}.")
elif 50000 <= income <= 100000:
    tax = income * 0.20
    print(f"Your tax is 20%, which amounts to ${tax:.2f}.")
else:
    tax = income * 0.30
    print(f"Your tax is 30%, which amounts to ${tax:.2f}.")
```

## 4. **Day of the Week Checker**

```python
# User input for the day of the week
day = input("Enter a day of the week: ").capitalize()

# Check if the day is a weekday or weekend
if day == "Saturday" or day == "Sunday":
    print("It's a weekend! Enjoy your time off! 🎉")
elif day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    print("It's a weekday. Back to work! 💼")
else:
    print("Invalid input. Please enter a valid day of the week.")
```

## 5. **Driving Eligibility Checker**

```python
# User input for age
age = int(input("Enter your age: "))

# Eligibility check based on age
if age < 16:
    print("You are too young to get a driving license. 🚫")
elif 16 <= age < 18:
    print("You need parental consent to get a driving license. 📝")
else:
    print("You are eligible to get a driving license. 🚗")
```

These exercises cover various real-world scenarios where `if`, `if-else`, and `if-elif` statements can be effectively used. Let me know if you'd like more exercises or any additional details! 😊