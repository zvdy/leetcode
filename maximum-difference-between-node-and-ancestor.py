# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(node, mn, mx):
            if not node:
                return
            mn = min(mn, node.val)
            mx = max(mx, node.val)
            if not node.left and not node.right:
                self.ans = max(self.ans, mx - mn)
            dfs(node.left, mn, mx)
            dfs(node.right, mn, mx)
        dfs(root, root.val, root.val)
        return self.ans