inputs: list = open("inputs/day3.txt", "r").read().splitlines()


def part1():
    def find_largest_ten(number: str) -> (int, str):
        largest = 0
        largest_index = 0

        for index, digit in enumerate(number):
            if index == len(number) - 1:
                break

            int_digit = int(digit)
            if int_digit > largest:
                largest = int_digit
                largest_index = index

        return (largest, number[largest_index+1:])

    def find_largest_one(number: str) -> int:
        largest = 0
        for digit in number:
            int_digit = int(digit)
            if int_digit > largest:
                largest = int_digit
        return largest
    
    cur_sum = 0

    for line in inputs:
        ten = find_largest_ten(line)
        cur_sum += 10 * ten[0] + find_largest_one(ten[1])

    print(cur_sum)


def find_largest_nth(number: str, n: int) -> tuple[int, str]:
    """Returns largest digit that isn't among the last (n-1) 
    digits, and also the afterwards following digits."""
    largest = 0
    largest_index = 0

    for index, digit in enumerate(number):
        if index == len(number) - (n - 1):
            break

        int_digit = int(digit)
        if int_digit > largest:
            largest = int_digit
            largest_index = index

    return (largest, number[largest_index+1:])


def part2():
    cur_sum = 0

    for line in inputs:
        rest = line
        for i in range(12):
            result = find_largest_nth(rest, 12 - i)
            cur_sum += pow(10, 12 - i - 1) * result[0]
            rest = result[1]
    print(cur_sum)


part2()