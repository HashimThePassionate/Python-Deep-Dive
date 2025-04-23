# **50 Time Complexity Analysis Examples**  (Big O, Omega, Theta) 📚

This document provides 50 practical Python examples frequently encountered in technical interviews, focusing on time complexity analysis using **Big O** (upper bound), **Omega** (lower bound), and **Theta** (tight bound) notations. Each example includes a detailed explanation of the problem, the Python code, and a comprehensive time complexity analysis for all three notations. These examples span various domains such as searching, sorting, string manipulation, arrays, recursion, dynamic programming, and more. Let’s dive in! 🚀

---

## 1. Linear Search (Finding an Element in an Array) 🔍

### Code

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Test
arr = [5, 2, 9, 1, 7]
target = 9
print(linear_search(arr, target))  # Output: 2
```

### Explanation

This function searches for a target element in an unsorted array by checking each element sequentially.

- **Big O (Worst Case):** In the worst case, the target is either at the end of the array or not present, requiring a full traversal. Time complexity: **O(n)**, where `n` is the length of the array.
- **Omega (Best Case):** In the best case, the target is at the first index, requiring only one comparison. Time complexity: **Ω(1)**.
- **Theta (Average Case):** On average, we expect to search through half the array, but for a tight bound, we consider the worst case. Theta: **Θ(n)**.

---

## 2. Binary Search (Finding an Element in a Sorted Array) 🔎

### Code

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Test
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 6
print(binary_search(arr, target))  # Output: 5
```

### Explanation

This function performs a binary search on a sorted array, halving the search space with each iteration.

- **Big O (Worst Case):** Each iteration reduces the search space by half, leading to `log(n)` iterations. Time complexity: **O(log n)**.
- **Omega (Best Case):** If the target is at the middle index in the first iteration, it takes constant time. Time complexity: **Ω(1)**.
- **Theta (Average Case):** On average, binary search takes `log(n)` iterations. Theta: **Θ(log n)**.

---

## 3. Bubble Sort (Sorting an Array) 📈

### Code

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Test
arr = [64, 34, 25, 12, 22]
print(bubble_sort(arr))  # Output: [12, 22, 25, 34, 64]
```

### Explanation

Bubble sort repeatedly compares adjacent elements and swaps them if they are in the wrong order, pushing the largest unsorted element to the end in each pass.

- **Big O (Worst Case):** It performs `n * (n-1)/2` comparisons in the worst case (e.g., array sorted in reverse order). Time complexity: **O(n²)**.
- **Omega (Best Case):** If the array is already sorted, it makes one pass with no swaps. Time complexity: **Ω(n)**.
- **Theta (Average Case):** On average, it still performs `n²` comparisons. Theta: **Θ(n²)**.

---

## 4. Check if a String is a Palindrome 📝

### Code

```python
def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

# Test
s = "Radar"
print(is_palindrome(s))  # Output: True
```

### Explanation

This function checks if a string is a palindrome by comparing it with its reverse.

- **Big O (Worst Case):** Reversing the string and comparing it requires processing all characters. Time complexity: **O(n)**.
- **Omega (Best Case):** The operation is the same in all cases (reversing and comparing). Time complexity: **Ω(n)**.
- **Theta (Average Case):** The operation always takes `n` steps. Theta: **Θ(n)**.

---

## 5. Find Maximum Element in an Array 🔝

### Code

```python
def find_max(arr):
    max_val = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
    return max_val

# Test
arr = [3, 7, 2, 9, 1]
print(find_max(arr))  # Output: 9
```

### Explanation

This function finds the maximum element in an array by comparing each element with the current maximum.

- **Big O (Worst Case):** It traverses the entire array once. Time complexity: **O(n)**.
- **Omega (Best Case):** The operation is the same in all cases (full traversal). Time complexity: **Ω(n)**.
- **Theta (Average Case):** It always performs `n-1` comparisons. Theta: **Θ(n)**.

---

## 6. Reverse a String 🔄

### Code

```python
def reverse_string(s):
    return s[::-1]

# Test
s = "Hello"
print(reverse_string(s))  # Output: olleH
```

### Explanation

This function reverses a string using Python’s slicing.

- **Big O (Worst Case):** Slicing creates a new string by processing all characters. Time complexity: **O(n)**.
- **Omega (Best Case):** The operation is the same in all cases. Time complexity: **Ω(n)**.
- **Theta (Average Case):** It always processes `n` characters. Theta: **Θ(n)**.

---

## 7. Factorial of a Number 🔢

### Code

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Test
n = 5
print(factorial(n))  # Output: 120
```

### Explanation

This function calculates the factorial of a number using recursion.

