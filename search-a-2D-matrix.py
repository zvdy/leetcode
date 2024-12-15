from typing import *
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        for row in matrix:
            if target in row:
                return True
        return False