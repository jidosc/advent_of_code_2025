import time

inputs: list = open("inputs/day4.txt", "r").read().splitlines()
width = len(inputs[0])
start = time.time()

def list_to_string(lst: list):
    string = ""
    for c in lst:
        string += c
    return string

mega_string = list_to_string(inputs)

def part1():
    accessible = 0
    for index, pos in enumerate(mega_string):
        if is_paper(index, []):
            if get_neighbors(index, []) < 4:
                accessible += 1
    print(accessible)


def part2():
    accessible = 0
    try_again = True
    removed_indices = []
    last_start = 0
    while try_again:
        removed_this_pass = 0
        for index in range(last_start, len(mega_string)):
            if is_paper(index, removed_indices):
                neighb = get_neighbors(index, removed_indices)
                if neighb < 4:
                    if neighb == 0 and removed_this_pass == 0:
                        last_start = index
                    removed_indices.append(index)
                    removed_this_pass += 1
                    accessible += 1
        if removed_this_pass == 0:
            try_again = False
    print(accessible)

def get_neighbors(index: int, removed_indices) -> int:
    neighbors = 0

    has_left = (index % width) > 0
    has_right = (index % width) < (width - 1)
    has_above = (index // width) > 0
    has_below = (index // width) < ((len(mega_string) // width) - 1)

    if has_left:
        if has_above and is_paper(index - 1 - width, removed_indices):
            neighbors += 1
        if has_below and is_paper(index - 1 + width, removed_indices):
            neighbors += 1
        if is_paper(index - 1, removed_indices):
            neighbors += 1
    if has_right:
        if has_above and is_paper(index + 1 - width, removed_indices):
            neighbors += 1
        if has_below and is_paper(index + 1 + width, removed_indices):
            neighbors += 1
        if is_paper(index + 1, removed_indices):
            neighbors += 1
    if has_above:
        if is_paper(index - width, removed_indices):
            neighbors += 1
    if has_below:
        if is_paper(index + width, removed_indices):
            neighbors += 1
    
    return neighbors


def is_paper(index: int, removed: list) -> bool:
    return mega_string[index] == "@" and index not in removed


part2()
# print("--- %s seconds ---" % (time.time() - start))