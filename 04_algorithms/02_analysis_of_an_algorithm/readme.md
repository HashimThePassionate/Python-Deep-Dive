# **Performance Analysis of an Algorithm** ⏱️📊

The performance of an algorithm is primarily measured by how its running time and memory usage scale with the size of the input data, ( n ). When evaluating an algorithm, two critical factors are considered:

- **Time Complexity:**\
  The amount of time an algorithm takes to execute.

- **Space Complexity:**\
  The amount of memory required during the execution.

Key operations—such as comparison, assignment, or looping—determine the overall cost of the algorithm. In performance analysis, the focus is on how these costs grow as the input size increases.

## Examples of Time Complexity in Python

To illustrate time complexity, we provide two Python examples that demonstrate how different algorithms perform with varying input sizes. Each example includes code, a description of its functionality, and an analysis of its time complexity.

### Example 1: Simple Sum (O(n) - Linear Time)

This algorithm calculates the sum of all numbers in a list by iterating through each element once.

```python
def simple_sum(arr):
    total = 0
    for num in arr:  # Visit each element once
        total += num
    return total

# Test
numbers = [1, 2, 3, 4, 5]
print(simple_sum(numbers))  # Output: 15
```

**Explanation**:

- **Functionality**: The `simple_sum` function takes a list `arr` as input and initializes a variable `total` to 0. It iterates through each element in the list, adding it to `total`, and returns the final sum.
- **Time Complexity**: O(n), where `n` is the number of elements in the list. The algorithm performs one operation (addition) per element, so the total number of operations is proportional to `n`.
- **Use Case**: This is efficient for tasks requiring a single pass through the data, such as summing or averaging values.

### Example 2: Pair Sum (O(n²) - Quadratic Time)

This algorithm finds a pair of numbers in a list that add up to a given target sum by checking all possible pairs.

```python
def pair_sum(arr, target):
    for i in range(len(arr)):  # First loop
        for j in range(i + 1, len(arr)):  # Second loop
            if arr[i] + arr[j] == target:
                return arr[i], arr[j]
    return None

# Test
numbers = [1, 2, 3, 4, 5]
target = 9
print(pair_sum(numbers, target))  # Output: (4, 5)
```

**Explanation**:

- **Functionality**: The `pair_sum` function takes a list `arr` and a `target` sum as input. It uses nested loops to compare each pair of elements (without repeating pairs) and returns the first pair that sums to the target. If no such pair exists, it returns `None`.
- **Time Complexity**: O(n²), where `n` is the number of elements in the list. The outer loop runs `n` times, and the inner loop runs approximately `n-1`, `n-2`, ..., 1 times, leading to roughly `n * (n-1)/2` operations, which simplifies to O(n²).
- **Use Case**: This brute-force approach is simple but inefficient for large lists. More efficient solutions (e.g., using a hash table) can reduce the time complexity to O(n).

### Comparison of Examples

- **Simple Sum (O(n))**: For a list with 1000 elements, it performs \~1000 operations, making it suitable for large inputs.
- **Pair Sum (O(n²))**: For a list with 1000 elements, it performs \~500,000 operations, which can be significantly slower for large inputs.

---

The performance of an algorithm is determined by how its runtime scales with the input size, ( n ). A key factor in this is the **key operations**—like comparisons, assignments, or loops—that dominate the execution time. For example, in sorting algorithms, comparisons often take up most of the runtime compared to other operations like assignments. Ideally, these key operations should be independent of hardware, operating systems, or programming languages, ensuring consistent analysis across environments. 🚀

Each line of code takes a constant amount of time to execute, but different lines may require different times. By focusing on the key operations, we can better understand and predict an algorithm’s runtime, helping us choose the most efficient solution for a problem. 📈

## Understanding Key Operations 🔍

Key operations are the critical tasks an algorithm performs repeatedly, which significantly impact its runtime. For instance:

- In **sorting algorithms**, comparisons (e.g., checking if one element is greater than another) are typically the key operation.
- In **search algorithms**, comparisons to match elements with a target value drive the runtime.

By counting these operations, we can estimate how the algorithm’s performance scales with input size. Below, we explore two Python examples to see how key operations affect runtime in practice. 🐍

