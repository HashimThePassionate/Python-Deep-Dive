# **Composing Complexity Classes** 📚

Understanding how to combine **complexity classes** is key to analyzing the **time complexity** of algorithms. By breaking down operations and combining their complexities, we can determine the overall performance of a function or algorithm. This guide explains the process in detail with clear examples, using **Big O notation** to express worst-case runtime. Let’s dive in!

---

## 1. What Are Complexity Classes? 📚

A **complexity class** describes how the runtime of an algorithm scales with the input size (`n`). Common complexity classes include:

- **O(1)**: Constant time (e.g., accessing an array element).
- **O(n)**: Linear time (e.g., iterating through an array).
- **O(n²)**: Quadratic time (e.g., nested loops).
- **O(log n)**: Logarithmic time (e.g., binary search).
- **O(n log n)**: Linearithmic time (e.g., efficient sorting algorithms like quicksort).

When analyzing complex algorithms, we often combine the complexities of individual operations to find the total runtime. There are two main ways to combine complexities: **addition** (for sequential operations) and **multiplication** (for repeated operations). Let’s explore these with examples! 🌟

---

## 2. Combining Complexity Classes 🔗

### 2.1 Addition: Sequential Operations ➕

When operations execute **sequentially** (one after another), their time complexities are **added**. The final complexity is dominated by the **highest-order term** in Big O notation.

**Example 1: Inserting and Sorting a List** 📋

Suppose we:

1. Insert an element into a list: **O(n)** (e.g., appending to a dynamic array may require shifting elements).
2. Sort the list: **O(n log n)** (e.g., using quicksort).

**Code:**

```python
def example(arr):
    arr.append(5)  # O(n)
    arr.sort()     # O(n log n)
    return arr
```

**Calculation:**

- Insert: **O(n)**.
- Sort: **O(n log n)**.
- Total: **O(n + n log n)**.
- In Big O, we take the dominant term: **O(n log n)** (since `n log n` grows faster than `n`).

**Why?**\
The two operations happen one after the other, so their complexities add up. The sorting operation dominates because it has a higher growth rate.

---

### 2.2 Multiplication: Repeated Operations ✖️

When an operation is **repeated** (e.g., inside a loop), we **multiply** its complexity by the number of repetitions.

**Example 2: Repeating a Quadratic Operation** 🔄

Consider a function with **O(n²)** complexity that is executed `n` times in a loop:

**Code:**

```python
def complex_function(arr):
    # O(n²) operation
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i], arr[j])

def main(n):
    for i in range(n):  # Runs n times
        complex_function([1, 2, 3, ..., n])  # O(n²)
```

**Calculation:**

- `complex_function`: **O(n²)**.
- Repeated `n` times: **O(n)**.
- Total: **O(n²) × O(n) = O(n × n²) = O(n³)**.

**Why?**\
Each execution of the quadratic function takes `n²` time, and it runs `n` times, resulting in `n × n² = n³` total time.

---

## 3. Nested Loops 🔁

Nested loops are common in algorithms, and their complexity is calculated by **multiplying** the number of iterations of each loop.

**Example 3: Simple Nested Loop** 🌀

**Code:**

```python
def nested_loop(n):
    for i in range(n):      # Runs n times
        for j in range(n):  # Runs n times
            print(i, j)     # O(1)
```

**Calculation:**

- Inner loop: `n` iterations.
- Outer loop: `n` iterations.
- Each `print` statement: **O(1)**.
- Total: **O(1) × n × n = O(n²)**.

**Why?**\
The inner loop runs `n` times for each iteration of the outer loop, resulting in `n × n = n²` total iterations. Since the operation inside is constant time, the complexity is **O(n²)**.

---

**Example 4: Consecutive Statements in Loops** 📜

When loops contain multiple statements, we add their complexities and multiply by the number of iterations.

**Code:**

```python
def fun(n):
    for i in range(n):      # Runs n times
        print(i)            # O(1), constant time (c1)
    
    for i in range(n):      # Runs n times
        for j in range(n):  # Runs n times
            print(j)        # O(1), constant time (c2)
```

**Calculation:**

1. First loop:
   - `n` iterations, each with a `print` statement (**O(1)**).
   - Total: **c1 × n**.
2. Second (nested) loop:
   - Outer loop: `n` iterations.
   - Inner loop: `n` iterations.
   - `print` statement: **O(1)**.
   - Total: **c2 × n × n = c2 × n²**.
3. Combined:
   - Total: **c1 × n + c2 × n²**.
   - Dominant term: **O(n²)**.

