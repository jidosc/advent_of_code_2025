from itertools import combinations_with_replacement, combinations
import math

"""
setup:
- extrahera antal lampor (och vilka som ska vara på)
- extrahera knappar och vilka de sätter på

för varje rad
- loop igenom alla kombinationer av knapptryckningar
- en kombination är godkänd om lampor som ska vara på har % 2 == 1 tryckningar, och alla som ska vara av har % 2 == 0 tryckningar
- en kombination är den bästa om den det är så få som möjligt
- därav: iterera uppåt från 1 tryckning och uppåt till vi hittar en lösning som är godkänd

slutkläm
- addera antal knapptryck totalt (så lagra tidigare siffror)
"""


def fewest_presses_for_indicators(buttons: list, indicators: list) -> int:
    count = len(indicators)
    press_count = 1

    found_combination = False
    while True:
        presses_to_try = combinations(buttons, press_count)
        for current_press in presses_to_try:

            # evaluate current presses
            evaluation = [0 for i in range(count)]

            for press in current_press:
                for lamp in press:
                    evaluation[lamp] += 1

            evaluation = list(map(lambda c: c % 2 == 1, evaluation))
            if evaluation == indicators:
                found_combination = True
                break
        if found_combination:
            break
        press_count += 1
    return press_count


def get_compositions(parts, total, max_parts, p = []):
    # thanks to https://stackoverflow.com/a/36748940 :)
    b = len(max_parts) - parts
    if parts > 1:
        for i in range(total, -1, -1):
            if (total - i > max_parts[b]) or ((parts - 1) <= 1 and i > max_parts[b+1]) :
                continue
            else:
                yield from get_compositions(parts - 1, i, max_parts, p + [total - i])
    else:
        yield p + [total]


def fewest_presses_for_joltages(buttons: list, joltages: list) -> int:
    count = len(joltages)
    joltage_sum = sum(joltages)
    press_count = joltage_sum // max(*map(len, buttons))
    found_combination = False

    sleepy_buttons: set = set()
    for j in range(len(joltages)):
        if joltages[j] == 0:
            sleepy_buttons.add(j)

    # set max presses
    max_presses = [-1 for i in range(len(buttons))]
    for b in range(len(buttons)):
        max_allowed = -1
        for jolt in buttons[b]:
            max_p = joltages[jolt]
            if max_allowed < 0 or max_p < max_allowed:
                max_allowed = max_p
        max_presses[b] = max_allowed

    while True:
        invalid_starts = []
        for c in get_compositions(len(buttons), press_count, max_presses):
            valid = True
            button_count = []
            for i in range(len(buttons)):
                button_count.append(c[i])
            for i in invalid_starts:
                if button_count[:len(i)] == i:
                    valid = False
                    break
            if not valid: continue

            # evaluate current presses
            evaluation = [0 for i in range(count)]

            for i in range(len(buttons)):
                valid = True
                if button_count[i] == 0:
                    continue
                for jolt in buttons[i]:
                    if jolt in sleepy_buttons:
                        valid = False
                        break
                    evaluation[jolt] += button_count[i]
                    if evaluation[jolt] > joltages[jolt]:
                        invalid_starts.append(button_count[:i+1])
                        valid = False
                        break
                if not valid:
                    break
            else:
                if evaluation == joltages:
                    found_combination = True
                    break
        if found_combination:
            break
        press_count += 1
    return press_count


def part1():
    inputs = [x.split() for x in open("inputs/day10.txt", "r").read().splitlines()]
    indicators = [list(map(lambda c: c == "#", list(x[0].strip("[]")))) for x in inputs]
    buttons = [[list(map(int, list(y.strip("()").split(",")))) for y in x[1:-1]] for x in inputs]

    total_presses = 0
    for i in range(len(indicators)):
        total_presses += fewest_presses_for_indicators(buttons[i], indicators[i])

    print(total_presses)


def part2():
    inputs = [x.split() for x in open("inputs/day10.txt", "r").read().splitlines()]
    joltages = [list(map(int, x[-1].strip("{}").split(","))) for x in inputs]
    buttons = [[list(map(int, list(y.strip("()").split(",")))) for y in x[1:-1]] for x in inputs]

    total_presses = 0
    for i in range(len(joltages)):
        total_presses += fewest_presses_for_joltages(buttons[i], joltages[i])
        print(f"{i+1} / {len(joltages)} done")

    print(total_presses)


# part1()
part2()