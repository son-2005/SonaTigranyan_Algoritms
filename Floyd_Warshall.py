def floyd_warshall(dist):
    n = len(dist)  

    for k in range(n):
        
        for i in range(n):
            
            for j in range(n):
                
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

INF = 10**9  

dist = [
    [0,   3,   INF, 7],   
    [8,   0,   2,   INF], 
    [5,   INF, 0,   1], 
    [2,   INF, INF, 0]    
]

result = floyd_warshall(dist)

print("All-pairs shortest paths:")
for row in result:
    print(row)
