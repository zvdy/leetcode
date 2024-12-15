from typing import *
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        # If the root is None, return an empty list
        if not root:
            return []
        
        # Define a helper function for depth-first search
        def dfs(node):
            # If the node is None, return
            if not node:
                return
            # Recursively call dfs on the left child
            dfs(node.left)
            # Increment the frequency of the node's value
            self.freq[node.val] = self.freq.get(node.val,0)+1
            # Recursively call dfs on the right child
            dfs(node.right)
        
        # Initialize the frequency dictionary
        self.freq = {}
        # Start the depth-first search from the root
        dfs(root)
        # Find the maximum frequency
        max_freq = max(self.freq.values())
        # Return a list of all values with the maximum frequency
        return [k for k,v in self.freq.items() if v==max_freq]