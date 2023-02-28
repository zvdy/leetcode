# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def traverse(root):
            if not root:
                return "#"
            left = traverse(root.left)
            right = traverse(root.right)
            tree = f"{root.val},{left},{right}"
            count[tree] += 1
            if count[tree] == 2:
                res.append(root)
            return tree
        count = collections.Counter()
        res = []
        traverse(root)
        return res