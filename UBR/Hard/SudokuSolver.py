"""
Write a program to solve a Sudoku puzzle by filling the empty cells.
A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

Example 1:
Input: board = 
[["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]]
Output: 
[["5","3","4","6","7","8","9","1","2"],
["6","7","2","1","9","5","3","4","8"],
["1","9","8","3","4","2","5","6","7"],
["8","5","9","7","6","1","4","2","3"],
["4","2","6","8","5","3","7","9","1"],
["7","1","3","9","2","4","8","5","6"],
["9","6","1","5","3","7","2","8","4"],
["2","8","7","4","1","9","6","3","5"],
["3","4","5","2","8","6","1","7","9"]]

Explanation: The input board is shown above and the only valid solution is shown below:

Constraints:
board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
It is guaranteed that the input board has only one solution.
"""

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def is_valid(board, row, col, num):

            # Check the row
            for i in range(9):
                if board[row][i] == num and i != col:
                    return False

            # Check the column
            for i in range(9):
                if board[i][col] == num and i != row:
                    return False

            # Check the 3x3 subgrid
            start_row = (row // 3) * 3
            start_col = (col // 3) * 3
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    if board[i][j] == num and (i, j) != (row, col):
                        return False

            return True
        
        # time limit exceed
        # while True:
        #     for i in range(9):
        #         for j in range(9):
        #             if board[i][j] == ".":
        #                 temp = []
        #                 for k in range(1,10):
        #                     if is_valid(board, i, j, str(k)):
        #                         temp.append(str(k))
        #                 if len(temp) == 1:
        #                     board[i][j] = temp[0]           
                            
        #     if not any(any(item == "." for item in sublist) for sublist in board):
        #         break

        # backtracking algorithm
        def backtrack(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        for num in range(1, 10):
                            if is_valid(board, i, j, str(num)):
                                board[i][j] = str(num)
                                if backtrack(board):
                                    print(i, j, num)
                                    return True
                                board[i][j] = "." # incorrect num, to try another num
                        return False
            return True

        backtrack(board)
