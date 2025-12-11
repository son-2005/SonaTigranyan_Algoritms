def floyd_warshall(graph):
    nodes = list(graph.keys())
    V = len(nodes)
    
    node_index = {node: i for i, node in enumerate(nodes)}
    
    D = [[float('inf')] * V for _ in range(V)]
    
    for u in graph:
        i = node_index[u]
        D[i][i] = 0 
        
        for v, weight in graph[u].items():
            j = node_index[v]
            D[i][j] = weight
            
    for k in range(V):
        for i in range(V):
            for j in range(V):
                
                if D[i][k] != float('inf') and D[k][j] != float('inf'):
                    new_distance = D[i][k] + D[k][j]
                    
                    if new_distance < D[i][j]:
                        D[i][j] = new_distance
                        
    for i in range(V):
        if D[i][i] < 0:
            print(f"\nWARNING: Negative cycle detected through {nodes[i]}։")
            return None, nodes

    return D, nodes
graph_data = {
    'A': {'C': 3},
    'B': {'A': 2, 'D': 4},
    'C': {'B': 7},
    'D': {'A': 6, 'C': -1}, 
}

final_matrix, node_list = floyd_warshall(graph_data)

if final_matrix:
    print("\nFinal Shortest Path Matrix (Floyd-Warshall):")
    
    header = "   " + " ".join(f"{n:4}" for n in node_list)
    print(header)
    print("---" * (len(node_list) + 1))
    
    for i, row in enumerate(final_matrix):
        row_str = " ".join(f"{val:4}" if val != float('inf') else " inf" for val in row)
        print(f"{node_list[i]:2}| {row_str}")
