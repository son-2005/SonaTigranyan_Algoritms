def bellman_ford_shortest_path(edges, nodes, start_node):
    V = len(nodes)
    
    distances = {node: float('inf') for node in nodes}
    distances[start_node] = 0
    
    for i in range(V - 1):
        made_change = False 
        
        for u, v, weight in edges:
            
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                
                distances[v] = distances[u] + weight
                made_change = True
        
        if not made_change:
            break
                
    print("\n--- Negative Cycle Check (V-th iteration) ---")
    
    for u, v, weight in edges:
        if distances[u] != float('inf') and distances[v] > distances[u] + weight:
            print(f"WARNING: Negative cycle detected around the edge {u} -> {v}")
            return None 

    return distances

nodes = ['S', 'A', 'B', 'C', 'D', 'E']
edges = [
    ('S', 'A', 6), ('S', 'B', 7), 
    ('A', 'C', 5), ('A', 'D', -4),
    ('B', 'A', -3), ('B', 'C', -2),
    ('C', 'D', 8),
    ('D', 'E', 1),
    ('E', 'B', 2) 
]
start = 'S'
shortest_distances = bellman_ford_shortest_path(edges, nodes, start)

if shortest_distances:
    print("\nShortest distances(Bellman-Ford):")
    for node, dist in shortest_distances.items():
        print(f"Up to {node}: {dist}") #minchev