- **Big O (Worst Case):** It makes `n` recursive calls. Time complexity: **O(n)**.
- **Omega (Best Case):** The operation is the same in all cases (n calls). Time complexity: **Ω(n)**.
- **Theta (Average Case):** It always makes `n` calls. Theta: **Θ(n)**.

---

## 8. Fibonacci Sequence (Recursive) 🌟

### Code

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Test
n = 6
print(fibonacci(n))  # Output: 8
```

### Explanation

This function calculates the nth Fibonacci number using recursion.

- **Big O (Worst Case):** Each call branches into two more calls, leading to exponential growth. Time complexity: **O(2^n)**.
- **Omega (Best Case):** For base cases (`n=0` or `n=1`), it takes constant time. Time complexity: **Ω(1)**.
- **Theta (Average Case):** The average case is still exponential. Theta: **Θ(2^n)**.

---

## 9. Merge Sort (Sorting an Array) 🗂️

### Code

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Test
arr = [64, 34, 25, 12, 22]
print(merge_sort(arr))  # Output: [12, 22, 25, 34, 64]
```

### Explanation

Merge sort divides the array into two halves, recursively sorts them, and then merges the sorted halves.

- **Big O (Worst Case):** It performs `n log(n)` operations (log(n) levels, with n comparisons per level). Time complexity: **O(n log n)**.
- **Omega (Best Case):** The operation is the same in all cases (divide and merge). Time complexity: **Ω(n log n)**.
- **Theta (Average Case):** It always performs `n log(n)` operations. Theta: **Θ(n log n)**.

---

## 10. Check if Two Strings are Anagrams 🧩

### Code

```python
def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

# Test
s1, s2 = "listen", "silent"
print(are_anagrams(s1, s2))  # Output: True
```

### Explanation

This function checks if two strings are anagrams by sorting and comparing them.

- **Big O (Worst Case):** Sorting dominates the time complexity. Time complexity: **O(n log n)**.
- **Omega (Best Case):** The operation is the same in all cases (sorting). Time complexity: **Ω(n log n)**.
- **Theta (Average Case):** It always performs sorting. Theta: **Θ(n log n)**.

---

## 11. Count Occurrences of an Element in an Array 📊

### Code

```python
def count_occurrences(arr, target):
    count = 0
    for x in arr:
        if x == target:
            count += 1
    return count

# Test
arr = [1, 2, 2, 3, 2, 4]
target = 2
print(count_occurrences(arr, target))  # Output: 3
```

### Explanation

This function counts how many times a target element appears in an array.

- **Big O (Worst Case):** It traverses the entire array. Time complexity: **O(n)**.
- **Omega (Best Case):** The operation is the same in all cases (full traversal). Time complexity: **Ω(n)**.
- **Theta (Average Case):** It always performs `n` comparisons. Theta: **Θ(n)**.

---

## 12. Find Subarray with Given Sum ➕

### Code

```python
def subarray_sum(arr, target):
    curr_sum = 0
    start = 0
    for end in range(len(arr)):
        curr_sum += arr[end]
        while curr_sum > target and start <= end:
            curr_sum -= arr[start]
            start += 1
        if curr_sum == target:
            return start, end
    return -1, -1

# Test
arr = [1, 4, 20, 3, 10, 5]
target = 33
print(subarray_sum(arr, target))  # Output: (2, 4)
```

### Explanation

This function finds a contiguous subarray with a sum equal to the target using a sliding window approach.

- **Big O (Worst Case):** In the worst case, the inner while loop runs for each element, leading to `n²` operations. Time complexity: **O(n²)**.
- **Omega (Best Case):** If the subarray is found early, it may take linear time. Time complexity: **Ω(n)**.
- **Theta (Average Case):** On average, it may still take `n²` operations. Theta: **Θ(n²)**.

---

## 13. Rotate an Array 🔄

### Code

```python
def rotate_array(arr, k):
    k = k % len(arr)
    return arr[-k:] + arr[:-k]

# Test
arr = [1, 2, 3, 4, 5]
k = 2
print(rotate_array(arr, k))  # Output: [4, 5, 1, 2, 3]
```

### Explanation

This function rotates an array by `k` positions to the right using slicing.

- **Big O (Worst Case):** Slicing and concatenation copy the entire array. Time complexity: **O(n)**.
- **Omega (Best Case):** The operation is the same in all cases. Time complexity: **Ω(n)**.
- **Theta (Average Case):** It always performs `n` operations. Theta: **Θ(n)**.

---

## 14. Check if an Array is Sorted 📉

### Code

```python
def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

# Test
arr = [1, 2, 3, 4, 5]
print(is_sorted(arr))  # Output: True
```

### Explanation

This function checks if an array is sorted in non-decreasing order.

- **Big O (Worst Case):** It traverses the entire array. Time complexity: **O(n)**.
- **Omega (Best Case):** If the first two elements are out of order, it returns early. Time complexity: **Ω(1)**.
- **Theta (Average Case):** On average, it may check half the array, but the tight bound is: **Θ(n)**.

