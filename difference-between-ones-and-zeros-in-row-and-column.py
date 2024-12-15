from typing import *
class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        # Get the number of rows and columns
        m = len(grid)
        n = len(grid[0])

        # Initialize arrays to count the number of ones in each row and column
        onesRow = [0] * m
        onesCol = [0] * n

        # Count the number of ones in each row and column
        for i in range(m):
            for j in range(n):
                onesRow[i] += grid[i][j]
                onesCol[j] += grid[i][j]

        # Initialize a 2D array to store the difference between the number of ones and zeros
        diff = [[0] * n for _ in range(m)]
        # Calculate the difference for each cell in the grid
        for i in range(m):
            for j in range(n):
                diff[i][j] = 2 * onesRow[i] + 2 * onesCol[j] - n - m

        # Return the difference grid
        return diff
