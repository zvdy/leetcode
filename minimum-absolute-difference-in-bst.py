from typing import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def inorder(root):
            if root:
                inorder(root.left)
                self.res = min(self.res, root.val - self.prev)
                self.prev = root.val
                inorder(root.right)
                
        self.prev = float('-inf')
        self.res = float('inf')
        inorder(root)
        return self.res