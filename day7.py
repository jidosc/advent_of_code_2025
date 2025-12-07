import copy

rows: list = open("inputs/day7.txt", "r").read().splitlines()
manifold_map: list[list] = [[x for x in y] for y in rows]

cached_values: dict[tuple, int] = {}


def move_beam(map, coord: tuple) -> list[list]:
    if map[coord[1] + 1][coord[0]] == "^":
        # split
        has_split = 0
        if coord[0] > 0:
            # check left
            if map[coord[1] + 1][coord[0] - 1] != "|":
                map[coord[1] + 1][coord[0] - 1] = "|"
                has_split += 1
        if coord[0] < len(map[coord[1] + 1]) - 1:
            # check right
            if map[coord[1] + 1][coord[0] + 1] != "|":
                map[coord[1] + 1][coord[0] + 1] = "|"
                has_split += 1
        return (map, has_split)
    else:
        map[coord[1] + 1][coord[0]] = "|"
        return (map, 0)


def part1():
    real_map = copy.deepcopy(manifold_map)
    total_splits = 0
    for y_ind, y in enumerate(real_map):
        if y_ind == len(real_map) - 1:
            break
        for x_ind, x in enumerate(y):
            if real_map[y_ind][x_ind] == "S" or real_map[y_ind][x_ind] == "|":
                mod = move_beam(real_map, (x_ind, y_ind))
                real_map = mod[0]
                if mod[1] > 0:
                    total_splits += 1
    print(total_splits)


def find_paths(coord):
    totals = 1
    global cached_values
    if cached_values.get(coord):
        return cached_values.get(coord)

    x, y = coord
    if y == len(manifold_map) - 1:
        pass
    elif manifold_map[y][x] == "^":
        totals = find_paths((x - 1, y)) + (find_paths((x + 1, y)))
    else:
        totals = find_paths((x, y + 1))

    cached_values[(x, y)] = totals
    return totals


def part2():
    paths = 0
    for x_ind, x in enumerate(manifold_map[0]):
        if x == "S":
            paths = find_paths((x_ind, 0))
            break
    print(paths)


part1()
part2()