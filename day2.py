inputs: list = open("inputs/day2.txt", "r").read().split(",")


def part1():
    def repeated_once(id: str) -> bool:
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
            if repeated_once(str(start_id + i)):
                invalid_ids.append(start_id + i)
    print(sum(invalid_ids))


def part2():
    def is_repeated(id: str) -> bool:
        cur_pattern = ""
        for digit in id:
            cur_pattern += digit
            cur_length = len(cur_pattern)
            if cur_length > len(id) // 2:
                break
            if len(id) % cur_length == 0:
                for cou in range(len(id) // cur_length):
                    if id[cou * cur_length: (cou+1) * cur_length] != cur_pattern:
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