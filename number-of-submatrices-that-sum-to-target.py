from typing import *
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        # If the matrix is empty, return 0
        if not matrix or not matrix[0]:
            return 0
        
        # Get the number of rows and columns in the matrix
        m, n = len(matrix), len(matrix[0])
        
        # For each row in the matrix, calculate the prefix sum of the row
        for row in matrix:
            for i in range(1, n):
                row[i] += row[i-1]
        
        # Initialize the result to 0
        res = 0
        
        # Iterate over each pair of columns
        for i in range(n):
            for j in range(i, n):
                # Initialize a counter to count the number of submatrices with a certain sum
                counter = collections.Counter()
                # There's always one submatrix with a sum of 0: an empty submatrix
                counter[0] = 1
                
                # Initialize the current sum to 0
                cur = 0
                
                # Iterate over each row
                for k in range(m):
                    # Calculate the sum of the submatrix between the current pair of columns and the first k rows
                    cur += matrix[k][j] - (matrix[k][i-1] if i > 0 else 0)
                    # If there's a submatrix with a sum of cur - target, add the number of such submatrices to the result
                    res += counter[cur - target]
                    # Increment the count of submatrices with a sum of cur
                    counter[cur] += 1
        
        # Return the number of submatrices with a sum of target
        return res