---

## 15. Remove Duplicates from a Sorted Array 🗑️

### Code

```python
def remove_duplicates(arr):
    if not arr:
        return arr
    write_index = 1
    for i in range(1, len(arr)):
        if arr[i] != arr[write_index - 1]:
            arr[write_index] = arr[i]
            write_index += 1
    return arr[:write_index]

# Test
arr = [1, 1, 2, 2, 3]
print(remove_duplicates(arr))  # Output: [1, 2, 3]
```

### Explanation

This function removes duplicates from a sorted array in-place and returns the unique elements.

- **Big O (Worst Case):** It traverses the entire array once. Time complexity: **O(n)**.
- **Omega (Best Case):** The operation is the same in all cases. Time complexity: **Ω(n)**.
- **Theta (Average Case):** It always performs `n` operations. Theta: **Θ(n)**.

---

## 16. Find First Non-Repeating Character in a String 🔠

### Code

```python
def first_non_repeating(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    for char in s:
        if freq[char] == 1:
            return char
    return None

# Test
s = "swiss"
print(first_non_repeating(s))  # Output: w
```

### Explanation

This function finds the first character in a string that does not repeat.

- **Big O (Worst Case):** It traverses the string twice to build and check the frequency dictionary. Time complexity: **O(n)**.
- **Omega (Best Case):** The operation is the same in all cases. Time complexity: **Ω(n)**.
- **Theta (Average Case):** It always performs `2n` operations. Theta: **Θ(n)**.

---

## 17. Generate All Substrings of a String 📜

### Code

```python
def all_substrings(s):
    result = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            result.append(s[i:j])
    return result

# Test
s = "abc"
print(all_substrings(s))  # Output: ['a', 'ab', 'abc', 'b', 'bc', 'c']
```

### Explanation

This function generates all possible substrings of a given string.

- **Big O (Worst Case):** It uses nested loops to generate `n * (n+1)/2` substrings. Time complexity: **O(n²)**.
- **Omega (Best Case):** The operation is the same in all cases. Time complexity: **Ω(n²)**.
- **Theta (Average Case):** It always generates `n²` substrings. Theta: **Θ(n²)**.

---

## 18. Find Longest Common Prefix 🔤

### Code

```python
def longest_common_prefix(strs):
    if not strs:
        return ""
    shortest = min(strs, key=len)
    for i, char in enumerate(shortest):
        for s in strs:
            if s[i] != char:
                return shortest[:i]
    return shortest

# Test
strs = ["flower", "flow", "flight"]
print(longest_common_prefix(strs))  # Output: fl
```

### Explanation

This function finds the longest common prefix among an array of strings.

- **Big O (Worst Case):** It checks each character of the shortest string against all strings. Time complexity: **O(n \* m)**, where `n` is the number of strings and `m` is the length of the shortest string.
- **Omega (Best Case):** If the first character mismatches, it returns early. Time complexity: **Ω(1)**.
- **Theta (Average Case):** On average, it checks half the characters. Theta: **Θ(n \* m)**.

---

## 19. Matrix Spiral Traversal 🌀

### Code

```python
def spiral_order(matrix):
    if not matrix:
        return []
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
    return result

# Test
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(spiral_order(matrix))  # Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
```

### Explanation

This function traverses a matrix in a spiral order (clockwise from the outer layer to the inner).

- **Big O (Worst Case):** It visits each element exactly once. Time complexity: **O(m \* n)**, where `m` is the number of rows and `n` is the number of columns.
- **Omega (Best Case):** The operation is the same in all cases. Time complexity: **Ω(m \* n)**.
- **Theta (Average Case):** It always visits `m * n` elements. Theta: **Θ(m \* n)**.

---

## 20. Find Pair with Given Sum in an Array ➕

### Code

```python
def find_pair_with_sum(arr, target):
    seen = set()
    for num in arr:
        if target - num in seen:
            return num, target - num
        seen.add(num)
    return None

# Test
arr = [2, 7, 11, 15]
target = 9
print(find_pair_with_sum(arr, target))  # Output: (7, 2)
```

### Explanation

This function finds a pair of numbers in an array that sum to the target using a hash set.

- **Big O (Worst Case):** It traverses the array once, with hash set operations being O(1). Time complexity: **O(n)**.
- **Omega (Best Case):** If the pair is found early, it returns quickly. Time complexity: **Ω(1)**.
- **Theta (Average Case):** On average, it performs `n` operations. Theta: **Θ(n)**.

---

## 21. Insertion Sort (Sorting an Array) 📊

