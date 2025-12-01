inputs: list = open("input.txt", "r").read().splitlines()


def part1():
    zero_times: int = 0
    sum: int = 50

    for inp in inputs:
        mag = int(inp[1:])
        mag = -mag if inp[0] == "L" else mag
        sum = (sum + mag) % 100
        if sum == 0:
            zero_times += 1

    print(zero_times)


def part2():
    zero_times: int = 0
    sum: int = 50

    for inp in inputs:
        mag = int(inp[1:])
        mag = -mag if inp[0] == "L" else mag

        hundreds = abs(mag) // 100
        if hundreds != 0:
            zero_times += hundreds
            if mag <= -100:
                mag += hundreds * 100
            elif mag >= 100:
                mag -= hundreds * 100

        old_sum = sum
        sum = (sum + mag)
        if ((mag < 0 and (old_sum > 0 and sum < 0)) 
            or (mag > 0 and (old_sum < 100 and sum > 100))):
                zero_times += 1

        sum = sum % 100
        if sum == 0:
            zero_times += 1

    print(zero_times)


part1()
part2()