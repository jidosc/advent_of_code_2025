inputs: list = open("inputs/day5.txt", "r").read().splitlines()

ranges = []
ingredients = []

for index, i in enumerate(inputs):
    if i == "":
        ranges = inputs[:index]
        ingredients = inputs[index+1:]
        break


def is_within_range(value: int) -> bool:
    for range in ranges:
        start = int(range.split("-")[0])
        end = int(range.split("-")[1])

        if start <= value <= end:
            return True
    return False


def part1():
    fresh_count = 0
    for ingred in ingredients:
        if is_within_range(int(ingred)):
            fresh_count += 1

    print(fresh_count)


def add_range(r: str, spans: list[tuple]):
    start = int(r.split("-")[0])
    end = int(r.split("-")[1])

    queue_spans = spans[:]

    if len(spans) == 0:
        spans.append((start, end))
    else:
        g = (start, end)
        while len(queue_spans) > 0:
            s = queue_spans.pop(0)
            print(f"comparing {g} and {s}")
            if (g[0] > s[1] and g[1] > s[1]):
                # no overlap
                print("No overlap")
                continue
            elif (g[0] < s[0] and g[1] < s[0]):
                # no overlap
                print("No overlap")
                continue
            elif (g[0] >= s[0] and g[1] <= s[1]):
                # within
                print("Subsumed by other range")
                return spans
            elif (g[0] < s[0] and g[1] > s[1]):
                # range within
                print("Consumes other range")
                spans.remove(s)
                continue
            elif (g[0] < s[0] and g[1] <= s[1] and g[1] >= s[0]):
                #end within
                print("End within")
                g = (g[0], s[1])
                spans.remove(s)
                continue
            elif (g[0] >= s[0] and g[0] <= s[1] and g[1] > s[1]):
                # start within
                print("Start within")
                g = (s[0], g[1])
                spans.remove(s)
                continue

        spans.append(g)
    spans.sort(key=lambda x: x[0])
    return spans


def get_length_of_ranges(ranges: list[tuple]):
    sum = 0
    for r in ranges:
        print(r)
        sum += len(range(r[0], r[1])) + 1
    return sum


def part2():
    unique_spans: list[tuple] = []
    for r in ranges:
        unique_spans = add_range(r, unique_spans)
    print(get_length_of_ranges(unique_spans))


part1()
part2()