graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def dfs_iterative(graph, start_node):
    visited = set()
    
    stack = [start_node]
    traversal_path = [] 

    while stack:
        g = stack.pop() 

        if g not in visited:
            visited.add(g)
            traversal_path.append(g)
                        
            for neighbor in reversed(graph[g]):
                if neighbor not in visited:
                    stack.append(neighbor)                    
    return traversal_path

start = 'A'
print(f"DFS-ի ճանապարհը (սկիզբը '{start}'):")
result = dfs_iterative(graph, start)
print(" -> ".join(result))
        
