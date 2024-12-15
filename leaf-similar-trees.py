from typing import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # Define a generator function for depth-first search (DFS)
        def dfs(node):
            # If the node exists
            if node:
                # If the node is a leaf (i.e., it has no children)
                if not node.left and not node.right:
                    # Yield the value of the leaf
                    yield node.val
                # Recursively perform DFS on the left child
                yield from dfs(node.left)
                # Recursively perform DFS on the right child
                yield from dfs(node.right)
        
        # Compare the leaf sequences of the two trees
        # If they are the same, return True; otherwise, return False
        return list(dfs(root1)) == list(dfs(root2))
