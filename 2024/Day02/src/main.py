from sys import argv


def parse_input(lines: list[str]) -> list[list[int]]:
  return [[int(l) for l in line.split(" ")] for line in lines]


def is_safe(report: list[int]) -> bool:
  i, all_levels_valid = 0, True
  while i < len(report) - 2 and all_levels_valid:
    difference_1 = report[i] - report[i + 1]
    difference_2 = report[i + 1] - report[i + 2]
    if difference_1 * difference_2 < 0 or not (1 <= abs(difference_1) <= 3) or not (1 <= abs(difference_2) <= 3):
      all_levels_valid = False
    else:
      i += 1
  return all_levels_valid


def part_one(reports: list[list[int]]) -> int:
  return sum(1 for report in reports if is_safe(report))


def part_two(reports: list[list[int]]) -> int:
  result = 0
  for report in reports:
    if not is_safe(report):
      for level_idx in range(len(report)):
        if is_safe(report[:level_idx] + (report[level_idx+1:])):
          result += 1
          break
    else:
      result += 1
  return result


if __name__ == "__main__":
  with open(argv[1]) as file:
    reports = parse_input(file.readlines())
    print("Part one: ", part_one(reports))
    print("Part two: ", part_two(reports))
