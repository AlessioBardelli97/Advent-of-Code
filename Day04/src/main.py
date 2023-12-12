from sys import argv


def fully_contains(pair_elves: list[str]) -> bool:
    tmp = list(map(int, pair_elves))
    return (tmp[0] <= tmp[2] and tmp[1] >= tmp[3]) or \
           (tmp[0] >= tmp[2] and tmp[1] <= tmp[3])


def overlap_all(pair_elves: list[str]) -> bool:
    tmp = list(map(int, pair_elves))
    firstRange = list(range(tmp[0],tmp[1]+1))
    secondRange = list(range(tmp[2],tmp[3]+1))
    for sectnioID in firstRange:
        if sectnioID in secondRange:
            return True
    return False


if __name__ == "__main__" and len(argv) >= 2:
    with open(argv[1]) as file:
        countPartOne, countPartTwo = 0, 0
        list_of_pairs = file.read().split("\n")
        for pair_elves in list_of_pairs:
            pair_elves = pair_elves.replace(",", "-").split("-")
            if fully_contains(pair_elves):
                countPartOne += 1
            if overlap_all(pair_elves):
                countPartTwo += 1
        print("  Part One:", countPartOne)
        print("  Part Two:", countPartTwo)
