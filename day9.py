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
    return abs(corner2[0] - corner1[0] + 1) * abs(corner2[1] - corner1[1] + 1)


def part2():
    largest_corners: list = [(0, 0), (0, 0)]
    largest_area: float = 0

    for x in corners:
        for y in corners:
            area = get_area(x, y)
            if area > largest_area and is_valid_rect(x, y):
                largest_corners[0] = x
                largest_corners[1] = y
                largest_area = area
                continue
    print(largest_corners)
    print(largest_area)


def is_point_inside_polygon(point, polygon):
    def is_on_edge(point, edge):
        # check if on edge
        x, y = point
        (x0, y0), (x1, y1) = edge

        if (min(x0, x1) <= x <= max(x0, x1)) and (min(y0, y1) <= y <= max(y0, y1)):
            cross_product = (x - x0) * (y1 - y0) - (y - y0) * (x1 - x0)
            return cross_product == 0
        return False
    

    x, y = point
    n = len(polygon)
    inside = False

    for i in range(n):
        x0, y0 = polygon[i]
        x1, y1 = polygon[(i + 1) % n]

        if is_on_edge(point, ((x0, y0), (x1, y1))):
            return True

        if (y > min(y0, y1)):
            if (y <= max(y0, y1)):
                if (x <= max(x0, x1)):
                    xinters = (y - y0) * (x1 - x0) / (y1 - y0) + x0
                    if (x0 == x1 or x <= xinters):
                        inside = not inside
    return inside


def is_valid_rect(a, b):
    p0 = (a[0], b[1])
    p1 = (b[0], a[1])

    return (is_point_inside_polygon(p0, corners) and is_point_inside_polygon(p1, corners))


part1()
part2()
