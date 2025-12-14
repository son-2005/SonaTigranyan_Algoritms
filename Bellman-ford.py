edges = [
    (0, 1, 4),   
    (0, 2, 2),   
    (1, 2, 3),  
    (2, 1, 1)    
]

V = 3

INF = 10**9
dist = [INF] * V
dist[0] = 0 

for i in range(V - 1):
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            dist[v] = dist[u] + w

print("Shortest distances from S:")
for i in range(V):
    print(f"To {i}: {dist[i]}")
