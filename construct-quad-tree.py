from typing import *
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def construct(grid, i, j, n):
            if n == 1:
                return Node(grid[i][j], True, None, None, None, None)
            n //= 2
            topLeft = construct(grid, i, j, n)
            topRight = construct(grid, i, j + n, n)
            bottomLeft = construct(grid, i + n, j, n)
            bottomRight = construct(grid, i + n, j + n, n)
            if topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf and topLeft.val == topRight.val and topRight.val == bottomLeft.val and bottomLeft.val == bottomRight.val:
                return Node(topLeft.val, True, None, None, None, None)
            return Node('*', False, topLeft, topRight, bottomLeft, bottomRight)
        return construct(grid, 0, 0, len(grid))