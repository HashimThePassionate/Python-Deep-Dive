# **Dynamic Programming**

Dynamic programming (DP) is a powerful technique for solving **optimization problems** with multiple possible solutions. It builds on the intuition of the **divide-and-conquer** approach but is tailored for problems with **overlapping sub-problems**. Let’s dive into the world of DP and explore its mechanics, characteristics, and techniques with clear examples! 🌟

---

## What is Dynamic Programming? 🤔

Dynamic programming solves complex problems by:

- Breaking them into smaller **sub-problems**.
- Solving each sub-problem **only once** and storing its result.
- Combining sub-problem solutions to solve the larger problem.

Unlike **divide-and-conquer**, where sub-problems are **non-overlapping** (disjoint), DP handles **overlapping sub-problems** by reusing previously computed results. This avoids redundant calculations, making DP highly efficient for problems like the Fibonacci series or shortest path algorithms. 💡

### Key Difference: Divide-and-Conquer vs. Dynamic Programming ⚖️

- **Divide-and-Conquer**: Solves independent sub-problems (e.g., merge sort). Each sub-problem is computed separately.
- **Dynamic Programming**: Handles overlapping sub-problems by storing results to avoid recomputation.

---

## Characteristics of Dynamic Programming Problems 🧩

For a problem to be solvable with DP, it must exhibit these two properties:

1. **Optimal Substructure** ✅

   - The optimal solution to the problem can be constructed from the optimal solutions of its sub-problems.
   - **Example**: In the Fibonacci series, `fib(6)` is computed as `fib(5) + fib(4)`, showing that the solution depends on smaller sub-problems.

2. **Overlapping Sub-Problems** 🔄

   - The same sub-problems are solved multiple times during computation.
   - **Example**: Calculating `fib(5)` involves repeatedly computing `fib(3)` and `fib(2)`. DP stores these results to avoid redundant work.

When a problem has these characteristics, DP can significantly improve efficiency by reusing stored solutions. 

---

## Dynamic Programming vs. Recursion 🔍

Both recursion and DP break problems into sub-problems, but they differ in how they handle computation:

- **Recursion**: Solves sub-problems repeatedly, even if they’ve been computed before. This can lead to high time complexity (e.g., O(2^n) for Fibonacci).
- **Dynamic Programming**: Solves each sub-problem **once** and stores the result, ensuring no recomputation. This reduces time complexity (e.g., O(n) for Fibonacci).

By tracking previously solved sub-problems, DP eliminates the inefficiency of redundant calculations. 🛠️

---

## Dynamic Programming Approaches 🛤️

DP problems can be solved using two main strategies:

### 1. Top-Down with Memoization 📝

- **How it works**:
  - Start with the original problem and recursively break it into smaller sub-problems.
  - Store the solution to each sub-problem in a data structure (e.g., array or hash table).
  - When a sub-problem is encountered again, retrieve its precomputed result instead of recalculating.
- **Memoization**: The process of storing sub-problem solutions to "remember" them for future use.
- **Advantages**:
  - Intuitive, as it follows the recursive structure of the problem.
  - Efficient for problems with many overlapping sub-problems.
- **Example**: Fibonacci series with memoization.

### 2. Bottom-Up Approach 🏗️

- **How it works**:
  - Solve the smallest sub-problems first and use their solutions to build solutions for larger sub-problems.
  - Store results in a table (e.g., array) and iterate until the final problem is solved.
  - Each sub-problem is solved only once, and prerequisite solutions are always available.
- **Advantages**:
  - Iterative, so it avoids recursive stack overhead.
  - Often more space-efficient for some problems.
- **Example**: Fibonacci series using a table.

---