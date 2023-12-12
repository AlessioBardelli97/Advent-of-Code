from itertools import zip_longest
from functools import cmp_to_key
from sys import argv


def compare(left: list, right: list) -> int:
    pairs = zip_longest(left, right)
    result = 0
    for pair in pairs:
        l, r = pair
        if isinstance(l, int) and isinstance(r, int):
            if l < r:
                return -1
            elif l > r:
                return 1
        elif isinstance(l, list) and isinstance(r, list):
            result = compare(l, r)
        elif isinstance(l, int) and isinstance(r, list):
            result = compare([l], r)
        elif isinstance(l, list) and isinstance(r, int):
            result = compare(l, [r])
        elif l == None:
            return -1
        elif r == None:
            return 1
        if result != 0:
            return result
    return result


if __name__ == "__main__" and len(argv) >= 2:
    with open(argv[1]) as file:
        lines = file.read().split("\n")
        pair_in_right_order = []
        packets = [[[2]], [[6]]]
        for i in range(0, len(lines), 3):
            left = eval(lines[i])
            right = eval(lines[i+1])
            packets.extend([left, right])
            if compare(left, right) < 0:
                pair_in_right_order.append(i // 3 + 1)
        print("Part One:", sum(pair_in_right_order))
        packets = sorted(packets, key=cmp_to_key(compare))
        idx_1, idx_2 = packets.index([[2]]), packets.index([[6]])
        print("Part Two:", (idx_1+1) * (idx_2+1))
