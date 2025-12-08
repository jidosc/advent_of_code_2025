import math

junctions: list = [
    tuple(map(int, x.split(",")))
    for x in open("inputs/day8.txt", "r").read().splitlines()
]

CONNS = 1000


def get_closest(pos: list, boxes: list, blacklist: list = []):
    closest: list
    closest_distance: int

    closest = boxes[0] if boxes[0] != pos else boxes[1]
    closest_distance = distance_3d(pos, closest)

    for b in boxes:
        if pos == b or b in blacklist:
            continue
        dist = distance_3d(pos, b)
        if dist < closest_distance:
            closest_distance = dist
            closest = b
    return closest, closest_distance


def distance_3d(pos1, pos2):
    return math.sqrt(
        math.pow(pos2[0] - pos1[0], 2)
        + math.pow(pos2[1] - pos1[1], 2)
        + math.pow(pos2[2] - pos1[2], 2)
    )


def add_to_circuits(pos: tuple, pair: tuple, circs: list) -> list:
    new_circs = []
    added = False

    for c in circs:
        new_circs.append(c.copy())

    for c in new_circs:
        if pair in c or pos in c:
            if pos not in c:
                c.append(pos)
                added = True
            elif pair not in c:
                c.append(pair)
                added = True
            break
    else:
        new_circs.append([])
        new_circs[-1].append(pos)
        new_circs[-1].append(pair)
        added = True
    #print(new_circs)
    return (new_circs, added)


def part1():
    circuits: list = []
    closest = []

    for a in junctions:
        checked = []
        for i in range(8):
            b, dist = get_closest(a, junctions, checked)

            for c in closest:
                if (c["b"] == a and c["a"] == b):
                    break
            else:
                closest.append({"a": a, "b": b, "dist": dist})

            checked.append(b)
    closest.sort(key=lambda x: x["dist"])

    made_conns = 0
    while made_conns < CONNS:
        cur = closest.pop(0)
        res = add_to_circuits(cur["a"], cur["b"], circuits)
        circuits = res[0]
        if res[1]:
            made_conns += 1

    product = 1
    circuits.sort(key=lambda x: len(x), reverse=True)
    for i in range(3):
        if len(circuits) - 1 < i:
            product *= 1
        else:
            #print(product, len(circuits[i]))
            product *= len(circuits[i])
    print(product)


part1()