**Why?**\
The nested loop’s quadratic complexity (`n²`) dominates the linear complexity (`n`) of the first loop, so the overall complexity is **O(n²)**.

---

## 4. Logarithmic Complexity 🌲

**Logarithmic complexity** arises when the problem size is reduced by a constant factor (e.g., halved) in each iteration, as in binary search or doubling loops.

**Example 5: Doubling Loop** 🔢

**Code:**

```python
def log_example(n):
    i = 1
    while i <= n:
        i = i * 2  # Doubles i each iteration
        print(i)
```

**Behavior:**

- For `n = 10`: Prints `2, 4, 8, 16` (4 iterations).
- For `n = 20`: Prints `2, 4, 8, 16, 32` (5 iterations).
- Each time `n` doubles, the number of iterations increases by **1**.

**Calculation:**

- Let the loop run `k` iterations.
- In the last iteration, `i = 2^k`.
- The loop stops when `i > n`, so: **2^k ≈ n**.
- Thus: **k ≈ log₂(n)**.
- Each iteration is **O(1)**, so total complexity: **O(log n)**.

**Why?**\
The number of iterations is proportional to the logarithm of `n` (base 2), as the problem size (represented by `i`) doubles each time.

---

## 5. Putting It All Together: A Mixed Example 🛠️

Let’s analyze a function with multiple types of operations to see how complexities combine.

**Code:**

```python
def mixed_example(n):
    # Sequential operation: O(n)
    for i in range(n):
        print(i)
    
    # Nested loop: O(n²)
    for i in range(n):
        for j in range(n):
            print(i, j)
    
    # Logarithmic loop: O(log n)
    i = 1
    while i <= n:
        i = i * 2
        print(i)
```

**Calculation:**

1. First loop: **O(n)**.
2. Nested loop: **O(n²)**.
3. Logarithmic loop: **O(log n)**.
4. Total: **O(n + n² + log n)**.
5. Dominant term: **O(n²)**.

**Why?**\
The quadratic term (`n²`) grows faster than both `n` and `log n`, so it dominates the overall complexity.

---

## 6. Real-World Example: A Practical Algorithm 🌍

Imagine a program that:

1. Sorts an array: **O(n log n)**.
2. Prints each element: **O(n)**.
3. Processes data in a nested loop: **O(n²)**.

**Code:**

```python
def real_world(n, arr):
    arr.sort()  # O(n log n)
    
    for i in range(n):  # O(n)
        print(arr[i])
    
    for i in range(n):  # O(n²)
        for j in range(n):
            print(i, j)
```

**Calculation:**

- Sorting: **O(n log n)**.
- Printing: **O(n)**.
- Nested loop: **O(n²)**.
- Total: **O(n log n + n + n²) = O(n²)**.

**Why?**\
The quadratic term (`n²`) dominates, making the overall complexity **O(n²)**.

---


# Time Complexity Analysis of Python Snippets 📊

Below is a detailed analysis of the time complexity for four Python code snippets. Each snippet is analyzed step-by-step to determine how many iterations occur and the overall time complexity, presented in a professional and clear manner. 🚀

---

## Snippet a: Doubling Loop 🔄

```python
i = 1
while i < n:
    i *= 2
    print("data")
```

### Analysis 🧠

- **What’s happening?**

  - Initializes `i = 1`.
  - The `while` loop continues as long as `i < n`.
  - In each iteration, `i` is multiplied by 2 (`i = i * 2`), effectively doubling `i`.
  - A `print` statement inside the loop takes constant time, `O(1)`.

- **How many iterations?**

  - Starting with `i = 1`, the sequence of `i` is: `1, 2, 4, 8, 16, ..., 2^k`, where `k` is the iteration number.
  - The loop stops when `i >= n`, i.e., when `2^k >= n`.
  - Solving for `k`, we get `k >= log₂(n)`.
  - Thus, the loop runs approximately `log₂(n)` times.

- **Time Complexity**:

  - Each iteration performs a constant-time `print` operation (`O(1)`).
  - With `log₂(n)` iterations, the total time is `log₂(n) * O(1) = O(log n)`.

**Result**: Time complexity is **O(log n)**. ✅

---

## Snippet b: Halving Loop ➗

```python
i = n
while i > 0:
    print('complexity')
    i /= 2
```

### Analysis 🧠

