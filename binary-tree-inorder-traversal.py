from typing import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Check if the root is None, return an empty list
        if root is None:
            return []
        
        stack = []  # Initialize a stack to store nodes
        result = []  # Initialize a list to store the inorder traversal result
        
        while True:
            while root is not None:
                stack.append(root)  # Push the current node to the stack
                root = root.left  # Move to the left child
            
            if len(stack) == 0:
                return result  # If the stack is empty, return the result
            
            root = stack.pop()  # Pop the top node from the stack
            result.append(root.val)  # Add the value of the popped node to the result
            root = root.right  # Move to the right child
        
        # The function will never reach this point, as it always returns in the while loop