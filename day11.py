from functools import cache

data = open("inputs/day11.txt", "r").read().splitlines()
inputs = [row.split(" ")[0].rstrip(":") for row in data]
outputs = [row.split(" ")[1:] for row in data]
register = {}
for i in range(len(inputs)):
    register[inputs[i]] = outputs[i]


def part1():
    pass


def part2():
    print(valid_paths("svr", set()))


dead_ends = []
def valid_paths(input, already_visited: set) -> int:
    if input == "out":
        return 1 if {"dac", "fft"}.issubset(already_visited) else 0

    if is_dead_end(input, already_visited):
        return 0
    
    travel_guide = already_visited.copy()
    travel_guide.add(input)

    total = 0
    for o in register[input]:
        total += valid_paths(o, travel_guide)
    return total


def is_dead_end(input, already_visited: tuple) -> bool:
    if input in already_visited:
        return True
    return False


#part1()
part2()