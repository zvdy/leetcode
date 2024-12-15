from typing import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subRoot:
            return True
        def check_same(p,q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            return check_same(p.left,q.left) and check_same(p.right,q.right)
        
        if root.val == subRoot.val:
            if check_same(root,subRoot):
                return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)