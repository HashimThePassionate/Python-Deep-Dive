# Higher-Order Functions

## Introduction
A higher-order function is a function that takes another function as an argument or returns a function as its result. Examples of higher-order functions in Python include `map`, `filter`, `reduce`, and `sorted`.

## Sorting with Higher-Order Functions

### Example 7-3: Sorting a List of Words by Length
To sort a list of words by their length, you can use the `sorted` function with the `len` function as the key.

```python
>>> fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
>>> sorted(fruits, key=len)
['fig', 'apple', 'cherry', 'banana', 'raspberry', 'strawberry']
```

#### Explanation: Sorting a List of Words by Length

1. **Original List:**
   - The original list of fruits is: `['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']`.

2. **Using the `sorted` Function:**
   - The `sorted` function is called with the list of fruits and the `key` argument set to `len`.
   - `key=len` means that each item in the list will be passed to the `len` function to determine its length.

3. **Calculating Lengths:**
   - The length of each word in the list is calculated:
     - `len('strawberry')` returns `10`
     - `len('fig')` returns `3`
     - `len('apple')` returns `5`
     - `len('cherry')` returns `6`
     - `len('raspberry')` returns `9`
     - `len('banana')` returns `6`

4. **Sorting by Length:**
   - The `sorted` function sorts the words based on their lengths in ascending order:
     - `fig` (length `3`)
     - `apple` (length `5`)
     - `cherry` (length `6`)
     - `banana` (length `6`)
     - `raspberry` (length `9`)
     - `strawberry` (length `10`)

5. **Resulting Sorted List:**
   - The sorted list is: `['fig', 'apple', 'cherry', 'banana', 'raspberry', 'strawberry']`.

Thus, the list is sorted by the length of each word in ascending order. The shortest word (`fig`) appears first, and the longest word (`strawberry`) appears last. If two words have the same length (`cherry` and `banana`), their original order is preserved in the sorted list.

### Example 7-4: Sorting a List of Words by Their Reversed Spelling
To sort words based on their reversed spelling, you can define a function that reverses a string and use it as the key in the `sorted` function.

```python
>>> def reverse(word):
...     return word[::-1]
>>> reverse('testing')
'gnitset'
>>> sorted(fruits, key=reverse)
['banana', 'apple', 'fig', 'raspberry', 'strawberry', 'cherry']
```

#### Explanation: Sorting a List of Words by Their Reversed Spelling

1. **Original List:**
   - The original list of fruits is: `['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']`.

2. **Defining the `reverse` Function:**
   - The `reverse` function takes a word and returns its reversed spelling.
   - For example, `reverse('testing')` returns `'gnitset'`.

3. **Using the `sorted` Function:**
   - The `sorted` function is called with the list of fruits and the `key` argument set to the `reverse` function.
   - `key=reverse` means that each item in the list will be passed to the `reverse` function to determine its reversed spelling, which will be used as the sorting criterion.

4. **Reversing Each Word:**
   - The reversed spelling of each word in the list is calculated:
     - `reverse('strawberry')` returns `'yrrebwarts'`
     - `reverse('fig')` returns `'gif'`
     - `reverse('apple')` returns `'elppa'`
     - `reverse('cherry')` returns `'yrrehc'`
     - `reverse('raspberry')` returns `'yrrebpsar'`
     - `reverse('banana')` returns `'ananab'`

5. **Sorting by Reversed Spelling:**
   - The `sorted` function sorts the words based on their reversed spellings in ascending order:
     - `'ananab'` (original word: `banana`)
     - `'elppa'` (original word: `apple`)
     - `'gif'` (original word: `fig`)
     - `'yrrebpsar'` (original word: `raspberry`)
     - `'yrrebwarts'` (original word: `strawberry`)
     - `'yrrehc'` (original word: `cherry`)

6. **Resulting Sorted List:**
   - The sorted list is: `['banana', 'apple', 'fig', 'raspberry', 'strawberry', 'cherry']`.

Thus, the list is sorted by the reversed spelling of each word in ascending order. The word `banana`, whose reversed spelling is `ananab`, appears first, and the word `cherry`, whose reversed spelling is `yrrehc`, appears last.

## Functional Programming Paradigm

In functional programming, common higher-order functions include `map`, `filter`, `reduce`, and `apply`. The `apply` function was deprecated in Python 2.3 and removed in Python 3. You can achieve the same functionality using `fn(*args, **kwargs)`.

### Modern Replacements for `map`, `filter`, and `reduce`
Although `map`, `filter`, and `reduce` are still available, Python offers better alternatives through list comprehensions and generator expressions.

### Example 7-5: Using `map` and `filter` with Alternatives
Compare the use of `map` and `filter` with list comprehensions.

```python
>>> def factorial(n):
... """returns n!"""
... return 1 if n < 2 else n * factorial(n - 1)

>>> list(map(factorial, range(6)))
[1, 1, 2, 6, 24, 120]

>>> [factorial(n) for n in range(6)]
[1, 1, 2, 6, 24, 120]

>>> list(map(factorial, filter(lambda n: n % 2, range(6))))
[1, 6, 120]

>>> [factorial(n) for n in range(6) if n % 2]
[1, 6, 120]
```

### Explanation of Example 7-5
1. Build a list of factorials from 0! to 5! using `map`.
2. Achieve the same with a list comprehension for readability.
3. Create a list of factorials for odd numbers up to 5! using `map` and `filter`.
4. Replace `map` and `filter` with a list comprehension, eliminating the need for `lambda`.

### Example 7-6: Sum of Integers with `reduce` and `sum`
Compare the use of `reduce` and `sum` to sum integers up to 99.

```python
>>> from functools import reduce
>>> from operator import add
>>> reduce(add, range(100))
4950

>>> sum(range(100))
4950
```

### Explanation of Example 7-6
1. Import `reduce` from `functools` and `add` from `operator`.
2. Use `reduce` to sum integers up to 99.
3. Achieve the same with the `sum` function, enhancing readability and performance.

### Reducing Functions
- `all(iterable)`: Returns `True` if all elements are truthy or if the iterable is empty.
- `any(iterable)`: Returns `True` if any element is truthy or if the iterable is non-empty.

### Usage of Anonymous Functions
To use higher-order functions conveniently, sometimes you need a small, one-off function, which is where anonymous functions (lambdas) come in handy.

## Conclusion
Higher-order functions like `map`, `filter`, and `reduce` provide powerful tools for functional programming in Python. Modern alternatives like list comprehensions and generator expressions offer more readable and often more efficient solutions. Understanding and utilizing these functions can greatly enhance your programming skills.