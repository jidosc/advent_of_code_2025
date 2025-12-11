def part1():
    data = open("inputs/day11.txt", "r").read().splitlines()

    inputs = [row.split(" ")[0].rstrip(":") for row in data]
    outputs = [row.split(" ")[1:] for row in data]
    register = {}
    for i in range(len(inputs)):
        register[inputs[i]] = outputs[i]

    print(valid_paths(register, "you", []))


def part2():
    data = open("inputs/day11.txt", "r").read().splitlines()

    inputs = [row.split(" ")[0].rstrip(":") for row in data]
    outputs = [row.split(" ")[1:] for row in data]
    register = {}
    for i in range(len(inputs)):
        register[inputs[i]] = outputs[i]

    print(valid_paths(register, "svr", []))


def valid_paths(register, input, already_visited) -> int:
    if is_dead_end(register, input, already_visited):
        return 0
    if input == "out":
        return "dac" in already_visited and "fft" in already_visited
    
    travel_guide = already_visited[:]
    travel_guide.append(input)

    total = 0
    for o in register[input]:
        total += valid_paths(register, o, travel_guide)
    return total


def is_dead_end(register, input, already_visited) -> bool:
    if input in already_visited:
        return True
    return False


#part1()
part2()