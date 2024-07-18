# Anonymous Functions

## Introduction
Anonymous functions, also known as lambdas, are functions defined without a name. They are created using the `lambda` keyword within a Python expression. Due to Python's simple syntax, the body of a lambda function is limited to a single expression.

## Characteristics of Lambda Functions
- **Pure Expressions Only:** The body of a lambda function can only contain pure expressions. It cannot include statements such as `while`, `try`, etc.
- **No Assignment Statements:** Assignment using `=` is not allowed in a lambda function. Although the new assignment expression syntax (`:=`) can be used, it often makes the lambda complicated and hard to read. In such cases, it's better to refactor the lambda into a regular function using `def`.

## Best Use of Anonymous Functions
The best use of lambda functions is as arguments to higher-order functions. They are particularly useful when a small, throwaway function is needed.

### Example 7-7: Sorting a List of Words by Their Reversed Spelling Using Lambda
Here’s the rhyme index example from Example 7-4, rewritten with a lambda function:

```python
>>> fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
>>> sorted(fruits, key=lambda word: word[::-1])
['banana', 'apple', 'fig', 'raspberry', 'strawberry', 'cherry']
```

#### Explanation: Sorting a List of Words by Their Reversed Spelling Using Lambda

1. **Original List:**
   - The original list of fruits is: `['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']`.

2. **Using the `sorted` Function with Lambda:**
   - The `sorted` function is called with the list of fruits and the `key` argument set to a lambda function.
   - `key=lambda word: word[::-1]` means that each word in the list will be reversed, and the reversed spelling will be used as the sorting criterion.

3. **Reversing Each Word:**
   - The lambda function reverses the spelling of each word:
     - `'strawberry'` becomes `'yrrebwarts'`
     - `'fig'` becomes `'gif'`
     - `'apple'` becomes `'elppa'`
     - `'cherry'` becomes `'yrrehc'`
     - `'raspberry'` becomes `'yrrebpsar'`
     - `'banana'` becomes `'ananab'`

4. **Sorting by Reversed Spelling:**
   - The `sorted` function sorts the words based on their reversed spellings in ascending order:
     - `'ananab'` (original word: `banana`)
     - `'elppa'` (original word: `apple`)
     - `'gif'` (original word: `fig`)
     - `'yrrebpsar'` (original word: `raspberry`)
     - `'yrrebwarts'` (original word: `strawberry`)
     - `'yrrehc'` (original word: `cherry`)

5. **Resulting Sorted List:**
   - The sorted list is: `['banana', 'apple', 'fig', 'raspberry', 'strawberry', 'cherry']`.

Thus, the list is sorted by the reversed spelling of each word in ascending order. The word `banana`, whose reversed spelling is `ananab`, appears first, and the word `cherry`, whose reversed spelling is `yrrehc`, appears last.

## When Not to Use Lambda Functions
Outside the context of arguments to higher-order functions, anonymous functions are rarely useful in Python. The syntactic restrictions can make nontrivial lambdas either unreadable or unworkable. If a lambda is hard to read, it is better to refactor it into a regular function using `def`.

### Fredrik Lundh’s Lambda Refactoring Recipe
If you find a piece of code hard to understand because of a lambda, Fredrik Lundh suggests this refactoring procedure:

1. **Write a Comment:** Explain what the lambda does.
2. **Think of a Name:** Consider a name that captures the essence of the comment.
3. **Convert to `def`:** Convert the lambda to a `def` statement using the chosen name.
4. **Remove the Comment:** Remove the original comment.

#### Example: Refactoring a Complex Lambda
Consider the following complex lambda function:

```python
# Original lambda function
>>> numbers = [1, 2, 3, 4, 5]
>>> list(map(lambda x: x**2 if x % 2 == 0 else x**3, numbers))
[1, 4, 27, 16, 125]
```

1. **Write a Comment:**
   ```python
   # This lambda function squares even numbers and cubes odd numbers
   ```

2. **Think of a Name:**
   - Let's name it `process_number`.

3. **Convert to `def`:**
   ```python
   def process_number(x):
       if x % 2 == 0:
           return x**2
       else:
           return x**3
   ```

4. **Remove the Comment:**
   ```python
   def process_number(x):
       if x % 2 == 0:
           return x**2
       else:
           return x**3

   # Refactored code
   >>> numbers = [1, 2, 3, 4, 5]
   >>> list(map(process_number, numbers))
   [1, 4, 27, 16, 125]
   ```

### Explanation: Refactoring a Complex Lambda

1. **Original Lambda:**
   - The original lambda function `lambda x: x**2 if x % 2 == 0 else x**3` processes each number in the list. If the number is even, it squares the number; if it is odd, it cubes the number.

2. **Comment:**
   - Adding a comment to explain what the lambda does: `# This lambda function squares even numbers and cubes odd numbers`.

3. **Naming:**
   - Choosing the name `process_number` to reflect the purpose of the function.

4. **Conversion to `def`:**
   - Converting the lambda into a regular function using `def`:
     ```python
     def process_number(x):
         if x % 2 == 0:
             return x**2
         else:
             return x**3
     ```

5. **Refactored Code:**
   - The refactored code is more readable and maintainable:
     ```python
     >>> numbers = [1, 2, 3, 4, 5]
     >>> list(map(process_number, numbers))
     [1, 4, 27, 16, 125]
     ```

## Conclusion
The lambda syntax is just syntactic sugar: a lambda expression creates a function object just like the `def` statement. It is one of several kinds of callable objects in Python. Using lambda functions effectively can enhance your code, but it's essential to know when to refactor them for better readability and maintainability.