### Code

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Test
arr = [12, 11, 13, 5, 6]
print(insertion_sort(arr))  # Output: [5, 6, 11, 12, 13]
```

### Explanation

Insertion sort builds a sorted array one element at a time by inserting each element into its correct position.

- **Big O (Worst Case):** In the worst case (reverse sorted array), it performs `n * (n-1)/2` comparisons. Time complexity: **O(n²)**.
- **Omega (Best Case):** If the array is already sorted, it makes one comparison per element. Time complexity: **Ω(n)**.
- **Theta (Average Case):** On average, it performs `n²/4` comparisons. Theta: **Θ(n²)**.

---

## 22. Quick Sort (Sorting an Array) ⚡

### Code

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Test
arr = [64, 34, 25, 12, 22]
print(quick_sort(arr))  # Output: [12, 22, 25, 34, 64]
```

### Explanation

Quick sort partitions the array around a pivot and recursively sorts the subarrays.

- **Big O (Worst Case):** In the worst case (e.g., already sorted array with a bad pivot), it takes `n²` comparisons. Time complexity: **O(n²)**.
- **Omega (Best Case):** With a good pivot, it takes `n log(n)` operations. Time complexity: **Ω(n log n)**.
- **Theta (Average Case):** On average, it performs `n log(n)` operations. Theta: **Θ(n log n)**.

---

## 23. Find the Missing Number in an Array 🔢

### Code

```python
def find_missing_number(arr, n):
    expected_sum = (n * (n + 1)) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

# Test
arr = [1, 2, 4, 5, 6]
n = 6
print(find_missing_number(arr, n))  # Output: 3
```

### Explanation

This function finds the missing number in an array of numbers from 1 to `n` using the sum formula.

- **Big O (Worst Case):** It calculates the sum of the array, which takes `n` operations. Time complexity: **O(n)**.
- **Omega (Best Case):** The operation is the same in all cases. Time complexity: **Ω(n)**.
- **Theta (Average Case):** It always performs `n` operations. Theta: **Θ(n)**.

---

## 24. Reverse a Linked List (Simplified with List) 🔗

### Code

```python
def reverse_linked_list(lst):
    return lst[::-1]

# Test
lst = [1, 2, 3, 4, 5]
print(reverse_linked_list(lst))  # Output: [5, 4, 3, 2, 1]
```

### Explanation

This function simulates reversing a linked list by reversing a Python list.

- **Big O (Worst Case):** Slicing copies the entire list. Time complexity: **O(n)**.
- **Omega (Best Case):** The operation is the same in all cases. Time complexity: **Ω(n)**.
- **Theta (Average Case):** It always performs `n` operations. Theta: **Θ(n)**.

---

## 25. Detect a Cycle in a Linked List (Simplified with List) 🔄

### Code

```python
def has_cycle(arr, pos):
    # Simulate a cycle by connecting the last element to pos (not actual linked list)
    seen = set()
    for i in range(len(arr)):
        if i in seen:
            return True
        seen.add(i)
    return False

# Test
arr = [3, 2, 0, -4]  # Simulating a cycle at pos=1
pos = 1
print(has_cycle(arr, pos))  # Output: True (simulated)
```

### Explanation

This function simulates detecting a cycle in a linked list using a set (Floyd’s cycle detection would be more efficient).

- **Big O (Worst Case):** It traverses the list once. Time complexity: **O(n)**.
- **Omega (Best Case):** If a cycle is detected early, it returns quickly. Time complexity: **Ω(1)**.
- **Theta (Average Case):** On average, it performs `n` operations. Theta: **Θ(n)**.

---

## 26. Find the Intersection of Two Arrays ∩

### Code

```python
def intersection(arr1, arr2):
    set1 = set(arr1)
    return [x for x in arr2 if x in set1]

# Test
arr1 = [1, 2, 2, 1]
arr2 = [2, 2]
print(intersection(arr1, arr2))  # Output: [2, 2]
```

### Explanation

This function finds the intersection of two arrays using a set for efficient lookup.

- **Big O (Worst Case):** Converting `arr1` to a set takes `O(n)`, and checking `arr2` takes `O(m)`. Time complexity: **O(n + m)**.
- **Omega (Best Case):** The operation is the same in all cases. Time complexity: **Ω(n + m)**.
- **Theta (Average Case):** It always performs `n + m` operations. Theta: **Θ(n + m)**.

---

## 27. Find the Union of Two Arrays ∪

### Code

```python
def union(arr1, arr2):
    return list(set(arr1 + arr2))

# Test
arr1 = [1, 2, 2, 1]
arr2 = [2, 3]
print(union(arr1, arr2))  # Output: [1, 2, 3]
```

### Explanation

This function finds the union of two arrays by converting them to a set.

