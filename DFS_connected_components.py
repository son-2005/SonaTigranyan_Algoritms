graph_components = {
    'A': ['B'],      
    'B': ['A'],
    'C': ['D'],      
    'D': ['C'],
    'E': []          
}
def dfs(graph, start_node, visited, current_component):
    visited.add(start_node)
    current_component.append(start_node)
    for neighbor in graph.get(start_node, []): 
        if neighbor not in visited:
            dfs(graph, neighbor, visited, current_component)

def find_connected_components(graph):
    visited = set()
    all_components = []    
    for node in graph:
        if node not in visited:
            current_component = [] 
            
            dfs(graph, node, visited, current_component)
            
            all_components.append(current_component)            
    return all_components

components = find_connected_components(graph_components)

print("Կապակցված գագաթների խմբերը DFS-ի միջոցով:")
for i, component in enumerate(components):
    print(f"Խումբ {i+1}: {', '.join(component)}")
