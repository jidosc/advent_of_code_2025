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
    print(valid_paths("svr", False, False, tuple()))


@cache
def valid_paths(input, foundDAC, foundFFT, already_visited: tuple) -> int:
    if input == "out":
        return foundDAC and foundFFT

    if is_dead_end(input, already_visited):
        return 0
    
    travel_guide = already_visited + (input,)

    if not foundDAC and input == "dac":
       foundDAC = True
    elif not foundFFT and input == "fft":
        foundFFT = True 

    total = 0
    for o in register[input]:
        total += valid_paths(o, foundDAC, foundFFT, travel_guide)
    return total


@cache
def is_dead_end(input, already_visited: tuple) -> bool:
    if input in already_visited:
        return True
    return False


#part1()
part2()