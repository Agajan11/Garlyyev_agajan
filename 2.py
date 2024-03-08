import matplotlib.pyplot as plt

def is_left_turn(p1, p2, p3):
    return ((p2[0] - p1[0]) * (p3[1] - p1[1]) - (p3[0] - p1[0]) * (p2[1] - p1[1])) > 0

def is_inside_polygon(point, polygon):
    n = len(polygon)
    count = 0

    for i in range(n):
        if (polygon[i][1] <= point[1] < polygon[(i + 1) % n][1]) or (polygon[(i + 1) % n][1] <= point[1] < polygon[i][1]):
            if point[0] > ((polygon[(i + 1) % n][0] - polygon[i][0]) / (polygon[(i + 1) % n][1] - polygon[i][1])) * (point[1] - polygon[i][1]) + polygon[i][0]:
                count += 1
    
    return count % 2 != 0

points = [(1, -1), (2, 2), (6, 0), (5, -5), (2, -6)]
test_point = (4, 1)

x = [point[0] for point in points]
y = [point[1] for point in points]

plt.plot(x + [x[0]], y + [y[0]], 'b-') 

if is_inside_polygon(test_point, points):
    plt.plot(test_point[0], test_point[1], 'ro')
else:
    plt.plot(test_point[0], test_point[1], 'ko')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Polygon')
plt.grid(True)
plt.show()