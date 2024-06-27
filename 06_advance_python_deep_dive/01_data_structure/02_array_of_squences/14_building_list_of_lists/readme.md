# Building Lists of Lists

Initializing a list with nested lists is a common task, especially for creating structures like teams of students or game boards. The best approach is using a list comprehension.

## Example 1: Tic-Tac-Toe Board

### Correct Approach
Use a list comprehension to create a list with three lists, each containing three items.
```python
# Create a tic-tac-toe board with list comprehension
board = [['_'] * 3 for i in range(3)]
print(board)  # Output: [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

# Place a mark in row 1, column 2
board[1][2] = 'X'
print(board)  # Output: [['_', '_', '_'], ['_', '_', 'X'], ['_', '_', '_']]
```

### Explanation
- **Initialization:** Create a list of three lists, each containing three underscores.
- **Modification:** Place a mark in row 1, column 2, and inspect the result.

## Example 2: Incorrect Approach

### Incorrect Approach
Avoid using multiplication to create nested lists, as it creates references to the same inner list.
```python
# Incorrect way to create nested lists
weird_board = [['_'] * 3] * 3
print(weird_board)  # Output: [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

# Attempt to place a mark in row 1, column 2
weird_board[1][2] = 'O'
print(weird_board)  # Output: [['_', '_', 'O'], ['_', '_', 'O'], ['_', '_', 'O']]
```

### Explanation
- **Issue:** The outer list contains three references to the same inner list.
- **Result:** Modifying one element affects all rows, as they are aliases of the same object.

## Detailed Comparison

### Incorrect Code Equivalent
This is how the incorrect approach behaves:
```python
row = ['_'] * 3
board = []
for i in range(3):
    board.append(row)
print(board)  # Output: [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

board[1][2] = 'O'
print(board)  # Output: [['_', '_', 'O'], ['_', '_', 'O'], ['_', '_', 'O']]
```

### Correct Code Equivalent
This is how the correct approach behaves:
```python
board = []
for i in range(3):
    row = ['_'] * 3
    board.append(row)
print(board)  # Output: [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

# Place a mark in row 2, column 0
board[2][0] = 'X'
print(board)  # Output: [['_', '_', '_'], ['_', '_', '_'], ['X', '_', '_']]
```

### Explanation
- **Correct Initialization:** Each iteration of the loop creates a new row and appends it to the board. This ensures that each sublist is a distinct object.
- **Modification:** When modifying one of the inner lists, only the specific sublist is changed, as expected.

## Conclusion

Using list comprehensions for nested lists ensures that each sublist is a distinct object, preventing unexpected behavior from shared references.
