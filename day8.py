"""
Dela in alla i individuella circuits.

För antalet anslutningar:
- Ta närmaste par
    - Skippa om redan i samma
    - Annars: Anslut och slå ihop circuits

Multiplicera N största circuits.
"""

import math


def distance_3d(pos_a, pos_b) -> float:
    return math.sqrt(
        (pos_b[0] - pos_a[0]) ** 2
        + (pos_b[1] - pos_a[1]) ** 2
        + (pos_b[2] - pos_a[2]) ** 2
    )


def closest_pair(junctions, already_paired: list[set]) -> tuple:
    return min(
        *[
            (x, y, distance_3d(x, y))
            for x in junctions
            for y in junctions
            if x != y and any([not {x, y}.isdisjoint(s) for s in already_paired])
        ],
        key=lambda p: p[2],
    )


def shares_circuit(junc_a, junc_b, circuits) -> bool:
    return any({junc_a, junc_b}.issubset(circ) for circ in circuits)


def merge_circuits(junc_a, junc_b, circuits) -> list[list]:
    merge_circs = list(filter(lambda c: junc_a in c or junc_b in c, circuits))
    new_circuit = merge_circs[0] | merge_circs[1]

    modified_circuits = circuits.copy()
    modified_circuits.remove(merge_circs[0])
    modified_circuits.remove(merge_circs[1])
    modified_circuits.append(new_circuit)
    return modified_circuits


def part1():
    TARGET_CONNECTIONS = 50

    junctions: set = {
        tuple(map(int, x.split(",")))
        for x in open("inputs/day8.txt", "r").read().splitlines()
    }
    connections: list[set] = []
    connection_count = 0
    circuits: list[set] = []

    for j in junctions:
        circuits.append({j})

    while connection_count + 1 < TARGET_CONNECTIONS:
        conn = closest_pair(junctions, connections)
        connections.append({conn[0], conn[1]})
        if not shares_circuit(conn[0], conn[1], circuits):
            # print(f"Connects {conn}")
            circuits = merge_circuits(conn[0], conn[1], circuits)
            connection_count += 1
        # else:
        # print(f"Skips {conn}")

    circuits.sort(key=lambda c: len(c), reverse=True)
    print([len(c) for c in circuits])


part1()