## Examples of Key Operations in Python 🧑‍💻

Here are two Python examples that demonstrate how key operations (specifically comparisons) influence an algorithm’s runtime. Each example includes code, functionality details, and a time complexity analysis.

### Example 1: Bubble Sort (O(n²) - Comparison-Heavy) ➕

Bubble Sort is a simple sorting algorithm that repeatedly compares adjacent elements and swaps them if they’re in the wrong order. Comparisons are the key operation here.

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):  # Outer loop
        for j in range(0, n-i-1):  # Inner loop
            if arr[j] > arr[j+1]:  # Comparison: Key operation
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap
    return arr

# Test
numbers = [64, 34, 25, 12, 22, 11, 90]
print("Sorted array:", bubble_sort(numbers))  # Output: [11, 12, 22, 25, 34, 64, 90]
```

**Explanation** 🌟:

- **Functionality**: The `bubble_sort` function takes a list `arr` and sorts it in ascending order. It uses nested loops to compare each pair of adjacent elements (`arr[j] > arr[j+1]`), swapping them if needed.
- **Key Operation**: The comparison (`if arr[j] > arr[j+1]`) is the primary operation, executed for every pair in the inner loop. Swaps occur less frequently, so comparisons dominate the runtime.
- **Time Complexity**: O(n²), where ( n ) is the number of elements. The outer loop runs ( n ) times, and the inner loop runs approximately ( n-1, n-2, ..., 1 ) times, resulting in roughly ( n \* (n-1)/2 ) comparisons, which simplifies to O(n²). 📉
- **Impact**: With 1000 elements, Bubble Sort performs \~500,000 comparisons, making it slow for large inputs. The comparison operation’s constant time is consistent across platforms, but the sheer number of comparisons drives the high runtime. 🐢

### Example 2: Linear Search (O(n) - Comparison-Based) 🔎

Linear Search looks for a target value in a list by checking each element one by one. Comparisons are again the key operation, but fewer are needed compared to Bubble Sort.

```python
def linear_search(arr, target):
    for i in range(len(arr)):  # Single loop
        if arr[i] == target:  # Comparison: Key operation
            return i  # Return index if found
    return -1  # Return -1 if not found

# Test
numbers = [2, 4, 6, 8, 10]
target = 8
result = linear_search(numbers, target)
print(f"Element {target} found at index: {result}")  # Output: Element 8 found at index: 3
```

**Explanation** 🎉:

- **Functionality**: The `linear_search` function takes a list `arr` and a `target` value, checking each element to find a match. It returns the index of the target or `-1` if not found.
- **Key Operation**: The comparison (`if arr[i] == target`) is performed for each element until a match is found or the list ends. This drives the runtime.
- **Time Complexity**: O(n), where ( n ) is the number of elements. In the worst case (target not found or at the end), it performs ( n ) comparisons. 📏
- **Impact**: For 1000 elements, Linear Search performs up to 1000 comparisons—far fewer than Bubble Sort’s \~500,000 for the same input size. The comparison operation remains constant across hardware, but the linear scaling makes it more efficient. 🚀

### Comparing the Examples ⚖️

- **Bubble Sort (O(n²))** 🐢: Relies on many comparisons (\~500,000 for 1000 elements), making it inefficient for large lists due to the quadratic number of key operations.
- **Linear Search (O(n))** ✅: Uses fewer comparisons (\~1000 for 1000 elements), resulting in faster execution for the same input size. The key operation (comparison) is similar, but the algorithm’s structure requires fewer of them.

This shows how the **number of key operations** (comparisons in these cases) directly affects runtime, regardless of the constant time each comparison takes. 📊

# Let's look another example ⏱️✨

A constant amount of time is required to execute each line of code; however, each line may take a different amount of time to execute. In order to understand the running time required for an algorithm, consider the below code as an example:

## Understanding Runtime with Key Operations 🔍

Every line of code in an algorithm contributes to its runtime. Here’s how it works:

- **Constant Time Operations**: Statements like condition checks or single prints take a fixed time (e.g., ( c1, c2 )) regardless of input size.
- **Repeated Operations**: Statements inside loops run multiple times (e.g., ( n ) times), so their total time scales with the input size (e.g., ( c \* n )).
- **Total Runtime**: Add up the time for all statements, considering how often each runs, to get ( T(n) ).

The example below shows how this works in practice, with a focus on a conditional statement and a loop. 🐍

## Python Example: Conditional vs. Loop Runtime 🧑‍💻

Let’s look at a Python algorithm that uses a condition and a loop to demonstrate how runtime is calculated based on statement execution times. The code checks if the input ( n ) is 0 or 3, printing "data" if true, or runs a loop ( n ) times to print "structure" if false.

```python
def example_algorithm(n):
    if n == 0 or n == 3:  # Statement 1: Condition check
        print("data")     # Statement 2: Print if condition true
    else:                 # Statement 3: Else block start
        for i in range(n):  # Statement 4: Loop runs n times
            print("structure")  # Statement 5: Print inside loop

