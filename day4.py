import time
from collections import deque

inputs: list = open("inputs/day4.txt", "r").read().splitlines()
roll_map = [[x for x in list(row)] for row in inputs]
start = time.time()


def part1():
    accessible = 0
    for y, row in enumerate(roll_map):
        for x in range(len(row)):
            if is_paper((x, y)):
                if not is_neighboorhood_crowded((x, y)):
                    accessible += 1
    print(accessible)


def part2():
    accessible = 0
    while True:
        removed_this_pass = 0
        for y, row in enumerate(roll_map):
            for x in range(len(row)):
                if is_paper((x, y)):
                    if not is_neighboorhood_crowded((x, y)):
                        accessible += 1
                        removed_this_pass += 1
                        roll_map[y][x] = "."
        if removed_this_pass == 0:
            break
    print(accessible)


def alt_part2():
    def return_neighboring_rolls(coordinate: tuple) -> int:
        neighbors = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

        cx, cy = coordinate
        returnal = []
        for n in neighbors:
            nx, ny = n
            if is_paper((nx + cx, ny + cy)):
                returnal.append((nx+cx, ny+cy))
        return returnal
    
    queue: deque = deque()
    removed: set = set()

    for y, row in enumerate(roll_map):
        for x in range(len(row)):
            queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        if is_paper((x, y)):
            neighbors = return_neighboring_rolls((x, y))
            if len(neighbors) < 4:
                removed.add((x, y))
                roll_map[y][x] = "."

                for n in neighbors:
                    if n not in queue and n not in removed:
                        queue.append(n)
    print(len(removed))


def is_neighboorhood_crowded(coordinate: tuple) -> bool:
    neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
    neighbor_count = 0

    cx, cy = coordinate
    while neighbors:
        nx, ny = neighbors.pop(0)
        if is_paper((nx + cx, ny + cy)):
            neighbor_count += 1
            
        if neighbor_count >= 4:
            return True
        elif neighbor_count + len(neighbors) < 4:
            return False


def is_paper(coordinate: tuple) -> bool:
    cx, cy = coordinate
    if 0 <= cy < len(roll_map) and 0 <= cx < len(roll_map[cy]):
        return roll_map[cy][cx] == "@"
    return False


part1()
#part2()
alt_part2()
print("--- %s seconds ---" % (time.time() - start))