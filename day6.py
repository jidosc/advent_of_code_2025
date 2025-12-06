inputs: list = open("inputs/day6.txt", "r").read().splitlines()

def normal():
    columns = []
    width = len(inputs[0].split())
    for i in inputs:
        for index, x in enumerate(i.split()):
            if (len(columns) - 1) < (index % width):
                columns.append([])
            columns[index % width].append(x)
    return columns


def find_spacings(lst: list) -> list:
    def max_widths(lsts: list) -> int:
        widths = []
        for lst in lsts:
            width = 0
            for c in lst:
                width = len(c) if len(c) > width else width
            widths.append(width)
        return widths

    widths = max_widths(normal())
    columns = []
    for row in range(len(inputs)):
        last_w = 0
        for index, w in enumerate(widths):
            if len(columns) - 1 < index:
                columns.append([])
            columns[index].append(inputs[row][last_w:last_w+w])
            last_w = last_w + w + 1
    return columns


def construct_numbers(lst: list):
    numbers = []
    for index in range(len(lst[0])):
        new_number = "".join([x[index] for x in lst])
        numbers.append(int(new_number))
    return numbers


def sum_list(lst: list):
    if len(lst) == 1:
        return int(lst[0])
    return int(lst[0]) + sum_list(lst[1:])


def mult_list(lst: list):
    if len(lst) == 1:
        return int(lst[0])
    return int(lst[0]) * mult_list(lst[1:])


def part1():
    total = 0
    for c in normal():
        if c[-1] == "*":
            total += mult_list(c[:-1])
        elif c[-1] == "+":
            total += sum_list(c[:-1])
    print(total)


def part2():
    total = 0
    columns = find_spacings(inputs)
    print(f"columns: {columns}")
    for c in columns:
        numbers = construct_numbers(c[:-1])
        print(f"numbers: {numbers}")
        if "*" in c[-1]:
           total += mult_list(numbers) 
        elif "+" in c[-1]:
            total += sum_list(numbers)
    print(total)

part1()
part2()