# Test
n = 5
example_algorithm(n)  # Output: structure (5 times)
n = 0
example_algorithm(n)  # Output: data
```

### Step-by-Step Explanation 🌟

Assume each statement takes a constant time: ( c1, c2, c3, c4, c5 ) for statements 1 through 5, respectively. Here’s how the runtime breaks down:

- **Statement 1:** `if n == 0 or n == 3` ✅\
  This condition check runs once, taking constant time ( c1 ). It executes whether the condition is true or false.

- **Statement 2:** `print("data")` 📜\
  If the condition is true (( n == 0 ) or ( n == 3 )), this print runs once, taking constant time ( c2 ). It only executes in the true case.

- **Statement 3:** `else:` ➡️\
  If the condition is false, the else block starts, taking constant time ( c3 ). This runs once in the false case.

- **Statement 4:** `for i in range(n):` 🔄\
  The loop runs ( n ) times, and each iteration’s control (e.g., incrementing ( i )) takes constant time ( c4 ). Total time: ( c4 \* n ).

- **Statement 5:** `print("structure")` 🖨️\
  Inside the loop, this print runs ( n ) times, each taking constant time ( c5 ). Total time: ( c5 \* n ).

### Runtime Calculation 📊

- **When ( n == 0 ) or ( n == 3 )** 🎯:\
  Only the condition check (Statement 1) and print "data" (Statement 2) execute.\
  **T(n) = c1 + c2**\
  This is constant time since no loop runs. 🚀

- **When ( n ) is not 0 or 3 (e.g., ( n = 5 ))** 🔁:\
  The condition check (Statement 1), else block start (Statement 3), loop control (Statement 4), and print "structure" (Statement 5) execute.\
  **T(n) = c1 + c3 + c4 \* n + c5 \* n**\
  This is linear time because the runtime grows with ( n ) due to the loop. 📈

### Why It Matters ⚖️

This example shows how the **frequency of execution** (e.g., once for condition vs. ( n ) times for loop) and **statement times** (( c1, c2, etc. )) determine the runtime. For small ( n ) (like 0 or 3), the constant-time path (( T(n) = c1 + c2 )) is super fast. For large ( n ) (like 1000), the loop path (( T(n) = c1 + c3 + c4 \* n + c5 \* n )) takes much longer because of the ( n ) repetitions. Understanding this helps us predict and optimize algorithm performance! 💡

# Linear Search Runtime Analysis ⏱️✨

Let's dive into **linear search**, a simple algorithm that looks for an element in a list by checking each item one by one. We’ll analyze its **worst-case**, **average-case**, and **best-case** time complexities to see how it performs under different conditions. Each case depends on the number of **comparisons**—the key operation driving the runtime. Let’s explore with a Python example and break it down step-by-step! 🐍📈

## Linear Search: The Code 🔍

Here’s the linear search algorithm we’re analyzing. It searches for an element in a list and returns its index (or -1 if not found).

```python
def linear_search(input_list, element):
    for index, value in enumerate(input_list):
        if value == element:
            return index
    return -1

