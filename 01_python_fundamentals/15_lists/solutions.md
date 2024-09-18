# 🌟 Python List Practice Solutions
## 📜 Table of Contents

### 📝 Basic List Operations
1. [🔢 Create a list of the first 10 natural numbers and print it.](#create-a-list-of-the-first-10-natural-numbers-and-print-it)
2. [📥 Access and print the first, last, and middle elements of the list.](#2-📥-access-and-print-the-first-last-and-middle-elements-of-the-list-1020304050)
3. [➕ Append the number `60` to the list and print the updated list.](#3-➕-append-the-number-60-to-the-list-1020304050-and-print-the-updated-list)
4. [📌 Insert the number `25` at the 3rd position in the list and print the updated list.](#4-📌-insert-the-number-25-at-the-3rd-position-in-the-list-1020304050-and-print-the-updated-list)
5. [🗑️ Remove the number `30` from the list and print the updated list.](#5-🗑️-remove-the-number-30-from-the-list-1020304050-and-print-the-updated-list)
6. [🚮 Pop the last element from the list and print the updated list.](#6-🚮-pop-the-last-element-from-the-list-1020304050-and-print-the-updated-list)
7. [🔍 Count the occurrences of the number `2` in the list.](#7-🔍-count-the-occurrences-of-the-number-2-in-the-list-2352738)
8. [📍 Find the index of the number `40` in the list.](#8-📍-find-the-index-of-the-number-40-in-the-list-1020304050)
9. [🔄 Sort the list in ascending order and print the result.](#9-🔄-sort-the-list-538672-in-ascending-order-and-print-the-result)
10. [🔄 Reverse the list and print the result.](#10-🔄-reverse-the-list-1020304050-and-print-the-result)

### 📝 Intermediate List Operations
11. [🧮 Create a list comprehension that generates a list of the squares of numbers from 1 to 10.](#11-🧮-create-a-list-comprehension-that-generates-a-list-of-the-squares-of-numbers-from-1-to-10)
12. [🔢 Filter the even numbers from the list using list comprehension.](#12-🔢-filter-the-even-numbers-from-the-list-12345678910-using-list-comprehension)
13. [🔄 Create a list comprehension that generates a list of tuples where each tuple contains a number and its square.](#13-🔄-create-a-list-comprehension-that-generates-a-list-of-tuples-where-each-tuple-contains-a-number-and-its-square)
14. [📚 Flatten a list of lists using list comprehension.](#14-📚-flatten-a-list-of-lists-12-34-56-using-list-comprehension)
15. [🔠 Create a list comprehension that extracts the vowels from a string.](#15-🔠-create-a-list-comprehension-that-extracts-the-vowels-from-the-string-hello-world)
16. [🔗 Concatenate two lists and print the result.](#16-🔗-concatenate-two-lists-1-2-3-and-4-5-6-and-print-the-result)
17. [🔡 Create a list comprehension that converts all strings in a list to uppercase.](#17-🔡-create-a-list-comprehension-that-converts-all-strings-in-the-list-a-b-c-d-to-uppercase)
18. [🚫 Remove all occurrences of a value from a list.](#18-🚫-remove-all-occurrences-of-the-value-3-from-the-list-1-3-5-3-7-3-9)
19. [❓ Check if a list is empty and print a message accordingly.](#19-❓-check-if-a-list-is-empty-and-print-empty-if-it-is-otherwise-print-not-empty)
20. [🌟 Create a list comprehension that replaces each vowel in a string with an asterisk.](#20-🌟-create-a-list-comprehension-that-replaces-each-vowel-in-a-string-with-an-asterisk)

### 📝 Advanced List Operations
21. [🔢 Generate a list of the first 10 Fibonacci numbers.](#21-🔢-generate-a-list-of-the-first-10-fibonacci-numbers)
22. [📄 Split a list into two halves and print both halves.](#22-📄-split-a-list-1-2-3-4-5-6-7-8-into-two-halves-and-print-both-halves)
23. [🥈 Find the second largest number in a list.](#23-🥈-find-the-second-largest-number-in-the-list-10-20-4-45-99-4-28)
24. [🌟 Create a list comprehension that generates a list of numbers divisible by both 3 and 5.](#24-🌟-create-a-list-comprehension-that-generates-a-list-of-numbers-from-1-to-100-that-are-divisible-by-both-3-and-5)
25. [🔢 Create a list comprehension that generates a list of all prime numbers less than 50.](#25-🔢-create-a-list-comprehension-that-generates-a-list-of-all-the-prime-numbers-less-than-50)
26. [🔗 Zip two lists into a list of tuples and print the result.](#26-🔗-zip-two-lists-1-2-3-and-a-b-c-into-a-list-of-tuples-and-print-the-result)
27. [📤 Unzip a list of tuples into two separate lists.](#27-📤-unzip-a-list-of-tuples-1-a-2-b-3-c-into-two-separate-lists)
28. [🔄 Rotate a list to the right by 2 positions.](#28-🔄-rotate-a-list-1-2-3-4-5-to-the-right-by-2-positions)
29. [🔍 Find the common elements between two lists and print the result.](#29-🔍-find-the-common-elements-between-two-lists-1-2-3-4-and-3-4-5-6-and-print-the-result)
30. [🔄 Create a list comprehension that generates a list of reversed strings.](#30-🔄-create-a-list-comprehension-that-generates-a-list-of-strings-where-each-string-is-the-reverse-of-the-corresponding-string-in-the-list-abc-def-ghi)

---

## 📝 Basic List Operations

### 1. 🔢 Create a list of the first 10 natural numbers and print it.

```python
numbers = list(range(1, 11))
print(numbers)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

- **📝 Explanation:** The `range(1, 11)` function generates numbers from 1 to 10. The `list()` function then converts this range into a list. Finally, we print the list.

---

### 2. 📥 Access and print the first, last, and middle elements of the list `[10, 20, 30, 40, 50]`.

```python
my_list = [10, 20, 30, 40, 50]
first_element = my_list[0]
last_element = my_list[-1]
middle_element = my_list[len(my_list) // 2]

print(first_element)  # Output: 10
print(last_element)   # Output: 50
print(middle_element) # Output: 30
```

- **📝 Explanation:** 
  - **🟢 First Element:** Accessed using `my_list[0]`, which gives the element at index 0.
  - **🔴 Last Element:** Accessed using `my_list[-1]`, which gives the last element in the list.
  - **🔵 Middle Element:** Calculated using `len(my_list) // 2`, which gives the index of the middle element.

---

### 3. ➕ Append the number `60` to the list `[10, 20, 30, 40, 50]` and print the updated list.

```python
my_list = [10, 20, 30, 40, 50]
my_list.append(60)
print(my_list)  # Output: [10, 20, 30, 40, 50, 60]
```

- **📝 Explanation:** The `append()` method adds the element `60` to the end of the list.

---

### 4. 📌 Insert the number `25` at the 3rd position in the list `[10, 20, 30, 40, 50]` and print the updated list.

```python
my_list = [10, 20, 30, 40, 50]
my_list.insert(2, 25)
print(my_list)  # Output: [10, 20, 25, 30, 40, 50]
```

- **📝

 Explanation:** The `insert()` method adds an element at a specified index. Here, `insert(2, 25)` inserts `25` at index `2`.

---

### 5. 🗑️ Remove the number `30` from the list `[10, 20, 30, 40, 50]` and print the updated list.

```python
my_list = [10, 20, 30, 40, 50]
my_list.remove(30)
print(my_list)  # Output: [10, 20, 40, 50]
```

- **📝 Explanation:** The `remove()` method removes the first occurrence of the specified value (`30`) from the list.

---

### 6. 🚮 Pop the last element from the list `[10, 20, 30, 40, 50]` and print the updated list.

```python
my_list = [10, 20, 30, 40, 50]
my_list.pop()
print(my_list)  # Output: [10, 20, 30, 40]
```

- **📝 Explanation:** The `pop()` method removes and returns the last element of the list. Here, it removes `50`.

---

### 7. 🔍 Count the occurrences of the number `2` in the list `[2, 3, 2, 5, 2, 7, 8]`.

```python
my_list = [2, 3, 2, 5, 2, 7, 8]
count_2 = my_list.count(2)
print(count_2)  # Output: 3
```

- **📝 Explanation:** The `count()` method returns the number of times the specified value (`2`) appears in the list.

---

### 8. 📍 Find the index of the number `40` in the list `[10, 20, 30, 40, 50]`.

```python
my_list = [10, 20, 30, 40, 50]
index_40 = my_list.index(40)
print(index_40)  # Output: 3
```

- **📝 Explanation:** The `index()` method returns the index of the first occurrence of the specified value (`40`) in the list.

---

### 9. 🔄 Sort the list `[5, 3, 8, 6, 7, 2]` in ascending order and print the result.

```python
my_list = [5, 3, 8, 6, 7, 2]
my_list.sort()
print(my_list)  # Output: [2, 3, 5, 6, 7, 8]
```

- **📝 Explanation:** The `sort()` method sorts the elements of the list in ascending order.

---

### 10. 🔄 Reverse the list `[10, 20, 30, 40, 50]` and print the result.

```python
my_list = [10, 20, 30, 40, 50]
my_list.reverse()
print(my_list)  # Output: [50, 40, 30, 20, 10]
```

- **📝 Explanation:** The `reverse()` method reverses the elements of the list in place.

---

## 📝 Intermediate List Operations

### 11. 🧮 Create a list comprehension that generates a list of the squares of numbers from 1 to 10.

```python
squares = [i**2 for i in range(1, 11)]
print(squares)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

- **📝 Explanation:** The list comprehension `[i**2 for i in range(1, 11)]` iterates over each number from `1` to `10`, squares it, and stores the result in a new list.

---

### 12. 🔢 Filter the even numbers from the list `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` using list comprehension.

```python
evens = [i for i in range(1, 11) if i % 2 == 0]
print(evens)  # Output: [2, 4, 6, 8, 10]
```

- **📝 Explanation:** This list comprehension iterates over the numbers from `1` to `10` and includes only those that are even (`i % 2 == 0`).

---

### 13. 🔄 Create a list comprehension that generates a list of tuples where each tuple contains a number and its square.

```python
tuples = [(i, i**2) for i in range(1, 11)]
print(tuples)  # Output: [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64), (9, 81), (10, 100)]
```

- **📝 Explanation:** The list comprehension generates a list of tuples. Each tuple contains a number and its square.

---

### 14. 📚 Flatten a list of lists `[[1, 2], [3, 4], [5, 6]]` using list comprehension.

```python
matrix = [[1, 2], [3, 4], [5, 6]]
flat_list = [item for sublist in matrix for item in sublist]
print(flat_list)  # Output: [1, 2, 3, 4, 5, 6]
```

- **📝 Explanation:** This list comprehension flattens a list of lists into a single list by iterating over each sublist and then over each item within those sublists.

---

### 15. 🔠 Create a list comprehension that extracts the vowels from the string `"hello world"`.

```python
vowels = [char for char in "hello world" if char in "aeiou"]
print(vowels)  # Output: ['e', 'o', 'o']
```

- **📝 Explanation:** The list comprehension iterates through each character in the string `"hello world"`, and includes the character in the new list if it is a vowel (`char in "aeiou"`).

---

### 16. 🔗 Concatenate two lists `[1, 2, 3]` and `[4, 5, 6]` and print the result.

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print(combined_list)  # Output: [1, 2, 3, 4, 5, 6]
```

- **📝 Explanation:** The `+` operator concatenates two lists. `list1 + list2` creates a new list containing all elements from both lists.

---

### 17. 🔡 Create a list comprehension that converts all strings in the list `['a', 'b', 'c', 'd']` to uppercase.

```python
letters = ['a', 'b', 'c', 'd']
upper_letters = [letter.upper() for letter in letters]
print(upper_letters)  # Output: ['A', 'B', 'C', 'D']
```

- **📝 Explanation:** The list comprehension iterates through each string in the list `letters`, converts it to uppercase using the `upper()` method, and stores the result in a new list.

---

### 18. 🚫 Remove all occurrences of the value `3` from the list `[1, 3, 5, 3, 7, 3, 9]`.

```python
my_list = [1, 3, 5, 3, 7, 3, 9]
filtered_list = [x for x in my_list if x != 3]
print(filtered_list)  # Output: [1, 5, 7, 9]
```

- **📝 Explanation:** The list comprehension creates a new list that includes all elements from `my_list` except those that are equal to `3`.

---

### 19. ❓ Check if a list is empty and print `"Empty"` if it is, otherwise print `"Not Empty"`.

```python
my_list = []
if not my_list:
    print("Empty")
else:
    print("Not Empty")  # Output: Empty
```

- **📝 Explanation:** The `not` operator checks if the list is empty (`not my_list`). If the list is empty, "Empty" is printed; otherwise, "Not Empty" is printed.

---

### 20. 🌟 Create a list comprehension that replaces each vowel in a string with an asterisk (`'*'`).

```python
text = "hello world"
replaced_vowels = ''.join(['*' if char in 'aeiou' else char for char in text])
print(replaced_vowels)  # Output: h*ll* w*rld
```

- **📝 Explanation:** The list comprehension iterates through each character in the string `text`, replacing vowels with `'*'` and leaving other characters unchanged. The `join()` method then combines the list into a single string.

---

## 📝 Advanced List Operations

### 21. 🔢 Generate a list of the first 10 Fibonacci numbers.

```python
fib = [0, 1]
for

 i in range(8):
    fib.append(fib[-1] + fib[-2])
print(fib)  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

- **📝 Explanation:** We start with the first two Fibonacci numbers `[0, 1]` and generate the next eight by adding the last two numbers in the list (`fib[-1] + fib[-2]`).

---

### 22. 📄 Split a list `[1, 2, 3, 4, 5, 6, 7, 8]` into two halves and print both halves.

```python
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
half = len(my_list) // 2
first_half = my_list[:half]
second_half = my_list[half:]

print(first_half)  # Output: [1, 2, 3, 4]
print(second_half)  # Output: [5, 6, 7, 8]
```

- **📝 Explanation:** We calculate the midpoint of the list using `len(my_list) // 2` and then slice the list into two halves using `my_list[:half]` for the first half and `my_list[half:]` for the second half.

---

### 23. 🥈 Find the second largest number in the list `[10, 20, 4, 45, 99, 4, 28]`.

```python
my_list = [10, 20, 4, 45, 99, 4, 28]
unique_sorted_list = sorted(set(my_list))
second_largest = unique_sorted_list[-2]
print(second_largest)  # Output: 45
```

- **📝 Explanation:** We first remove duplicates using `set()`, then sort the list with `sorted()`. The second largest number is the second last element in the sorted list (`unique_sorted_list[-2]`).

---

### 24. 🌟 Create a list comprehension that generates a list of numbers from 1 to 100 that are divisible by both 3 and 5.

```python
divisible_by_3_and_5 = [i for i in range(1, 101) if i % 3 == 0 and i % 5 == 0]
print(divisible_by_3_and_5)  # Output: [15, 30, 45, 60, 75, 90]
```

- **📝 Explanation:** The list comprehension iterates through numbers from `1` to `100` and includes those that are divisible by both `3` and `5` (`i % 3 == 0 and i % 5 == 0`).

---

### 25. 🔢 Create a list comprehension that generates a list of all the prime numbers less than 50.

```python
primes = [x for x in range(2, 50) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))]
print(primes)  # Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
```

- **📝 Explanation:** This list comprehension checks each number in the range `2` to `50` to see if it is divisible by any number other than `1` and itself. If it is not, the number is prime.

---

### 26. 🔗 Zip two lists `[1, 2, 3]` and `['a', 'b', 'c']` into a list of tuples and print the result.

```python
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped_list = list(zip(list1, list2))
print(zipped_list)  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]
```

- **📝 Explanation:** The `zip()` function pairs elements from `list1` and `list2` to create tuples, which are then converted to a list using `list()`.

---

### 27. 📤 Unzip a list of tuples `[(1, 'a'), (2, 'b'), (3, 'c')]` into two separate lists.

```python
zipped_list = [(1, 'a'), (2, 'b'), (3, 'c')]
list1, list2 = zip(*zipped_list)
print(list(list1))  # Output: [1, 2, 3]
print(list(list2))  # Output: ['a', 'b', 'c']
```

- **📝 Explanation:** The `*` operator unpacks the list of tuples, and `zip()` separates the elements into two lists, which are then converted back into lists using `list()`.

---

### 28. 🔄 Rotate a list `[1, 2, 3, 4, 5]` to the right by 2 positions.

```python
my_list = [1, 2, 3, 4, 5]
n = 2
rotated_list = my_list[-n:] + my_list[:-n]
print(rotated_list)  # Output: [4, 5, 1, 2, 3]
```

- **📝 Explanation:** The list is sliced into two parts: the last `n` elements (`my_list[-n:]`) and the rest (`my_list[:-n]`). These slices are then concatenated to achieve the rotation.

---

### 29. 🔍 Find the common elements between two lists `[1, 2, 3, 4]` and `[3, 4, 5, 6]` and print the result.

```python
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common_elements = list(set(list1) & set(list2))
print(common_elements)  # Output: [3, 4]
```

- **📝 Explanation:** We convert the lists to sets and use the `&` operator to find the intersection (common elements). The result is then converted back to a list.

---

### 30. 🔄 Create a list comprehension that generates a list of strings where each string is the reverse of the corresponding string in the list `['abc', 'def', 'ghi']`.

```python
strings = ['abc', 'def', 'ghi']
reversed_strings = [s[::-1] for s in strings]
print(reversed_strings)  # Output: ['cba', 'fed', 'ihg']
```

- **📝 Explanation:** The list comprehension reverses each string in the list using slicing (`[::-1]`) and creates a new list with the reversed strings.
```
