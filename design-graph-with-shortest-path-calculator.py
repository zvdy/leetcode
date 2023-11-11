class Graph:
    # Initialize the graph with a given number of nodes and edges
    def __init__(self, n: int, edges: List[List[int]]):
        # Create an adjacency list with n empty lists
        self.adj_list = [[] for _ in range(n)]
        # For each edge, add it to the adjacency list
        for from_node, to_node, cost in edges:
            self.adj_list[from_node].append((to_node, cost))

    # Add an edge to the graph
    def addEdge(self, edge: List[int]) -> None:
        # Unpack the edge into from_node, to_node, and cost
        from_node, to_node, cost = edge
        # Add the edge to the adjacency list
        self.adj_list[from_node].append((to_node, cost))

    # Find the shortest path between two nodes
    def shortestPath(self, node1: int, node2: int) -> int:
        # Get the number of nodes in the graph
        n = len(self.adj_list)
        # Initialize a priority queue with the start node and a cost of 0
        pq = [(0, node1)]
        # Initialize a list of costs for each node, with a default value of infinity
        cost_for_node = [inf] * (n)
        # The cost to reach the start node is 0
        cost_for_node[node1] = 0

        # While there are nodes in the priority queue
        while pq:
            # Pop the node with the lowest cost
            curr_cost, curr_node = heappop(pq)
            # If the current cost is greater than the stored cost for this node, skip it
            if curr_cost > cost_for_node[curr_node]:
                continue
            # If we've reached the end node, return the cost
            if curr_node == node2:
                return curr_cost
            # For each neighbor of the current node
            for neighbor, cost in self.adj_list[curr_node]:
                # Calculate the new cost to reach the neighbor
                new_cost = curr_cost + cost
                # If the new cost is less than the stored cost for the neighbor
                if new_cost < cost_for_node[neighbor]:
                    # Update the cost for the neighbor
                    cost_for_node[neighbor] = new_cost
                    # Add the neighbor to the priority queue with the new cost
                    heappush(pq, (new_cost, neighbor))
        # If there's no path to the end node, return -1
        return -1

# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)