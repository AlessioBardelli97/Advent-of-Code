from sys import argv
from re import search, compile


if __name__ == "__main__" and len(argv) >= 2:
  with open(argv[1]) as file:
    left_side: list[int] = []
    right_side: list[int] = []
    pattern = compile(r"^(\d+)\s+(\d+)$")
    for line in file.readlines():
      match = search(pattern, line)
      if match:
        left_side.append(int(match.group(1)))
        right_side.append(int(match.group(2)))
    left_side.sort()
    right_side.sort()
    print("Part One:", sum(abs(r - l) for l, r in zip(left_side, right_side)))
    print("Part Two:", sum(l * right_side.count(l) for l in left_side))
