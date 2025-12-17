from sys import argv


def parse_input(line: str) -> list[range]:
  result = []
  for r in line.split(","):
    idx = r.split("-")
    result.append(range(int(idx[0]), int(idx[1]) + 1))
  return result


def part_one(ids: list[range]) -> int:
  result = 0
  for r in ids:
    for _id in r:
      middle = len(str(_id)) // 2
      if str(_id)[:middle] == str(_id)[middle:]:
        result += _id
  return result


def part_two(ids: list[range]) -> int:
  result = 0
  for r in ids:
    for _id in r:
      middle = len(str(_id)) // 2
      for dimension in range(1, middle):
        value = _id[:dimension]
        equals = True
        while equals and ...:
          if ... != value:
            equals = False
        if equals:
          result += _id
  return result


if __name__ == "__main__":
  with open(argv[1]) as file:
    ranges = parse_input(file.readline())
    print("Part one: ", part_one(ranges.copy()))
    print("Part two: ", part_two(ranges.copy()))
