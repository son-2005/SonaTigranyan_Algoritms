network_graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def bfs_network_traversal(graph, start_node):
    visited = {start_node}    
    queue = [start_node]
    
    traversal_path = []
    print(f"BFS starts in {start_node}:")
    
    while queue:
        current_vertex = queue.pop(0) 
        
        traversal_path.append(current_vertex)

        for neighbor in graph.get(current_vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                
                queue.append(neighbor)
                
    return traversal_path

start = 'A'
bfs_result = bfs_network_traversal(network_graph, start)

print("\nnetwork visit sequence(BFS):")
print(" -> ".join(bfs_result))