# Test
input_list = [3, 4, 1, 6, 14]
element = 4
print("Index position for the element x is:", linear_search(input_list, element))
# Output: Index position for the element x is: 1
```

**What Does It Do?**\
The `linear_search` function takes a list (`input_list`) and an `element` to find. It checks each item in the list:

- If the element is found, it returns the **index** (e.g., `4` is at index 1).
- If the element isn’t in the list, it returns `-1`.\
  The **key operation** is the comparison (`if value == element`), which happens for each element until a match is found or the list ends. Let’s see how this affects runtime in different scenarios! 🌟

## Analyzing Time Complexity 📊

Time complexity measures how an algorithm’s runtime scales with input size (`n`, the number of elements in the list). We’ll look at three cases: **worst-case**, **average-case**, and **best-case**, focusing on the number of comparisons needed.

### 1. Worst-Case Time Complexity 😓

The **worst-case** represents the maximum time an algorithm takes for any input. It’s the upper bound, guaranteeing that the runtime won’t exceed this limit no matter what.

**In Linear Search**:

- The worst-case occurs when:
  - The element is at the **last position** in the list, or
  - The element is **not in the list** at all.
- In these scenarios, the algorithm must check **every element**, traversing the entire list of `n` elements.

**Example**:

- For `input_list = [3, 4, 1, 6, 14]` and `element = 14` (last element), it takes 5 comparisons (checking indices 0 to 4).
- For `element = 10` (not in the list), it also takes 5 comparisons to check all elements and return -1.

**Time Complexity**:

- Each comparison takes constant time (say, `c`).
- In the worst-case, `n` comparisons are needed for `n` elements.
- Total time: **T(n) = c \* n**, which is **O(n)** (linear time).
- This means the runtime grows directly with the list size `n`. 📉

**Why It Matters**:\
Worst-case analysis is super useful because it provides a **guarantee**—the algorithm will never take longer than `O(n)` for any input. This is often used in real-world applications to ensure predictable performance. ✅

### 2. Average-Case Time Complexity 🤔

The **average-case** measures the average time an algorithm takes across **all possible inputs**. For linear search, we assume the element could be at any index (or not in the list), with each position being equally likely.

**In Linear Search**:

- If the element is in the list, the number of comparisons depends on its position:
  - At index 0: 1 comparison.
  - At index 1: 2 comparisons.
  - At index 2: 3 comparisons.
  - ... up to index n-1: n comparisons.
- We typically assume the element is found (for simplicity) and calculate the average number of comparisons across all positions.

**Calculation**:

- Total comparisons if the element is at each index: 1 + 2 + 3 + ... + n.
- This is an arithmetic series with sum: **(n \* (n + 1)) / 2**.
- Average comparisons: **\[(n \* (n + 1)) / 2\] / n = (n + 1) / 2**.
- Each comparison takes constant time (`c`), so average-case time:\
  **T(n) = c \* (n + 1) / 2**, which is **O(n)** (linear time).

**Example**:

- For a list with 5 elements (`n = 5`):
  - Total comparisons: 1 + 2 + 3 + 4 + 5 = 15.
  - Average: 15 / 5 = 3 comparisons.
- On average, you’ll check about half the list to find the element. 🔄

**Why It Matters**:\
Average-case is great for understanding typical performance when inputs are random. It assumes the element is equally likely to be anywhere, which may not always hold true but gives a realistic estimate. 📊

### 3. Best-Case Time Complexity 😎

The **best-case** is the minimum time an algorithm takes. It’s the lower bound, showing how fast the algorithm can be under ideal conditions.

**In Linear Search**:

- The best-case happens when the element is at the **first position** (index 0).
- Only **one comparison** is needed to find the element and return its index.

**Example**:

- For `input_list = [3, 4, 1, 6, 14]` and `element = 3`, the first comparison (index 0) finds the element.
- Comparisons: 1.

**Time Complexity**:

- One comparison takes constant time (`c`).
- Total time: **T(n) = c**, which is **O(1)** (constant time).
- The runtime doesn’t depend on `n`—it’s always one comparison. 🚀

**Why It’s Less Used**:\
Best-case is less practical because it only occurs in ideal scenarios. It doesn’t guarantee performance for typical or worst inputs, so it’s rarely used for planning. 🌈

## Relating to the Code 🎯

Let’s connect the analysis back to the example:

```python
input_list = [3, 4, 1, 6, 14]
element = 4
# Output: Index position for the element x is: 1
```

- **Best-Case**: If `element = 3`, it’s found at index 0 with 1 comparison. **T(n) = O(1)**. 😊
- **Average-Case**: On average, it takes \~3 comparisons for `n = 5` (as calculated). For `element = 4`, it took 2 comparisons (indices 0 and 1), which is close to the average. **T(n) = O(n)**. 🤝
- **Worst-Case**: If `element = 14` or a missing element like 10, it takes 5 comparisons to check the whole list. **T(n) = O(n)**. 🥳

## Key Takeaways 💡

- **Worst-Case (O(n))**: Most used because it guarantees the runtime won’t exceed `n` comparisons, no matter where the element is (or if it’s missing). Perfect for real-world reliability. 🛡️
- **Average-Case (O(n))**: Useful for random inputs, showing you’ll typically check about half the list. Still linear, but a bit optimistic. 📉
- **Best-Case (O(1))**: Only happens when the element is first, which is rare and not a reliable measure for planning. 🌟

---

# **Space Complexity Analysis**⏱️✨

Let’s explore **space complexity**, a key measure of how much memory an algorithm needs to run and produce its output, based on the input size. It’s a crucial factor in determining an algorithm’s efficiency—less memory usage often means a better algorithm, especially when other factors like time complexity are equal. Join us as we break it down with examples and see how memory impacts performance! 🧠💾

## What is Space Complexity? 🔍

Space complexity estimates the **total memory** an algorithm requires as a function of the input size (`n`). This includes:

- **Input Storage**: Memory to hold the input data.
- **Auxiliary Space**: Extra memory for variables, temporary data structures, or intermediate calculations.
- **Program Instructions**: Memory for the code itself (usually constant and minimal).
- **Output**: Memory needed to store the result.

When we analyze space complexity, we focus on **auxiliary space**—the extra memory used by the algorithm’s logic, beyond the input and output. Why? Because it shows how efficiently the algorithm manages resources as `n` grows. 📈

**Why It Matters**:\
If two algorithms solve the same problem with similar time complexity, the one using **less memory** is more efficient. This is critical in real-world applications, like mobile devices or big data systems, where memory is limited. Understanding space complexity helps us build lean, scalable solutions! 🌟

## Example 1: Squaring Numbers (O(n) Space) ➕

Let’s start with an algorithm that takes a list of integers and returns a new list of their squares. This shows how creating a new data structure affects space complexity.

```python
def squares(n):
    square_numbers = []  # New list for squares
    for number in n:     # Loop through each number
        square_numbers.append(number * number)  # Add square to list
    return square_numbers

