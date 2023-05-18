class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # Create a set of all nodes
        nodes = set(range(n))
        
        # Remove all nodes that are not the destination of an edge
        for edge in edges:
            if edge[1] in nodes:
                nodes.remove(edge[1])
        
        # Return the remaining nodes
        return nodes