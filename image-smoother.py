from typing import *
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)  # Get the number of rows in the image
        n = len(img[0])  # Get the number of columns in the image
        
        res = [[0 for _ in range(n)] for _ in range(m)]  # Initialize a result matrix with the same dimensions as the image
        
        for i in range(m):
            for j in range(n):
                count = 0  # Initialize a counter to keep track of the number of neighboring cells
                
                for x in range(i-1, i+2):
                    for y in range(j-1, j+2):
                        if 0 <= x < m and 0 <= y < n:  # Check if the neighboring cell is within the image boundaries
                            res[i][j] += img[x][y]  # Add the value of the neighboring cell to the result
                            count += 1  # Increment the counter
                
                res[i][j] //= count  # Calculate the average value by dividing the sum by the count
                
        return res  # Return the resulting smoothed image