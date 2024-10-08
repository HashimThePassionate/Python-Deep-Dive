# 📝 Solutions

### 1. **Buffet: Menu Management**

A buffet-style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.

- Use a `for` loop to print each food the restaurant offers.
- Try to modify one of the items, and make sure that Python rejects the change.
- The restaurant changes its menu, replacing two of the items with different foods. Add a line that rewrites the tuple, and then use a `for` loop to print each of the items on the revised menu.

### Solution

```python
# Original menu
foods = ("Pizza", "Pasta", "Salad", "Soup", "Bread")
print("Original menu:")
for food in foods:
    print(food)

# Attempt to modify the tuple (will raise an error)
# foods[0] = "Burger"  # Uncommenting this line will raise a TypeError

# Revised menu
foods = ("Burger", "Pasta", "Salad", "Sandwich", "Bread")
print("\nRevised menu:")
for food in foods:
    print(food)
```

### 2. **Geographic Coordinates**

Create a program that stores the coordinates (latitude and longitude) of three different cities in a tuple. Then:

- Print each city's coordinates in a formatted string.
- Attempt to change the coordinates of one city and observe the error.
- Simulate updating the coordinates by reassigning the entire tuple.

### Solution

```python
# City coordinates (latitude, longitude)
coordinates = (("New York", 40.7128, -74.0060), ("London", 51.5074, -0.1278), ("Tokyo", 35.6895, 139.6917))

# Print each city's coordinates
for city in coordinates:
    print(f"{city[0]}: Latitude {city[1]}, Longitude {city[2]}")

# Attempt to modify the tuple (will raise an error)
# coordinates[0] = ("New York", 40.7306, -73.9352)  # Uncommenting this line will raise a TypeError

# Simulate updating the coordinates
coordinates = (("New York", 40.7306, -73.9352), ("London", 51.5074, -0.1278), ("Tokyo", 35.6895, 139.6917))
print("\nUpdated Coordinates:")
for city in coordinates:
    print(f"{city[0]}: Latitude {city[1]}, Longitude {city[2]}")
```

### 3. **Immutable Game Settings**

Create a program that stores game settings like resolution, audio level, and difficulty level in a tuple. Then:

- Print the current settings.
- Try to change one of the settings and handle the error appropriately.
- Provide an option to "reset" all settings by reassigning the tuple.

### Solution

```python
# Game settings
settings = ("1920x1080", 70, "Hard")

# Print current settings
print(f"Current settings: Resolution = {settings[0]}, Audio = {settings[1]}%, Difficulty = {settings[2]}")

# Attempt to change the settings (will raise an error)
# settings[1] = 50  # Uncommenting this line will raise a TypeError

# Resetting settings
settings = ("1280x720", 50, "Normal")
print("\nSettings have been reset.")
print(f"New settings: Resolution = {settings[0]}, Audio = {settings[1]}%, Difficulty = {settings[2]}")
```

### 4. **Student Grades Tracker**

Write a program that stores a tuple of five students' names and another tuple of their corresponding grades. Then:

- Print each student's name with their grade.
- Attempt to modify a grade and show that it's not possible.
- Simulate correcting a mistake by creating a new tuple of grades.

### Solution

```python
# Student names and grades
students = ("Alice", "Bob", "Charlie", "Diana", "Eve")
grades = (85, 90, 78, 88, 92)

# Print each student's name with their grade
for i in range(len(students)):
    print(f"{students[i]}: {grades[i]}")

# Attempt to modify a grade (will raise an error)
# grades[0] = 95  # Uncommenting this line will raise a TypeError

# Simulate correcting a mistake
grades = (95, 90, 78, 88, 92)
print("\nCorrected Grades:")
for i in range(len(students)):
    print(f"{students[i]}: {grades[i]}")
```

### 5. **Sorting and Tuple Packing**

Create a program that accepts a list of numbers from the user and converts it to a tuple. Then:

- Print the sorted tuple without modifying the original tuple.
- Pack and unpack the sorted tuple into separate variables and print them.

### Solution

```python
# User input for list of numbers
numbers = tuple(map(int, input("Enter numbers separated by spaces: ").split()))

# Print sorted tuple
sorted_numbers = tuple(sorted(numbers))
print(f"Sorted tuple: {sorted_numbers}")

# Packing and unpacking the sorted tuple
first, second, third, *rest = sorted_numbers
print(f"First: {first}, Second: {second}, Third: {third}, Rest: {rest}")
```

### 6. **Top 3 Favorite Movies**

Create a program that stores your top 3 favorite movies in a tuple. Then:

- Print them in order.
- Swap the first and last movie using tuple packing/unpacking.
- Show the tuple before and after the swap.

### Solution