# Test
nums = [2, 3, 5, 8]
print(squares(nums))  # Output: [4, 9, 25, 64]
```

### Space Complexity Breakdown 📊

- **Input**: The list `nums` has `n` elements (here, n=4: \[2, 3, 5, 8\]). It takes O(n) space, but we often exclude input from auxiliary space calculations since it’s part of the problem.
- **Auxiliary Space**:
  - `square_numbers`: A new list that stores `n` squares (e.g., \[4, 9, 25, 64\]). This requires **O(n)** space since it grows linearly with `n`.
  - `number`: A temporary variable in the loop, holding one integer at a time. This takes **O(1)** (constant) space.
- **Output**: The returned `square_numbers` list also takes O(n) space, and since it’s a new allocation, we include it in the analysis.
- **Total Space Complexity**: The dominant factor is `square_numbers`, which uses O(n) space. The temporary variable is negligible (O(1)). Thus, the space complexity is **O(n)**. 📉

**Takeaway**: This algorithm creates a new list proportional to the input size, so memory usage scales linearly. It’s fine for small inputs but can be memory-heavy for large `n`. 🐢

## Example 2: Calculating Sum (O(1) Space) ✅

Now, let’s look at a more memory-efficient algorithm that calculates the sum of a list without creating extra data structures. This highlights constant space usage.

```python
def calculate_sum(input_list):
    total = 0  # Variable to store sum
    for number in input_list:
        total += number  # Add each number
    return total

