from typing import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def amountOfTime(self, root: TreeNode, start: int) -> int:
        # Create a dictionary to store the tree nodes and their adjacent nodes
        tree_map: Dict[int, Set[int]] = {}
        # Convert the binary tree to a graph
        self.convert(root, 0, tree_map)
        # Initialize a queue with the starting node
        queue = deque([start])
        # Initialize the minute counter
        minute = 0
        # Initialize a set to store visited nodes
        visited = {start}

        # Perform a breadth-first search
        while queue:
            # Get the number of nodes at the current level
            level_size = len(queue)
            while level_size > 0:
                # Dequeue a node
                current = queue.popleft()
                # Visit all adjacent nodes
                for num in tree_map[current]:
                    # If the node has not been visited, add it to the visited set and enqueue it
                    if num not in visited:
                        visited.add(num)
                        queue.append(num)
                # Decrease the level size
                level_size -= 1
            # Increase the minute counter
            minute += 1

        # Return the total time minus 1 (since the last increment happens after all nodes are visited)
        return minute - 1

    def convert(self, current: TreeNode, parent: int, tree_map: Dict[int, Set[int]]):
        # Base case: if the current node is None, return
        if current is None:
            return
        # If the current node is not in the tree map, add it
        if current.val not in tree_map:
            tree_map[current.val] = set()
        # Get the set of adjacent nodes
        adjacent_list = tree_map[current.val]
        # If the parent node is not 0, add it to the adjacent list
        if parent != 0:
            adjacent_list.add(parent)
        # If the current node has a left child, add it to the adjacent list
        if current.left:
            adjacent_list.add(current.left.val)
        # If the current node has a right child, add it to the adjacent list
        if current.right:
            adjacent_list.add(current.right.val)
        # Recursively convert the left and right subtrees
        self.convert(current.left, current.val, tree_map)
        self.convert(current.right, current.val, tree_map)
