import math

def shares_circuit(juncs: set, circuits) -> bool:
    # returns whether a pair of elements is in a single set, or separated
    for circ in circuits:
        if len(circ) <= 1:
            continue
        if juncs <= circ:
            return True
        elif juncs.isdisjoint(circ):
            continue
        return False
    return False


def merge_circuits(juncs, circuits) -> list[list]:
    # finds overlapping circuits
    merge_circs = list(filter(lambda c: not juncs.isdisjoint(c), circuits))
    new_circuit = merge_circs[0] | merge_circs[1]

    modified_circuits = circuits.copy()
    modified_circuits.remove(merge_circs[0])
    modified_circuits.remove(merge_circs[1])
    modified_circuits.append(new_circuit)
    return modified_circuits


def part1():
    TARGET_CONNECTIONS = 1000

    # create coordinates of individual junctions
    junctions: set = {
        tuple(map(int, x.split(",")))
        for x in open("inputs/day8.txt", "r").read().splitlines()
    }
    connection_count = 0
    circuits: list[set] = []

    # creates all pairs of coordinates and sorts from small to large by distance
    pairs: list[tuple] = []
    for i, x in enumerate(junctions):
        for y in list(junctions)[i+1:]:
            if x == y:
                continue
            pairs.append((x, y))
    pairs.sort(key = lambda p: math.dist(p[0], p[1]))

    # initializes all junctions in separate sets (circuits)
    for j in junctions:
        circuits.append({j})

    # until we've connected 1000
    while connection_count < TARGET_CONNECTIONS:
        conn = set(pairs.pop(0))
        if not shares_circuit(conn, circuits):
            circuits = merge_circuits(conn, circuits)
            # connection_count += 1 # inside for part 2
        connection_count += 1
        if len(circuits) == 1:
            break
    # print(conn) for part 2

    # sort and output circuits by size, large to small
    circuits.sort(key=lambda c: len(c), reverse=True)
    print([len(c) for c in circuits])


part1()
