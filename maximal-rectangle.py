from typing import *
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])  # Get matrix dimensions

        if rows == 1 and cols == 1:  # Handle base case: single element matrix
            return 1 if matrix[0][0] == '1' else 0

        heights = [0] * (cols + 1)  # Initialize heights array with an extra element for convenience
        max_area = 0

        for i, row in enumerate(matrix):
            stack = [-1]  # Stack to store indices for calculating rectangle areas
            row.append('0')  # Add a sentinel '0' to simplify rightmost rectangle handling

            for j, val in enumerate(row):
                # Build the heights array:
                if val == '1':
                    heights[j] += 1  # Increment height if '1'
                else:
                    heights[j] = 0  # Reset height to 0 if '0'

                # Monotonic stack for efficient area calculation:
                while len(stack) > 1 and (j == cols or heights[j] < heights[stack[-1]]):
                    # Pop from stack until a smaller or equal height is found or the end is reached
                    max_height = heights[stack.pop()]
                    width = j - stack[-1] - 1  # Calculate rectangle width
                    area = max_height * width  # Calculate rectangle area
                    max_area = max(max_area, area)  # Update max area if necessary

                # Push current index onto the stack for future calculations
                stack.append(j)

        return max_area