# Test
nums = [2, 3, 5, 8]
print("Sum of list:", calculate_sum(nums))  # Output: Sum of list: 18
```

### Space Complexity Breakdown 📏

- **Input**: The `input_list` has `n` elements (here, n=4: \[2, 3, 5, 8\]). It takes O(n) space, but we exclude it from auxiliary space as it’s given.
- **Auxiliary Space**:
  - `total`: A single integer variable storing the running sum. It takes **O(1)** space since it’s just one value, regardless of `n`.
  - `number`: A temporary loop variable holding one integer at a time. It also takes **O(1)** space.
- **Output**: The returned `total` is a single integer, using **O(1)** space.
- **Total Space Complexity**: Only `total` and `number` contribute to auxiliary space, both constant (O(1)). No new data structures are created, so the space complexity is **O(1)**. 🚀

**Takeaway**: This algorithm is super memory-efficient because it uses a fixed amount of extra space, no matter how large the input is. Perfect for memory-constrained environments! 😎

## Comparing the Examples ⚖️

Let’s see how these algorithms stack up:

- **Squares (O(n))**: Creates a new list (`square_numbers`) to store `n` squares, so memory usage grows with `n`. Useful when you need a new data structure, but it’s memory-intensive for large inputs. 🐘
- **Calculate Sum (O(1))**: Uses only a couple of variables (`total`, `number`), keeping memory constant regardless of input size. Ideal when you just need a single result without extra storage. 🦒

**What We Learn**:\
If both algorithms had similar time complexity, `calculate_sum` would be the winner because its **O(1)** space complexity is more efficient than `squares`’ **O(n)**. In real-world scenarios, like processing huge datasets or running on devices with limited RAM, O(1) space is a big advantage! 💪

---

## Asymptotic Efficiency 🔄

- **Asymptotic Analysis:** Focuses on growth rates for very large \(n\).  
- **Big O Notation:** Abstracts away constants to compare algorithms at scale.  
- **Practical Takeaway:** For large inputs, prefer algorithms whose space grows linearly (\(O(n)\)) or better (\(O(\log n)\), \(O(1)\)) rather than quadratic or worse.

---

## **Asymptotic Notation** 📈

When input sizes get large, we focus on how an algorithm’s running time **grows** rather than its exact runtime. Asymptotic analysis lets us:

- **Ignore** lower‑order terms (e.g. the “+ 2n” in 3n² + 2n + 1)  
- **Drop** constant multipliers (e.g. the “3” in 3n²)  
- Compare algorithms by their **order of growth** (how they scale)

---

### Why It Matters 🎯

- Helps predict performance for very large inputs  
- Makes it easy to compare algorithms across different machines  
- Guides you to choose the most scalable solution

---

### Common Notations 🔣

| Notation | Meaning                                           | Reads As                                          |
|----------|---------------------------------------------------|---------------------------------------------------|
| **Θ(f(n))** | **Tight bound**: the running time grows exactly on the order of f(n)   | “Theta of f of n”                                 |
| **O(f(n))** | **Upper bound**: the running time grows at most on the order of f(n)   | “Big‑O of f of n”                                 |
| **Ω(f(n))** | **Lower bound**: the running time grows at least on the order of f(n)  | “Omega of f of n”                                 |

- **Θ(f(n))** means the algorithm’s time is both O(f(n)) and Ω(f(n)).  
- **O(f(n))** guarantees the runtime will **not exceed** some constant × f(n) for large n.  
- **Ω(f(n))** guarantees the runtime will be **at least** some constant × f(n) for large n.  

---

### How to Simplify a Function 🧮

Given a running‑time expression, say:

```
T(n) = 3n^2 + 2n + 1
```

1. **Drop lower‑order term** (`2n` and `1`)  
2. **Ignore constant factor** (`3`)  
3. Conclude **T(n) is O(n²)**, Ω(n²), and therefore Θ(n²)

---

### Quick Reference Table 📊

| Expression         | Simplified Bound | Example Notation |
|--------------------|------------------|------------------|
| 5n + 20            | O(n)             | O(n)             |
| n log n + 100     | O(n log n)       | Θ(n log n)       |
| 2n² + 7n + 10     | Θ(n²)            | Ω(n²)            |
| 100               | O(1)             | Θ(1), Ω(1)       |

---
