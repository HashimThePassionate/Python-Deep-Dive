import heapq

def prims_algorithm(graph, start_node):
    """
    Finds the Minimum Spanning Tree (MST) using Prim's algorithm.
    
    Args:
        graph (dict): A dictionary representing the graph's adjacency list.
                      Example: {'A': [('B', 5), ('C', 1)], ...}
        start_node (str): The node to start the algorithm from.

    Returns:
        tuple: A tuple containing the total cost of the MST and a list of its edges.
    """
    # Priority queue to store edges to visit: (weight, from_node, to_node)
    min_heap = []
    
    # Set to keep track of vertices already in the MST
    visited = set()
    
    # List to store the edges of the final MST
    mst_edges = []
    
    # Total cost of the MST
    total_cost = 0

    # Function to add all edges from a node to the priority queue
    def add_edges(node):
        visited.add(node)
        for neighbor, weight in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(min_heap, (weight, node, neighbor))

    # Start the algorithm from the given start_node
    add_edges(start_node)

    # Loop until the heap is empty or we've visited all nodes
    while min_heap and len(visited) < len(graph):
        # Get the edge with the smallest weight
        weight, from_node, to_node = heapq.heappop(min_heap)

        # If the destination node is already visited, this edge would form a cycle.
        # So, we skip it.
        if to_node not in visited:
            # Add the new node and its edges to our MST
            total_cost += weight
            mst_edges.append((from_node, to_node, weight))
            add_edges(to_node)
            
    return total_cost, mst_edges

# --- Example Usage ---
# Let's use the same graph from the previous example
example_graph = {
    'A': [('B', 5), ('C', 1)],
    'B': [('A', 5), ('C', 5), ('D', 3)],
    'C': [('A', 1), ('B', 5), ('D', 7), ('E', 9), ('F', 2)],
    'D': [('B', 3), ('C', 7), ('G', 4)],
    'E': [('C', 9), ('F', 6)],
    'F': [('C', 2), ('E', 6), ('G', 8)],
    'G': [('D', 4), ('F', 8), ('H', 10)],
    'H': [('B', 12), ('G', 10)]
}

# Run the algorithm starting from node 'A'
cost, edges = prims_algorithm(example_graph, 'A')

# Print the results
print(f"Total cost of the Minimum Spanning Tree: {cost} 💰")
print("Edges in the MST:")
for edge in edges:
    print(f"  {edge[0]} --({edge[2]})-- {edge[1]}")