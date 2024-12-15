from typing import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # Base case: if the root is None, return 0
        if root is None:
            return 0
        
        # If the value of the root is less than the lower bound,
        # recursively call the function on the right subtree
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        
        # If the value of the root is greater than the upper bound,
        # recursively call the function on the left subtree
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)
        
        # If the value of the root is within the range,
        # recursively call the function on both the left and right subtrees,
        # and return the sum of the root value and the results from the subtrees
        return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)