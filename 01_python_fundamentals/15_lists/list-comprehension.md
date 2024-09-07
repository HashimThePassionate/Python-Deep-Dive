# 📚 What is List Comprehension?

List comprehension is a powerful and concise way to create lists in Python. It allows you to generate a new list by applying an expression to each item in an existing iterable (like a list, tuple, or string). List comprehensions make your code more readable and often reduce the need for traditional loops.

### 🔍 List Comprehension Syntax:
```python
[expression for item in iterable if condition]
```
- **`expression`**: The operation or value you want to include in the new list.
- **`item`**: Each item in the original iterable.
- **`iterable`**: The original iterable (like a list, tuple, etc.).
- **`condition`**: (Optional) A condition that filters items from the original iterable.

---

## 🔄 Examples with and without List Comprehensions

Let's look at 10 examples where we compare traditional loops with list comprehensions.

---

### 1. **Creating a List of Squares** 📐

- **Without List Comprehension:**
  ```python
  squares = []
  for i in range(10):
      squares.append(i**2)
  print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
  ```

  - **Explanation:** 📝 Here, we start with an empty list `squares` and use a `for` loop to iterate over the range from 0 to 9. For each number `i`, we calculate its square (`i**2`) and append it to the `squares` list.

- **With List Comprehension:**
  ```python
  squares = [i**2 for i in range(10)]
  print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
  ```

  - **Explanation:** 🚀 List comprehension simplifies the process. We achieve the same result in one line by directly including the square operation in the comprehension.

---

### 2. **Filtering Even Numbers** 🔢

- **Without List Comprehension:**
  ```python
  evens = []
  for i in range(10):
      if i % 2 == 0:
          evens.append(i)
  print(evens)  # Output: [0, 2, 4, 6, 8]
  ```

  - **Explanation:** 📝 Here, we loop through numbers 0 to 9, check if each number is even (`i % 2 == 0`), and append it to the `evens` list.

- **With List Comprehension:**
  ```python
  evens = [i for i in range(10) if i % 2 == 0]
  print(evens)  # Output: [0, 2, 4, 6, 8]
  ```

  - **Explanation:** 🚀 List comprehension allows us to filter the even numbers directly in the expression, making the code shorter and more readable.

---

### 3. **Converting Strings to Uppercase** 🔠

- **Without List Comprehension:**
  ```python
  fruits = ["apple", "banana", "cherry"]
  upper_fruits = []
  for fruit in fruits:
      upper_fruits.append(fruit.upper())
  print(upper_fruits)  # Output: ['APPLE', 'BANANA', 'CHERRY']
  ```

  - **Explanation:** 📝 We start with a list of fruits and use a loop to convert each fruit name to uppercase using the `upper()` method.

- **With List Comprehension:**
  ```python
  fruits = ["apple", "banana", "cherry"]
  upper_fruits = [fruit.upper() for fruit in fruits]
  print(upper_fruits)  # Output: ['APPLE', 'BANANA', 'CHERRY']
  ```

  - **Explanation:** 🚀 List comprehension directly applies the `upper()` method to each fruit, resulting in a more concise code.

---

### 4. **Flattening a List of Lists** 📚

- **Without List Comprehension:**
  ```python
  matrix = [[1, 2], [3, 4], [5, 6]]
  flat_list = []
  for sublist in matrix:
      for item in sublist:
          flat_list.append(item)
  print(flat_list)  # Output: [1, 2, 3, 4, 5, 6]
  ```

  - **Explanation:** 📝 We use nested loops to iterate through each sublist in `matrix` and append each item to `flat_list`, effectively flattening the list of lists.

- **With List Comprehension:**
  ```python
  matrix = [[1, 2], [3, 4], [5, 6]]
  flat_list = [item for sublist in matrix for item in sublist]
  print(flat_list)  # Output: [1, 2, 3, 4, 5, 6]
  ```

  - **Explanation:** 🚀 List comprehension simplifies the flattening process by combining both loops into a single line.

---

### 5. **Creating a List of Tuples** 🎲

- **Without List Comprehension:**
  ```python
  pairs = []
  for i in range(3):
      for j in range(3):
          pairs.append((i, j))
  print(pairs)  # Output: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
  ```

  - **Explanation:** 📝 We use nested loops to generate pairs of numbers (i, j) and append them as tuples to the `pairs` list.

