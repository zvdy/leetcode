# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # If the root is None, return an empty list
        if not root:
            return []
        
        # Initialize a deque with the root node and an empty list to store the maximum values
        q = deque([root])
        res = []
        
        # Loop until the deque is empty
        while q:
            # Get the size of the deque and initialize a variable to store the maximum value
            size = len(q)
            max_val = float('-inf')
            
            # Loop over the nodes in the current level of the tree
            for _ in range(size):
                # Pop the leftmost node from the deque and update the maximum value
                node = q.popleft()
                max_val = max(max_val, node.val)
                
                # If the node has a left or right child, add them to the deque
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            # Append the maximum value of the current level to the result list
            res.append(max_val)
        
        # Return the list of maximum values for each level of the tree
        return res