- **Big O (Worst Case):** Concatenation and set conversion take `O(n + m)`. Time complexity: **O(n + m)**.
- **Omega (Best Case):** The operation is the same in all cases. Time complexity: **Ω(n + m)**.
- **Theta (Average Case):** It always performs `n + m` operations. Theta: **Θ(n + m)**.

---

## 28. Check if a Number is Prime 🔢

### Code

```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test
n = 29
print(is_prime(n))  # Output: True
```

### Explanation

This function checks if a number is prime by testing divisibility up to its square root.

- **Big O (Worst Case):** It checks up to `sqrt(n)`. Time complexity: **O(√n)**.
- **Omega (Best Case):** If the number is divisible by 2, it returns early. Time complexity: **Ω(1)**.
- **Theta (Average Case):** On average, it checks `√n` numbers. Theta: **Θ(√n)**.

---

## 29. Generate Prime Numbers (Sieve of Eratosthenes) 🔍

### Code

```python
def sieve_of_eratosthenes(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i in range(n + 1) if sieve[i]]

# Test
n = 30
print(sieve_of_eratosthenes(n))  # Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```

### Explanation

This function generates all prime numbers up to `n` using the Sieve of Eratosthenes algorithm.

- **Big O (Worst Case):** The algorithm performs `n log(log(n))` operations. Time complexity: **O(n log log n)**.
- **Omega (Best Case):** The operation is the same in all cases. Time complexity: **Ω(n log log n)**.
- **Theta (Average Case):** It always performs `n log(log(n))` operations. Theta: **Θ(n log log n)**.

---

## 30. Find the GCD of Two Numbers (Euclidean Algorithm) ➗

### Code

```python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Test
a, b = 48, 18
print(gcd(a, b))  # Output: 6
```

### Explanation

This function calculates the GCD of two numbers using the Euclidean algorithm.

- **Big O (Worst Case):** The number of steps is proportional to `log(min(a, b))`. Time complexity: **O(log(min(a, b)))**.
- **Omega (Best Case):** If `b` divides `a` immediately, it takes one step. Time complexity: **Ω(1)**.
- **Theta (Average Case):** On average, it takes `log(min(a, b))` steps. Theta: **Θ(log(min(a, b)))**.

---

## 31. Find the Longest Substring Without Repeating Characters 📜

### Code

```python
def longest_substring_no_repeat(s):
    seen = {}
    max_len = start = 0
    for i, char in enumerate(s):
        if char in seen and seen[char] >= start:
            start = seen[char] + 1
        else:
            max_len = max(max_len, i - start + 1)
        seen[char] = i
    return max_len

# Test
s = "abcabcbb"
print(longest_substring_no_repeat(s))  # Output: 3 ("abc")
```

### Explanation

This function finds the length of the longest substring without repeating characters using a sliding window.

- **Big O (Worst Case):** It traverses the string once. Time complexity: **O(n)**.
- **Omega (Best Case):** The operation is the same in all cases. Time complexity: **Ω(n)**.
- **Theta (Average Case):** It always performs `n` operations. Theta: **Θ(n)**.

---

## 32. Find All Permutations of a String 🔄

### Code

```python
def permutations(s):
    if len(s) <= 1:
        return [s]
    result = []
    for i, char in enumerate(s):
        rest = s[:i] + s[i+1:]
        for p in permutations(rest):
            result.append(char + p)
    return result

# Test
s = "abc"
print(permutations(s))  # Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
```

### Explanation

This function generates all permutations of a string using recursion.

- **Big O (Worst Case):** It generates `n!` permutations, with each permutation taking `O(n)` to construct. Time complexity: **O(n \* n!)**.
- **Omega (Best Case):** For a string of length 1, it takes constant time. Time complexity: **Ω(1)**.
- **Theta (Average Case):** It always generates `n!` permutations. Theta: **Θ(n \* n!)**.

---

## 33. Find the Median of Two Sorted Arrays 📊

### Code

```python
def find_median_sorted_arrays(nums1, nums2):
    merged = sorted(nums1 + nums2)
    total_len = len(merged)
    if total_len % 2 == 0:
        return (merged[total_len // 2 - 1] + merged[total_len // 2]) / 2
    return merged[total_len // 2]

# Test
nums1 = [1, 3]
nums2 = [2]
print(find_median_sorted_arrays(nums1, nums2))  # Output: 2.0
```

### Explanation

This function finds the median of two sorted arrays by merging and sorting them (a more efficient solution exists with O(log(min(m, n))), but this is simpler).

- **Big O (Worst Case):** Merging and sorting take `O((m+n) log(m+n))`. Time complexity: **O((m+n) log(m+n))**.
- **Omega (Best Case):** The operation is the same in all cases. Time complexity: **Ω((m+n) log(m+n))**.
- **Theta (Average Case):** It always performs sorting. Theta: **Θ((m+n) log(m+n))**.

---

