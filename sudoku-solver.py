from typing import *
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def is_valid(i, j, num):
            for k in range(9):
                if board[i][k] == num:
                    return False
                if board[k][j] == num:
                    return False
            x = i // 3 * 3
            y = j // 3 * 3
            for k in range(x, x + 3):
                for l in range(y, y + 3):
                    if board[k][l] == num:
                        return False
            return True
        def dfs(i, j):
            if i == 9:
                return True
            if j == 9:
                return dfs(i + 1, 0)
            if board[i][j] != '.':
                return dfs(i, j + 1)
            for num in '123456789':
                if is_valid(i, j, num):
                    board[i][j] = num
                    if dfs(i, j + 1):
                        return True
            board[i][j] = '.'
            return False
        dfs(0, 0)
        return board