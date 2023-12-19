from sys import argv
from re import findall


if __name__ == "__main__" and len(argv) >= 2:
    with open(argv[1]) as file:
        lines = file.readlines()
        print("Part One:", sum([int(val[0] + val[-1]) for val in ["".join(findall(r"\d", line)) for line in lines]]))