## 34. Kadane’s Algorithm (Maximum Subarray Sum) ➕

### Code

```python
def max_subarray_sum(arr):
    max_so_far = max_ending_here = arr[0]
    for num in arr[1:]:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

# Test
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray_sum(arr))  # Output: 6 ([4, -1, 2, 1])
```

### Explanation

Kadane’s algorithm finds the maximum sum of a contiguous subarray using a dynamic programming approach.

- **Big O (Worst Case):** It traverses the array once. Time complexity: **O(n)**.
- **Omega (Best Case):** The operation is the same in all cases. Time complexity: **Ω(n)**.
- **Theta (Average Case):** It always performs `n` operations. Theta: **Θ(n)**.

---

## 35. Find the Longest Palindromic Substring 📝

### Code

```python
def longest_palindromic_substring(s):
    n = len(s)
    start = max_len = 0
    for i in range(n):
        # Odd length palindromes
        left = right = i
        while left >= 0 and right < n and s[left] == s[right]:
            if right - left + 1 > max_len:
                start = left
                max_len = right - left + 1
            left -= 1
            right += 1
        # Even length palindromes
        left, right = i, i + 1
        while left >= 0 and right < n and s[left] == s[right]:
            if right - left + 1 > max_len:
                start = left
                max_len = right - left + 1
            left -= 1
            right += 1
    return s[start:start + max_len]

# Test
s = "babad"
print(longest_palindromic_substring(s))  # Output: "bab" (or "aba")
```

### Explanation

This function finds the longest palindromic substring by expanding around each center (odd and even lengths).

- **Big O (Worst Case):** For each character, it may expand to the full string. Time complexity: **O(n²)**.
- **Omega (Best Case):** If no palindromes are found, it performs minimal expansions. Time complexity: **Ω(n)**.
- **Theta (Average Case):** On average, it performs `n²` operations. Theta: **Θ(n²)**.

---

## 36. Find the Minimum Window Substring 📜

### Code

```python
def min_window(s, t):
    if not s or not t:
        return ""
    freq_t = {}
    for char in t:
        freq_t[char] = freq_t.get(char, 0) + 1
    required = len(freq_t)
    freq_s = {}
    formed = 0
    left = right = 0
    min_len = float('inf')
    min_window_sub = ""
    while right < len(s):
        char = s[right]
        freq_s[char] = freq_s.get(char, 0) + 1
        if char in freq_t and freq_s[char] == freq_t[char]:
            formed += 1
        while left <= right and formed == required:
            char = s[left]
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_window_sub = s[left:right + 1]
            freq_s[char] -= 1
            if char in freq_t and freq_s[char] < freq_t[char]:
                formed -= 1
            left += 1
        right += 1
    return min_window_sub

# Test
s = "ADOBECODEBANC"
t = "ABC"
print(min_window(s, t))  # Output: "BANC"
```

### Explanation

This function finds the smallest window in string `s` that contains all characters of string `t` using a sliding window approach.

- **Big O (Worst Case):** It traverses the string twice (expanding and shrinking the window). Time complexity: **O(n)**.
- **Omega (Best Case):** The operation is the same in all cases. Time complexity: **Ω(n)**.
- **Theta (Average Case):** It always performs `n` operations. Theta: **Θ(n)**.

---

## 37. Find the Longest Increasing Subsequence (LIS) 📈

### Code

```python
def length_of_lis(nums):
    if not nums:
        return 0
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

# Test
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(length_of_lis(nums))  # Output: 4 ([2, 3, 7, 101])
```

### Explanation

This function finds the length of the longest increasing subsequence using dynamic programming.

- **Big O (Worst Case):** It uses two nested loops. Time complexity: **O(n²)**.
- **Omega (Best Case):** If the array has no increasing subsequence, it still performs all checks. Time complexity: **Ω(n²)**.
- **Theta (Average Case):** It always performs `n²` operations. Theta: **Θ(n²)**.

---

## 38. Find the Longest Common Subsequence (LCS) 🔠

### Code

```python
def longest_common_subsequence(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]

# Test
s1, s2 = "ABCDGH", "AEDFHR"
print(longest_common_subsequence(s1, s2))  # Output: 3 ("ADH")
```

### Explanation

This function finds the length of the longest common subsequence between two strings using dynamic programming.

- **Big O (Worst Case):** It fills a `m * n` DP table. Time complexity: **O(m \* n)**.
- **Omega (Best Case):** The operation is the same in all cases. Time complexity: **Ω(m \* n)**.
- **Theta (Average Case):** It always fills the `m * n` table. Theta: **Θ(m \* n)**.

---

## 39. Find the Minimum Path Sum in a Grid 🛤️

### Code

