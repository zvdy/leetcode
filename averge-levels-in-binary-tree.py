from typing import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return []
        queue = [root]
        res = []
        while queue:
            res.append(sum([node.val for node in queue]) / len(queue))
            queue = [child for node in queue for child in (node.left, node.right) if child]
        return res