import time

inputs: list = open("inputs/day4.txt", "r").read().splitlines()
roll_map = [[x for x in list(row)] for row in inputs]
start = time.time()

def part1():
    accessible = 0
    for y in range(len(roll_map)):
        for x in range(len(roll_map[y])):
            if is_paper((x, y)):
                if get_neighbors((x, y)) < 4:
                    accessible += 1
    print(accessible)


def part2():
    accessible = 0
    while True:
        removed_this_pass = 0
        for y in range(len(roll_map)):
            for x in range(len(roll_map[y])):
                if is_paper((x, y)):
                    if get_neighbors((x, y)) < 4:
                        accessible += 1
                        removed_this_pass += 1
                        roll_map[y][x] = "."
        if removed_this_pass == 0:
            break
    print(accessible)


def get_neighbors(coordinate: tuple) -> int:
    neighbors = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    neighbor_count = 0

    cx, cy = coordinate
    for n in neighbors:
        nx, ny = n
        if is_paper((nx + cx, ny + cy)):
            neighbor_count += 1
    return neighbor_count


def is_paper(coordinate: tuple) -> bool:
    cx, cy = coordinate
    if 0 <= cy < len(roll_map) and 0 <= cx < len(roll_map[cy]):
        return roll_map[cy][cx] == "@"
    return False


part1()
part2()
print("--- %s seconds ---" % (time.time() - start))