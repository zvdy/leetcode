from typing import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans = 0

        def traverse(node):
            nonlocal ans
            
            if not node:
                return 0, 0
            
            # Traverse left and right subtrees
            left_sum, left_count = traverse(node.left)
            right_sum, right_count = traverse(node.right)
            
            # Calculate sum and count for current subtree
            curr_sum = node.val + left_sum + right_sum
            curr_count = 1 + left_count + right_count
            
            # Check if current subtree has average equal to node value
            if curr_sum // curr_count == node.val:
                ans += 1
            
            return curr_sum, curr_count
        
        # Start traversal from root
        traverse(root)
        return ans