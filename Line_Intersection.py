def find_line_intersection(p1, p2, p3, p4):    
    # Ax + By = C
    A1 = p2[1] - p1[1] # A1 = y2 - y1
    B1 = p1[0] - p2[0] # B1 = x1 - x2
    C1 = A1 * p1[0] + B1 * p1[1] # C1 = A1*x1 + B1*y1

    A2 = p4[1] - p3[1]
    B2 = p3[0] - p4[0]
    C2 = A2 * p3[0] + B2 * p3[1]
        
    determinant = A1 * B2 - A2 * B1
        
    if abs(determinant) < 1e-9: 
        return "No intersection or infinite", None

    
    x = (C1 * B2 - C2 * B1) / determinant
    y = (A1 * C2 - A2 * C1) / determinant    
    return "Lines intersect", (x, y)

P1 = (1, 1)
P2 = (5, 5)

P3 = (1, 5)
P4 = (5, 1)

status, intersection_point = find_line_intersection(P1, P2, P3, P4)

print(f"Line 1: {P1} - {P2}")
print(f"Line 2: {P3} - {P4}")
print(status)

if intersection_point:
    print(f"Intersection point: ({intersection_point[0]}, {intersection_point[1]})")
