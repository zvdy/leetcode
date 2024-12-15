from typing import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            return node.val + dfs(node.left) + dfs(node.right)
        total = dfs(root)
        ans = 0
        def dfs2(node):
            nonlocal ans
            if not node:
                return 0
            left = dfs2(node.left)
            right = dfs2(node.right)
            ans = max(ans, left * (total - left), right * (total - right))
            return node.val + left + right
        dfs2(root)
        return ans % (10 ** 9 + 7)