from typing import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""  # If the root is None, return an empty string
        
        if root.left is None and root.right is None:
            return str(root.val)  # If the root has no children, return the value of the root as a string
        
        if root.right is None:
            # If the root has a left child but no right child, recursively convert the left subtree to a string
            return str(root.val) + "(" + self.tree2str(root.left) + ")"
        
        # If the root has both left and right children, recursively convert both subtrees to strings
        return str(root.val) + "(" + self.tree2str(root.left) + ")" + "(" + self.tree2str(root.right) + ")"