- **With List Comprehension:**
  ```python
  pairs = [(i, j) for i in range(3) for j in range(3)]
  print(pairs)  # Output: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
  ```

  - **Explanation:** 🚀 List comprehension allows us to create the same list of tuples in a more compact form.

---

### 6. **Applying a Function to Elements** 🧠

- **Without List Comprehension:**
  ```python
  def square(x):
      return x * x

  numbers = [1, 2, 3, 4, 5]
  squared_numbers = []
  for number in numbers:
      squared_numbers.append(square(number))
  print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
  ```

  - **Explanation:** 📝 We define a function `square` and use a loop to apply it to each number in the list, appending the result to `squared_numbers`.

- **With List Comprehension:**
  ```python
  def square(x):
      return x * x

  numbers = [1, 2, 3, 4, 5]
  squared_numbers = [square(number) for number in numbers]
  print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
  ```

  - **Explanation:** 🚀 List comprehension applies the `square` function to each element directly, resulting in a clean and efficient solution.

---

### 7. **Creating a Dictionary from Two Lists** 📖

- **Without List Comprehension:**
  ```python
  keys = ['name', 'age', 'gender']
  values = ['John', 25, 'Male']
  my_dict = {}
  for i in range(len(keys)):
      my_dict[keys[i]] = values[i]
  print(my_dict)  # Output: {'name': 'John', 'age': 25, 'gender': 'Male'}
  ```

  - **Explanation:** 📝 We manually pair each key with its corresponding value using a loop, then store the pairs in a dictionary.

- **With List Comprehension (using `zip`):**
  ```python
  keys = ['name', 'age', 'gender']
  values = ['John', 25, 'Male']
  my_dict = {keys[i]: values[i] for i in range(len(keys))}
  print(my_dict)  # Output: {'name': 'John', 'age': 25, 'gender': 'Male'}
  ```

  - **Explanation:** 🚀 List comprehension can be combined with `zip` to pair keys and values more efficiently, creating the dictionary in a single line.

---

### 8. **Filtering Words Longer Than 3 Characters** 🔤

- **Without List Comprehension:**
  ```python
  words = ["hello", "hi", "welcome", "bye"]
  long_words = []
  for word in words:
      if len(word) > 3:
          long_words.append(word)
  print(long_words)  # Output: ['hello', 'welcome']
  ```

  - **Explanation:** 📝 We use a loop to check the length of each word and append it to

 `long_words` if it has more than 3 characters.

- **With List Comprehension:**
  ```python
  words = ["hello", "hi", "welcome", "bye"]
  long_words = [word for word in words if len(word) > 3]
  print(long_words)  # Output: ['hello', 'welcome']
  ```

  - **Explanation:** 🚀 List comprehension allows us to filter the words directly within the expression, resulting in cleaner and more efficient code.

---

### 9. **Replacing Vowels in a String** 🅰️🅾️

- **Without List Comprehension:**
  ```python
  text = "hello"
  vowels = "aeiou"
  result = []
  for char in text:
      if char in vowels:
          result.append('*')
      else:
          result.append(char)
  print("".join(result))  # Output: h*ll*
  ```

  - **Explanation:** 📝 We use a loop to check if each character in `text` is a vowel. If it is, we replace it with `*`, otherwise, we keep the character as is.

- **With List Comprehension:**
  ```python
  text = "hello"
  vowels = "aeiou"
  result = ''.join(['*' if char in vowels else char for char in text])
  print(result)  # Output: h*ll*
  ```

  - **Explanation:** 🚀 List comprehension combines the character replacement and string creation into a single line, making the code more concise.

---

### 10. **Generating a List of Factorials** 🔢

- **Without List Comprehension:**
  ```python
  import math

  factorials = []
  for i in range(1, 6):
      factorials.append(math.factorial(i))
  print(factorials)  # Output: [1, 2, 6, 24, 120]
  ```

  - **Explanation:** 📝 We use a loop to calculate the factorial of each number from 1 to 5 using `math.factorial`, then append the result to `factorials`.

- **With List Comprehension:**
  ```python
  import math

  factorials = [math.factorial(i) for i in range(1, 6)]
  print(factorials)  # Output: [1, 2, 6, 24, 120]
  ```

  - **Explanation:** 🚀 List comprehension allows us to calculate and store the factorials in a single, elegant line.

---

