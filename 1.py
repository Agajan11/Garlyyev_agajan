import matplotlib.pyplot as plt

def is_left_turn(p1, p2, p3):
    return ((p2[0] - p1[0]) * (p3[1] - p1[1]) - (p3[0] - p1[0]) * (p2[1] - p1[1])) > 0

def is_intersecting(p1, q1, p2, q2):
    return (is_left_turn(p1, q1, p2) != is_left_turn(p1, q1, q2)) and (is_left_turn(p2, q2, p1) != is_left_turn(p2, q2, q1))

def get_polygon_type(points):
    n = len(points)
    left_turn = is_left_turn(points[n - 2], points[0], points[1])

    for i in range(1, n - 1):
        if is_left_turn(points[i - 1], points[i], points[i + 1]) != left_turn:
            return "CONCAVE"
    
    return "CONVEX"

def is_self_intersecting(points):
    n = len(points)

    for i in range(n - 1):
        for j in range(i + 1, n - 1):
            if is_intersecting(points[i], points[i + 1], points[j], points[j + 1]):
                return True
    
    return False

points = [(-3, -1), (-5, 1), (-3, 3), (5, 1), (1, 0)]

polygon_type = get_polygon_type(points)
self_intersecting = is_self_intersecting(points)

x = [point[0] for point in points]
y = [point[1] for point in points]

plt.plot(x + [x[0]], y + [y[0]], 'b-') # Connect the last point with the first point

if polygon_type == "CONVEX" and not self_intersecting:
    plt.fill(x, y, 'none')
elif polygon_type == "CONCAVE" or self_intersecting:
    plt.fill(x, y, 'none')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Polygon')
plt.grid(True)
plt.show()