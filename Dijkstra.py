graph = [
    [(1, 10), (2, 1)],
    [(3, 5)],           
    [(3, 3), (4, 2)],   
    [(4, 2)],           
    []                  
]
NUM_NODES = 5
START_NODE = 0 

def dijkstra(graph, num_nodes, start_node):
    distance = [float('inf')] * num_nodes 
    distance[start_node] = 0
    unvisited = list(range(num_nodes)) 

    while unvisited:
        min_distance = float('inf')
        current_node_index = None
        
        for node_index in unvisited:
            if distance[node_index] < min_distance:
                min_distance = distance[node_index]
                current_node_index = node_index

        if current_node_index is None:
            break 

        unvisited.remove(current_node_index)

        for neighbor_index, weight in graph[current_node_index]:
            new_distance = distance[current_node_index] + weight
            
            if new_distance < distance[neighbor_index]:
                distance[neighbor_index] = new_distance
                
    return distance
shortest_paths = dijkstra(graph, NUM_NODES, START_NODE)

print(f"Ամենակարճ հեռավորությունները սկսած {START_NODE} ('A') գագաթից:")
print(shortest_paths)
