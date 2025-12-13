graph_components = {
    'A': ['B'],    
    'B': ['A'],
    'C': ['D'],    
    'D': ['C'],
    'E': []        
}

def dfs_find_component(graph, start_node, visited):
    stack = [start_node]
    component = []

    while stack:
        g = stack.pop()

        if g not in visited:
            visited.add(g)
            component.append(g)

            for neighbor in reversed(graph[g]):
                if neighbor not in visited:
                    stack.append(neighbor)    
    return component

def find_connected_components(graph):
    visited = set()
    components = []

    for node in graph:
        if node not in visited:
            
            component = dfs_find_component(graph, node, visited)
            
            components.append(component)
            
    return components

all_components = find_connected_components(graph_components)
print("Կապակցված գագաթների խմբերը:", all_components)
