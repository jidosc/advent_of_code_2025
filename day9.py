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
    points_in_polygon = []
    largest_corners: list = [(0, 0), (0, 0)]
    largest_area: float = 0

    max_x = max([x[0] for x in corners]) + 1
    max_y = max([y[1] for y in corners]) + 1
    print(max_x, max_y)

    structure = [["." for __ in range(max_x + 2)] for _ in range(max_y + 1)]

    for y, y_pos in enumerate(range(max_y)):
        for x, x_pos in enumerate(range(max_x)):
            if (x_pos, y_pos) in corners:
                structure[y][x] = "#"
            elif is_point_inside_polygon((x_pos, y_pos), corners):
                structure[y][x] = "X"
                points_in_polygon.append((x, y))
    print("\n".join(["".join(a) for a in structure]))
        

    for x in corners:
        for y in corners:
            if x == y:
                continue

            area = get_area(x, y)
            if area > largest_area and is_valid_rect(x, y, points_in_polygon):
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

        if y > min(y0, y1):
            if y <= max(y0, y1):
                if x <= max(x0, x1):
                    xinters = (y - y0) * (x1 - x0) / (y1 - y0) + x0
                    if x0 == x1 or x <= xinters:
                        inside = not inside
    return inside


def is_valid_rect(a, b, polygon_points=None):
    p0 = (a[0], b[1])
    p1 = (b[0], a[1])
    
    is_valid = (is_point_inside_polygon(p0, corners)
        and is_point_inside_polygon(p1, corners)
        and is_point_inside_polygon(a, corners)
        and is_point_inside_polygon(b, corners))
    
    if not is_valid:
        #print(f"rect {a} to {b} is not valid: corner.")
        return False

    for x in range(min(a[0], b[0])+1, max(a[0], b[0])):
        for y in range(min(a[1], b[1])+1, max(a[1], b[1])):
            if (x, y) not in polygon_points:
                #print(f"rect {a} to {b} is not valid: points [{(x, y)}]")
                return False
    #print(f"rect {a} to {b} is valid.")
    return True


part1()
part2()
