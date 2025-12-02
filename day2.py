inputs: list = open("inputs/day2.txt", "r").read().split(",")


def part1():
    def is_palindrome(id: str) -> bool:
        if len(id) % 2 == 0:
            i = len(id) // 2
            if id[:i] == id[i:]:
                return True
        return False
    
    invalid_ids: list = []

    for id_pair in inputs:
        ids = id_pair.split("-")

        start_id = int(ids[0])
        end_id = int(ids[1])
        id_range = end_id - start_id

        for i in range(id_range + 1):
            if is_palindrome(str(start_id + i)):
                invalid_ids.append(start_id + i)
    print(sum(invalid_ids))


def part2():
    def is_repeated(id: str) -> bool:
        cur = ""
        for digit in id:
            cur += digit

            le = len(cur)
            if le > len(id) // 2:
                break

            if len(id) % le == 0:
                for cou in range(len(id) // le):
                    if id[cou * le: (cou+1) * le] != cur:
                        break
                else:
                    return True
        return False
    
    invalid_ids: list = []
    
    for id_pair in inputs:
        ids = id_pair.split("-")

        start_id = int(ids[0])
        end_id = int(ids[1])
        id_range = end_id - start_id

        for i in range(id_range + 1):
            if is_repeated(str(start_id + i)):
                invalid_ids.append(start_id + i)
        
    print(sum(invalid_ids))


part1()
part2()