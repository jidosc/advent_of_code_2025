corners: list = [
    tuple(map(int, x.split(",")))
    for x in open("inputs/day9.txt", "r").read().splitlines()
]


def part1():
    largest_corners: list = [(0, 0), (0, 0)]
    largest_area: float = 0

    for x in corners:
        for y in corners:
            area = get_area(x, y)
            if area > largest_area:
                largest_corners[0] = x
                largest_corners[1] = y
                largest_area = area
                continue
    print(largest_corners)
    print(largest_area)


def get_area(corner1, corner2) -> float:
    return (abs(corner2[0] - corner1[0]) + 1) * (abs(corner2[1] - corner1[1]) + 1)


def part2():
    corn = largest_rect(corners)
    print(get_area(corn[0], corn[1]))


def largest_rect(polygon):
    largest_corners: list = [(0, 0), (0, 0)]
    largest_area: float = 0

    for x in polygon:
        for y in polygon:
            if x == y:
                continue
            area = get_area(x, y)
            if area > largest_area and is_valid_rect(x, y, polygon):
                largest_corners[0] = x
                largest_corners[1] = y
                largest_area = area
                continue
    return largest_corners


def is_valid_rect(a, c, polygon):
    b = (a[0], c[1])
    d = (c[0], a[1])

    rect = [a, b, c, d]
    for v in rect:
        if not is_point_inside_polygon(v, polygon):
            return False
    return not any_edges_intersecting(rect, polygon)


def any_edges_intersecting(edges1, edges2):
    for i, _ in enumerate(edges1):
        a = (edges1[i], edges1[(i + 1) % len(edges1)])
        if not is_edge_inside_polygon(a, edges2):
            return True
    return False


def is_edge_inside_polygon(edge, polygon):
    ea, eb = edge
    if not (is_point_inside_polygon(ea, polygon) and is_point_inside_polygon(eb, polygon)):
        return False
    
    n = len(polygon)
    for i in range(n):
        pi = polygon[i]
        pj = polygon[(i+1)%n]
        if is_edges_intersecting(edge, (pi, pj)):
            return False
        
    samples = [0.25, 0.5, 0.75]
    for t in samples:
        sx = ea[0] + (eb[0] - ea[0]) * t
        sy = ea[1] + (eb[1] - ea[1]) * t
        if not is_point_inside_polygon((sx, sy), polygon):
            return False

    return True


def orientation(p, q, r):
    return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])


def is_point_inside_polygon(point, polygon):
    def is_on_edge(point, edge):
        if orientation(edge[0], edge[1], point) != 0:
            return False
        
        x, y = point
        (x0, y0), (x1, y1) = edge
        return (min(x0, x1) <= x <= max(x0, x1)) and (min(y0, y1) <= y <= max(y0, y1))

    x, y = point
    n = len(polygon)
    inside = False

    for i in range(n):
        x0, y0 = polygon[i]
        x1, y1 = polygon[(i + 1) % n]

        if is_on_edge(point, ((x0, y0), (x1, y1))):
            return True

        if (y0 > y) != (y1 > y):
            x_intersect = ((y - y0) * (x1 - x0)) / (y1 - y0) + x0
            if x < x_intersect:
                inside = not inside
    return inside


def is_edges_intersecting(a, b):
    a0, a1 = a  # polygon
    b0, b1 = b  # rectangle

    o1 = orientation(a0, a1, b0)
    o2 = orientation(a0, a1, b1)
    o3 = orientation(b0, b1, a0)
    o4 = orientation(b0, b1, a1)

    if o1 == 0 or o2 == 0 or o3 == 0 or o4 == 0:
        return False
    return (o1 > 0) != (o2 > 0) and (o3 > 0) != (o4 > 0)


def test_cases():
    try:
        rect = largest_rect(
            [
                tuple(map(int, x.split(",")))
                for x in open("inputs/test_cases/1.txt", "r").read().splitlines()
            ]
        )
        area = get_area(rect[0], rect[1])
        assert area == 24
    except AssertionError:
        print(f"Expected 24, got {area} because of corners {rect}")

    try:
        rect = largest_rect(
            [
                tuple(map(int, x.split(",")))
                for x in open("inputs/test_cases/2.txt", "r").read().splitlines()
            ]
        )
        area = get_area(rect[0], rect[1])
        assert area == 40
    except AssertionError:
        print(f"Expected 40, got {area} because of corners {rect}")

    try:
        rect = largest_rect(
            [
                tuple(map(int, x.split(",")))
                for x in open("inputs/test_cases/3.txt", "r").read().splitlines()
            ]
        )
        area = get_area(rect[0], rect[1])
        assert area == 100
    except AssertionError:
        print(f"Expected 100, got {area} because of corners {rect}")


# part1()
part2()
# test_cases()
