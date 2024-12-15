from typing import *
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        row = len(matrix)
        col = len(matrix[0])
        res = []
        left, right, top, bottom = 0, col - 1, 0, row - 1
        while left <= right and top <= bottom:
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            for i in range(top + 1, bottom + 1):
                res.append(matrix[i][right])
            if left < right and top < bottom:
                for i in range(right - 1, left, -1):
                    res.append(matrix[bottom][i])
                for i in range(bottom, top, -1):
                    res.append(matrix[i][left])
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        return res