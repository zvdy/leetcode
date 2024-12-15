from typing import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        stack = []
        trav = root
        prev = -float('inf')
        while trav or stack:
            if trav:
                stack.append(trav)
                trav = trav.left
            else:
                u = stack.pop()
                if u:
                    if u.val <= prev:
                        return False
                    prev = u.val
                trav = u.right
        return True