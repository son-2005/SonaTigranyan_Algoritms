points = [
    (0, 3), (1, 1), (2, 2), (4, 4),
    (0, 0), (1, 2), (3, 1), (3, 3)
]
def cross_product(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def jarvis_march_simplified_start(points):
    if len(points) < 3:
        return points
    
    start_point = points[0]
    
    for p in points[1:]:
        
        if p[1] < start_point[1]:
            start_point = p
            
        elif p[1] == start_point[1] and p[0] < start_point[0]:
            start_point = p            

    convex_hull = []
    current_point = start_point
    
    while True:
        convex_hull.append(current_point)
        
        next_point = points[0]
        if next_point == current_point:
            next_point = points[1]
        
        for p in points:
            if p == current_point:
                continue
            
            orientation = cross_product(current_point, next_point, p)
            
            if orientation < 0: 
                next_point = p
                
        current_point = next_point
        if current_point == start_point:
            break
            
    return convex_hull

hull = jarvis_march_simplified_start(points)
print(f"Ուռուցիկ Կեղևի Գագաթները:")
print(hull)
