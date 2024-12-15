from typing import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        # Initialize the maximum difference as 0
        self.ans = 0

        # Define a recursive function to perform depth-first search
        def dfs(node, mn, mx):
            # If the node is None, return
            if not node:
                return
            # Update the minimum and maximum values found so far
            mn = min(mn, node.val)
            mx = max(mx, node.val)
            # If the node is a leaf node, update the maximum difference
            if not node.left and not node.right:
                self.ans = max(self.ans, mx - mn)
            # Recursively call the function for the left and right children
            dfs(node.left, mn, mx)
            dfs(node.right, mn, mx)

        # Call the recursive function for the root node
        dfs(root, root.val, root.val)

        # Return the maximum difference
        return self.ans