```python
def min_path_sum(grid):
    if not grid:
        return 0
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = grid[0][0]
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    return dp[m-1][n-1]

# Test
grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
print(min_path_sum(grid))  # Output: 7 (1→3→1→1→1)
```

### Explanation

This function finds the minimum path sum from the top-left to the bottom-right of a grid using dynamic programming (only right and down moves allowed).

- **Big O (Worst Case):** It fills a `m * n` DP table. Time complexity: **O(m \* n)**.
- **Omega (Best Case):** The operation is the same in all cases. Time complexity: **Ω(m \* n)**.
- **Theta (Average Case):** It always fills the `m * n` table. Theta: **Θ(m \* n)**.

---

## 40. Find the Number of Islands in a Grid 🏝️

### Code

```python
def num_islands(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    def dfs(i, j):
        if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] != "1":
            return
        grid[i][j] = "0"  # Mark as visited
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)
    
    islands = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "1":
                islands += 1
                dfs(i, j)
    return islands

# Test
grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
print(num_islands(grid))  # Output: 3
```

### Explanation

This function counts the number of islands (connected groups of "1"s) in a grid using DFS.

- **Big O (Worst Case):** It visits each cell once. Time complexity: **O(m \* n)**.
- **Omega (Best Case):** The operation is the same in all cases. Time complexity: **Ω(m \* n)**.
- **Theta (Average Case):** It always visits `m * n` cells. Theta: **Θ(m \* n)**.

---

## 41. Find the Kth Largest Element in an Array 🔝

### Code

```python
def find_kth_largest(nums, k):
    return sorted(nums, reverse=True)[k-1]

# Test
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(find_kth_largest(nums, k))  # Output: 5
```

### Explanation

This function finds the kth largest element in an array by sorting it in descending order (a more efficient solution using a min-heap would be O(n log k)).

- **Big O (Worst Case):** Sorting takes `O(n log n)`. Time complexity: **O(n log n)**.
- **Omega (Best Case):** The operation is the same in all cases. Time complexity: **Ω(n log n)**.
- **Theta (Average Case):** It always performs sorting. Theta: **Θ(n log n)**.

---

## 42. Find the Majority Element (Boyer-Moore Voting Algorithm) 🗳️

### Code

```python
def majority_element(nums):
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    return candidate

# Test
nums = [3, 2, 3]
print(majority_element(nums))  # Output: 3
```

### Explanation

This function finds the majority element (appears more than `n/2` times) using the Boyer-Moore voting algorithm.

- **Big O (Worst Case):** It traverses the array once. Time complexity: **O(n)**.
- **Omega (Best Case):** The operation is the same in all cases. Time complexity: **Ω(n)**.
- **Theta (Average Case):** It always performs `n` operations. Theta: **Θ(n)**.

---

## 43. Find the First and Last Position of an Element in a Sorted Array 🔍

### Code

```python
def search_range(nums, target):
    def binary_search(nums, target, left_bias):
        left, right = 0, len(nums) - 1
        i = -1
        while left <= right:
            mid = (left + right) // 2
            if target < nums[mid] or (left_bias and target == nums[mid]):
                right = mid - 1
            elif target > nums[mid] or (not left_bias and target == nums[mid]):
                left = mid + 1
            else:
                i = mid
                break
        return i
    
    left = binary_search(nums, target, True)
    right = binary_search(nums, target, False)
    return [left, right]

# Test
nums = [5, 7, 7, 8, 8, 10]
target = 8
print(search_range(nums, target))  # Output: [3, 4]
```

### Explanation

This function finds the first and last positions of a target in a sorted array using modified binary search.

- **Big O (Worst Case):** Two binary searches take `O(log n)` each. Time complexity: **O(log n)**.
- **Omega (Best Case):** The operation is the same in all cases. Time complexity: **Ω(log n)**.
- **Theta (Average Case):** It always performs `log(n)` operations. Theta: **Θ(log n)**.

---

## 44. Find the Peak Element in an Array ⛰️

### Code

```python
def find_peak_element(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return left

# Test
nums = [1, 2, 3, 1]
print(find_peak_element(nums))  # Output: 2
```

### Explanation

This function finds a peak element (greater than its neighbors) in an array using binary search.

- **Big O (Worst Case):** It performs binary search. Time complexity: **O(log n)**.
- **Omega (Best Case):** The operation is the same in all cases. Time complexity: **Ω(log n)**.
- **Theta (Average Case):** It always performs `log(n)` operations. Theta: **Θ(log n)**.

---

## 45. Find the Minimum in a Rotated Sorted Array 🔄

### Code

```python
def find_min_rotated(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]

# Test
nums = [3, 4, 5, 1, 2]
print(find_min_rotated(nums))  # Output: 1
```

### Explanation

This function finds the minimum element in a rotated sorted array using binary search.

