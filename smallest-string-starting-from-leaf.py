from typing import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
    self.smallest_string = ""
    self.dfs(root, "")
    return self.smallest_string

  # DFS helper to construct string prepending characters at each node
  def dfs(self, root, current_string):
    if not root: return  # Base case: null node
    current_string = chr(root.val + ord('a')) + current_string  # Prepend char
    if not root.left and not root.right:
      if not self.smallest_string or self.smallest_string > current_string:
        self.smallest_string = current_string  # Update smallest string
    if root.left: self.dfs(root.left, current_string)  # Recur left subtree
    if root.right: self.dfs(root.right, current_string)  # Recur right subtree
