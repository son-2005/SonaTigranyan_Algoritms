weighted_graph = {
    'A': {'B': 3, 'C': 7},
    'B': {'A': 3, 'D': 2, 'E': 4},
    'C': {'A': 7, 'D': 1},
    'D': {'B': 2, 'C': 1, 'E': 6},
    'E': {'B': 4, 'D': 6}
}
def dijkstra_no_libraries(graph, start_node):
    all_nodes = list(graph.keys())
    
    distances = {node: float('inf') for node in all_nodes}
    distances[start_node] = 0

    visited = set()

    def get_shortest_unvisited_node(distances, visited):
        min_distance = float('inf')
        shortest_node = None

        for node in all_nodes:
            if node not in visited and distances[node] < min_distance:
                min_distance = distances[node]
                shortest_node = node
        return shortest_node

    current_node = start_node
    
    while current_node is not None:
        
        visited.add(current_node)
        current_distance = distances[current_node]

        for neighbor, weight in graph[current_node].items():
            
            new_distance = current_distance + weight
            
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance

        current_node = get_shortest_unvisited_node(distances, visited)
        
    return distances

start = 'A'
shortest_distances = dijkstra_no_libraries(weighted_graph, start)

print(f"Shortest distances starting from {start}(Dijkstra, O(V^2)):")
for node, dist in shortest_distances.items():
    print(f"Up to {node}: {dist}")