- **Big O (Worst Case):** It performs binary search. Time complexity: **O(log n)**.
- **Omega (Best Case):** The operation is the same in all cases. Time complexity: **Ω(log n)**.
- **Theta (Average Case):** It always performs `log(n)` operations. Theta: **Θ(log n)**.

---

## 46. Find the Longest Valid Parentheses 🔐

### Code

```python
def longest_valid_parentheses(s):
    stack = [-1]
    max_len = 0
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_len = max(max_len, i - stack[-1])
    return max_len

# Test
s = "(()"
print(longest_valid_parentheses(s))  # Output: 2 ("()")
```

### Explanation

This function finds the length of the longest valid parentheses substring using a stack.

- **Big O (Worst Case):** It traverses the string once. Time complexity: **O(n)**.
- **Omega (Best Case):** The operation is the same in all cases. Time complexity: **Ω(n)**.
- **Theta (Average Case):** It always performs `n` operations. Theta: **Θ(n)**.

---

## 47. Find the Maximum Product Subarray ➕

### Code

```python
def max_product_subarray(nums):
    max_so_far = max_ending_here = min_ending_here = nums[0]
    for num in nums[1:]:
        temp = max_ending_here
        max_ending_here = max(num, max(max_ending_here * num, min_ending_here * num))
        min_ending_here = min(num, min(temp * num, min_ending_here * num))
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

# Test
nums = [2, 3, -2, 4]
print(max_product_subarray(nums))  # Output: 6 ([2, 3])
```

### Explanation

This function finds the maximum product of a contiguous subarray, handling negative numbers by tracking both maximum and minimum products.

- **Big O (Worst Case):** It traverses the array once. Time complexity: **O(n)**.
- **Omega (Best Case):** The operation is the same in all cases. Time complexity: **Ω(n)**.
- **Theta (Average Case):** It always performs `n` operations. Theta: **Θ(n)**.

---

## 48. Find the Longest Consecutive Sequence 📈

### Code

```python
def longest_consecutive(nums):
    if not nums:
        return 0
    num_set = set(nums)
    max_len = 0
    for num in num_set:
        if num - 1 not in num_set:
            curr_num = num
            curr_len = 1
            while curr_num + 1 in num_set:
                curr_num += 1
                curr_len += 1
            max_len = max(max_len, curr_len)
    return max_len

# Test
nums = [100, 4, 200, 1, 3, 2]
print(longest_consecutive(nums))  # Output: 4 ([1, 2, 3, 4])
```

### Explanation

This function finds the longest consecutive sequence in an array using a set for O(1) lookups.

- **Big O (Worst Case):** It traverses the array once, with each number being processed at most twice. Time complexity: **O(n)**.
- **Omega (Best Case):** The operation is the same in all cases. Time complexity: **Ω(n)**.
- **Theta (Average Case):** It always performs `n` operations. Theta: **Θ(n)**.

---

## 49. Find the Minimum Number of Coins for a Given Amount 💰

### Code

```python
def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

# Test
coins = [1, 2, 5]
amount = 11
print(coin_change(coins, amount))  # Output: 3 (5+5+1)
```

### Explanation

This function finds the minimum number of coins needed to make a given amount using dynamic programming.

- **Big O (Worst Case):** It fills a DP table of size `amount` for each coin. Time complexity: **O(amount \* len(coins))**.
- **Omega (Best Case):** The operation is the same in all cases. Time complexity: **Ω(amount \* len(coins))**.
- **Theta (Average Case):** It always fills the table. Theta: **Θ(amount \* len(coins))**.

---

## 50. Find the Maximum Profit from Stock Prices 📈

### Code

```python
def max_profit(prices):
    if len(prices) < 2:
        return 0
    min_price = prices[0]
    max_profit = 0
    for price in prices[1:]:
        if price < min_price:
            min_price = price
        else:
            curr_profit = price - min_price
            max_profit = max(max_profit, curr_profit)
    return max_profit

# Test
prices = [7, 1, 5, 3, 6, 4]
print(max_profit(prices))  # Output: 5 (buy at 1, sell at 6)
```

### Explanation

This function finds the maximum profit from buying and selling a stock by tracking the minimum price seen so far.

- **Big O (Worst Case):** It traverses the array once. Time complexity: **O(n)**.
- **Omega (Best Case):** The operation is the same in all cases. Time complexity: **Ω(n)**.
- **Theta (Average Case):** It always performs `n` operations. Theta: **Θ(n)**.

---

## Conclusion 🎉

These 50 examples cover a wide range of problems commonly asked in technical interviews, with detailed time complexity analyses using Big O, Omega, and Theta notations. They include fundamental algorithms (searching, sorting), string manipulations, array operations, recursion, dynamic programming, and more advanced problems. Practice these to strengthen your understanding of time complexity and algorithmic problem-solving! 💪