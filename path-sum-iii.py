from typing import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:        
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        q, paths = deque([(root, targetSum, [])]), []
        
        while q:
            cur, target, path = q.pop()  
            if not (cur.left or cur.right) and cur.val == target:
                paths.append(path + [cur.val])
            else:
                if cur.left:
                    q.appendleft((cur.left, target - cur.val, path + [cur.val]))
                if cur.right:
                    q.appendleft((cur.right, target - cur.val, path + [cur.val]))
                                 
        return paths