```python
# Top 3 favorite movies
movies = ("Inception", "The Matrix", "Interstellar")

print("Original order of favorite movies:")
print(movies)

# Swapping the first and last movie
movies = (movies[2], movies[1], movies[0])

print("\nMovies after swapping first and last:")
print(movies)
```

### 7. **Tuple Calculator**

Write a program that asks the user for two numbers and then stores them in a tuple. Provide options for the user to perform different mathematical operations (addition, subtraction, multiplication, division) using these numbers.

### Solution

```python
# Asking user for two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
numbers = (num1, num2)

# Operations
print(f"Addition: {numbers[0]} + {numbers[1]} = {numbers[0] + numbers[1]}")
print(f"Subtraction: {numbers[0]} - {numbers[1]} = {numbers[0] - numbers[1]}")
print(f"Multiplication: {numbers[0]} * {numbers[1]} = {numbers[0] * numbers[1]}")
if numbers[1] != 0:
    print(f"Division: {numbers[0]} / {numbers[1]} = {numbers[0] / numbers[1]}")
else:
    print("Cannot divide by zero.")
```

### 8. **Quiz Game with Tuples**

Create a quiz game using tuples to store questions and their corresponding answers. Then:

- Ask the user each question.
- Check their answers against the tuple of correct answers.
- Keep track of the score and display it at the end.

### Solution

```python
# Quiz questions and answers
questions = ("What is the capital of France?", "What is 2 + 2?", "What is the capital of Japan?")
answers = ("Paris", "4", "Tokyo")

score = 0

# Asking questions
for i in range(len(questions)):
    user_answer = input(f"{questions[i]}: ")
    if user_answer.lower() == answers[i].lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

print(f"\nYour final score is: {score}/{len(questions)}")
```

### 9. **Month Temperature Tracker**

Store the average monthly temperatures (in Celsius) for a year in a tuple. Then:

- Calculate and print the average temperature of the year.
- Find the hottest and coldest month without modifying the tuple.
- Simulate updating the temperatures by creating a new tuple.

### Solution

```python
# Monthly average temperatures (in Celsius)
temperatures = (4.5, 5.3, 9.1, 12.8, 18.3, 22.4, 25.6, 25.0, 21.4, 15.2, 9.7, 5.8)

# Average temperature of the year
average_temp = sum(temperatures) / len(temperatures)
print(f"Average temperature of the year: {average_temp:.2f}°C")

# Hottest and coldest month
hottest = max(temperatures)
coldest = min(temperatures)
print(f"Hottest month temperature: {hottest}°C")
print(f"Coldest month temperature: {coldest}°C")

# Simulate updating temperatures
updated_temperatures = temperatures[:11] + (6.0,)  # Example of modifying December
print(f"\nUpdated temperatures: {updated_temperatures}")
```



### 10. **3D Vector Operations**

Create a program that stores two 3D vectors in tuples. Then:

- Print their original values.
- Compute their dot product and cross product using functions without modifying the tuples.
- Display the results of these operations.

### Solution

```python
# 3D vectors
vector1 = (1, 2, 3)
vector2 = (4, 5, 6)

# Dot product function
def dot_product(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1] + v1[2] * v2[2]

# Cross product function
def cross_product(v1, v2):
    return (v1[1] * v2[2] - v1[2] * v2[1],
            v1[2] * v2[0] - v1[0] * v2[2],
            v1[0] * v2[1] - v1[1] * v2[0])

# Printing original vectors
print(f"Vector 1: {vector1}")
print(f"Vector 2: {vector2}")

# Calculating dot product and cross product
print(f"Dot product: {dot_product(vector1, vector2)}")
print(f"Cross product: {cross_product(vector1, vector2)}")
```

### 11. **Filter Cities Based on Longitude**

Create a program that displays the name, latitude, and longitude of metro areas where the longitude is less than or equal to 0. Use a tuple to represent each city's information.

### Solution

```python
# List of metro areas with city name, country code, population (in millions), and (latitude, longitude)
metro_areas = [
    ('Karachi', 'PK', 14.91, (24.8607, 67.0011)),
    ('Lahore', 'PK', 11.13, (31.5497, 74.3436)),
    ('Islamabad', 'PK', 1.15, (33.6844, 73.0479)),
    ('Quetta', 'PK', 1.00, (30.1798, 66.9750)),
    ('Multan', 'PK', 1.87, (30.1575, 71.5249)),
]

def main():
    # Print header
    print(f'{"City":15} | {"Latitude":>9} | {"Longitude":>9}')
    
    # Loop through each city in the list and unpack its values
    for name, _, _, (lat, lon) in metro_areas:
        # Check if the longitude is less than or equal to 0
        if lon <= 0:
            # Print the formatted output for cities with longitude <= 0
            print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')

if __name__ == '__main__':
    main()
```
