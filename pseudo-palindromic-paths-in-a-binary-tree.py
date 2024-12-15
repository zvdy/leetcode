from typing import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        # Define a recursive function to traverse the tree and count the pseudo-palindromic paths
        def dfs(node, path):
            # If the node is None, we've reached a leaf node, so return 0
            if not node:
                return 0
            # Use bitwise XOR to toggle the bit at the position of the node's value in the path
            path ^= 1 << node.val
            # If the node is a leaf node (it has no left or right child)
            if not node.left and not node.right:
                # Check if the path is a pseudo-palindrome (it has at most one bit set)
                # If it is, return 1, otherwise return 0
                return int(path & (path - 1) == 0)
            # If the node is not a leaf node, continue the traversal on its left and right child
            # and return the sum of the results
            return dfs(node.left, path) + dfs(node.right, path)
        # Start the traversal from the root of the tree with an empty path (0)
        return dfs(root, 0)
