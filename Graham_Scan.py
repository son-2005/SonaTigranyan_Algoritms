import math
def cross_product(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def distance_sq(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

def graham_scan_simplified_sort(input_points):
    if len(input_points) < 3:
        return input_points
        
    points = list(set(input_points))
    
    P0 = points[0]
    for p in points[1:]:
        if p[1] < P0[1] or (p[1] == P0[1] and p[0] < P0[0]):
            P0 = p
    
    remaining_points = []
    for p in points:
        if p != P0:
            remaining_points.append(p)
            
    points_with_angles = []
    for p in remaining_points:
        angle = math.atan2(p[1] - P0[1], p[0] - P0[0])
        dist_sq = distance_sq(P0, p)
        
        points_with_angles.append((angle, dist_sq, p))

    points_with_angles.sort()
    
    sorted_points = [p[2] for p in points_with_angles]
    
    if len(sorted_points) < 2:
         return [P0] + sorted_points 

    stack = [P0, sorted_points[0], sorted_points[1]]
    
    for i in range(2, len(sorted_points)):
        next_point = sorted_points[i]
        
        while len(stack) >= 2 and cross_product(stack[-2], stack[-1], next_point) <= 0:
            stack.pop()
            
        stack.append(next_point)
        
    return stack
points = [
    (0, 3), (1, 1), (2, 2), (4, 4),
    (0, 0), (1, 2), (3, 1), (3, 3)
]
hull = graham_scan_simplified_sort(points)

print(f"Ուռուցիկ Կեղևի Գագաթները:")
print(hull)
