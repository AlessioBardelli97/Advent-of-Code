from sys import argv


def parse_input(lines: list[str]) -> list[str]:
  return [line[:-1] for line in lines]


def general_part(banks: list[str], dimension: int) -> int:
  result = 0
  for bank in banks:
    joltage, max_idx, max_value, curr_idx,  = "", 0, bank[0], 1
    last_idx = curr_idx + (len(bank) - curr_idx) - (dimension - len(joltage) - 1)
    while len(joltage) < dimension:
      while curr_idx < last_idx:
        if bank[curr_idx] > max_value:
          max_idx = curr_idx
          max_value = bank[curr_idx]
        curr_idx += 1
      joltage += bank[max_idx]
      if len(joltage) < dimension:
        max_idx += 1
        max_value = bank[max_idx]
        curr_idx = max_idx + 1
        last_idx = curr_idx + (len(bank) - curr_idx) - (dimension - len(joltage) - 1)
    result += int(joltage)
  return result


def part_one(banks: list[str]) -> int:
  return general_part(banks, 2)


def part_two(banks: list[str]) -> int:
  return general_part(banks, 12)


if __name__ == "__main__":
  with open(argv[1]) as file:
    banks = parse_input(file.readlines())
    print("Part one: ", part_one(banks))
    print("Part two: ", part_two(banks))
