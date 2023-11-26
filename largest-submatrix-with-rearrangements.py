class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        # Get the number of rows and columns in the matrix
        m, n = len(matrix), len(matrix[0])
        
        # Iterate over the matrix, starting from the second row
        for i in range(1, m):
            for j in range(n):
                # If the current cell is 1, add the value of the cell above it
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i-1][j]
        
        # Initialize the maximum area
        res = 0
        
        # Iterate over each row in the matrix
        for row in matrix:
            # Sort the row in descending order
            row.sort(reverse=True)
            
            # Iterate over the sorted row
            for i in range(n):
                # Update the maximum area
                res = max(res, row[i] * (i+1))
        
        # Return the maximum area
        return res
