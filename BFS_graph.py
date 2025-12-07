graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def bfs(graph, start_node):
    visited = {start_node}
    queue = [start_node]
    traversal_path = []

    while queue:
        g = queue.pop(0) 
        
        traversal_path.append(g)

        for neighbor in graph[g]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)                
    return traversal_path

start = 'A'
print("BFS-ի ճանապարհը (սկիզբը 'A'):")
result = bfs(graph, start)
print(" -> ".join(result))