- **What’s happening?**

  - Initializes `i = n`.
  - The `while` loop continues as long as `i > 0`.
  - In each iteration, `i` is divided by 2 (`i = i / 2`).
  - A `print` statement inside the loop takes `O(1)` time.
  - Note: Assuming integer division (common in time complexity analysis), `i` becomes smaller until it’s less than 1.

- **How many iterations?**

  - Starting with `i = n`, the sequence of `i` is: `n, n/2, n/4, n/8, ..., n/2^k`.
  - The loop stops when `i < 1`, i.e., when `n / 2^k < 1`, or equivalently, `2^k > n`.
  - Solving for `k`, we get `k > log₂(n)`.
  - Thus, the loop runs approximately `log₂(n)` times.

- **Time Complexity**:

  - Each iteration performs a constant-time `print` operation (`O(1)`).
  - With `log₂(n)` iterations, the total time is `log₂(n) * O(1) = O(log n)`.

**Result**: Time complexity is **O(log n)**. ✅

---

## Snippet c: Nested Doubling Loop 🔗

```python
for i in range(1, n):
    j = i
    while j < n:
        j *= 2
```

### Analysis 🧠

- **What’s happening?**

  - This is a nested loop structure.
  - **Outer loop**: Iterates `i` from 1 to `n-1`, running `n-1` times, i.e., `O(n)` iterations.
  - **Inner loop**: For each `i`, initializes `j = i` and continues as long as `j < n`. In each iteration, `j` is doubled (`j = j * 2`).
  - The inner loop has no explicit body, but we assume it’s iterating to double `j`.

- **How many iterations for the inner loop?**

  - For a given `i`, `j` starts at `i` and takes values: `i, 2i, 4i, 8i, ..., 2^k * i`.
  - The inner loop stops when `2^k * i >= n`, i.e., `2^k >= n/i`.
  - Thus, the inner loop runs `k >= log₂(n/i)` times, or `O(log(n/i))` iterations per `i`.

- **Total work?**

  - The outer loop runs `n-1` times.
  - For each `i`, the inner loop runs `log(n/i)` times.
  - Total iterations = Σ (from `i=1` to `n-1`) `log(n/i)`.
  - This sum is approximately `log(n) + log(n/2) + ... + log(1) = log((n-1)!)`.
  - Using Stirling’s approximation, `log(n!) ≈ n log n`, so the sum is `O(n log n)`.
  - Alternatively, the inner loop’s work is maximized for small `i` and decreases as `i` grows, but the total still evaluates to `O(n log n)`.

- **Time Complexity**:

  - Outer loop: `O(n)`.
  - Inner loop per `i`: `O(log(n/i))`.
  - Total: `O(n log n)`.

**Result**: Time complexity is **O(n log n)**. ✅

---

## Snippet d: Squaring Loop 📈

```python
i = 1
while i < n:
    print('python')
    i = i**2
```

### Analysis 🧠

- **What’s happening?**

  - Initializes `i = 1`.
  - The `while` loop continues as long as `i < n`.
  - In each iteration, `i` is squared (`i = i * i`).
  - A `print` statement inside the loop takes `O(1)` time.

- **How many iterations?**

  - Starting with `i = 1`, let’s compute the sequence:
    - After 1st iteration: `i = 1² = 1`.
    - After 2nd iteration: `i = (1²)² = 1⁴ = 1`.
    - This suggests a potential issue, as `i` remains 1, creating an infinite loop.
  - **Correction**: The likely intended behavior is that `i` grows double-exponentially, e.g., `i = 2^(2^k)`.
    - Let’s assume after `k` iterations, `i = 2^(2^k)`.
    - The loop stops when `2^(2^k) >= n`, i.e., `2^k >= log₂(n)`.
    - Solving for `k`, we get `k >= log₂(log₂(n))`.
  - Thus, the loop runs `O(log log n)` times.

- **Time Complexity**:

  - Each iteration performs a constant-time `print` operation (`O(1)`).
  - With `log₂(log₂(n))` iterations, the total time is `log₂(log₂(n)) * O(1) = O(log log n)`.

**Result**: Time complexity is **O(log log n)**. ✅

---

## Summary of Results 🎉

| Snippet | Time Complexity | Reason |
| --- | --- | --- |
| a | O(log n) | Loop doubles `i`, runs `log n` times. |
| b | O(log n) | Loop halves `i`, runs `log n` times. |
| c | O(n log n) | Outer loop `n` times, inner loop `log(n/i)` times, sums to `n log n`. |
| d | O(log log n) | Loop squares `i`, runs `log log n` times due to double-exponential growth. |

---