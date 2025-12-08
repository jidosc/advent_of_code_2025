"""
Dela in alla i individuella circuits.

För antalet anslutningar:
- Ta närmaste par
    - Skippa om redan i samma
    - Annars: Anslut och slå ihop circuits

Multiplicera N största circuits.
"""

import math


def closest_pair(junctions: set, circuits) -> tuple:
    min_pair: set = set()
    min_dist: float = 10000000

    for x in junctions:
        y = min(
            filter(
                lambda b: b != x and not shares_circuit({x, b}, circuits), junctions
            ),
            key=lambda b: math.dist(x, b),
        )
        dist = math.dist(x, y)
        if dist >= min_dist:
            continue
        if not min_pair or dist < min_dist:
            min_pair = {x, y}
            min_dist = dist
            continue
    return min_pair


def shares_circuit(juncs: set, circuits) -> bool:
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
    merge_circs = list(filter(lambda c: not juncs.isdisjoint(c), circuits))
    new_circuit = merge_circs[0] | merge_circs[1]

    modified_circuits = circuits.copy()
    modified_circuits.remove(merge_circs[0])
    modified_circuits.remove(merge_circs[1])
    modified_circuits.append(new_circuit)
    return modified_circuits


def part1():
    TARGET_CONNECTIONS = 1000

    junctions: set = {
        tuple(map(int, x.split(",")))
        for x in open("inputs/day8.txt", "r").read().splitlines()
    }
    connection_count = 0
    circuits: list[set] = []

    pairs: list[tuple] = []
    for i, x in enumerate(junctions):
        for y in list(junctions)[i+1:]:
            if x == y:
                continue
            pairs.append((x, y))
    pairs.sort(key = lambda p: math.dist(p[0], p[1]))

    for j in junctions:
        circuits.append({j})

    while connection_count + 1 < TARGET_CONNECTIONS:
        conn = set(pairs.pop(0))
        if not shares_circuit(conn, circuits):
            circuits = merge_circuits(conn, circuits)
            # connection_count += 1 # inside for part 2
        connection_count += 1
    # print(conn) for part 2

    circuits.sort(key=lambda c: len(c), reverse=True)
    print([len(c) for c in circuits])


part1()
