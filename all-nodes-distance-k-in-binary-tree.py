from typing import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
            
            def dfs(node, parent=None):
                if node:
                    node.parent = parent
                    dfs(node.left, node)
                    dfs(node.right, node)
    
            dfs(root)
    
            queue = deque([(target, 0)])
            visited = set([target])
    
            while queue:
                node, level = queue.popleft()
    
                if level == k:
                    return [node.val] + [node.val for node, level in queue]
    
                for neighbor in [node.left, node.right, node.parent]:
                    if neighbor and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, level + 1))
    
            return []