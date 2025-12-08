english_levels_dag = {
    'A1 (Beginner)':      ['A2 (Elementary)'],
    'A2 (Elementary)':    ['B1 (Intermediate)'],
    'B1 (Intermediate)':  ['B2 (Upper-Intermediate)'],
    'B2 (Upper-Intermediate)': ['C1 (Advanced)'],
    'C1 (Advanced)':      ['C2 (Proficiency)'],
    'C2 (Proficiency)':   []
}
def topological_sort_dfs(graph):
    visited = set()
    result_stack = []

    def dfs_visit(node):
        visited.add(node)        
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs_visit(neighbor)        
        result_stack.append(node)

    for node in graph:
        if node not in visited:
            dfs_visit(node)
    return result_stack[::-1]

sorted_levels = topological_sort_dfs(english_levels_dag)

print("Topological Sort of English Levels:")
print(" -> ".join(sorted_levels))
