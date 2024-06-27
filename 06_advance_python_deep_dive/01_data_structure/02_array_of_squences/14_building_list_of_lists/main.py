board = [['_'] * 3 for i in range(3)]
print(board)  # Output: [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

# Place a mark in row 1, column 2
board[1][2] = 'X'
print(board)  


weird_board = [['_'] * 3] * 3
print(weird_board)  # Output: [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

# Attempt to place a mark in row 1, column 2
weird_board[1][2] = 'O'
print(weird_board)  # Output: [['_', '_', 'O'], ['_', '_', 'O'], ['_', '_', 'O']]

board = []
for i in range(3):
    row = ['_'] * 3
    board.append(row)
print(board)  # Output: [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

# Place a mark in row 2, column 0
board[2][0] = 'X'
print(board) 


